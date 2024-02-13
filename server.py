# web starter
import json
from socket import *
# Using Nitter from ntscraper becouse X.com rate limit is suck -w- (Thanks Elon :<)
from ntscraper import Nitter


serverPort = 6666
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print('The server is ready to receive \'w\'b\n')

while True:
    connectionSocket, addr = serverSocket.accept()
    username = connectionSocket.recv(1024).decode()
    if username == 'stop':
        break
    tweets = Nitter().get_tweets(username, mode='user', number=1)
    list_of_content = [tweets]
    data = json.dumps(list_of_content, indent=2)

    # data = username
    connectionSocket.send(data.encode())
    connectionSocket.close()
    
serverSocket.close()