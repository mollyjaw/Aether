import ctypes
import time
import requests
from Functions.functions import Log
import Functions.design
from Functions import art, design, functions
import os

def Post(Webhook,Message):
    try:
        data = requests.post(Webhook, json={'content': Message})
        if data.status_code == 204 or data.status_code == 200:
            Log(f"Message Sent | {Functions.design.greenblue(f'Code: {str(data.status_code)}')}")
    except Exception as e:
        print(e)
        Log(f"Dead Webhook | {Functions.design.greenblue(Webhook)}")
        time.sleep(5)
        return

def Spam(Webhook,Message,Amount):
    for i in range(Amount):
        try:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Aether | Sent: {str(i)} | A Kyanite Production")
            data = requests.post(Webhook, json={'content': Message})
            if data.status_code == 204 or data.status_code == 200:
                Log(f"Message Sent | {Functions.design.greenblue(f'Code: {str(data.status_code)}')}")
        except Exception as e:
            print(e)
            Log(f"Dead Webhook | {Functions.design.greenblue(Webhook)}")
            time.sleep(5)
            break


def Delete(Webhook):
    try:
        data = requests.delete(Webhook)
        ctypes.windll.kernel32.SetConsoleTitleW(f"Aether | Deleted: {str(Webhook)} | A Kyanite Production")
        if data.status_code == 204 or data.status_code == 200:
            Log(f"Deleted Webhook | {Functions.design.greenblue(f'Code: {str(data.status_code)}')}")
    except Exception as e:
        print(e)
        Log(f"Dead Webhook | {Functions.design.greenblue(Webhook)}")
        time.sleep(5)


def Ping(Webhook):
    try:
        data = requests.post(Webhook, json={'content': "This is a ping"})
        if data.status_code == 204 or data.status_code == 200:
            Log(f"Pinged Webhook (VALID) | {Functions.design.greenblue(f'Code: {str(data.status_code)}')}")
    except Exception as e:
        print(e)
        Log(f"Dead Webhook | {Functions.design.greenblue(Webhook)}")
        time.sleep(5)
        return