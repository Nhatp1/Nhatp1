print(""" \033[97m█████████\033[1;97m\033[37m
 \033[97m█▄█████▄█\033[1;97m
 \033[97m█\033[91m▼▼▼▼▼▼\033[97m\033[97m  
 \033[97m█\033[97m      \033[91m \033[97m TOOL OBFUSCATION X DECRYPTION \033[91m>\033[97m NHẬT TOOL\033[96m  
 \033[97m█\033[91m▲▲▲▲▲▲\033[97m\033[97m
 \033[97m█████████ \033[1;97m\033[31m
 \033[97m ██ ██           
""")

__builtins__.bbllaacckk_minhh_tokenize = __import__('tokenize')
__builtins__.bbllaacckk_sieu_nhan_gao_den = __import__('os')
__builtins__.bbllaacckk_sieu_nhan_gao_hong = __import__('subprocess')
__builtins__.bbllaacckk_khong_co_gi_la_kho = __import__('sys')
__builtins__.bbllaacckk_sieu_nhan_gao_trang = __import__('marshal')
__builtins__.bbllaacckk_minhh_dep_trai_dang_test_thu_unhexlify = __import__('binascii').unhexlify
__builtins__.bbllaacckk_minhh_BytesIO = __import__('io').BytesIO
__builtins__.bbllaacckk_stdout__ = __import__('sys').stdout
__builtins__.bbllaacckk_nhung_modules_bi_khoa = ['os', 'threading', 'subprocess', 'sys']
__builtins__.bbllaacckk___devnull__ = open('nul' if __builtins__.bbllaacckk_sieu_nhan_gao_den.name == 'nt' else '/dev/null', 'wb')

try:
    __cpy_syspath__ = __cpy_syspath__ + "\\python.exe"
except NameError:
    __cpy_syspath__ = __builtins__.bbllaacckk_khong_co_gi_la_kho.executable

