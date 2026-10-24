import os
import sys
import time
import requests
import webbrowser

# ANSI Color Codes
RED     = '\033[91m'
GREEN   = '\033[92m'
YELLOW  = '\033[93m'
BLUE    = '\033[94m'
MAGENTA = '\033[95m'
CYAN    = '\033[96m'
WHITE   = '\033[97m'
RESET   = '\033[0m'

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def banner():
    clear_screen()
    print(f"""{CYAN}
  ████████╗ ██████╗  ██████╗     ████████╗███████╗ █████╗ ███╗   ███╗
  ╚══██╔══╝██╔════╝ ██╔══██╗    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
     ██║   ██║  ███╗██████╔╝       ██║   █████╗  ███████║██╔████╔██║
     ██║   ██║   ██║██╔══██║       ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
     ██║   ╚██████╔╝██║  ██║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║
     ╚═╝    ╚═════╝ ╚═╝  ╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
    {RESET}""")
    print(f"{YELLOW}    Cyber Security {RESET}")
    print(f"{MAGENTA}    ————————————————————————————————————————{RESET}")
    print(f"{GREEN}    DEVELOPER     :{RESET} {WHITE}RAFI TRADAR{RESET}")
    print(f"{GREEN}    TELEGRAM      :{RESET} {BLUE}@rafitreder{RESET}")
    print(f"{GREEN}    TOOL          :{RESET} {CYAN}API TESTER{RESET}")
    print(f"{GREEN}    STATUS        :{RESET} {RED}FREE{RESET}")
    print(f"{MAGENTA}    ————————————————————————————————————————{RESET}\n")

def open_telegram():
    url = "https://t.me/rafitreder"
    print(f"\n{YELLOW}[!] Opening Telegram channel...{RESET}")
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"{RED}[!] Error opening browser: {e}{RESET}")
    time.sleep(2)

def main_menu():
    open_telegram()

    while True:
        banner()
        print(f"{GREEN}[ 1 ]{RESET} {WHITE}START API TEST{RESET}")
        print(f"{GREEN}[ 2 ]{RESET} {WHITE}TELEGRAM{RESET}")
        print(f"{GREEN}[ 3 ]{RESET} {WHITE}EXIT{RESET}")
        
        choice = input(f"\n{CYAN}Select an option (1-3)➤ {RESET}").strip()
        
        if choice == '1':
            phone = input(f"\n{YELLOW}TARGET NUMBER➤ {RESET}").strip()
            send_api_request(phone)
        elif choice == '2':
            open_telegram()
        elif choice == '3':
            print(f"\n{RED}Exiting...{RESET}")
            sys.exit(0)
        else:
            print(f"\n{RED}Invalid choice. Try again.{RESET}")
            time.sleep(1)

def send_api_request(phone_number):
    nid = "5845888855"
    url = f"https://CobraExpire.freedev.app/roct_main.php?phone={phone_number}&nid={nid}"
    
    print(f"\n{CYAN}Sending request for number: {phone_number}{RESET}\n")
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"{GREEN}TGR TEAM [ REQUEST SUCCESS √ ]{RESET}")
        else:
            print(f"{RED}TGR TEAM [ STATUS: {response.status_code} ]{RESET}")
    except requests.exceptions.RequestException:
        print(f"{RED}TGR TEAM [ CONNECTION ERROR / RETRYING ]{RESET}")
    
    input(f"\n{YELLOW}Press Enter to return to menu...{RESET}")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{RED}Exiting program.{RESET}")
        sys.exit(0)
