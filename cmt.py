import requests,sys,os,time,random

# SETUP TOOL
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
put = f"{trang}[{do}+{trang}] => {luc}"
out = f"{trang}[{do}-{trang}] => {luc}"
list_cmt = []
tokenl = []
list_acc = []
success = []

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    ban = f'''
\x1b[38;5;226m╔═════════════════════════════════════════════════════════════════╗

\x1b[38;5;226m╠═════════════════════════════════════════════════════════════════╣
\x1b[38;5;226m║\x1b[38;5;46m▶ Nhóm Zalo  : \x1b[38;5;207mhttps://zalo.me/g/ozebne540                       \x1b[38;5;226m║
\x1b[38;5;226m╚═════════════════════════════════════════════════════════════════╝
\x1b[38;5;46m-----------------------------------------------------------------
'''
    for i in ban:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.00)

def sleep(delay):
    for i in range(delay, -1, -1):
        print(f"Vui lòng đợi sau {i} giây để tiếp tục...",end='')
        print("\r",end='')
        time.sleep(1)

def huytool():
    print(f"{luc}---------------------------------------------------------------------------")

def tool_cmt(session, listcmt, tokenl, post, sl, time, acc, jsondatapage):
    while True:
        for acccmt in acc:
            tokenrun = tokenl[acccmt]
            name = jsondatapage['data'][acccmt]['name']
            id = jsondatapage['data'][acccmt]['id']
            print(f"{out}TÊN : {vang}{name} {luc}: ID : {xduong}{id}")
            for i in range(int(sl)):
                message = random.choice(listcmt)
                data = {
                    'access_token': tokenrun,
                    'message': message
                }
                rq = session.post(f"https://graph.facebook.com/{post}/comments", data=data).json()
                if 'id' in rq:
                    print(f"{trang}[{do}{len(success)+1}{trang}]{luc} MESSAGE : {message} : STATUS : SUCCESS")
                    success.append(rq['id'])
                    sleep(time)
                else:
                    print(f"{trang}[{do}{i+1}{trang}]{vang} MESSAGE : {message} : STATUS : FAILED")
                    break

banner()
session = requests.Session()
id_post = input(f"{put}Nhập ID Bài Viết: {vang}")
cookie = input(f"{put}Nhập Cookie Acc: {vang}")
session.cookies.update({'cookie': cookie})
token = "EAAG"+session.get('https://business.facebook.com/business_locations/').text.split("EAAG")[1].split('"')[0]
getpage = session.get(f"https://graph.facebook.com/me/accounts?access_token={token}").json()
for getp in getpage['data']:
    print(f"{trang}[{do}{len(tokenl)+1}{trang}] {luc}Tên : {vang}{getp['name']}{luc} : ID : {xduong}{getp['id']}")
    tokenl.append(getp['access_token'])
huytool()
soacc = input(f"{put}Nhập Acc Cần Chạy Comment (1+2+3...) Hoặc (all): {vang}")
if soacc == 'all':
    for i in range(len(tokenl)):
        list_acc.append(i)
else:
    acc = soacc.split('+')
    for accrun in acc:
        list_acc.append(int(accrun)-1)
huytool()
while True:
    socmt = int(len(list_cmt))+1
    cmt = input(f"{out}Nhập Comments {socmt}: {vang}")
    if cmt == '':
        break
    list_cmt.append(cmt)
huytool()
slcmt = input(f"{put}Sau Bao Nhiêu Comments Thì Đổi Acc: {vang}")
delaytime = int(input(f"{put}Delay Comments: {vang}"))
huytool()
tool_cmt(session,list_cmt,tokenl,id_post,slcmt,delaytime,list_acc,getpage)