class bbllaacckk_NguyenMinhTricker:
    def rm_filedechay():
        try:
            __import__("shutil").rmtree("_filedechay_")
        except:
            pass
    def get_py_ver():
        return ".".join(__builtins__.bbllaacckk_khong_co_gi_la_kho.version.split(" ")[0].split(".")[:-1])
    def get_f_d(bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum):
        file_name = "/".join(bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum.split(".")[0].split("\\")).split("/")[-1]
        folder = "/".join(bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum.split("\\")).split("/")[:-1]
        if __builtins__.bbllaacckk_sieu_nhan_gao_den.name == 'nt':
            folder = "\\".join(folder) + "\\"
            if folder == "\\":
                folder = "." + folder
        else:
            folder = "/".join(folder) + "/"
            if folder == "/":
                folder = "." + folder
        return file_name,folder
    def get_license(file_name, bbllaacckk_day_la_binary):
        return f"# HYPERION DEOBF BY NguyenMinhTricker\n# FB : https://fb.me/i.urs.bin.python.NguyenMinhh \n# FILE NAME : [{file_name}.py] (".encode('utf8') + str('pyc' if bbllaacckk_day_la_binary else 'py').encode('utf8') + " - ".encode('utf8') + __builtins__.bbllaacckk_NguyenMinhTricker.get_py_ver().encode('utf8') + ")\n\n".encode('utf8')
    def get_code(self):
        return __builtins__.bbllaacckk_NguyenMinhTricker_tokenize.untokenize(self.ntokens)
    def replace_var(self, target, var):
        self.ntokens = []
        for token in self.content:
            string = token.string

            if int(token.type) == 1:
                if str(string) == str(target):
                    string = str(var)

            self.ntokens.append(__builtins__.bbllaacckk_minhh_tokenize.TokenInfo(token.type, string, token.start, token.end, token.line))
        self.put_code(self.get_code())

    def put_code(self, content):
        self.content = list(__builtins__.bbllaacckk_minhh_tokenize.tokenize(__builtins__.bbllaacckk_minhh_BytesIO(content).readline))

    def replace_by_minhh_dep_trai(tai_sao_em_khong_dua_cho_anh_code, bbllaacckk_thang_nao_bao_em_khong_dep_trai, bbllaacckk_tao_dep_trai_nhat_vu_tru):
        tai_sao_em_khong_dua_cho_anh_code = tai_sao_em_khong_dua_cho_anh_code.split(b"\n")
        for __builtins__.bbllaacckk_minhh_dep_trai_qua in range(0, len(tai_sao_em_khong_dua_cho_anh_code), 1):
            if bbllaacckk_thang_nao_bao_em_khong_dep_trai in tai_sao_em_khong_dua_cho_anh_code[__builtins__.bbllaacckk_minhh_dep_trai_qua]:
                __builtins__.bbllaacckk_sieu_nhan_gao_do = tai_sao_em_khong_dua_cho_anh_code[__builtins__.bbllaacckk_minhh_dep_trai_qua]
                for __builtins__.bbllaacckk_sieu_nhan_gao_xanh in range(0, len(__builtins__.bbllaacckk_sieu_nhan_gao_do), 1):
                    try:
                        if __builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_sieu_nhan_gao_xanh:__builtins__.bbllaacckk_sieu_nhan_gao_xanh+len(bbllaacckk_thang_nao_bao_em_khong_dep_trai)] == bbllaacckk_thang_nao_bao_em_khong_dep_trai:
                            if (__builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_sieu_nhan_gao_xanh+len(bbllaacckk_thang_nao_bao_em_khong_dep_trai):__builtins__.bbllaacckk_sieu_nhan_gao_xanh+len(bbllaacckk_thang_nao_bao_em_khong_dep_trai)+1] in globals()["mot_dong_string_rat_dai"]) or (__builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_sieu_nhan_gao_xanh-1:__builtins__.bbllaacckk_sieu_nhan_gao_xanh] in globals()["mot_dong_string_rat_dai"]):
                                break
                            else:
                                __builtins__.bbllaacckk_sieu_nhan_gao_do = __builtins__.bbllaacckk_sieu_nhan_gao_do[:__builtins__.bbllaacckk_sieu_nhan_gao_xanh] + bbllaacckk_tao_dep_trai_nhat_vu_tru + __builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_sieu_nhan_gao_xanh+len(bbllaacckk_thang_nao_bao_em_khong_dep_trai):]
                    except IndexError:
                        break

                tai_sao_em_khong_dua_cho_anh_code[__builtins__.bbllaacckk_minhh_dep_trai_qua] = __builtins__.bbllaacckk_sieu_nhan_gao_do

        tai_sao_em_khong_dua_cho_anh_code = b"\n".join(tai_sao_em_khong_dua_cho_anh_code)
        return tai_sao_em_khong_dua_cho_anh_code
    def read(bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum, bbllaacckk_day_la_binary,is_dump=False):
        print("\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m 2 Files Obfuscation Done...!")
        print("\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m 2 Files Saved At  \033[1;91m\n\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m Main File  \033[1;91m>> \033[1;97mminh-obf.py \n\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m Secondary File  \033[1;91m>>\033[1;97m minh-obf-1.py")
                
        print("\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m The File Has Just Been Encrypted... ")
        if bbllaacckk_day_la_binary:
            for __builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao in range(1,101,1):
                try:
                    __builtins__.bbllaacckk_sieu_nhan_gao_do = ""
                    if "<code object <module>" in str(__builtins__.bbllaacckk_sieu_nhan_gao_trang.loads(open(bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum, "rb").read()[__builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao:])):
                        __builtins__.bbllaacckk_sieu_nhan_gao_do = open(bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum, "rb").read()[__builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao:]
                        print(">> found pyc at {}!".format(__builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao))
                        break
                except ValueError:
                    pass
            if not __builtins__.bbllaacckk_sieu_nhan_gao_do:
                print("!! cannot deobfuscate this file !!")
                input()
                __import__('sys').exit()
            __builtins__.bbllaacckk_sieu_nhan_gao_do = __builtins__.bbllaacckk_sieu_nhan_gao_trang.dumps(compile("""
__import__('minh-obf-1').__spec__ = __import__('zlib').__spec__
__import__('sys').modules['zlib']=__import__('sys').modules['minh-obf-1']
__import__('zlib').decompress.__module__ = 'zlib'
__file__ = \"\"\"{0}\"\"\"

exec(__import__('marshal').loads(""".format(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum) + str(__builtins__.bbllaacckk_sieu_nhan_gao_do) + "),globals())", '<NguyenMinhTricker>', 'exec'))
        else:
            __builtins__.bbllaacckk_sieu_nhan_gao_do = __builtins__.bbllaacckk_sieu_nhan_gao_trang.dumps(compile("""
__import__('minh-obf-1').__spec__ = __import__('zlib').__spec__
__import__('sys').modules['zlib']=__import__('sys').modules['minh-obf-1']
__import__('zlib').decompress.__module__ = 'zlib'
__file__ = \"\"\"{0}\"\"\"

""".format(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum).encode('utf8') + open(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum, "rb").read(), '<NguyenMinhTricker>', 'exec'))
        try:
            if is_dump:
                file_name, folder = __builtins__.bbllaacckk_NguyenMinhTricker.get_f_d(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum)
                try:
                    __import__("shutil").rmtree(folder + file_name + "_py")
                except:
                    pass
                try:__builtins__.bbllaacckk_sieu_nhan_gao_den.mkdir(folder + file_name + "_py")
                except:pass
                folder = folder + file_name + "_py" + folder[-1:]
                folder = folder.replace("\\","\\\\")
                __builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao = __builtins__.bbllaacckk_sieu_nhan_gao_trang.dumps(compile('''
import zlib
from zlib import *
global NguyenMinhTricker
NguyenMinhTricker=0
__file__ = \"\"\"{0}\"\"\"
txxt = {3}
def decompress(code):
    global NguyenMinhTricker
    try:
        open({2}.decode('utf8') + 'deobf_layer_{{}}_{1}.txt'.format(NguyenMinhTricker),"wb").write(txxt + zlib.decompress(code))
    except:
        open({2}.decode('utf8') + 'deobf_layer_{{}}_{1}.txt'.format(NguyenMinhTricker),"w").write(str(txxt.decode('utf8')) + str(zlib.decompress(code)))
    minhcount+=1
    return zlib.decompress(code)

'''.format(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum, file_name, str(folder.encode('utf8')), str(__builtins__.bbllaacckk_NguyenMinhTricker.get_license(file_name, __builtins__.bbllaacckk_day_la_binary))), '<NguyenMinhTricker>', 'exec'))
                print(">> Obf code will start now! please wait.....")
            else:
                __builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao = __builtins__.bbllaacckk_sieu_nhan_gao_trang.dumps(compile('''
from zlib import *
__file__ = \"\"\"{0}\"\"\"
def decompress(code):
    open("minh-tricker.py","wb").write(code)
    __import__("sys").exit(0)
'''.format(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum), '<NguyenMinhTricker>', 'exec'))
            open('minh-obf-1.py','w').write('# OBFUSCATION : NgocVu3007 乄 NguyenMinh3004\nexec(__import__("marshal").loads(__import__("zlib").decompress(__import__("base64").b64decode(' + str(__import__("base64").b64encode(__import__("zlib").compress(__builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao))[::-1]) + "[::-1]))),globals())")
            del __builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao
        except KeyboardInterrupt:
            print("!! cannot write file !!")
            input()
        try:
            open('minh-obf.py','w').write('# OBFUSCATION : NgocVu3007 乄 NguyenMinh3004\nexec(__import__("marshal").loads(__import__("zlib").decompress(__import__("base64").b64decode(' + str(__import__("base64").b64encode(__import__("zlib").compress(__builtins__.bbllaacckk_sieu_nhan_gao_trang.dumps(compile("""
__file__ = \"\"\"{0}\"\"\"
while 1:
    try:
        exec(__import__('marshal').loads(__import__("zlib").decompress(__import__("base64").b64decode(""" + str(__import__("base64").b64encode(__import__("zlib").compress(__builtins__.bbllaacckk_sieu_nhan_gao_do))) + """))),globals())
        break
    except ModuleNotFoundError as e:
        __import__('sys').modules[str(e).split()[-1][1:-1]] = __import__('sys').modules['sys']
""".format(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum), '<NguyenMinhTricker>', 'exec'))))[::-1]) + "[::-1]))),globals())")
        except SyntaxError:
            __builtins__.bbllaacckk_sieu_nhan_gao_den.unlink('minh-obf-1.py')
            print("!! obf code is error !!")
            __import__('sys').exit()
        try:
            cmd = f"{__cpy_syspath__} minh-obf.py" if __builtins__.bbllaacckk_sieu_nhan_gao_den.name == 'nt' else '{} minh-obf.py'.format(__builtins__.bbllaacckk_khong_co_gi_la_kho.executable)
            if __builtins__.bbllaacckk_sieu_nhan_gao_den.name == 'nt':
                __builtins__.bbllaacckk_sieu_nhan_gao_hong.check_output(cmd, timeout = 15, stderr = __builtins__.bbllaacckk___devnull__)
            else:
                __builtins__.bbllaacckk_sieu_nhan_gao_hong.run(cmd, stderr = __builtins__.bbllaacckk___devnull__, shell=True)
            __builtins__.bbllaacckk_NguyenMinhTricker.rm_filedechay()
            __builtins__.bbllaacckk_sieu_nhan_gao_den.unlink('minh-obf-1.py')
            del cmd
            if is_dump:
                return ""
            __builtins__.bbllaacckk_sieu_nhan_gao_do = open("minh-tricker.py",'rb').read()
            if not __builtins__.bbllaacckk_sieu_nhan_gao_do:
                __builtins__.bbllaacckk_sieu_nhan_gao_den.unlink('minh-obf.py')
                print("!! cannot auto detect real code! please manually input code+vars if you can!")
                input()
                __import__('sys').exit()
            else:
                open('minh-tricker.py','wb').write(__import__('zlib').decompress(__builtins__.bbllaacckk_sieu_nhan_gao_do))
        except __builtins__.bbllaacckk_sieu_nhan_gao_hong.TimeoutExpired:
            __builtins__.bbllaacckk_sieu_nhan_gao_den.unlink('minh-obf.py')
            __builtins__.bbllaacckk_sieu_nhan_gao_den.unlink('minh-obf-1.py')
            if is_dump:
                return ""
            print('!! failed when deobfuscate!')
            input()
            __import__('sys').exit()
        except __builtins__.bbllaacckk_sieu_nhan_gao_hong.CalledProcessError:
            __builtins__.bbllaacckk_sieu_nhan_gao_den.unlink('minh-obf.py')
            __builtins__.bbllaacckk_sieu_nhan_gao_den.unlink('minh-obf-1.py')
            if __builtins__.bbllaacckk_day_la_binary:
                print("!! only support pyc python3.11 !!")
            else:
                print("!! cannot auto detect real code! please manually input code+vars if you can!")
            print('!! failed when deobfuscate!')
            input()
            __import__('sys').exit()
        except PermissionError as e:
            __builtins__.bbllaacckk_sieu_nhan_gao_den.unlink('minh-obf.py')
            __builtins__.bbllaacckk_sieu_nhan_gao_den.unlink('minh-obf-1.py')
            print('>> permission error: {}'.format(e))
            input()
            __import__('sys').exit()
        except FileNotFoundError:
            __builtins__.bbllaacckk_sieu_nhan_gao_den.unlink('minh-obf.py')
            print("\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m DCM LỖI FILE RỒI ! ")
            input()
            __import__('sys').exit()

        __builtins__.bbllaacckk_sieu_nhan_gao_den.unlink('minh-obf.py')

        __builtins__.bbllaacckk_sieu_nhan_gao_do = open("minh-tricker.py","rb").read().split(b"\n")
        __builtins__.bbllaacckk_sieu_nhan_gao_den.unlink('minh-tricker.py')
        return __builtins__.bbllaacckk_sieu_nhan_gao_do

