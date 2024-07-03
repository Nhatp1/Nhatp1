import requests
import threading
from time import sleep
from art import *
import os
from colorama import Fore
from random import randint
os.system('cls' if os.name == 'nt' else 'clear')
tprint("DENO","rnd-xlarge")
print(Fore.RED+'\t\tTOOL BY NHẬT')

def AUTO(file):
    headers = {
            'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Origin': 'https://hamsterkombat.io',
            'Referer': 'https://hamsterkombat.io/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
            'accept': 'application/json',
            'authorization': file,
            'content-type': 'application/json',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
        }
    soluongclick = randint(20,50)
    json_data = {
        'count': soluongclick,
        'availableTaps': 1,
        'timestamp': 1718033141,
    }
    count = str(soluongclick)
    response = requests.post('https://api.hamsterkombat.io/clicker/tap', headers=headers, json=json_data).text
    sleep(2)
    coin = str(response)
    totalcoin = coin.split('"balanceCoins":')[1].split(",")[0]
    print(Fore.WHITE+'ĐÃ CLICK '+Fore.RED+count+Fore.WHITE+' LAN SO COIN CUA BAN : '+Fore.YELLOW+totalcoin)
    response2 = requests.post('https://api.hamsterkombat.io/clicker/sync', headers=headers).text
    boosturl = 'https://api.hamsterkombat.io/clicker/boosts-for-buy'
    response3 = requests.post(boosturl,headers=headers).text
    SR1 = str(response3).split('"BoostFullAvailableTaps"')[1].split('"level"')[0]
    CD = SR1.split('ds":')[1].split(',')[0]
    if int(CD)==0:
        print(Fore.CYAN+'DANG BOOST...')
        Buy_boost = 'https://api.hamsterkombat.io/clicker/buy-boost'
        json_data = {
            'boostId': 'BoostFullAvailableTaps',
            'timestamp': 1718196045,
        }
        boost = requests.post(Buy_boost,headers=headers,json=json_data).text
def LEVEL(LEVELUP,response,upgradesuser,ATLEVEL):
    soluongclick = randint(20,50)
    json_data = {
        'count': soluongclick,
        'availableTaps': 1,
        'timestamp': 1718033141,
    }
    count = str(soluongclick)
    response1 = requests.post('https://api.hamsterkombat.io/clicker/tap', headers=headers, json=json_data).text
    sleep(2)
    coin = str(response1)
    totalcoin = coin.split('"balanceCoins":')[1].split(",")[0]
    print(Fore.WHITE+'DA CLICK '+Fore.RED+count+Fore.WHITE+' LAN SO COIN CUA BAN : '+Fore.YELLOW+totalcoin)
    response2 = requests.post('https://api.hamsterkombat.io/clicker/sync', headers=headers).text
    boosturl = 'https://api.hamsterkombat.io/clicker/boosts-for-buy'
    response3 = requests.post(boosturl,headers=headers).text
    SR1 = str(response3).split('"BoostFullAvailableTaps"')[1].split('"level"')[0]
    CD = SR1.split('ds":')[1].split(',')[0]
    if int(CD)==0:
        print(Fore.CYAN+'DANG BOOST...')
        Buy_boost = 'https://api.hamsterkombat.io/clicker/buy-boost'
        json_data = {
            'boostId': 'BoostFullAvailableTaps',
            'timestamp': 1718196045,
        }
        boost = requests.post(Buy_boost,headers=headers,json=json_data).text
    if int(LEVELUP)<ATLEVEL:
        return 0
    else:
        UPGRADE(upgradesuser,LEVELUP)
def UPGRADE(upgradesuser,LEVELUP):
    API = 'https://api.hamsterkombat.io/clicker/buy-upgrade'
    json = {
        'timestamp': 1718467685286,
        'upgradeId': upgradesuser,
    }
    LEVELUPAPI = requests.post(API,headers=headers,json=json).json()
    response2 = requests.post('https://api.hamsterkombat.io/clicker/sync', headers=headers)
    if "clickerUser" in LEVELUPAPI:
        print('DA NANG CAP CARD LEVEL HIEN TAI LA : '+Fore.YELLOW+str(LEVELUPAPI["clickerUser"]["upgrades"][upgradesuser]['level']))
        if int(LEVELUPAPI["clickerUser"]["upgrades"][upgradesuser]['level'])<=int(LEVELUP):
            return 0
        else :
            UPGRADE(upgradesuser,LEVELUP)
