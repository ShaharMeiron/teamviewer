import keyboard
import socket
import threading
import pygame
import pyautogui
import json

img_path = r"C:\Users\Shahar\Downloads\teamviewer\screenshot.jpg"
    #mouse command msg\r\n
    #left/right\r\n
    #x\r\n
    #y\r\n\r\n

    #keyboard command message : key\r\n

    #screenshot msg:
    #length\r\n
    #content
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
    t1 = threading.Thread(target=send_keys_thread,args=(kb_socket))
    t2 = threading.Thread(target=send_mouseclicks,args=(mouse_socket))
    t3 = threading.Thread(target=get_stream,args=(stream_socket))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()



def get_stream(socket):
    pygame.init()
    x = 1200
    y = 1200
    scrn = pygame.display.set_mode((x, y))
    while True:
        header = ""
        while header[-2:] != "\r\n":
            header += socket.recv(1).decode()
        length = str(header[:-2])
        content = socket.recv(length)
        f1 = open(img_path,'rb')
        f1.write(content)
        f1.close()
        imp = pygame.image.load(img_path).convert()
        scrn.blit(imp, (0, 0))
        pygame.display.flip()
        


    pass


def send_mouseclicks():

    pass

def send_keys_thread(socket):
    socket.listen()
    socket.accept()
    while True:
        key = keyboard.read_key() + "\r\n"
        socket.send(key.encode())
        
        
        


print(pyautogui.size())
