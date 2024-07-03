# Source Generated with Decompyle++
# File: regpro5_dump_(code)_306.txt_pyc.pyc (Python 3.11)

import requests
import os
import random
from time import sleep
list_clone = []
list_img = []
dem = 0
stt = 0
stt2 = 0

class API_PRO5_ByNgDucPhat:
    
    def banner(self):
        if os.name == 'nt':
            pass
        'cls'('clear')
        banner = 'TOOL REG PRO5'
        print(banner)

    
    def ndp_delay_tool(self, p):
        if p > 1:
            p = p - 1
            print(f'''[ 🌺 NHẬT - TOOL 🌺][|][LO......][{p}]''', '     ', end = '\r')
            sleep(0.166667)
            print(f'''[ 🌺 NHẬT - TOOL 🌺][/][LOA.....][{p}]''', '     ', end = '\r')
            sleep(0.166667)
            print(f'''[ 🌺 NHẬT - TOOL 🌺][-][LOAD....][{p}]''', '     ', end = '\r')
            sleep(0.166667)
            print(f'''[ 🌺 NHẬT - TOOL 🌺][+][LOADI...][{p}]''', '     ', end = '\r')
            sleep(0.166667)
            print(f'''[ 🌺 NHẬT - TOOL 🌺][\\][LOADIN..][{p}]''', '     ', end = '\r')
            sleep(0.166667)
            print(f'''[ 🌺 NHẬT - TOOL 🌺][|][LOADING.][{p}]''', '     ', end = '\r')
            sleep(0.166667)
            return None

    
    def getthongtinfacebook(self = None, cookie = None):
        headers_get = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'viewport-width': '1184',
            'cookie': cookie }
        print('\x1b[38;5;208mĐang Tiến Hành Check Live', end = '\r')
        url_profile = requests.get('https://www.facebook.com/me', headers = headers_get).url
        get_dulieu_profile = requests.get(url = url_profile, headers = headers_get).text
        return False
        uid_get = cookie.split('c_user=')[1].split(';')[0]
        fb_dtsg_get = get_dulieu_profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
        jazoest_get = get_dulieu_profile.split('{"name":"jazoest","value":"')[1].split('"},')[0]
        name_get = get_dulieu_profile.split('<title>')[1].split('</title>')[0]
        return (name_get, uid_get, fb_dtsg_get, jazoest_get)
        uid_get = cookie.split('c_user=')[1].split(';')[0]
        fb_dtsg_get = get_dulieu_profile.split(',"f":"')[1].split('","l":null}')[0]
        jazoest_get = get_dulieu_profile.split('&jazoest=')[1].split('","e":"')[0]
        name_get = get_dulieu_profile.split('<title>')[1].split('</title>')[0]
        return (name_get, uid_get, fb_dtsg_get, jazoest_get)
        return False

    
    def UpAvt(self, cookie, id_page, link_anh):
        sleep(5)
        json_upavt = requests.get(f'''https://api-ndpcutevcl.000webhostapp.com/api/upavtpage.php?cookie={cookie}&id={id_page}&link_anh={link_anh}''').json()
        if json_upavt['status'] == 'success':
            return json_upavt
        return None
        return False

    
    def RegPage(self, cookie, name, uid, fb_dtsg, jazoest):
        global dem
        namepage = requests.get('https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/male?count=2').json()['data'][0]['name']
        headers_reg = cookie
        data_reg = {
            '__spin_r': '1006496476',
            '__spin_b': 'trunk',
            '__spin_t': '1667200829',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
            'variables': '{"input":{"bio":"reg auto by dp","categories":["181475575221097"],"creation_source":"comet","name":"' + namepage + '","page_referrer":"launch_point","actor_id":"' + uid + '","client_mutation_id":"1"}}',
            'server_timestamps': 'true',
            'doc_id': '5903223909690825' }
        idpage = requests.post('https://www.facebook.com/api/graphql/', headers = headers_reg, data = data_reg, timeout = 20).json()['data']['additional_profile_plus_create']['additional_profile']['id']
        dem += 1
        print(f'''\x1b[38;5;46m{dem} | SUCCESS | NAME FB: {name} | UID PRO5: {idpage} | NAME PRO5: {namepage}''')
        return idpage
        '800444344545377'
        print('\x1b[38;5;46mReg Thất Bại Có Vẻ Acc Của Bạn Đã Bị Block!!')
        return False


dpcutevcl = API_PRO5_ByNgDucPhat()
dpcutevcl.banner()
print('\x1b[38;5;208m[ENTER - ĐỂ DỪNG NHẬP]')
stt += 1
cookie_fb = input(f'''\x1b[38;5;46mVUI LÒNG NHẬP COOKIE THỨ [{stt}]: ''')
if cookie_fb == '':
    pass
checklive = dpcutevcl.getthongtinfacebook(cookie_fb)
if checklive != False:
    print('Name Facebook: ' + checklive[0])
    list_clone.append(f'''{cookie_fb}|{checklive[0]}|{checklive[1]}|{checklive[2]}|{checklive[3]}''')
    print('──────────────────────────────────────────────────')
stt - 1
print('Cookie ' + cookie_fb.split('c_user=')[1].split(';')[0] + ', Die Or Out Vui Lòng Kiểm Tra Lại!!')
print('──────────────────────────────────────────────────')
luachon = input('\x1b[38;5;208mBẠN MUỐN REG PAGE XONG UP AVT KHÔNG? [Y/N]: ')
print('──────────────────────────────────────────────────')
print('[\x1b[38;5;46mENTER - ĐỂ DỪNG NHẬP]')
stt2 += 1
link_img = input(f'''\x1b[38;5;208mVUI LÒNG NHẬP LINK ẢNH THỨ [{stt2}]: ''')
if link_img == '':
    pass
list_img.append(link_img)
print('──────────────────────────────────────────────────')
slpage = int(input('\x1b[38;5;46mBẠN MUỐN TẠO BAO NHIÊU PAGE THÌ DỪNG TOOL: '))
print('──────────────────────────────────────────────────')
delay = int(input('\x1b[38;5;46mVUI LÒNG NHẬP DELAY REG PAGE: '))
print('──────────────────────────────────────────────────')
dpcutevcl.banner()
print('──────────────────────────────────────────────────')
print('\x1b[38;5;208mĐã Tìm Thấy: ' + str(len(list_clone)) + ' Cookie')
print('\x1b[38;5;46mĐã Tìm Thấy: ' + str(len(list_img)) + ' Link Image')
print('──────────────────────────────────────────────────')
for dulieuclone in list_clone:
    idpage = dpcutevcl.RegPage(str(dulieuclone).split('|')[0], str(dulieuclone).split('|')[1], str(dulieuclone).split('|')[2], str(dulieuclone).split('|')[3], str(dulieuclone).split('|')[4])
    if luachon == 'Y' or luachon == 'y':
        link_anh = random.choice(list_img)
        dpcutevcl.UpAvt(str(dulieuclone).split('|')[0], idpage, link_anh)
        if dpcutevcl != False:
            print(f'''\x1b[38;5;208m╰─> UP_AVT_SUCCESS | [UID PAGE: {idpage}]''')
        print(f'''\x1b[38;5;208m╰─> UP_AVT_ERROR | [UID PAGE: {idpage}]''')
    dpcutevcl.ndp_delay_tool(delay)
    if dem == slpage:
        input(f'''\x1b[38;5;46mDone {dem}, Page </> ENTER ĐỂ EXIT''')
        exit()
