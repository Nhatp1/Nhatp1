#dec cái con mẹ mày
#cracked Tool By NgxHieeus

class api_tds(object):
    
    def __init__(self = None, token_tds = None):
        self.token_tds = token_tds
        self.session = requests.Session()

    
    def info(self):
        info = self.session.get(f'https://traodoisub.com/api/?fields=profile&access_token={self.token_tds}').json()
        return info

    
    def run_fb(self, id):
        run = self.session.get(f'https://traodoisub.com/api/?fields=run&id={id}&access_token={self.token_tds}').json()
        return run

    
    def get_nv(self, fields):
        list_nv = self.session.get(f'https://traodoisub.com/api/?fields={fields}&access_token={self.token_tds}').json()
        return list_nv

    
    def get_xu(self, type, id):
        get_xu = self.session.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token_tds}').json()
        return get_xu



class api_fb(object):
    
    def __init__(self,cookies):
        self.session = requests
        self.cookie_origin = cookies
        cookie = cookies.split(';')
        title = []
        value = []
        for i in range(len(cookie) - 1):
            title.append(cookie[i].split('=')[0].strip())
            value.append(cookie[i].split('=')[1].strip())
        self.cookies = dict(zip(title, value))
        self.headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'dpr': '1',
        'referer': 'https://mbasic.facebook.com/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="117.0.5938.132", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"7.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'viewport-width': '708',
        }
        self.uid = self.cookies['c_user']

    def info(self):
        Home = self.session.get(f"https://mbasic.facebook.com/{self.uid}/", headers=self.headers, cookies=self.cookies).text
        self.username = Home.split("<title>")[1].split("</")[0]
        return self.username, self.uid

    
    def follow(self, uid):
        Home = self.session.get(f"https://mbasic.facebook.com/{uid}", headers=self.headers,cookies=self.cookies).text
        try:
            FollowNode = "https://mbasic.facebook.com/a/subscribe.php?"+Home.split('/a/subscribe.php?')[1].split('"')[0].replace("amp;", "")
            Follow = self.session.get(FollowNode,headers=self.headers,cookies=self.cookies)
            if Follow.status_code == 200:
                return Follow
        except:
            return False
    
    def reaction(self, id, type):
        Home = requests.get(f"https://mbasic.facebook.com/{id}",headers=self.headers,cookies=self.cookies).text
        try:
            React = "https://mbasic.facebook.com/reactions/picker/?"+Home.split("/reactions/picker/?")[1].split('"')[0].replace("amp;","")
            ReactWeb = requests.get(React, headers=self.headers,cookies=self.cookies).text
            ReactList = re.findall(r'\/ufi\/reaction\/\?.*?"',ReactWeb)
            index = 0 if type == "LIKE" else 1 if type == "LOVE" else 2 if type == "CARE" else 3 if type == "HAHA" else 4 if type == "WOW" else 5 if type == "SAD" else 6
            ReactComplete = requests.get("https://mbasic.facebook.com/"+ReactList[index].replace("amp;","").replace('"',""),headers=self.headers,cookies=self.cookies)
            return True
        except:
            return False

    def share(self, id_post, content_share):
        Home = self.session.get(f"https://mbasic.facebook.com/{id_post}",   headers=self.headers,cookies=self.cookies).text
        try:
            ShareNode = "https://mbasic.facebook.com/composer/mbasic/?"+Home.split("/composer/mbasic/?")[1].split('"')[0].replace("amp;","")
            ShareWeb = self.session.get(ShareNode, headers=self.headers,cookies=self.cookies).text
            UrlPost = "https://mbasic.facebook.com/composer/mbasic/?csid="+ShareWeb.split('action="/composer/mbasic/?csid=')[1].split('"')[0].replace("amp;","")
            fb_dtsg = ShareWeb.split('name="fb_dtsg" value="')[1].split('"')[0]
            jazoest = ShareWeb.split('name="jazoest" value="')[1].split('"')[0]
            target = ShareWeb.split('name="target" value="')[1].split('"')[0]
            csid = ShareWeb.split('name="csid" value="')[1].split('"')[0]
            privacyx = ShareWeb.split('name="privacyx" value="')[1].split('"')[0]
            appid = ShareWeb.split('name="appid" value="')[1].split('"')[0]
            sid = ShareWeb.split('name="sid" value="')[1].split('"')[0]
            shared_from_post_id = ShareWeb.split('name="shared_from_post_id" value="')[1].split('"')[0]
            data = {
                'fb_dtsg': fb_dtsg,
                'jazoest': jazoest,
                'target': target,
                'csid': csid,
                'c_src': 'share',
                'referrer': 'permalink',
                'ctype': 'advanced',
                'cver': 'amber_share',
                'waterfall_source': 'advanced_composer_timeline',
                'privacyx': privacyx,
                'appid': appid,
                'sid': sid,
                'm': 'self',
                'xc_message': content_share,
                'view_post': 'Chia sẻ',
                'shared_from_post_id': shared_from_post_id,  
            }
            Share = self.session.post(UrlPost,headers=self.headers,cookies=self.cookies,data=data)
            if Share.status_code == 200:
                return Share
        except:
            return False

    
    def like_page(self, id):
        header = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'cookie': self.cookie_origin,
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin' }
        response = self.session.get('https://www.facebook.com/', headers = header).text
        matches = re.findall('\\[\\"DTSGInitialData\\",\\[\\],{\\"token\\":\\"(.*?)\\"}', response)
        if len(matches) > 0:
            self.fb_dtsg = matches[0]
            self.jazoest = response.split('jazoest=')[1].split('"')[0]
            self.actor_id = re.findall('\\"ACCOUNT_ID\\":\\"(.*?)\\"', response)[0]
            self.lsd = re.findall('\\[\\"LSD\\",\\[\\],{\\"token\\":\\"(.*?)\\"}', response)[0]
        response = self.session.post('https://www.facebook.com/api/graphql/', headers = header, data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'lsd': self.lsd,
            'variables': '{"input":{"is_tracking_encrypted":true,"page_id":"' + id + '","source":"unknown","tracking":[],"actor_id":"' + self.actor_id + '","client_mutation_id":"2"},"isAdminView":false}',
            'doc_id': '5556947024325929' })
        return response

    
    def group(self, id):
        header = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'cookie': self.cookie_origin,
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin' }
        response = self.session.get('https://www.facebook.com/', headers = header).text
        matches = re.findall('\\[\\"DTSGInitialData\\",\\[\\],{\\"token\\":\\"(.*?)\\"}', response)
        if len(matches) > 0:
            self.fb_dtsg = matches[0]
            self.jazoest = response.split('jazoest=')[1].split('"')[0]
            self.actor_id = re.findall('\\"ACCOUNT_ID\\":\\"(.*?)\\"', response)[0]
            self.lsd = re.findall('\\[\\"LSD\\",\\[\\],{\\"token\\":\\"(.*?)\\"}', response)[0]
        response = self.session.post('https://www.facebook.com/api/graphql/', headers = header, data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'lsd': self.lsd,
            'variables': '{"feedType":"DISCUSSION","groupID":"' + id + '","imageMediaType":"image/x-auto","input":{"group_id":"' + id + '","source":"group_mall","actor_id":"' + self.actor_id + '","client_mutation_id":"3"},"scale":1,"source":"GROUP_MALL","renderLocation":"group_mall"}',
            'doc_id': '8097744130297884' })
        return response

    
    def comment(self, id_post, content):
        Home = requests.get(f"https://mbasic.facebook.com/{id_post}",headers=self.headers,cookies=self.cookies).text
        try:
            UrlPost = "https://mbasic.facebook.com/a/comment.php?"+Home.split('action="/a/comment.php?')[1].split('"')[0].replace("amp;","")
            fb_dtsg = Home.split('name="fb_dtsg" value="')[1].split('"')[0]
            jazoest = Home.split('name="jazoest" value="')[1].split('"')[0]
            data = {
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'comment_text': content,
            }
            Comment = requests.post(UrlPost,headers=self.headers,cookies=self.cookies,data=data)
            if Comment.status_code == 200:
                return True
        except:
            return False