__builtins__.bbllaacckk_NguyenMinhTricker = bbllaacckk_NguyenMinhTricker
del bbllaacckk_NguyenMinhTricker
__builtins__.bbllaacckk_NguyenMinhTricker.rm_filedechay()
#get code from enc

print("\033[97m╔══════════════════════════════════════════════════════════╗""")
print("║\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m obf_medium ram file! Above 10 [MB] Anti dec 98%  ║  ")
print("\033[97m╚══════════════════════════════════════════════════════════╝""")
print("\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m Việc enc bản obf tốn khoảng thời gian ")
print("\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m nhất định nhưng đổi lại file của bạn sẽ được ")
print("\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m tối ưu và bảo mật cao hơn ! ")
print("\033[97m══════════════════════════════════════════════════════════""")#┌─╼[/sdcard/download/dec]
 #└╼ ❯❯❯
while 1:
    inp = input("┌─╼\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m You Want Encryption Medium  [Y] \n└─╼❯❯❯ ").lower()
    if inp == "y":
        while 1:
            try:
                __builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum = input("┌─╼\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m Input file obf_medium\033[1;91m \033[1;97m\n└─╼❯❯❯ ").replace("\"","")
                __builtins__.bbllaacckk_sieu_nhan_gao_xanh = open(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum, 'rb').read(4)
                if b"\r\r\n" in __builtins__.bbllaacckk_sieu_nhan_gao_xanh:
                    __builtins__.bbllaacckk_day_la_binary = True
                else:
                    __builtins__.bbllaacckk_day_la_binary = False
                if int(__builtins__.bbllaacckk_sieu_nhan_gao_den.stat(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum).st_size) > 524288000:
                    print('>> this file to large!')
                    continue
                break
            except FileNotFoundError:
                print('>> file not found!')
            except PermissionError:
                print('>> permission denied!')
            except OSError:
                continue
        __builtins__.bbllaacckk_sieu_nhan_gao_do = __builtins__.bbllaacckk_NguyenMinhTricker.read(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum,__builtins__.bbllaacckk_day_la_binary,False)
        break
    elif inp == "n":
        while 1:
            inp = str(input("!! Do you want to deobf all first layer? [Y/n]: "))
            if inp == "y":
                while 1:
                    try:
                        __builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum = input("<< Input full file Hyperion: ").replace("\"","")
                        __builtins__.bbllaacckk_sieu_nhan_gao_xanh = open(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum, 'rb').read(4)
                        if b"\r\r\n" in __builtins__.bbllaacckk_sieu_nhan_gao_xanh:
                            __builtins__.bbllaacckk_day_la_binary = True
                        else:
                            __builtins__.bbllaacckk_day_la_binary = False
                        if int(__builtins__.bbllaacckk_sieu_nhan_gao_den.stat(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum).st_size) > 524288000:
                            print('>> this file to large!')
                            continue
                        break
                    except FileNotFoundError:
                        print('>> file not found!')
                    except PermissionError:
                        print('>> permission denied!')
                    except OSError:
                        continue
                __builtins__.bbllaacckk_sieu_nhan_gao_do = __builtins__.bbllaacckk_NguyenMinhTricker.read(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum,__builtins__.bbllaacckk_day_la_binary,True)
                print(">> Done all first layer!")
                __import__('sys').exit(0)
            elif inp == "n":
                __builtins__.bbllaacckk_day_la_binary = False
                print("!! you must deobfuscate the first layer Hyperion into a file first!")
                while 1:
                    try:
                        __builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum = input("<< Input file code+vars (one file): ").replace("\"","")
                        __builtins__.bbllaacckk_sieu_nhan_gao_do = open(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum, 'rb').read(1)
                        if int(__builtins__.bbllaacckk_sieu_nhan_gao_den.stat(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum).st_size) > 524288000:
                            print('>> this file to large!')
                            continue
                        break
                    except FileNotFoundError:
                        print('>> file not found!')
                    except PermissionError:
                        print('>> permission denied!')
                    except OSError:
                        continue
                print('>> reading file....')
                __builtins__.bbllaacckk_sieu_nhan_gao_do = open(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum, 'rb').read().split(b"\n")
                break
        if inp=="y" or inp=="n":
            break

