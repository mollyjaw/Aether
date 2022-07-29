import ctypes
import json
import os
import sys
import time
from colorama import Fore as fore
from pystyle import Center,Box
from Functions import art, design, functions
from Functions.functions import Log
import Functions.design
from Functions.spammer import Delete, Ping, Post, Spam

os.system('mode 60, 20')
os.system('cls;clear')

w = fore.WHITE
lb = fore.LIGHTBLUE_EX
columns = os.get_terminal_size().columns
conf = json.load(open('config.json'))

msg = conf['message']
msgdel = conf['deletemessage']
sendmsgafterdel = conf['send-message-before-deletion']


logo = '''
 █████╗ ███████╗████████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔════╝╚══██╔══╝██║  ██║██╔════╝██╔══██╗
███████║█████╗     ██║   ███████║█████╗  ██████╔╝
██╔══██║██╔══╝     ██║   ██╔══██║██╔══╝  ██╔══██╗
██║  ██║███████╗   ██║   ██║  ██║███████╗██║  ██║
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
'''





def Logo():
    for line in logo.splitlines():
        print(Functions.design.greenblue((line.center(columns))))
    print(F"{lb}{'━'*columns}")



def HelpScreen():
    Log("Spam   <WEBHOOK> <AMOUNT>")
    Log("Delete <WEBHOOK>")
    Log("Ping   <WEBHOOK>")
    print(F"{lb}{'━'*columns}")



def MainMenu():
    ctypes.windll.kernel32.SetConsoleTitleW("Aether | A Kyanite Production")
    Log("Type Help For Help")
    choice = input(art.ask)
    functions.cls()
    if choice.lower().__contains__("help"):
        Logo()
        HelpScreen()
        MainMenu()
    elif choice.lower().__contains__("spam"):
        webhook = ""
        args = choice.split(" ")
        amt = ""
        try:
            webhook = args[1]
            amt = args[2]
            Logo()
            Spam(webhook,msg,int(amt))
            MainMenu()
        except Exception as e:
            Log(e)
            time.sleep(2)
            MainMenu()
    elif choice.lower().__contains__("del"):
        webhook = ""
        args = choice.split(" ")
        try:
            Logo()
            webhook = args[1]
            if(sendmsgafterdel):
                Post(webhook,msgdel)
            Delete(webhook)
            MainMenu()
        except Exception as e:
            Log(e)
            time.sleep(2)
            MainMenu()

    elif choice.lower().__contains__("ping"):
        webhook = ""
        args = choice.split(" ")
        try:
            Logo()
            webhook = args[1]
            Ping(webhook)
            MainMenu()
        except Exception as e:
            Log(e)
            time.sleep(2)
            MainMenu()



    else:
        functions.cls()
        Logo()
        MainMenu()
        
Logo()
MainMenu()

