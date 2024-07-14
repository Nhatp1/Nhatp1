def banner():
    print("    ____  _____  ____  ____       _     _________   _________    ___      ___   _____     
|_   \|_   _||_   ||   _|     / \   |  _   _  | |  _   _  | .'   `.  .'   `.|_   _|    
  |   \ | |    | |__| |      / _ \  |_/ | | \_| |_/ | | \_|/  .-.  \/  .-.  \ | |      
  | |\ \| |    |  __  |     / ___ \     | |         | |    | |   | || |   | | | |   _  
 _| |_\   |_  _| |  | |_  _/ /   \ \_  _| |_       _| |_   \  `-'  /\  `-'  /_| |__/ | 
|_____|\____||____||____||____| |____||_____|     |_____|   `.___.'  `.___.'|________| 
                                                                                       ")
    print('        \x1b[1;37mCopyright © NHAT TOOL | Version 2.0\n\x1b[1;31m────────────────────────────────────────────────────────\n\x1b[1;37m~\x1b[1;31m[\x1b[1;32m●\x1b[1;31m]\x1b[1;37m ➩\x1b[1;35m Admin: \x1b[1;36m NHẬT TOOL \n\x1b[1;37m~\x1b[1;31m[\x1b[1;32m●\x1b[1;31m]\x1b[1;37m ➩\x1b[1;36m Zalo: \x1b[1;31m0386358592\n\x1b[1;37m~\x1b[1;31m[\x1b[1;32m●\x1b[1;31m]\x1b[1;37m ➩\x1b[1;32m Box Zalo: \x1b[1;37mhttps://zalo.me/g/ozebne540\n\x1b[1;37m~\x1b[1;31m[\x1b[1;32m●\x1b[1;31m]\x1b[1;37m ➩\x1b[1;33m BOX SPAM SMS : \x1b[1;37mhttps://t.me/sharebotvip\n\x1b[1;31m────────────────────────────────────────────────────────\n ')
den = '\x1b[1;90m'
luc = '\x1b[1;32m'
trang = '\x1b[1;37m'
red = '\x1b[1;31m'
vang = '\x1b[1;33m'
tim = '\x1b[1;35m'
lamd = '\x1b[1;34m'
lam = '\x1b[1;36m'
purple = '\\e[35m'
hong = '\x1b[1;95m'
thanh_xau = trang + '~' + red + '[' + vang + '⟨⟩' + red + '] ' + trang + '➩ ' + luc
thanh_dep = trang + '~' + red + '[' + vang + '✓' + red + '] ' + trang + '➩ ' + luc

import requests ,json 
from time import sleep 
from datetime import datetime 
import os 
from sys import platform 
from threading import Thread 
OO0O0OO0O0OOOOOO0 ='mb'if platform [0 :3 ]=='lin'else 'pc'
def O000O0OOO0000OO00 (OO0O000O0O0OOOOO0 ,OOOO0000O0OOOO0OO ,OOO0O0OO0O00OOO00 ):
	OO00O00O0O000O0O0 =datetime .now ().strftime ("%H:%M:%S")
	print (f'{vang}[{trang}{OO0O000O0O0OOOOO0}{vang}] {red}| {lam}{OO00O00O0O000O0O0} {red}| {vang}{OOOO0000O0OOOO0OO} {red}| {trang}{OOO0O0OO0O00OOO00} {red}|')
class OOOOOO000O0O0O0O0 (object ):
	def __init__ (OO00000O000OOO00O ,O0O0O00OOO000O000 ):
		OO00000O000OOO00O .token =O0O0O00OOO000O000 
	def login (O0O000OOOOO0OOO0O ):
		try :
			O0000OO0O0OO0OO00 =requests .post ('https://tuongtaccheo.com/logintoken.php',headers ={'Content-type':'application/x-www-form-urlencoded',},data ={'access_token':O0O000OOOOO0OOO0O .token })
			OOO000O0O0O000O0O =O0000OO0O0OO0OO00 .json ()['data']['user']
			O00OO0OOOO00O0OOO =O0000OO0O0OO0OO00 .json ()['data']['sodu']
			O0O000OOOOO0OOO0O .cookie ='PHPSESSID='+(O0000OO0O0OO0OO00 .cookies )['PHPSESSID']
			return OOO000O0O0O000O0O ,O00OO0OOOO00O0OOO 
		except :
			try :print (red +O0000OO0O0OO0OO00 .json ()['mess'])
			except :print (red +' Kiểm Tra Kết Nối Mạng (không đc sử dụng ip nước ngoài)')
			return False 
	def coin (O000OO00O00000O0O ):
		try :
			O0OO000000O00O00O ={'user-agent':'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36','cookie':O000OO00O00000O0O .cookie }
			OOO0OO0OOOOOOO00O =requests .post ('https://tuongtaccheo.com/home.php',headers =O0OO000000O00O00O ).text 
			OO00OOOO0O00OOOO0 =OOO0OO0OOOOOOO00O .split ('"soduchinh">')[1 ].split ('<')[0 ]
			return OO00OOOO0O00OOOO0 
		except :
			return False 
	def getnv (OOOO0O00O00OO000O ,OO0O00O0OOOO00000 ):
		try :
			OOO00O0O0O00OO00O ={'Content-type':'application/x-www-form-urlencoded','accept':'application/json, text/javascript, */*; q=0.01','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':OOOO0O00O00OO000O .cookie ,'referer':'https://tuongtaccheo.com/kiemtien/','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36','x-requested-with':'XMLHttpRequest'}
			O000O00OO0OOOOO0O =requests .post (f'https://tuongtaccheo.com/tiktok/kiemtien/{OO0O00O0OOOO00000}',headers =OOO00O0O0O00OO00O ).json ()
			return O000O00OO0OOOOO0O 
		except :
			return False 
	def nhantien (O00OO0OO000O000O0 ,O000OOOO000O00OO0 ,OOOOO00O00O000OOO ):
		try :
			OO0O0OO0OOO0OOO0O ='id='+O000OOOO000O00OO0 
			O00000OO0OOOO0OO0 =str (len (OO0O0OO0OOO0OOO0O ))
			O000OOO000O0OO000 ={'accept':'*/*','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-length':O00000OO0OOOO0OO0 ,'content-type':'application/x-www-form-urlencoded; charset=UTF-8','cookie':O00OO0OO000O000O0 .cookie ,'referer':'https://tuongtaccheo.com/kiemtien/','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36','x-requested-with':'XMLHttpRequest'}
			OOOOO000OO0OOOOO0 =requests .post (f'https://tuongtaccheo.com/tiktok/kiemtien/{OOOOO00O00O000OOO}',headers =O000OOO000O0OO000 ,data =OO0O0OO0OOO0OOO0O )
			if 'mess'in OOOOO000OO0OOOOO0 .text :
				O00OOOO0OO000OOO0 =OOOOO000OO0OOOOO0 .json ()['sodu']
				global O0O00OO0OO0O00O0O 
				O0O00OO0OO0O00O0O +=O00OOOO0OO000OOO0 
				OOO0OOO0OO0OOO000 =500 if OOOOO00O00O000OOO =='nhantien.php'else 1300 
				O0000OOO0O0OO000O =O00OOOO0OO000OOO0 //OOO0OOO0OO0OOO000 
				OO0O00O0O000OO0OO (14 )
				print (f'{lam}Nhận Thành Công {O0000OOO0O0OO000O} Nhiệm Vụ {red}| {luc}+{O00OOOO0OO000OOO0} {red}| {vang}{O0O00OO0OO0O00O0O}')
				OO0O00O0O000OO0OO (14 )
				if O00OOOO0OO000OOO0 ==0 :return False 
			elif '"error2":'in OOOOO000OO0OOOOO0 .text :
				print (red ,OOOOO000OO0OOOOO0 .json ()['error2'])
				OO0O00O0O000OO0OO (14 )
				return False 
			elif '"error":'in OOOOO000OO0OOOOO0 .text :
				print (red ,OOOOO000OO0OOOOO0 .json ()['error'])
				OO0O00O0O000OO0OO (14 )
			else :
				print (red +'Nhận Xu Thất Bại Vui, Lòng Thử Lại ')
				OO0O00O0O000OO0OO (14 )
		except :
			return False 
	def run (O0O0OOOO000O0OO0O ,OO0000OO0OOOOO000 ):
		try :
			O0O000OO00O000000 ={'Content-type':'application/x-www-form-urlencoded','accept':'application/json, text/javascript, */*; q=0.01','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','referer':'https://tuongtaccheo.com/cauhinh/tiktok.php','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36','x-requested-with':'XMLHttpRequest','cookie':O0O0OOOO000O0OO0O .cookie }
			O000OOOO00O0OO0O0 =requests .post ('https://tuongtaccheo.com/cauhinh/datnick.php',headers =O0O000OO00O000000 ,data ={'iddat[]':OO0000OO0OOOOO000 ,'loai':'tt'}).json ()
			return O000OOOO00O0OO0O0 
		except :
			return False 
	def acc_cau_hinh (OOO00O00000O000OO ):
		try :
			OOO00O0OOO000O00O =requests .get ('https://tuongtaccheo.com/cauhinh/tiktok.php',headers ={'user-agent':'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36','cookie':OOO00O00000O000OO .cookie }).text 
			O0000OO0O00OOO0OO =OOO00O0OOO000O00O .split ('Nick đang dùng:')[1 ].split ('/> ')[1 ].split ('<')[0 ]
			return O0000OO0O00OOO0OO 
		except :
			return False 
def OO0OOOOO000O00O00 (O0O0O0OOOOO0000O0 ):
  try :
    for O0O00OO0OOO0OO00O in range (O0O0O0OOOOO0000O0 ,-1 ,-1 ):
       print (f'{vang}[{trang}NGOCTOOL{vang}]['+trang +str (O0O00OO0OOO0OO00O )+vang +' Giây]           ',end ='\r')
       sleep (1 )
  except :
     sleep (O0O0O0OOOOO0000O0 )
     print (O0O0O0OOOOO0000O0 ,end ='\r')
def OO0O00O0O000OO0OO (OOOO0O0OO0O0OOO00 ):
	for O0OOO0OO0O00000OO in range (OOOO0O0OO0O0OOO00 ):
		print (red +'────',end ='')
	print ('')
def O0OOO0O0O0000OOO0 (OO0OOO00O0OOO0O0O ,O00000OOOOOOO00O0 ):
	if O00000OOOOOOO00O0 =='mb':
		os .system (f'xdg-open {OO0OOO00O0OOO0O0O}')
	else :
		os .system (f'cmd /c start {OO0OOO00O0OOO0O0O}')
def OOOO0OO000O0OOOO0 (OOO00OO0O00O00OO0 ):
	try :
		OO00000OOOO000OOO =requests .get (f'https://now.tiktok.com/@{OOO00OO0O00O00OO0}',headers ={'user-agent':'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36'}).text 
		OO000O0000OOO0OO0 =OO00000OOOO000OOO .split ('{"id":"')[1 ].split ('"')[0 ]
		OOOO000OO000O000O =OO00000OOOO000OOO .split ('"nickname":"')[1 ].split ('"')[0 ]
		return OO000O0000OOO0OO0 ,OOOO000OO000O000O 
	except :
		return False 
def OO000000000O000OO ():
	OOO000O00OOOOOOOO =0 
	OOO0OO00000O0O000 =0 
	OO0O0OO000O00O0O0 =0 
	OOOO0OOO000OO0O0O =''
	global O0O00OO0OO0O00O0O 
	banner ()
	while True :
		if os .path .exists ('configttc.txt'):
			with open ('configttc.txt','r')as O0000O0O0O0OO0O00 :
				O0O0O0O0OOOOOO000 =O0000O0O0O0OO0O00 .read ()
			OOOOOO00000O0OO00 =OOOOOO000O0O0O0O0 (O0O0O0O0OOOOOO000 )
			OOOO0OO00000O000O =OOOOOO00000O0OO00 .login ()
			if OOOO0OO00000O000O !=False :
				print (f'{thanh_xau}{luc}Nhập {vang}[{trang}1{vang}] {luc}Giữ Lại Tài Khoản {vang}'+OOOO0OO00000O000O [0 ])
				print (f'{thanh_xau}{luc}Nhập {vang}[{trang}2{vang}] {luc}Nhập Access_Token TTC Mới')
				OOOOO00O00OO0OO00 =input (f'{thanh_xau}{luc}Nhập {trang}===>: {vang}')
				if OOOOO00O00OO0OO00 =='2':
					os .remove ('configttc.txt')
				elif OOOOO00O00OO0OO00 =='1':
					pass 
				else :
					print (red +'Lựa chọn không xác định !!!');OO0O00O0O000OO0OO (14 )
					continue 
			else :
				os .remove ('configttc.txt')
		if not os .path .exists ('configttc.txt'):
			O0O0O0O0OOOOOO000 =input (f'{thanh_xau}{luc}Nhập Access_Token TTC: {vang}')
			with open ('configttc.txt','w')as O0000O0O0O0OO0O00 :
				O0000O0O0O0OO0O00 .write (O0O0O0O0OOOOOO000 )
		with open ('configttc.txt','r')as O0000O0O0O0OO0O00 :
			O0O0O0O0OOOOOO000 =O0000O0O0O0OO0O00 .read ()
		OOOOOO00000O0OO00 =OOOOOO000O0O0O0O0 (O0O0O0O0OOOOOO000 )
		OOOO0OO00000O000O =OOOOOO00000O0OO00 .login ()
		if OOOO0OO00000O000O !=False :
			O0O00OO0OO0O00O0O =OOOO0OO00000O000O [1 ]
			OO0OOO00O0O0OO00O =OOOO0OO00000O000O [0 ]
			print (lam +' Đăng Nhập Thành Công ')
			break 
		else :
			os .remove ('configttc.txt')
			continue 
	banner ()
	print (f'{thanh_xau}{luc}Tên Tài Khoản: {vang}{OO0OOO00O0O0OO00O}')
	print (f'{thanh_xau}{luc}Xu Hiện Tại: {vang}{O0O00OO0OO0O00O0O}')
	OO0O00O0O000OO0OO (14 )
	while True :
		OO0O0OO000O00O0O0 =0 
		print (f'{thanh_xau}{luc}Nhập {red}[{vang}1{red}] {luc}Để Chạy Nhiệm Vụ Tim')
		print (f'{thanh_xau}{luc}Nhập {red}[{vang}2{red}] {luc}Để Chạy Nhiệm Vụ Follow')
		print (f'{thanh_xau}{luc}Nhập {red}[{vang}3{red}] {luc}Để Chạy Nhiệm Vụ Follow Tiktok Now')
		print (f'{thanh_xau}{luc}Nhập {red}[{vang}4{red}] {luc}Để Chạy Nhiệm Vụ Follow Tiktok Qua Video')
		OO0OOO0OO000O00O0 =input (f'{thanh_xau}{luc}Nhập Số Để Chạy Nhiệm Vụ: {vang}')
		OO0OOO000OOO0O000 =int (input (f'{thanh_xau}{luc}Nhập Delay:{vang} '))
		OO0O00O0O000OO0OO (14 )
		while True :
			if OO0O0OO000O00O0O0 ==2 :break 
			OO0O0OO000O00O0O0 =0 
			OO00O00000O0OO0OO =int (input (f'{thanh_xau}{luc}Sau Bao Nhiêu Nhiệm Vụ Thì Nhận Xu: {vang}'))
			if OO00O00000O0OO0OO <8 :
				print (f'{red}Trên 8 Nhiệm Vụ Mới Được Nhận Tiền!')
				continue 
			OOO0O0OO0O00OO0O0 =OOOOOO00000O0OO00 .acc_cau_hinh ()
			if OOO0O0OO0O00OO0O0 !=False :
				print (f'{thanh_xau}{luc}Enter Để Dùng Cấu Hình Đã Lưu: {vang}{OOO0O0OO0O00OO0O0}')
			OO0OOO00O0O0OO00O =input (f'{thanh_xau}{luc}Nhập User Name Cần Cấu Hình:{vang} ')
			if OOO0O0OO0O00OO0O0 !=False and OO0OOO00O0O0OO00O =='':
				OO0O00O0O000OO0OO (14 )
				print (f'{lam}User {vang}{OOO0O0OO0O00OO0O0} {lam}Đã Được Cấu Hình Trước Đó')
			else :
				OO0O0000OOOOOOO00 =OOOO0OO000O0OOOO0 (OO0OOO00O0O0OO00O )
				if OO0O0000OOOOOOO00 ==False :print (red +'Sai User Name Tik Tok.');continue 
				O00OO0OO0000000OO =OOOOOO00000O0OO00 .run (OO0O0000OOOOOOO00 [0 ])
				print (O00OO0OO0000000OO )
				if O00OO0OO0000000OO ==1 :OO0O00O0O000OO0OO (14 );print (f'{luc}Đang Cấu Hình ID: {vang}{OO0O0000OOOOOOO00[0]} {red}| {luc}User: {vang}{OO0OOO00O0O0OO00O} {red}| {luc}Tên: {trang}{OO0O0000OOOOOOO00[1]} ');OO0O00O0O000OO0OO (14 )
				else :print (f'{red}Cấu Hình Thất Bại User: {vang}{OO0OOO00O0O0OO00O}');continue 
			while True :
				if OO0O0OO000O00O0O0 ==1 or OO0O0OO000O00O0O0 ==2 :break 
				if '1'in OO0OOO0OO000O00O0 :
					O000OO0OO0OOOO0O0 =OOOOOO00000O0OO00 .getnv ('getpost.php')
					if O000OO0OO0OOOO0O0 ==False :print (red +'Không Get Được Nhiệm Vụ Tim !');sleep (1 );print ('                                               ',end ='\r');continue 
					elif len (O000OO0OO0OOOO0O0 )==0 :print (red +'Hết Nhiệm Vụ Tim ',end ='\r');sleep (1 );print ('                                            ',end ='\r');continue 
					else :
						print (f'{luc}Tìm Thấy{vang}',len (O000OO0OO0OOOO0O0 ),f'{luc}Nhiệm Vụ Tim',end ='\r');sleep (1 );print ('                                            ',end ='\r');
						for OO000OOOOO0OO0000 in O000OO0OO0OOOO0O0 :
							OO0O00OO0O00000OO =OO000OOOOO0OO0000 ['link'];OO0O0000OOOOOOO00 =OO000OOOOO0OO0000 ['idpost']
							Thread (target =O0OOO0O0O0000OOO0 ,args =(OO0O00OO0O00000OO ,OO0O0OO0O0OOOOOO0 )).start ()
							OOOO0OOO000OO0O0O =OOOO0OOO000OO0O0O +str (OO0O0000OOOOOOO00 )+',';OOO0OO00000O0O000 +=1 ;O000O0OOO0000OO00 (OOO0OO00000O0O000 ,'TIM',OO0O0000OOOOOOO00 );OO0OOOOO000O00O00 (OO0OOO000OOO0O000 )
							if OOO0OO00000O0O000 %OO00O00000O0OO0OO ==0 :
								sleep (1 )
								OO0OO0O00000OO00O =OOOOOO00000O0OO00 .nhantien (OOOO0OOO000OO0O0O ,'nhantien.php')
								OOOO0OOO000OO0O0O =''
								if OO0OO0O00000OO00O ==False :
									print (luc +'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ')
									print (f'{thanh_xau}{luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
									print (f'{thanh_xau}{luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
									print (f'{thanh_xau}{luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
									OOOOO00O00OO0OO00 =input (f'{thanh_xau}{luc}Nhập {trang}===>: {vang}')
									OO0O00O0O000OO0OO (14 )
									if OOOOO00O00OO0OO00 =='1':OO0O0OO000O00O0O0 =2 ;break 
									elif OOOOO00O00OO0OO00 =='2':OO0O0OO000O00O0O0 =1 ;break 
				if OO0O0OO000O00O0O0 ==1 or OO0O0OO000O00O0O0 ==2 :break 
				if '2'in OO0OOO0OO000O00O0 :
					O000OO0OO0OOOO0O0 =OOOOOO00000O0OO00 .getnv ('subcheo/getpost.php')
					if O000OO0OO0OOOO0O0 ==False :print (red +'Không Get Được Nhiệm Vụ Follow !');sleep (1 );print ('                                               ',end ='\r');continue 
					elif len (O000OO0OO0OOOO0O0 )==0 :print (red +'Hết Nhiệm Vụ Follow ',end ='\r');sleep (1 );print ('                                            ',end ='\r');continue 
					else :
						print (f'{luc}Tìm Thấy{vang}',len (O000OO0OO0OOOO0O0 ),f'{luc}Nhiệm Vụ Follow',end ='\r');sleep (1 );print ('                                            ',end ='\r');
						for OO000OOOOO0OO0000 in O000OO0OO0OOOO0O0 :
							OO0O00OO0O00000OO =OO000OOOOO0OO0000 ['link'];OO0O0000OOOOOOO00 =OO000OOOOO0OO0000 ['idpost']
							Thread (target =O0OOO0O0O0000OOO0 ,args =(f'https://www.tiktok.com/@{OO0O00OO0O00000OO}',OO0O0OO0O0OOOOOO0 )).start ()
							OOOO0OOO000OO0O0O =OOOO0OOO000OO0O0O +str (OO0O0000OOOOOOO00 )+',';OOO0OO00000O0O000 +=1 ;O000O0OOO0000OO00 (OOO0OO00000O0O000 ,'FOLLOW',OO0O0000OOOOOOO00 );OO0OOOOO000O00O00 (OO0OOO000OOO0O000 )
							if OOO0OO00000O0O000 %OO00O00000O0OO0OO ==0 :
								sleep (1 )
								OO0OO0O00000OO00O =OOOOOO00000O0OO00 .nhantien (OOOO0OOO000OO0O0O ,'subcheo/nhantien.php')
								OOOO0OOO000OO0O0O =''
								if OO0OO0O00000OO00O ==False :
									print (luc +'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ')
									print (f'{thanh_xau}{luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
									print (f'{thanh_xau}{luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
									print (f'{thanh_xau}{luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
									OOOOO00O00OO0OO00 =input (f'{thanh_xau}{luc}Nhập {trang}===>: {vang}')
									OO0O00O0O000OO0OO (14 )
									if OOOOO00O00OO0OO00 =='1':OO0O0OO000O00O0O0 =2 ;break 
									elif OOOOO00O00OO0OO00 =='2':OO0O0OO000O00O0O0 =1 ;break 
				if OO0O0OO000O00O0O0 ==1 or OO0O0OO000O00O0O0 ==2 :break 
				if '3'in OO0OOO0OO000O00O0 :
					O000OO0OO0OOOO0O0 =OOOOOO00000O0OO00 .getnv ('subcheo/getpost.php')
					if O000OO0OO0OOOO0O0 ==False :print (red +'Không Get Được Nhiệm Vụ Follow !');sleep (1 );print ('                                               ',end ='\r');continue 
					elif len (O000OO0OO0OOOO0O0 )==0 :print (red +'Hết Nhiệm Vụ Follow ',end ='\r');sleep (1 );print ('                                            ',end ='\r');continue 
					else :
						print (f'{luc}Tìm Thấy{vang}',len (O000OO0OO0OOOO0O0 ),f'{luc}Nhiệm Vụ Follow',end ='\r');sleep (1 );print ('                                            ',end ='\r');
						for OO000OOOOO0OO0000 in O000OO0OO0OOOO0O0 :
							OO0O00OO0O00000OO =OO000OOOOO0OO0000 ['link'];OO0O0000OOOOOOO00 =OO000OOOOO0OO0000 ['idpost']
							Thread (target =O0OOO0O0O0000OOO0 ,args =(f'https://now.tiktok.com/@{OO0O00OO0O00000OO}',OO0O0OO0O0OOOOOO0 )).start ()
							OOOO0OOO000OO0O0O =OOOO0OOO000OO0O0O +str (OO0O0000OOOOOOO00 )+',';OOO0OO00000O0O000 +=1 ;O000O0OOO0000OO00 (OOO0OO00000O0O000 ,'FOLLOW_TIKTOK_NOW',OO0O0000OOOOOOO00 );OO0OOOOO000O00O00 (OO0OOO000OOO0O000 )
							if OOO0OO00000O0O000 %OO00O00000O0OO0OO ==0 :
								sleep (1 )
								OO0OO0O00000OO00O =OOOOOO00000O0OO00 .nhantien (OOOO0OOO000OO0O0O ,'subcheo/nhantien.php')
								OOOO0OOO000OO0O0O =''
								if OO0OO0O00000OO00O ==False :
									print (luc +'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ')
									print (f'{thanh_xau}{luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
									print (f'{thanh_xau}{luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
									print (f'{thanh_xau}{luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
									OOOOO00O00OO0OO00 =input (f'{thanh_xau}{luc}Nhập {trang}===>: {vang}')
									OO0O00O0O000OO0OO (14 )
									if OOOOO00O00OO0OO00 =='1':OO0O0OO000O00O0O0 =2 ;break 
									elif OOOOO00O00OO0OO00 =='2':OO0O0OO000O00O0O0 =1 ;break 
				if OO0O0OO000O00O0O0 ==1 or OO0O0OO000O00O0O0 ==2 :break 
				if '4'in OO0OOO0OO000O00O0 :
					O000OO0OO0OOOO0O0 =OOOOOO00000O0OO00 .getnv ('subcheo/getpost2.php')
					if O000OO0OO0OOOO0O0 ==False :print (red +'Không Get Được Nhiệm Vụ Follow !');sleep (1 );print ('                                               ',end ='\r');continue 
					elif len (O000OO0OO0OOOO0O0 )==0 :print (red +'Hết Nhiệm Vụ Follow ',end ='\r');sleep (1 );print ('                                            ',end ='\r');continue 
					else :
						print (f'{luc}Tìm Thấy{vang}',len (O000OO0OO0OOOO0O0 ),'{luc}Nhiệm Vụ Follow',end ='\r');sleep (1 );print ('                                            ',end ='\r');
						for OO000OOOOO0OO0000 in O000OO0OO0OOOO0O0 :
							OO0O00OO0O00000OO =OO000OOOOO0OO0000 ['link'];OO0O0000OOOOOOO00 =OO000OOOOO0OO0000 ['idpost']
							Thread (target =O0OOO0O0O0000OOO0 ,args =(f'{OO0O00OO0O00000OO}',OO0O0OO0O0OOOOOO0 )).start ()
							OOOO0OOO000OO0O0O =OOOO0OOO000OO0O0O +str (OO0O0000OOOOOOO00 )+',';OOO0OO00000O0O000 +=1 ;O000O0OOO0000OO00 (OOO0OO00000O0O000 ,'FOLLOW',OO0O0000OOOOOOO00 );OO0OOOOO000O00O00 (OO0OOO000OOO0O000 )
							if OOO0OO00000O0O000 %OO00O00000O0OO0OO ==0 :
								sleep (1 )
								OO0OO0O00000OO00O =OOOOOO00000O0OO00 .nhantien (OOOO0OOO000OO0O0O ,'subcheo/nhantien.php')
								OOOO0OOO000OO0O0O =''
								if OO0OO0O00000OO00O ==False :
									print (luc +'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ')
									print (f'{thanh_xau}{luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
									print (f'{thanh_xau}{luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
									print (f'{thanh_xau}{luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
									OOOOO00O00OO0OO00 =input (f'{thanh_xau}{luc}Nhập {trang}===>: {vang}')
									OO0O00O0O000OO0OO (14 )
									if OOOOO00O00OO0OO00 =='1':OO0O0OO000O00O0O0 =2 ;break 
									elif OOOOO00O00OO0OO00 =='2':OO0O0OO000O00O0O0 =1 ;break 
OO000000000O000OO ()