del inp

__builtins__.bbllaacckk_NguyenMinhTricker.rm_filedechay()

__builtins__.bbllaacckk_sieu_nhan_gao_xanh = 0

__builtins__.bbllaacckk_sieu_nhan_gao_vang = 0

__builtins__.bbllaacckk_ignore_var_by_minhh = False

print('>> split code....')
for __builtins__.bbllaacckk_minhh_dep_trai_nhi in range(0, len(__builtins__.bbllaacckk_sieu_nhan_gao_do), 1):
    if b"from builtins import " in __builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_minhh_dep_trai_nhi]:
        __builtins__.bbllaacckk_sieu_nhan_gao_xanh = __builtins__.bbllaacckk_minhh_dep_trai_nhi
        __builtins__.bbllaacckk_ignore_var_by_minhh = True
        break

__builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai = 0

__builtins__.bbllaacckk_line_removed = 0
if b'locals()[' not in __builtins__.bbllaacckk_sieu_nhan_gao_do[0]:
    print('>> remove license....')
    for __builtins__.bbllaacckk_minh_dep_trai_nhi in range(0, len(__builtins__.bbllaacckk_sieu_nhan_gao_do), 1):
        if b"locals()[" in __builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_minhh_dep_trai_nhi]:
            __builtins__.bbllaacckk_sieu_nhan_gao_do = __builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_minhh_dep_trai_nhi:]
            __builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai = __builtins__.bbllaacckk_minhh_dep_trai_nhi
            __builtins__.bbllaacckk_line_removed = __builtins__.bbllaacckk_minhh_dep_trai_nhi
            break


