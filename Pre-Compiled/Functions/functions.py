from colorama import Fore
from datetime import datetime
import Functions.design
from Functions import art, design, functions
import os

w = Fore.WHITE


def GrabTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time

def Checker(nip):
    return str(nip).lower()


def cls():
    return os.system('cls;clear')



def Log(text):
    print(f"{w}{functions.GrabTime()} | {Functions.design.greenblue('Message')} | {text}")
