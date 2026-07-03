import os, sys, time, socket, json, base64, subprocess
from datetime import datetime
import requests
import cloudscraper
from bs4 import BeautifulSoup  
from colorama import Fore, init
from pystyle import Colors, Colorate
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from pystyle import Colors, Colorate, Center
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn

console = Console()
init(autoreset=True)

def kiem_tra_mang():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
    except OSError:
        console.print(Panel.fit("❌ Mạng không ổn định hoặc bị mất kết nối. Vui lòng kiểm tra lại mạng.", style="bold red"))
        sys.exit(1)

kiem_tra_mang()

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner_text = r"""
╔═════════════════════════════════════════════════════════════╗
║                                                             ║
║    ███╗   ██╗██████╗  ██████╗  █████╗ ██╗   ██╗██████╗      ║
║    ████╗  ██║██╔══██╗██╔═████╗██╔══██╗██║   ██║╚════██╗     ║
║    ██╔██╗ ██║██████╔╝██║██╔██║╚██████║██║   ██║ █████╔╝     ║
║    ██║╚██╗██║██╔═══╝ ████╔╝██║ ╚═══██║╚██╗ ██╔╝ ╚═══██╗     ║
║    ██║ ╚████║██║     ╚██████╔╝ █████╔╝ ╚████╔╝ ██████╔╝     ║
║    ╚═╝  ╚═══╝╚═╝      ╚═════╝  ╚════╝   ╚═══╝  ╚═════╝      ║
║              © Bản Quyền Thuộc PhamNhat                     ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝
"""
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_red, banner_text, 2)))

def clear_and_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner())

scraper = cloudscraper.create_scraper()

def read_or_ask_auth():
	
    try:
        open("Authorization.txt", "x").close()
        open("token.txt", "x").close()
    except:
        pass

    with open("Authorization.txt", "r", encoding="utf-8", errors="ignore") as f:
        author = f.read().strip()
    with open("token.txt", "r", encoding="utf-8", errors="ignore") as f:
        token = f.read().strip()

    if not author:
        author = console.input("[bold green]NHẬP AUTHORIZATION: [yellow]").strip()
        token = console.input("[bold green]NHẬP T (Token): [yellow]").strip()
        with open("Authorization.txt", "w", encoding="utf-8") as f:
            f.write(author)
        with open("token.txt", "w", encoding="utf-8") as f:
            f.write(token)
    else:
        print (Colorate.Diagonal(Colors.cyan_to_green, "Nhấn Enter để vào TOOL\n     hoặc\nnhập AUTHORIZATION để vào acc khác.\n"))       
        select = console.input("[bold blue]\nNhập AUTHORIZATION tại đây (bỏ trống nếu dùng acc cũ): [yellow]").strip()
        kiem_tra_mang()
        if select:
            author = select
            token = console.input("[bold green]Nhập T (Token): [yellow]").strip()
            with open("Authorization.txt", "w", encoding="utf-8") as f:
                f.write(author)
            with open("token.txt", "w", encoding="utf-8") as f:
                f.write(token)
    return author, token

def make_headers(author, token):
    return {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=utf-8',
        'Authorization': author,
        't': token,
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'Referer': 'https://app.golike.net/account/manager/tiktok',
    }


def chonacc(headers):
    try:
        return scraper.get('https://gateway.golike.net/api/tiktok-account', headers=headers, json={}).json()
    except:
        return {"status": 0, "data": []}

def nhannv(headers, account_id):
    try:
        params = {
            'account_id': account_id,
            'data': 'null',
        }
        response = scraper.get(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',
            headers=headers,
            params=params,
            json={}
        )
        return response.json()
    except:
        return {}

def hoanthanh(headers, ads_id, account_id):
    try:
        json_data = {
            'ads_id': ads_id,
            'account_id': account_id,
            'async': True,
            'data': None,
        }
        response = scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
            headers=headers,
            json=json_data,
            timeout=6
        )
        return response.json()
    except:
        return {}