if __builtins__.bbllaacckk_ignore_var_by_minhh:
    print(">> code detected! try deobfuscate completely....")
    __builtins__.bbllaacckk_minhh_dep_trai_nhi = b"\n".join(__builtins__.bbllaacckk_sieu_nhan_gao_do[:__builtins__.bbllaacckk_sieu_nhan_gao_xanh-__builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai])
    __builtins__.bbllaacckk_Minhh_30 = b"\n".join(__builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_sieu_nhan_gao_xanh-__builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai:])
    __builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao = False
else:
    print(">> code undetected! only deobfuscate vars....")
    __builtins__.bbllaacckk_minhh_dep_trai_nhi = b"\n".join(__builtins__.bbllaacckk_sieu_nhan_gao_do)
    __builtins__.bbllaacckk_Minhh_30 = b"\n".join(__builtins__.bbllaacckk_sieu_nhan_gao_do)
    __builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao = True
    print("!! only deobfuscate vars is NOT recommend to reading vars !!")
    while 1:
        bbllaacckk_minhh_dep_trai_nhat = input(">> do you want to reading vars? [Y/n]: ").lower()
        if bbllaacckk_minhh_dep_trai_nhat=="y":
            __builtins__.bbllaacckk_ignore_var_by_minhh=True
            break
        elif bbllaacckk_minhh_dep_trai_nhat=="n":
            break

