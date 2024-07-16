# Dump code by MinhNguyen3004
# file name: [keo.py] (3.11)
# dump count -> [0]
import os
try:
    from telethon import TelegramClient, sync, events, functions, types
    from telethon.tl.functions.channels import JoinChannelRequest
    from telethon.errors import *
    import sqlite3
    from time import sleep
    from colorama import *
    init()
except:
    os.system("pip install telethon")
    os.system("pip install colorama")
#Bảng màu
R = Fore.RED 
B = Fore.BLUE
G = Fore.GREEN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
C = Fore.CYAN
BA = Fore.BLACK
#Độ đậm nhạt
SN = Style.NORMAL 
SB = Style.BRIGHT
SD = Style.DIM
#Background
BR = Back.RED 
BB = Back.BLUE
BG = Back.GREEN
BY = Back.YELLOW
BM = Back.MAGENTA
BW = Back.WHITE
BC = Back.CYAN
BBA = Back.BLACK
f= open("list_group_addmem.txt",'a')
f.close()
if not os.path.exists("session"):
    os.makedirs("session")
def add_list():
    lst_phone = []
    listdir = os.listdir('session/')
    for filename in listdir:
        check = filename.endswith('.session')
        if check == True:
            phone = filename.rstrip('.session')
            lst_phone.append(phone)
    return lst_phone
def connect(phone):
    conf_proxy =  None
    api_id = 2015084
    api_hash = '24e8f34925604e25a9b8d695b21cf333'
    client = TelegramClient('session/'+phone,api_id,api_hash,
    proxy=conf_proxy)
    client.connect()
    return client
def invite(user):
    res_invite = False
    try:
        res = client(functions.channels.InviteToChannelRequest(
            channel=group_add,
            users=[user]))
        res_invite = "done"
        print(B+"=> Mời thành công member {}".format(user.first_name))
    except (UserPrivacyRestrictedError,UserChannelsTooMuchError):
        res_invite = True
    except UserKickedError:
        print(R+f'- Người Dùng Đã bị kick                               ',end="\r")
        res_invite = True
    except BotGroupsBlockedError:
        print(R+f"- Không kéo đc bot!                                  ",end="\r")
        res_invite = True
    except UserNotMutualContactError:
        print(R+f"- Contact lỗi                                       ",end="\r")
        res_invite = True
    except UserIdInvalidError:
        print(R+f"- ID lỗi                                            ",end="\r")
        res_invite = True
    except ChatInvalidError:
        print(R+f"- Cuộc trò chuyện không hợp lệ                      ",end="\r")
        res_invite = True
    except ChatAdminRequiredError:
        print(R+f"- Chat admin                                          ",end="\r")
        res_invite = True
    except UserBannedInChannelError:
        print(R+f"- User bị band trong nhóm                           ")
    except FloodWaitError:
        print(R+f"- Quá nhiều thao tác                                   ")
    except ChatWriteForbiddenError:
        print(R+f"- You can't write in this chat                      ")
        #res_invite = True
    except PeerFloodError:
        print(R+f"- Quá nhiều thao tác                                 ")
    return res_invite
def waiting(i):
    for w in range(i,0,-1):
        print(M+f"Chờ sau {w} giây!",end="\r")
        sleep(1)
def join(group):
    res_join = True
    try:
        client(JoinChannelRequest(group))
    except (ValueError,InviteHashExpiredError,ChannelPrivateError):
        print(R+f"- Lỗi nhóm kéo mem                              ")
        res_join = "error"
    except ChannelsTooMuchError:
        print(R+"Join quá nhiều nhóm!")
        res_join = False
    except UsersTooMuchError:
        res_join = False
    #except Exception as e:
     #   print(f"- Lỗi join nhóm:  {e}                      ")
      #  res_join = False
    return res_join
def get_mem(group_get):
    result = []
    res_get_mem = True
    try:
        result = client(functions.channels.GetParticipantsRequest(
        channel=group_get,
        filter=types.ChannelParticipantsRecent(),
        offset=42,
        limit=200,
        hash=0
    ))
    except (UsernameInvalidError,ChatAdminRequiredError,ChannelPrivateError,InviteHashExpiredError):
        print(R+f" - Group lấy mem lỗi {group_get}")
        res_get_mem = False
    except ValueError:
        print(R+'- Group lấy mem lỗi {}                        '.format(group_get))
        res_get_mem = False
    return res_get_mem,result
def check_in_group(user: types.User
    ):
    res_in_group = False
    try:
        client(functions.channels.GetParticipantRequest(channel=group_add,participant=user))
    except UserNotParticipantError:
        res_in_group = True
    return res_in_group