def baoloi(headers, ads_id, object_id, account_id, loai):
    try:
        json_data1 = {
            'description': 'Tôi đã làm Job này rồi',
            'users_advertising_id': ads_id,
            'type': 'ads',
            'provider': 'tiktok',
            'fb_id': account_id,
            'error_type': 6,
        }
        scraper.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)
        json_data2 = {
            'ads_id': ads_id,
            'object_id': object_id,
            'account_id': account_id,
            'type': loai,
        }
        scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
            headers=headers,
            json=json_data2,
        )
    except:
        pass

def setup_adb_if_needed(loai_nhiem_vu):
    x_like = y_like = x_follow = y_follow = None
    console.print(Panel.fit("ADB tự động", style="bold magenta"))
    console.print("[cyan][1] Có   [2] Không")
    adbyn = console.input("[bold green]Nhập lựa chọn: [yellow]").strip()

    if adbyn != "1":
        return adbyn, x_like, y_like, x_follow, y_follow

    def setup_adb_internal():
        config_file = "adb_config.txt"
        like_coords_file = "toa_do_tim.txt"
        follow_coords_file = "toa_do_follow.txt"

        console.print(Panel.fit("Bạn có thể xem video hướng dẫn kết nối ADB\nhttps://youtu.be/vcWNzu2XRSE?si=_jFVm9nhSkNGBK_-", style="bold cyan"))
        ip = console.input("[bold green]Nhập IP thiết bị (vd 192.168.1.2): [yellow]").strip()
        adb_port = console.input("[bold green]Nhập port thiết bị (vd 39327): [yellow]").strip()

        x_like = y_like = x_follow = y_follow = None
        if os.path.exists(like_coords_file):
            try:
                with open(like_coords_file, "r") as f:
                    coords = f.read().split("|")
                    if len(coords) == 2:
                        x_like, y_like = coords
                        console.print(f"[green]Đã tìm thấy tọa độ nút tim: X={x_like}, Y={y_like}")
            except:
                pass
        if os.path.exists(follow_coords_file):
            try:
                with open(follow_coords_file, "r") as f:
                    coords = f.read().split("|")
                    if len(coords) == 2:
                        x_follow, y_follow = coords
                        console.print(f"[green]Đã tìm thấy tọa độ nút follow: X={x_follow}, Y={y_follow}")
            except:
                pass

        if not os.path.exists(config_file):
            console.print("[cyan]Lần đầu chạy, nhập mã ghép nối (6 số) và port ghép nối.")
            pair_code = console.input("[bold green]Nhập mã ghép nối 6 số (vd 322763): [yellow]").strip()
            pair_port = console.input("[bold green]Nhập port ghép nối (vd 44832): [yellow]").strip()
            with open(config_file, "w") as f:
                f.write(f"{pair_code}|{pair_port}")
        else:
            with open(config_file, "r") as f:
                pair_code, pair_port = [s.strip() for s in f.read().split("|")]

        console.print("[cyan]Đang ghép nối với thiết bị…")
        os.system(f"adb pair {ip}:{pair_port} {pair_code}")
        time.sleep(2)
        console.print("[cyan]Đang kết nối ADB…")
        os.system(f"adb connect {ip}:{adb_port}")
        time.sleep(2)
        devices = os.popen("adb devices").read()
        if ip not in devices:
            console.print(Panel.fit("❌ Kết nối ADB thất bại!", style="bold red"))
            sys.exit(1)

        console.print(Panel.fit("NHẬP TỌA ĐỘ NÚT", style="bold magenta"))
        if loai_nhiem_vu in [1, 3] and (not x_follow or not y_follow):
            x_follow = console.input("[bold green]Nhập X nút follow: [yellow]").strip()
            y_follow = console.input("[bold green]Nhập Y nút follow: [yellow]").strip()
            with open(follow_coords_file, "w") as f:
                f.write(f"{x_follow}|{y_follow}")
        if loai_nhiem_vu in [2, 3] and (not x_like or not y_like):
            x_like = console.input("[bold green]Nhập X nút tim: [yellow]").strip()
            y_like = console.input("[bold green]Nhập Y nút tim: [yellow]").strip()
            with open(like_coords_file, "w") as f:
                f.write(f"{x_like}|{y_like}")
        return x_like, y_like, x_follow, y_follow

    x_like, y_like, x_follow, y_follow = setup_adb_internal()
    return adbyn, x_like, y_like, x_follow, y_follow