def running2():
    response = requests.post('https://api.hamsterkombat.io/clicker/tap', headers=headers, json=json_data).json()
    response2 = requests.post('https://api.hamsterkombat.io/clicker/sync', headers=headers).text
    
    responsetext = str(response)
    upgradeslist = []
    i = 0
    print('_________________________________________________')
    for upgrades in response["clickerUser"]["upgrades"]:
        print(Fore.CYAN+str(i)+'.'+upgrades)
        upgradeslist.append(upgrades)
        i+=1
    print('_________________________________________________')
    choose= int(input("\n\n\n NHAP LUA CHON : "))
    upgradesuser = upgradeslist[choose]
    ATLEVEL = int(response["clickerUser"]["upgrades"][upgradesuser]['level'])
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[NHATTOOL] LEVEL CARD HIEN TAI : "+str(response["clickerUser"]["upgrades"][upgradesuser]['level']))
    print("[NHATTOOL] LUU Y : CHI DUNG VOI CARD DA MO KHOA!\n[*] LUU Y : NHAP LEVEL PHAI LON CHON LEVEL HIEN TAI")
    LEVELUP = int(input(Fore.GREEN+'\n\n\n[+] NHAP LEVEL MUON AUTO NANG CAP : '))
    soluong = int(input(Fore.GREEN+'[+] NHAP SO LAN CLICK : '))
    autoclick = []
    for i in range(1,soluong):
        response = requests.post('https://api.hamsterkombat.io/clicker/tap', headers=headers, json=json_data).json()
        response2 = requests.post('https://api.hamsterkombat.io/clicker/sync', headers=headers).text
        ATLEVEL = int(response["clickerUser"]["upgrades"][upgradesuser]['level'])
        t=threading.Thread(target=LEVEL(LEVELUP,response,upgradesuser,ATLEVEL+1))
        autoclick.append(t)
    for t in autoclick:
        t.start()
def running(file):
    soluong = int(input(Fore.GREEN+'[+] NHAP SO LAN CLICK : '))
    autoclick = []
    for i in range(1,soluong):
        t=threading.Thread(target=AUTO(file))
        autoclick.append(t)
    for t in autoclick:
        t.start()
def MORSE():
    MORSE = input(Fore.GREEN+'NHAP MA MORSE (DANG CHU VIET HOA) : ')
    json_data ={
        'cipher': MORSE,
    }
    response = requests.post('https://api.hamsterkombat.io/clicker/claim-daily-cipher', headers=headers, json=json_data).text
    if 'clickerUser' in response:
        print(Fore.CYAN+'NHAP MA THANH CONG!')
    else:
        print(Fore.RED+'NHAP MA THAT BAI!')
checkfile = os.path.isfile('AUTH.txt')
if checkfile == False:
    AUTHUR = input(Fore.GREEN+'[+]''NHAP Authorization : ')
    createfile = open('AUTH.txt','w')
    createfile.write(AUTHUR)
    createfile.close()
    readfile = open('AUTH.txt','r')
    file = readfile.read()
    readfile.close()
    headers = {
            'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Origin': 'https://hamsterkombat.io',
            'Referer': 'https://hamsterkombat.io/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
            'accept': 'application/json',
            'authorization': file,
            'content-type': 'application/json',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
        }
    os.system('cls' if os.name == 'nt' else 'clear')
    tprint("HAMSTER KOMBAT","rnd-xlarge")
    print(Fore.RED+'\t\tTOOL BY NHẬT')
    print(Fore.RED+'\t\tHAMSTER KOMBAT V3.0')
    print(Fore.CYAN+'[NHATTOOL] 1.CHAY AUTO THUONG (AUTO CLICK + BOOST)')
    print(Fore.CYAN+'[NHATTOOL] 2.CHAY AUTO VIP (AUTO UPGRADE CARD + AUTO CLICK + BOOST)')
    print(Fore.CYAN+'[NHATTOOL] 3.NHAP MA MORSE HANG NGAY')
    choose = int(input(Fore.GREEN+'\n\n\nNHAP LUA CHON CUA BAN : '))  
    if choose==1:
        running(file)
    elif choose == 2:
        running2()
    elif choose == 3:
        MORSE()
else:
    readfile = open('AUTH.txt','r')
    file = readfile.read()
    readfile.close()
    headers = {
            'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Origin': 'https://hamsterkombat.io',
            'Referer': 'https://hamsterkombat.io/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
            'accept': 'application/json',
            'authorization': file,
            'content-type': 'application/json',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
        }
    json_data = {
        'count': 35,
        'availableTaps': 6674,
        'timestamp': 1718443699,
    }
    print(Fore.CYAN+'[NHATTOOL] Authorization HIEN TAI : '+file)
    print(Fore.RED+'[NHATTOOL] 1.XOA Authorization HIEN TAI')
    print(Fore.RED+'[NHATTOOL] 2.SU DUNG Authorization CU')
    choose = int(input(Fore.CYAN+'\n\n\nNHAP LUA CHON : '))
    os.system('cls' if os.name == 'nt' else 'clear')
    tprint("HAMSTER KOMBAT","rnd-xlarge")
    print(Fore.RED+'\t\tTOOL BY NHẬT')
    print(Fore.RED+'\t\tHAMSTER KOMBAT V3.0')
    if choose==2:
        print(Fore.CYAN+'[NHATTOOL] 1.CHAY AUTO THUONG (AUTO CLICK + BOOST)')
        print(Fore.CYAN+'[NHATTOOL] 2.CHAY AUTO VIP (AUTO UPGRADE CARD + AUTO CLICK + BOOST)')
        print(Fore.CYAN+'[NHATTOOL] 3.NHAP MA MORSE HANG NGAY')
        choose = int(input(Fore.GREEN+'\n\n\nNHAP LUA CHON CUA BAN : ')) 
        os.system('cls' if os.name == 'nt' else 'clear')
        tprint("HAMSTER KOMBAT","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY NHẬT')
        print(Fore.RED+'\t\tHAMSTER KOMBAT V3.0')
        if choose==1:
            running(file)
        elif choose == 2:
            running2()
        elif choose == 3:
            MORSE()
    else:
        os.remove('AUTH.txt')