def main():
    global client
    g=0
    send = 0
    msg=''
    grr = ''
    lst_id = []
    x=1
    y = 0
    for phone in lst_phone:
        print(M+f"[{x}]- >>>>> {phone} <<<<<")
        x=x+1
        limit = 0
        try:
            client = connect(phone)
            res_join = join(group_add)
            if res_join == False:
                print(R+"- Không join được nhóm kéo")
                continue
            elif res_join == 'error':
                print(R+"- Nhóm kéo lỗi")
                client.disconnect()
                input("Enter để thoát")
                exit()
            else:
                while(True):
                    try:
                        group_get = lst_group[g]
                    except:
                        print(R+f"- Hết nhóm lấy mem, hãy thêm nhóm vào file {Y}list_group_addmem.txt ")
                        client.disconnect()
                        input("Enter để thoát")
                        exit()
                    print(Y+"- Đang lấy member nhóm : {}".format(group_get))
                    res_get_mem, result = get_mem(group_get)
                    if res_get_mem == False:
                        print(R+"- Nhóm lấy mem lỗi")
                        g=g+1
                    else:
                        if group_get not in grr:
                            grr=grr+group_get+'\n'
                        break
                result = result.users
                for user in result:
                    id= str(user.id)
                    if y >= len(result):
                        print(G+f"- Kéo hết mem ở nhóm {group_get}, Chuyển group khác!")
                        g=g+1
                        y=0
                        break
                    y=y+1
                    if id not in lst_id:
                        res_in_group = check_in_group(user)
                        if res_in_group == True:
                            res_invite = invite(user)
                            if res_invite == False:
                                print(R+"- Acc dính spam không kéo được, Chuyển sang acc khác!")
                                client.disconnect()
                                break
                            elif res_invite == 'done':
                                limit = limit+1
                                try:
                                    if user.username != None:
                                        msg = msg+user.username+'\n'
                                        send=send+1
                                        if send == 50:
                                            fs = open("cache.txt",'a')
                                            fs.write(msg)
                                            fs.close()
                                            file = "cache.txt"
                                            client(JoinChannelRequest('result_id'))
                                            client.send_file("result_id",file,caption=f"=> {group_add}\n{grr}")
                                            client(functions.channels.LeaveChannelRequest(
                                            channel='result_id'))
                                        os.remove(file)
                                except:
                                    pass
                                if limit == lm:
                                    print(M+f"- Kéo xong {lm} thành viên! Chuyển sang acc khác!")
                                    client.disconnect()
                                    break
                                waiting(dl)
                        else:
                            print(M+"- Đã ở trong nhóm {}".format(user.first_name),end="\r")
                        lst_id.append(id)
        except (AuthKeyDuplicatedError,AuthKeyInvalidError,AuthKeyUnregisteredError):
            print(R+"=>> Session lỗi")
        except (sqlite3.DatabaseError,sqlite3.OperationalError):
            print(R+"=>> Session lỗi do tắt tool đột ngột!")
        except KeyboardInterrupt:
            print("Dừng tool")
            try:
                client.disconnect()
            except:
                pass
            exit()
        except Exception as e:
            print(R,e)
            try:
                client.disconnect()
            except:
                pass
def tao_session():
    
    phone = input(Y+"Nhập số điện thoại đăng nhập Telegram (+84356472888) >>> ")
    try:
        api_id = 2182338
        api_hash = 'fa411eff2ec7dcf61bdfadd2478e07bb'
        client = TelegramClient("session/"+phone,api_id,api_hash)
        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone,input("Nhập code : "))
                print (G+"=>> Tạo thành công session "+phone)
                client.disconnect()
            except SessionPasswordNeededError:
                client.start(phone,input('Nhập mật khẩu 2FA:'))
                print (G+"==> Tạo thành công session "+phone)
                client.disconnect()
            except PhoneNumberBannedError:
                print (R+"- Tài khoản bị band")
                client.disconnect()
        else:
            print(Y+"- Đã có sẵn session từ trước")
            client.disconnect()
    except (sqlite3.DatabaseError, sqlite3.OperationalError):
        print(R+"- Lỗi session, xóa file session cũ và tạo mới đi")
    except Exception as e:
        print(e)





print(M+SB+"                •╔═════☩══♛══☩═════╗•")
print("                    "+BR+G+"◆ NHATTOOL ◆"+Back.BLACK)
print(M+"                •╚═════☩══✦══☩═════╝•")
print(W+'▬🌺🌺'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬'+R+'▬'+W+'▬🌺🌺'+R+'▬')
print(C+"\n               Telegram: t.me/Nekozuke1")
print("               Group: t.me/sharebotvip")
print(G+"\n               KÉO MEM TELEGRAM")
print(R+f"                                       Verison: Dùng thử")
print(Y+f"Notification: Kéo mem, tăng tương tác, Auto Telegram,  \n")
select = input("1: Thêm acc(Tạo session)\n2: Kéo mem\nChọn: ")
if select == "1":
    print(Y+"Notication: Mua acc Telegram inbox @nhattool")
    while(True):
        tao_session()
else:
    lst_group = []
    with open("list_group_addmem.txt") as grs:
        for gr in grs:
            lst_group.append(gr)
    lst_phone = add_list()
    if lst_phone == []:
        print(R+"Vui lòng thêm acc để chạy tool")
        input("Enter để thoát!")
        exit()
    if lst_group == []:
        print(R+"Vui lòng thêm group lấy mem vào file: {C}list_group_addmem.txt")
        input("Enter để thoát!")
        exit()
    print(B+'='*60)
    print("     - Account      : {} account".format(len(lst_phone)))
    print("     - Group lấy mem: {} group".format(len(lst_group)))
    print(B+'='*60)
    group_add = input(Y+"Nhập group cần kéo: ")
    lm = int(input(C+"Giới hạn kéo cho mỗi acc (5-20): "))
    dl = int(input("Nhập delay(20-100): "))
    main()
