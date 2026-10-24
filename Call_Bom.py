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
    # Clear terminal screen
    os.system('clear' if os.name != 'nt' else 'cls')

def banner():
    clear_screen()
    print(f"""{CYAN}
  ████████╗ ██████╗  ██████╗     ████████╗███████╗ █████╗ ███╗   ███╗
  ╚══██╔══╝██╔════╝ ██╔══██╗    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
     ██║   ██║  ███╗██████╔╝       ██║   █████╗  ███████║██╔████╔██║
     ██║   ██║   ██║██╔══██╗       ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
     ██║   ╚██████╔╝██║  ██║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║
     ╚═╝    ╚═════╝ ╚═╝  ╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
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
    # Open telegram once on script start
    open_telegram()

    while True:
        banner()
        print(f"{GREEN}[ 1 ]{RESET} {WHITE}START API TEST{RESET}")
        print(f"{GREEN}[ 2 ]{RESET} {WHITE}TELEGRAM{RESET}")
        print(f"{GREEN}[ 3 ]{RESET} {WHITE}EXIT{RESET}")
        
        choice = input(f"\n{CYAN}Select an option (1-3)➤ {RESET}").strip()
        
        if choice == '1':
            phone = input(f"\n{YELLOW}TARGET NUMBER➤ +88{RESET}").strip()
            full_number = "+88" + phone
            run_test(full_number)
        elif choice == '2':
            open_telegram()
        elif choice == '3':
            print(f"\n{RED}Exiting...{RESET}")
            sys.exit(0)
        else:
            print(f"\n{RED}Invalid choice. Try again.{RESET}")
            time.sleep(1)

def run_test(phone_number):
    print(f"\n{CYAN}Sending test request for: {phone_number}{RESET}")
    print(f"{YELLOW}Press Ctrl + C to stop and return to menu.{RESET}\n")
    
    url = f"https://httpbin.org/get?phone={phone_number}"
    
    try:
        while True:
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    print(f"{GREEN}TGR TEAM [ REQUEST SUCCESS √ ]{RESET}")
                else:
                    print(f"{RED}TGR TEAM [ ERROR STATUS: {response.status_code} ]{RESET}")
            except requests.exceptions.RequestException:
                print(f"{RED}TGR TEAM [ CONNECTION ERROR / RETRYING ]{RESET}")
            
            time.sleep(2)
            
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}[!] Stopped by user. Returning to menu...{RESET}")
        time.sleep(1.5)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{RED}Exiting program.{RESET}")
        sys.exit(0)
