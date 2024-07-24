import keyboard
import socket
import threading

    #mouse command msg\r\n
    #left/right\r\n
    #x\r\n
    #y\r\n\r\n

    #keyboard command message : key\r\n
def alt_tab():
    keyboard.press('q')


def tcp_server_socket(port):
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("127.0.0.1", port)
    socket.bind(addr)
    return socket


def udp_server_socket():
    pass

def main():
    kb_socket = tcp_server_socket(port = 1600)
    mouse_socket = tcp_server_socket(port = 1601)
    stream_socket = tcp_server_socket(port = 1602)
    t1 = threading.Thread(target=send_keys_thread)
    t2 = threading.Thread(target=send_mouseclicks)
    t3 = threading.Thread(target=get_stream)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()



def get_stream():
    pass


def send_mouseclicks():
    pass

def send_keys_thread(socket):
    socket.listen()
    socket.accept()
    while True:
        key = keyboard.read_key()
        print(key)
        
        
        



send_keys_thread()