class NgxHieeus(object):
    
    def __init__(self = None):
        self.session = requests.Session()

    
    def banner(self):
        if platform.node() == "localhost":
            os.system("clear")
        else:
            os.system("cls")
        FIVEX = '[COPYRIGHT: HOÀNG LONG NGŨ - FIVEX (ĐÃ DEC FULL SRC NHƯNG TÔN TRỌNG NGƯỜI LÀM TOOL)]\n[FIVEX    -   ZALO: 0386358592]\n[MOMO: 0355796207 - MB: 0355796207]\n\n'
        for i in FIVEX:
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.01)
                

    
    def delay(self, value):
        while not(value <= 1):
            value -= 0.123
            print(f'''[PVN][DELAY][P V N][{str(value)[0:5]}]''', '               ', end = '\r')
            sleep(0.02)
            print(f'''[PVN][DELAY][ V N ][{str(value)[0:5]}]''', '               ', end = '\r')
            sleep(0.02)
            print(f'''[PVN][DELAY][  P  ][{str(value)[0:5]}]''', '               ', end = '\r')
            sleep(0.02)
            print(f'''[PVN][DELAY][ V N ][{str(value)[0:5]}]''', '               ', end = '\r')
            sleep(0.02)
            print(f'''[PVN][DELAY][P V N][{str(value)[0:5]}]''', '               ', end = '\r')
            sleep(0.02)
        

    
    def countdown(self, value):
        while not(value <= 0) :
            value -= 0.1
            print(f'''[PVN][COUNTDOWN][X    ][{str(value)[0:5]}]''', '               ', end = '\r')
            sleep(0.02)
            print(f'''[PVN][COUNTDOWN][ X   ][{str(value)[0:5]}]''', '               ', end = '\r')
            sleep(0.02)
            print(f'''[PVN][COUNTDOWN][  X  ][{str(value)[0:5]}]''', '               ', end = '\r')
            sleep(0.02)
            print(f'''[PVN][COUNTDOWN][   X ][{str(value)[0:5]}]''', '               ', end = '\r')
            sleep(0.02)
            print(f'''[PVN][COUNTDOWN][    X][{str(value)[0:5]}]''', '               ', end = '\r')
            sleep(0.02)
    
    def main_tds(self):
        NgxHieeus().banner()
        print('[PVN][WAITING]', '               ', end = '\r')
        file_tds_path = "fivex_token_tds.txt"
        with open(file_tds_path, mode="r",encoding="utf-8") as file_token_tds:
            token_tds = file_token_tds.read()
            info = api_tds(token_tds).info()
        if 'error' in info:
            error = info['error'].upper()
            print(f'''[{error}]''')
            exit()
        if 'success' in info:
            user = info['data']['user'].upper()
            xu = info['data']['xu']
            xu_die = info['data']['xudie']
            print(f'''[USER: {user} - XU: {xu} - XU DIE: {xu_die}]\n''')
            print('[ENTER   -  DÙNG TOKEN TDS ĐÃ LƯU]\n[NHẬP BẤT KÌ - NHẬP TOKEN TDS MỚI]\n')
            choice_token = input('NHẬP LỰA CHỌN: ')
            if choice_token != '':
                NgxHieeus().banner()
                token_tds = input('NHẬP ACCESS_TOKEN TDS: ')
                info = api_tds(token_tds).info()
                if 'error' in info:
                    error = info['error'].upper()
                    print(f'''[{error}]''')
        if 'success' in info:
            NgxHieeus().banner()
            if choice_token != '':
                with open(file_token_tds, mode="a+", encoding="utf-8") as file:
                    file.write(token_tds)
            user = info['data']['user'].upper()
            xu = info['data']['xu']
            xu_die = info['data']['xudie']
            print(f'''[USER: {user} - XU: {xu} - XU DIE: {xu_die}]''')
            sleep(1)
        NgxHieeus().banner()
        print('[FIVEX][WAITING]', '               ', end = '\r')
        file_cookie_path = "fivex_cookie.txt"
        file_cookie = open(file_cookie_path, 'r', encoding = 'utf-8')
        list_cookie = []
        for cookie in file_cookie.read().split('\n'):
            if cookie != '' and not(cookie in list_cookie):
                list_cookie.append(cookie)
        print(f'''[PVN][TOTAL {len(list_cookie)} COOKIE FACEBOOK]\n''')
        print('[ENTER   -  DÙNG COOKIE FACEBOOK ĐÃ LƯU]\n[NHẬP BẤT KÌ - NHẬP COOKIE FACEBOOK MỚI]\n')
        choice_cookie = input('NHẬP LỰA CHỌN: ')
        if choice_cookie != "":
            list_cookie = []
            while True:
                cookie = input(f'[NHẬP COOKIE FACEBOOK THỨ {len(list_cookie)+1}]: ')
                if cookie != "":
                    list_cookie.append(cookie)
                else:
                    break
        sleep(1)
        for cookie in list_cookie:
            name_fb, id_fb = api_fb(cookie).info()
            run_fb = api_tds(token_tds).run_fb(id_fb)
            if 'success' in run_fb:
                with open(file_cookie_path, 'a+', encoding = 'utf-8') as file_cookie:
                    file_cookie.write(f'''{cookie}\n''')
                id_fb = run_fb['data']['id']
                msg = run_fb['data']['msg'].upper()
                print(f'''[{name_fb.upper()}][{id_fb}][{msg}]''')
            if 'error' in run_fb:
                error = run_fb['error'].upper()
                print(f'''[{error}]''')
        NgxHieeus().banner()
        print('[1: LIKE - 2: FOLLOW  - 3: REACTION - 4: REACTCMT]\n[5: COMMENT - 6: LIKE PAGE - 7 : SHARE - 8: GROUP]\n')
        print('[CÓ THỂ GHÉP SỐ ĐỂ CHẠY NHIỀU NHIỆM VỤ][VD: 123..]\n')
        print('[JOB REACTCMT (SỐ 4) ĐANG LỖI NÊN MN K CHỌN NHÉ !...]\n')
        list_fields = [
            'follow',
            'reaction',
            'reactcmt',
            'comment',
            'page',
            'share',
            'group']
        like = [
            'like',
            'likegiare',
            'likesieure']
        list_fields_choice = []
        choice_fields = input('NHẬP LỰA CHỌN: ')
        if '1' in choice_fields:
            list_fields_choice = like + list_fields_choice
        for i in choice_fields:
            if 0 <= int(i) - 2 or len(choice_fields) <= 8:
                list_fields_choice.append(list_fields[int(i) - 2])
        sleep(1)
        NgxHieeus().banner()
        min = int(input('DELAY MIN: '))
        if min >= 0:
            pass
        print('[PVN][?]')
        print('[PVN][?]')
        max = int(input('DELAY MAX: '))
        if max >= min:
            pass
        print('[PVN][?]')
        print('[PVN][?]')
        if len(list_cookie) > 1:
            change = int(input('SAU BAO NHIÊU NHIỆM VỤ THÌ ĐỔI NICK: '))
            if change > 0:
                pass
            print('[PVN][?]')
            print('[PVN][?]')
        change = 0
        stop = int(input('SAU BAO NHIÊU NHIỆM VỤ THÌ DỪNG TOOL: '))
        if stop > 0:
            pass
        print('[PVN][?]')
        print('[PVN][?]')
        total = 0
        change_ = 0
        countdown = 100
        NgxHieeus().banner()
        while True:
            for cookie in list_cookie:
                fail = 0
                change_ += 1
                fb = api_fb(cookie)
                (name_fb, id_fb) = fb.info()
                run_fb = api_tds(token_tds).run_fb(id_fb)
                if 'success' in run_fb:
                    id_fb = run_fb['data']['id']
                    msg = run_fb['data']['msg'].upper()
                    print(f'''[TOTAL: {len(list_cookie)} COOKIE LIVE][{name_fb.upper()}][{id_fb}][{msg}]''')
                else:
                    error = run_fb['error'].upper()
                    print(f'''[TOTAL: {len(list_cookie)} COOKIE LIVE][{error}]''')
                tds = api_tds(token_tds)
                for fields in list_fields_choice:
                    print(f'''[PVN][{fields.upper()}][WAITING]''', '               ', end = '\r')
                    list_nv = api_tds(token_tds).get_nv(fields)
                    if 'countdown' in list_nv and float(list_nv['countdown']) <= countdown:
                        NgxHieeus().countdown(float(list_nv['countdown']) + 1.5)
                    for nv in list_nv:
                        try:
                            id = nv['id']
                        except:
                            print('[PVN][NETWORK ERROR !]', '               ', end = '\r')
                        if fields == "follow":
                            try:
                                fb.follow(id)
                                get_xu = tds.get_xu(type=fields.upper(),id=id)
                            except:
                                print('[PVN][NETWORK ERROR !]', '               ', end = '\r')
                        
                        elif fields == "like" or fields == "likegiare" or fields == "likesieure":
                            try:
                                fb.reaction(id=id, type="LIKE")
                                get_xu = tds.get_xu(type=fields.upper(),id=id)
                            except:
                                print('[PVN][NETWORK ERROR !]', '               ', end = '\r')
                        elif fields == "reaction":
                            try:
                                type_reaction = nv['type']
                                fb.reaction(id=id, type=type_reaction)
                                get_xu = tds.get_xu(type=type_reaction,id=id)
                            except:
                                print('[PVN][NETWORK ERROR !]', '               ', end = '\r')
                        elif fields == "share":
                            try:
                                fb.share(id=id, content_share="")
                                get_xu = tds.get_xu(type=fields.upper(),id=id)
                            except:
                                print('[PVN][NETWORK ERROR !]', '               ', end = '\r')
                        elif fields == "group":
                            try:
                                fb.group(id=id)
                                get_xu = tds.get_xu(type=fields.upper(),id=id)
                            except:
                                print('[PVN][NETWORK ERROR !]', '               ', end = '\r')
                        elif fields == "page":
                            try:
                                fb.like_page(id=id)
                                get_xu = tds.get_xu(type=fields.upper(),id=id)
                            except:
                                print('[PVN][NETWORK ERROR !]', '               ', end = '\r')
                        if 'success' in get_xu:
                            fail = 0
                            total += 1
                            xu = get_xu['data']['xu']
                            msg = get_xu['data']['msg'].upper()
                            time = datetime.now().strftime('%H:%M:%S')
                            try:
                                print(f'''[PVN][{total}][{time}][{type_reaction}][{msg}][{xu}]''')
                            except:
                                print(f'''[PVN][{total}][{time}][{fields.upper()}][{msg}][{xu}]''')    
                            NgxHieeus().delay(randint(min, max))
                        fail += 1
                        print(f'''[PVN][{total}][{datetime.now().strftime('%H:%M:%S')}][FAILURE!]''', '          ', end = '\r')
                        if total == stop:
                            pass
                        if fail % 5 == 0 and fail != 0:
                            pass
                        if total == change * change_ and len(list_cookie) > 1:
                            pass
                        print('[PVN][NETWORK ERROR !]', '               ', end = '\r')
                        if total == stop:
                            pass
                    if fail % 10 == 0 and fail != 0:
                        pass
                    if total == change * change_ and len(list_cookie) > 1:
                        pass
                    if total == stop:
                        pass
                if fail % 10 == 0 and fail != 0:
                    print(f'''[PVN][{datetime.now().strftime('%H:%M:%S')}][{name_fb.upper()}][{type.upper()}][FAILURE: {fail}]''')



if __name__ == '__main__':
    from datetime import datetime
    from bs4 import BeautifulSoup
    from random import randint
    from time import sleep
    import re
    import requests
    import os
    import sys
    import platform

    fivex = NgxHieeus()
    fivex.banner()
    print('Xin chào, mình là FIVEX  TOOL')
    print("Nhập 'fivex' để vào tool...")
    user_input = input("=> ").lower()
    if (user_input == "fivex"):
        print("Xác thực thành công...")
        fivex.banner()
        fivex.main_tds()
    else:
        print("Xác thực không thành công...\nTạm biệt!")
        os.remove(sys.argv[0])

#Con này đang bị chặn follow nên kh bật job follow nhé
