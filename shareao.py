import os
import sys
import aiohttp
import asyncio
import datetime
import time

# Định nghĩa các mã màu
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

# Đọc nội dung từ file vào list
def read_lines_from_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            return [line.strip() for line in lines if line.strip()]  # Loại bỏ các dòng trống và loại bỏ khoảng trắng
    except FileNotFoundError:
        print(f"{do}File {filename} không tồn tại.")
        return []

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    ban = f'''{do}

███████╗██╗  ██╗ █████╗ ██████╗ ███████╗               █████╗  ██████╗ 
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝              ██╔══██╗██╔═══██╗
███████╗███████║███████║██████╔╝█████╗      █████╗    ███████║██║   ██║
╚════██║██╔══██║██╔══██║██╔══██╗██╔══╝      ╚════╝    ██╔══██║██║   ██║
███████║██║  ██║██║  ██║██║  ██║███████╗              ██║  ██║╚██████╔╝
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝              ╚═╝  ╚═╝ ╚═════╝ 
                                                                       

{luc}</> Tool by NTOOL </>{luc}
_____________________________________________________________________
{trang}[{do}</>{trang}] {vang}TOOL SHARE ẢO PRO5 MAX SPEED 
{trang}[{do}</>{trang}] {luc}ADMIN: {hong}NHATTOOL
{trang}[{do}</>{trang}] {hong}BOT SPAM SMS: {do} https://t.me/sharebotvip
_____________________________________________________________________
'''
    for i in ban:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.000012)

success = []
list_token = []

# API Lấy ID từ traođổi sub
async def getid(session, link):
    async with session.post('https://id.traodoisub.com/api.php', data={"link": link}) as response:
        rq = await response.json()
        if 'success' in rq:
            return rq["id"]
        else:
            exit(f"{do}Link post sai!!! Vui lòng nhập lại")

# API Lấy danh sách token từ Facebook
async def get_token(session, token, cookie):
    params = {
        'access_token': token
    }
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    async with session.get('https://graph.facebook.com/me/accounts', params=params, headers=headers) as r:
        rq = await r.json()
        if 'data' in rq:
            return rq
        else:
            exit("Token Hoặc Cookie Sai! Vui lòng nhập lại")

# API chính - Share Facebook
async def shareao(session, tk, ck, post):
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'cookie': ck,
            'priority': 'u=0, i',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
        }
        async with session.get(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{post}&published=0&access_token={tk}', headers=headers) as response:
            json = await response.json()
            if 'id' in json:
                print(xduong,len(success),current_time,"|",json['id'],"| Success")
                success.append(json['id'])
            else:
                print(do,len(success),current_time,": Failure")
                break

async def main(link, cookies_file, tokens_file):
    banner()
    async with aiohttp.ClientSession() as session:
        post = await getid(session, link)
        
        # Đọc danh sách cookie từ file
        cookies = read_lines_from_file(cookies_file)
        if not cookies:
            exit(f"{do}Mày thêm cookie chưa, hoặc die cookie rồi:))")
        
        # Đọc danh sách token từ file
        tokens = read_lines_from_file(tokens_file)
        if not tokens:
            exit(f"{do}Mày thêm token chưa, hoặc die token rồi:))")
        
        # Lấy token từng tài khoản
        total_tokens = 0
        for token in tokens:
            token_data = await get_token(session, token, cookies[0])  # Chỉ lấy cookie đầu tiên trong danh sách
            if 'data' in token_data:
                list_token.extend([t["access_token"] for t in token_data["data"]])
                total_tokens += len(token_data["data"])
                print(f"{luc}Token Tage: {vang}{len(token_data['data'])}")
        
        banner()
        print(hong,f"Tổng Số Token: {vang}{total_tokens}")
        await asyncio.gather(*[shareao(session, tk, cookies[0], post) for tk in list_token])  # Sử dụng cookie đầu tiên trong danh sách
        print(luc,"Success Share:",len(success))

# Chạy tool
if __name__ == "__main__":
    banner()
    link = input(f"{luc}Link Post: {vang}")
    cookies_file = input(f"{luc}File Cookie (Ví dụ: cookie.txt): {vang}")
    tokens_file = input(f"{luc}File Token (Ví dụ: token.txt): {vang}")
    asyncio.run(main(link, cookies_file, tokens_file))