def show_acc_table(chontktiktok):
    table_acc = Table(title="DANH SÁCH ACC TIKTOK", header_style="bold cyan")
    table_acc.add_column("STT", style="yellow", width=6, justify="right")
    table_acc.add_column("Nickname", style="bold green")
    for i, acc in enumerate(chontktiktok["data"], start=1):
        table_acc.add_row(str(i), acc.get("nickname", ""))
    console.print(table_acc)

def render_result_table(rows, total):
    table_job = Table(title="KẾT QUẢ NHIỆM VỤ", header_style="bold cyan")
    table_job.add_column("STT", style="yellow", width=6, justify="right")
    table_job.add_column("Thời gian", style="green", width=10)
    table_job.add_column("Status", style="bold")
    table_job.add_column("Loại", style="magenta", width=8)
    table_job.add_column("ID Acc", style="cyan", width=10)
    table_job.add_column("Xu", style="yellow", width=8, justify="right")
    table_job.add_column("Tổng", style="bright_cyan", width=10, justify="right")
    for r in rows[-1:]:  
        table_job.add_row(*r)
    console.print(table_job)
    console.print(Panel.fit(f"Tổng xu hiện tại: [bold yellow]{total}[/]", style="bold green"))

def main():
    clear_and_banner()

    author, token = read_or_ask_auth()
    headers = make_headers(author, token)

    clear_and_banner()
    console.print(Panel.fit("DANH SÁCH ACC TIKTOK", style="bold magenta"))
    chontktiktok = chonacc(headers)
    if chontktiktok.get("status") != 200:
        console.print(Panel.fit("❌ Authorization hoặc Token (t) sai.", style="bold red"))
        sys.exit(1)
    show_acc_table(chontktiktok)


    while True:
        try:
            luachon = int(console.input("[bold green]Chọn tài khoản TIKTOK: [yellow]"))
            if 1 <= luachon <= len(chontktiktok["data"]):
                account_id = chontktiktok["data"][luachon - 1]["id"]
                break
            else:
                console.print("[bold red]Số không hợp lệ!")
        except:
            console.print("[bold red]Sai định dạng!")


    while True:
        try:
            delay = int(console.input("[bold green]Delay (giây): [yellow]"))
            break
        except:
            console.print("[bold red]Sai định dạng!")


    while True:
        try:
            doiacc = int(console.input("[bold green]Thất bại bao nhiêu lần thì đổi acc: [yellow]"))
            break
        except:
            console.print("[bold red]Hãy nhập số!")


    clear_and_banner()
    table_nv = Table(title="CHỌN LOẠI NHIỆM VỤ", header_style="bold magenta")
    table_nv.add_column("Số", style="yellow", width=6, justify="right")
    table_nv.add_column("Loại nhiệm vụ", style="green")
    table_nv.add_row("1", "Follow")
    table_nv.add_row("2", "Like")
    table_nv.add_row("3", "Cả hai (Follow + Like)")
    console.print(table_nv)
    while True:
        try:
            loai_nhiem_vu = int(console.input("[bold green]Chọn loại nhiệm vụ: [yellow]"))
            if loai_nhiem_vu in [1, 2, 3]:
                break
            console.print("[bold red]Vui lòng chọn 1/2/3!")
        except:
            console.print("[bold red]Sai định dạng!")


    adbyn, x_like, y_like, x_follow, y_follow = setup_adb_if_needed(loai_nhiem_vu)


    dem = 0
    tong = 0
    checkdoiacc = 0
    dsaccloi = []
    result_rows = []  

    while True:
        if checkdoiacc == doiacc:
            nick = chontktiktok["data"][luachon - 1].get("nickname", "")
            dsaccloi.append(nick)
            clear_and_banner()
            console.print(Panel.fit(f"⚠️  Acc Tiktok gặp vấn đề: {', '.join(dsaccloi)}", style="bold red"))
            show_acc_table(chontktiktok)

            while True:
                try:
                    luachon = int(console.input("[bold green]Chọn tài khoản mới: [yellow]"))
                    if 1 <= luachon <= len(chontktiktok["data"]):
                        account_id = chontktiktok["data"][luachon - 1]["id"]
                        checkdoiacc = 0
                        break
                    else:
                        console.print("[bold red]Acc không có trong danh sách!")
                except:
                    console.print("[bold red]Sai định dạng!!!")


        nhanjob = None
        for _ in range(3):
            try:
                nhanjob = nhannv(headers, account_id)
                if nhanjob and nhanjob.get("status") == 200 and nhanjob["data"].get("link") and nhanjob["data"].get("object_id"):
                    break
            except:
                pass
            time.sleep(2)
        if not nhanjob or nhanjob.get("status") != 200:
            time.sleep(1)
            continue

        ads_id = nhanjob["data"]["id"]
        link = nhanjob["data"]["link"]
        object_id = nhanjob["data"]["object_id"]
        job_type = nhanjob["data"]["type"]  # "like" hoặc "follow"


        if (loai_nhiem_vu == 1 and job_type != "follow") or \
           (loai_nhiem_vu == 2 and job_type != "like") or \
           (job_type not in ["follow", "like"]):
            baoloi(headers, ads_id, object_id, account_id, job_type)
            continue

        try:
            if adbyn == "1":
                os.system(f'adb shell am start -a android.intent.action.VIEW -d "{link}" > /dev/null 2>&1')
            else:

                subprocess.run(["termux-open-url", link])

            time.sleep(3)
        except Exception as e:
            baoloi(headers, ads_id, object_id, account_id, job_type)
            continue


        if adbyn == "1":
            if job_type == "like" and x_like and y_like:
                os.system(f"adb shell input tap {x_like} {y_like}")
            elif job_type == "follow" and x_follow and y_follow:
                os.system(f"adb shell input tap {x_follow} {y_follow}")


        if delay > 0:
            with Progress(
                SpinnerColumn(),
                TextColumn("[cyan]Chờ delay"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                TimeRemainingColumn(),
                transient=True,
                console=console
            ) as progress:
                task = progress.add_task("", total=delay)
                for _ in range(delay):
                    time.sleep(1)
                    progress.advance(task, 1)


        nhantien = None
        for _ in range(2):
            try:
                nhantien = hoanthanh(headers, ads_id, account_id)
                if nhantien and nhantien.get("status") == 200:
                    break
            except:
                pass
            time.sleep(0.5)

        clear_and_banner()
        if nhantien and nhantien.get("status") == 200:
            dem += 1
            tien = nhantien["data"]["prices"]
            tong += tien
            now = datetime.now().strftime("%H:%M:%S")

            row = [
                str(dem),
                now,
                "[bold green]success[/]",
                job_type,
                "Ẩn ID",
                f"+{tien}",
                str(tong),
            ]
            result_rows.append(row)
            checkdoiacc = 0
            render_result_table(result_rows, tong)
        else:
            try:
                baoloi(headers, ads_id, object_id, account_id, job_type)
            except:
                pass
            checkdoiacc += 1
            console.print(Panel.fit("Bỏ qua nhiệm vụ / báo lỗi", style="bold yellow"))
            render_result_table(result_rows, tong)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Thoát theo yêu cầu (Ctrl+C).")