if __builtins__.bbllaacckk_ignore_var_by_minhh:
    # replace var in code
    __builtins__.bbllaacckk_ignore_var_by_minhh = [
        '__cpy_syspath__',
        '__name__', 
        'exit',
        '__doc__',
        '__file__',
        '__pycache__',
        '__package__',
        '__loader__',
        '__spec__',
        '__annotations__',
        '__builtins__',
        '__warningregistry__',
    ]

    print(">> prevent import....")
    __builtins__.bbllaacckk_chan_quyen_thoat_code = vars(__import__('sys')).copy()
    __import__('sys').exit = None
    __import__('builtins').exit = None
    exit = None

    __builtins__.bbllaacckk_backup_modules_vip_pro = {}
    for __builtins__.bbllaacckk_minhh_dep_trai_qua in __builtins__.bbllaacckk_nhung_modules_bi_khoa:
        try:
            __builtins__.bbllaacckk_backup_modules_vip_pro[__builtins__.bbllaacckk_minhh_dep_trai_qua] = __builtins__.bbllaacckk_khong_co_gi_la_kho.modules[__builtins__.bbllaacckk_minhh_dep_trai_qua]
            __builtins__.bbllaacckk_khong_co_gi_la_kho.modules[__builtins__.bbllaacckk_minhh_dep_trai_qua]=None
        except KeyError:
            pass

    # read var file
    print(">> reading vars....")
    print("================ [Use: <Ctrl + C> if code started!]\n")
    __builtins__.bbllaacckk_minhh_dep_trai_nhi = __builtins__.bbllaacckk_minhh_dep_trai_nhi.split(b"\n")
    __builtins__.bbllaacckk_max__ = len(__builtins__.bbllaacckk_minhh_dep_trai_nhi)
    __builtins__.bbllaacckk_min__ = 0
    for __builtins__.bbllaacckk_minhh_dep_trai_qua in __builtins__.bbllaacckk_minhh_dep_trai_nhi:
        try:
            exec(__builtins__.bbllaacckk_minhh_dep_trai_qua, globals())

            __builtins__.index = int(__builtins__.bbllaacckk_minhh_dep_trai_nhi.index(__builtins__.bbllaacckk_minhh_dep_trai_qua))+1
            __builtins__.i=int((100/(__builtins__.bbllaacckk_max__-__builtins__.bbllaacckk_min__))*(__builtins__.index-__builtins__.bbllaacckk_min__))
            __builtins__.bbllaacckk_stdout__.write(f"\r[%-25s] %d%% ({__builtins__.index}/{__builtins__.bbllaacckk_max__})" % ('='*int(__builtins__.i/4), __builtins__.i))
            __builtins__.bbllaacckk_stdout__.flush()

        except KeyboardInterrupt:
            print('\n!! break read vars [KeyboardInterrupt] !!')
            print('>> at line {} in code <<'.format(int(__builtins__.bbllaacckk_minhh_dep_trai_nhi.index(__builtins__.bbllaacckk_minhh_dep_trai_qua))+__builtins__.bbllaacckk_line_removed+1), end='')
            break
        except Exception as e:
            print('\n!! stop read vars due to [{}] !!'.format(str(e)))
            print('>> at line {} in code <<'.format(int(__builtins__.bbllaacckk_minhh_dep_trai_nhi.index(__builtins__.bbllaacckk_minhh_dep_trai_qua))+__builtins__.bbllaacckk_line_removed+1), end='')
            break
        except:
            print('\n!! stop read vars due to [unknown error] !!')
            print('>> at line {} in code <<'.format(int(__builtins__.bbllaacckk_minhh_dep_trai_nhi.index(__builtins__.bbllaacckk_minhh_dep_trai_qua))+__builtins__.bbllaacckk_line_removed+1), end='')
            break
    print("\n\n================ [read vars completed]")

    print(">> restore import....")
    for __builtins__.bbllaacckk_minhh_dep_trai_qua in __builtins__.bbllaacckk_backup_modules_vip_pro:
        try:
            __builtins__.bbllaacckk_khong_co_gi_la_kho.modules[__builtins__.bbllaacckk_minhh_dep_trai_qua] = __builtins__.bbllaacckk_backup_modules_vip_pro[__builtins__.bbllaacckk_minhh_dep_trai_qua]
        except KeyError:
            pass

    exit = __builtins__.bbllaacckk_chan_quyen_thoat_code['exit']
    __import__('sys').exit = exit
    __import__('builtins').exit = exit


    __builtins__.bbllaacckk_minhh_dep_trai_nhi = {}
    __builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai = 1

    for __builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai in globals():
        if __builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai in __builtins__.bbllaacckk_ignore_var_by_minhh:
            continue
        elif __builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai in __import__('builtins').__dict__:
            continue
        __builtins__.bbllaacckk_minhh_dep_trai_nhi[__builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai] = globals()[__builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai]

    __builtins__.bbllaacckk_minhh_dep_trai_nhi=dict(sorted(__builtins__.bbllaacckk_minhh_dep_trai_nhi.items(),key=lambda x: (len(x[0]),len(x[0])),reverse=True))

    unhexlify_name = "__builtins__.bbllaacckk_minhh_dep_trai_dang_test_thu_unhexlify"
    eval_name = "eval"
    mot_dong_string_rat_dai = [str(char).encode() for char in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"]

    if __builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao:
        __builtins__.bbllaacckk_replace_type = 0
        print("!! only deobfuscate vars is NOT recommend to replace vars string !!")
        while 1:
            bbllaacckk_minhh_dep_trai_nhat = input(">> do you want to replace vars string? [Y/n]: ").lower()
            if bbllaacckk_minhh_dep_trai_nhat=="y":
                __builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao=False
                break
            elif bbllaacckk_minhh_dep_trai_nhat=="n":
                break
    else:

        while 1:
            choose = str(input(">> replace vars [1 - Fast (Low accuracy), 2 - Very Slow (Extreme accuracy), 3 - Skip]: "))
            if choose == "1":
                __builtins__.bbllaacckk_replace_type = 0
                break
            elif choose == "2":
                __builtins__.bbllaacckk_replace_type = 1
                break
            elif choose == "3":
                __builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao = True
                break
        del choose
                
    if not __builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao:
        print('>> replace vars string [{} mode]....'.format(("Fast" if __builtins__.bbllaacckk_replace_type == 0 else "Very Slow")))
        if __builtins__.bbllaacckk_replace_type == 1:
            minhh = __builtins__.bbllaacckk_Minhh_30()
            minhh.put_code(__builtins__.bbllaacckk_Minhh_30)

        __tmp_list__ = list(__builtins__.bbllaacckk_minhh_dep_trai_nhi)
        __builtins__.bbllaacckk_max__ = len(__tmp_list__)
        __builtins__.bbllaacckk_min__ = 0

        for bbllaacckk_minhh_dep_trai_nhat in __builtins__.bbllaacckk_minhh_dep_trai_nhi:
            if len(bbllaacckk_minhh_dep_trai_nhat) >= 1:
                if bbllaacckk_minhh_dep_trai_nhat.encode() in __builtins__.bbllaacckk_Minhh_30:
                    __builtins__.bbllaacckk___tmp_var__ = str(type(__builtins__.bbllaacckk_minhh_dep_trai_nhi[bbllaacckk_minhh_dep_trai_nhat]))
                    if __builtins__.bbllaacckk___tmp_var__ == "<class 'bool'>" or __builtins__.bbllaacckk___tmp_var__ == "<class 'int'>" or __builtins__.bbllaacckk___tmp_var__ == "<class 'float'>":
                        __builtins__.bbllaacckk_minhh_number_one = str(__builtins__.bbllaacckk_minhh_dep_trai_nhi[bbllaacckk_minhh_dep_trai_nhat])
                    elif __builtins__.bbllaacckk___tmp_var__ == "<class 'function'>":
                        __builtins__.bbllaacckk_minhh_number_one = str(__builtins__.bbllaacckk_minhh_dep_trai_nhi[bbllaacckk_minhh_dep_trai_nhat]).split(" ")[1]
                    elif __builtins__.bbllaacckk___tmp_var__ == "<class 'builtin_function_or_method'>":
                        __builtins__.bbllaacckk___tmp_var__ = str(__builtins__.bbllaacckk_minhh_dep_trai_nhi[bbllaacckk_minhh_dep_trai_nhat]).split(" ")[-1][:-1]
                        if __builtins__.bbllaacckk___tmp_var__ == "unhexlify":
                            __builtins__.bbllaacckk___tmp_var__ = unhexlify_name
                        __builtins__.bbllaacckk_minhh_number_one = __builtins__.bbllaacckk___tmp_var__
                    elif __builtins__.bbllaacckk___tmp_var__ == "<class 'function'>":
                        __builtins__.bbllaacckk_minhh_number_one = str(__builtins__.bbllaacckk_minhh_dep_trai_nhi[bbllaacckk_minhh_dep_trai_nhat])
                        if "<function <lambda> at " in __builtins__.bbllaacckk_minhh_number_one:
                            continue
                        else:
                            __builtins__.bbllaacckk_minhh_number_one = " ".join(str(__builtins__.bbllaacckk_minhh_number_one).split(" ")[:-2][-1:]) + "() '''args: {}'''".format(str(__builtins__.bbllaacckk_minhh_dep_trai_nhi[bbllaacckk_minhh_dep_trai_nhat].__code__.co_varnames)) # <function test_function at 0x7fd1dc086fc0>
                    elif __builtins__.bbllaacckk___tmp_var__ == "<class 'type'>":
                        __builtins__.bbllaacckk_minhh_number_one = str(__builtins__.bbllaacckk_minhh_dep_trai_nhi[bbllaacckk_minhh_dep_trai_nhat]).split(" ")[1].split(".")[-1][:-2]
                    elif __builtins__.bbllaacckk___tmp_var__ == "<class 'bytes'>":
                        __builtins__.bbllaacckk_minhh_number_one = str(__builtins__.bbllaacckk_minhh_dep_trai_nhi[bbllaacckk_minhh_dep_trai_nhat]).replace("\r","\\r").replace("\n","\\n").replace("\t","\\t")
                    else:
                        __builtins__.bbllaacckk_minhh_number_one = str("\"" + str(__builtins__.bbllaacckk_minhh_dep_trai_nhi[bbllaacckk_minhh_dep_trai_nhat]).replace('\\',r"\\").replace('"', '\\"') + "\"").replace("\n", "\\n").replace("\t","\\t").replace("\r","\\r").replace("\b","\\b").replace("\f","\\f")
                    if __builtins__.bbllaacckk_replace_type == 1:
                        Minhh.replace_var(bbllaacckk_minhh_dep_trai_nhat, __builtins__.bbllaacckk_minhh_number_one)
                    elif __builtins__.bbllaacckk_replace_type == 0:
                        __builtins__.bbllaacckk_Minhh_30 = __builtins__.bbllaacckk_Minhh_30.replace_by_minhh_dep_trai(__builtins__.bbllaacckk_Minhh_30, bbllaacckk_minhh_dep_trai_nhat.encode(), __builtins__.bbllaacckk_minhh_number_one.encode())
            __builtins__.index = int(__tmp_list__.index(bbllaacckk_minhh_dep_trai_nhat))+1
            __builtins__.i=int((100/(__builtins__.bbllaacckk_max__-__builtins__.bbllaacckk_min__))*(__builtins__.index-__builtins__.bbllaacckk_min__))
            __builtins__.bbllaacckk_stdout__.write(f"\r[%-25s] %d%% ({__builtins__.index}/{__builtins__.bbllaacckk_max__} var)" % ('='*int(__builtins__.i/4), __builtins__.i))
            __builtins__.bbllaacckk_stdout__.flush()
        __builtins__.bbllaacckk_stdout__.write(f"\r[=========================] 100% ({__builtins__.bbllaacckk_max__}/{__builtins__.bbllaacckk_max__} var)")
        __builtins__.bbllaacckk_stdout__.flush()
        print("")
        
        if __builtins__.bbllaacckk_replace_type == 1:
            __builtins__.bbllaacckk_Minhh_30 =Minhh.get_code()
    ## Replace eval(unhexlify()) >> << eval(__builtins__.bbllaacckk_minhh_dep_trai_dang_test_thu_unhexlify())

    if "{}(".format(unhexlify_name).encode() in __builtins__.bbllaacckk_Minhh_30:
        if input("!! found unhexlify! do you want to decode it? [Y/n]: ").lower() == 'y':
            print('>> fixing unhexlify [this may take too long]....')
            song_chet_co_so = "{}({}(".format(eval_name,unhexlify_name).encode()
            __builtins__.bbllaacckk_Minhh_30 = __builtins__.bbllaacckk_Minhh_30.split(b"\n")
            __builtins__.bbllaacckk_minhh_number_one = b""

            __builtins__.bbllaacckk_max__ = len(__builtins__.bbllaacckk_Minhh_30)
            __builtins__.bbllaacckk_min__ = 0

            for bbllaacckk_minhh_dep_trai_nhat in range(0, len(__builtins__.bbllaacckk_Minhh_30), 1):
                if "{}(".format(unhexlify_name).encode() in __builtins__.bbllaacckk_Minhh_30[bbllaacckk_minhh_dep_trai_nhat]:
                    ghe_vay_sao = __builtins__.bbllaacckk_Minhh_30[bbllaacckk_minhh_dep_trai_nhat].split(b"=")
                    for __builtins__.bbllaacckk_minhh_dep_trai_nhi in range(0, len(ghe_vay_sao), 1):
                        if "{}(".format(unhexlify_name).encode() in ghe_vay_sao[__builtins__.bbllaacckk_minhh_dep_trai_nhi]:
                            __builtins__.bbllaacckk___tmp_var__ = ghe_vay_sao[__builtins__.bbllaacckk_minhh_dep_trai_nhi]
                            while 1:
                                while __builtins__.bbllaacckk___tmp_var__:
                                    if __builtins__.bbllaacckk___tmp_var__[:len(eval_name)+len(unhexlify_name)+2] == song_chet_co_so:
                                        while len(__builtins__.bbllaacckk___tmp_var__) > len(eval_name)+len(unhexlify_name)+2:
                                            try:
                                                if song_chet_co_so in __builtins__.bbllaacckk___tmp_var__:
                                                    __builtins__.bbllaacckk_minhh_number_one = eval(__builtins__.bbllaacckk___tmp_var__[5:-1]).encode()
                                                else:
                                                    __builtins__.bbllaacckk_minhh_number_one = eval(__builtins__.bbllaacckk___tmp_var__).encode()
                                                __builtins__.bbllaacckk_minhh_number_one = ghe_vay_sao[__builtins__.bbllaacckk_minhh_dep_trai_nhi].replace(__builtins__.bbllaacckk___tmp_var__,__builtins__.bbllaacckk_minhh_number_one)
                                                break
                                            except Exception:
                                                __builtins__.bbllaacckk___tmp_var__ = __builtins__.bbllaacckk___tmp_var__[:-1]
                                        break
                                    elif __builtins__.bbllaacckk___tmp_var__[:len(unhexlify_name)+1] == song_chet_co_so:
                                        while len(__builtins__.bbllaacckk___tmp_var__) > len(unhexlify_name)+1:
                                            try:
                                                __builtins__.bbllaacckk_minhh_number_one = eval(__builtins__.bbllaacckk___tmp_var__).encode()
                                                __builtins__.bbllaacckk_minhh_number_one = ghe_vay_sao[__builtins__.bbllaacckk_minhh_dep_trai_nhi].replace(__builtins__.bbllaacckk___tmp_var__,__builtins__.bbllaacckk_minhh_number_one)
                                                break
                                            except Exception:
                                                __builtins__.bbllaacckk___tmp_var__ = __builtins__.bbllaacckk___tmp_var__[:-1]
                                        break
                                    else:
                                        __builtins__.bbllaacckk___tmp_var__ = __builtins__.bbllaacckk___tmp_var__[1:]
                                if "{}(".format(unhexlify_name).encode() in __builtins__.bbllaacckk_minhh_number_one:
                                    ghe_vay_sao[__builtins__.bbllaacckk_minhh_dep_trai_nhi] = __builtins__.bbllaacckk_minhh_number_one
                                    __builtins__.bbllaacckk___tmp_var__ = __builtins__.bbllaacckk_minhh_number_one
                                    continue
                                
                                if not __builtins__.bbllaacckk___tmp_var__:
                                    __builtins__.bbllaacckk_minhh_number_one = ghe_vay_sao[__builtins__.bbllaacckk_minhh_dep_trai_nhi]
                                break

                            ghe_vay_sao[__builtins__.bbllaacckk_minhh_dep_trai_nhi] = __builtins__.bbllaacckk_minhh_number_one

                    __builtins__.bbllaacckk_Minhh_30[bbllaacckk_minhh_dep_trai_nhat] = b"=".join(ghe_vay_sao)

                __builtins__.i=int((100/(__builtins__.bbllaacckk_max__-__builtins__.bbllaacckk_min__))*(bbllaacckk_minhh_dep_trai_nhat-__builtins__.bbllaacckk_min__))+1
                __builtins__.bbllaacckk_stdout__.write(f"\r[%-25s] %d%% ({bbllaacckk_minhh_dep_trai_nhat+1}/{__builtins__.bbllaacckk_max__} unhexlify)" % ('='*int(__builtins__.i/4), __builtins__.i))
                __builtins__.bbllaacckk_stdout__.flush()
            __builtins__.bbllaacckk_stdout__.write(f"\r[=========================] 100% ({__builtins__.bbllaacckk_max__}/{__builtins__.bbllaacckk_max__} unhexlify)")
            __builtins__.bbllaacckk_stdout__.flush()
            print("")
            __builtins__.bbllaacckk_Minhh_30 = b"\n".join(__builtins__.bbllaacckk_Minhh_30)
        else:
            __builtins__.bbllaacckk_Minhh_30 = b"from binascii import unhexlify\n" + __builtins__.bbllaacckk_Minhh_30
    __builtins__.bbllaacckk_Minhh_30 = __builtins__.bbllaacckk_Minhh_30.replace(unhexlify_name.encode(), b"unhexlify")

# write file
file_name, folder = __builtins__.bbllaacckk_NguyenMinhTricker.get_f_d(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum)

print(f'>> saving.... [nhin_cai_lon_{file_name}.py]')
open(f'{folder}nhin_cai_lon_{file_name}.py','wb').write(__builtins__.bbllaacckk_NguyenMinhTricker.get_license(file_name, __builtins__.bbllaacckk_day_la_binary) + __builtins__.bbllaacckk_Minhh_30)
print(">> DONE !")
