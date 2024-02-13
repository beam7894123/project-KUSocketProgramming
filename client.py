import socket
import time
import sys
import threading

# loading_animation :3
def loading_animation():
    animation_chars = ['-', '\\', '|', '/']
    i = 0
    while not response_received:
        sys.stdout.write('\r₍⑅ᐢ..ᐢ₎ waiting for response ' + animation_chars[i])
        sys.stdout.flush()
        time.sleep(0.1)  
        i = (i + 1) % len(animation_chars)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 6666)

# Connect to the server's address and port
try:
    client_socket.connect(server_address)
    print("Connected to server (=´∀｀)人(´∀｀=)\n")
except Exception as e:
    print(f"!Error connecting to server! (ᵕ—ᴗ—)\n")
    print(f"{e}")
    print("Exiting with E |˶˙^˙ )ﾉﾞ")
    sys.exit(1)

try:
    # Send a message to the server
    print('-*-*-*-*-*-*-*-*-*-*- Twitter(X) latest tweet lookup -*-*-*-*-*-*-*-*-*-*-')
    print("(To shutdow server use: stop)")
    username = input("Enter the X username: ")
    client_socket.send(username.encode())

    print("Send! Cat in the internet is looking for username that u request, plz wait! :3")
    print("(This may take 2-10min '^')")

    print('\n\n\n')
    response_received = False

    loading_animation_thread = threading.Thread(target=loading_animation)
    loading_animation_thread.start()

    response = client_socket.recv(1024).decode()
    response_received = True
    print(" oh!")

    print('\n')

    if not response:
        print('Look like this Nitter instances rate limit or just bad...')
        print('Plz try again! >m<')
        print("\nExiting with E |˶˙^˙ )ﾉﾞ")
    else:
        print('Server response *w*:\n', response)
        print("\nExiting with 0 |˶˙ᵕ˙ )ﾉﾞ")

except Exception as e:
    print(f"Error during communication with server: {e}")
    print("\nExiting with E |˶˙^˙ )ﾉﾞ")

finally:
    client_socket.close()
    if 'loading_animation_thread' in locals() and loading_animation_thread.is_alive():
            loading_animation_thread.join()







