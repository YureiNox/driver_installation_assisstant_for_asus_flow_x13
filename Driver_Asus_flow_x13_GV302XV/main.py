import os
import sys
import time
import json
import subprocess
from tools.modulchecker import modulchecker

path = "files/"
file_path = "main.json" 

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
PURPLE = "\033[35m"
RESET = "\033[0m"

absolute_file_path = os.path.abspath(file_path)
if not os.path.exists(absolute_file_path):
    print(f"{RED}Error: JSON file not found at {absolute_file_path}{RESET}")
    sys.exit()

if modulchecker():
    print(f"{GREEN}All modules are installed{RESET}")
    time.sleep(1)
else:
    print(f"{RED}An error occurred{RESET}")
    print(f"{YELLOW}Trying to install modules again{RESET}")
    time.sleep(1)
    if modulchecker():
        print(f"{GREEN}All modules are installed{RESET}")
        time.sleep(1)
    else:
        print(f"{RED}An error occurred{RESET}")
        print(f"{RED}Exiting...{RESET}")
        time.sleep(1)
        sys.exit()

import requests

def load_json_data(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"{RED}Error: JSON file not found at {file_path}{RESET}")
        sys.exit()
    except json.JSONDecodeError:
        print(f"{RED}Error: JSON file is not properly formatted{RESET}")
        sys.exit()

def download(url, path):
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        print(f"{YELLOW}Downloading packet...{RESET}")
        r = requests.get(url)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
        print(f"{GREEN}Download complete{RESET}")
        print(f"{GREEN}File saved to: {path}{RESET}")
        
        if path.endswith(".exe"):
            print(f"{YELLOW}Executing file...{RESET}")
            subprocess.run([path], check=True) 
        
    except requests.exceptions.RequestException as e:
        print(f"{RED}Download failed: {e}{RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{RED}Failed to execute the file: {e}{RESET}")

def main():
    print(f"{PURPLE}Welcome to DriverAssistant currently supporting Asus rog Flow X13 GV302XV{RESET}")
    
    data = load_json_data(absolute_file_path)
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
[1] BIOS Update
[2] Pilotes/Drivers Update
[3] Quit
""")
        option = input(f"{YELLOW}Select an option: {RESET}")
        
        if option == '1':
            print(f"{RED}Option currently not available{RESET}")
        elif option == '2':
            driver_update_menu(data)
        elif option == '3':
            break
        else:
            print(f"{RED}Invalid option, please try again.{RESET}")

def driver_update_menu(drivers):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
[1] Network
[2] Chipset
[3] Audio
[4] Graphics
[5] Lecteur de carte
[6] Pavé tactile
[7] USB
[8] Bluetooth 
[9] Hotfix
[10] Utilitaires
[11] Retour
""")
    
    option = input(f"{YELLOW}Select a driver to download: {RESET}")
    
    driver_keys = [
        'Network', 'Chipset', 'Audio', 'Graphics',
        'Lecteur', 'Pave', 'USB', 'Bluetooth',
        'Hotfix', 'Utilitaire'
    ]
    
    if option.isdigit() and 1 <= int(option) <= len(driver_keys):
        selected_driver = driver_keys[int(option) - 1]
        driver_info = drivers[selected_driver]
        
        url = driver_info["URL"]
        file_name = driver_info.get("Filename", url.split("/")[-1])
        
        download(url, os.path.join(path, file_name))
    elif option == '11':
        return
    else:
        print(f"{RED}Invalid option, please try again.{RESET}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
    input("Press Enter to exit and delete all downloaded files...")
    for file in os.listdir(path):
        os.remove(os.path.join(path, file))
    pycache_path = "tools/__pycache__"
    if os.path.exists(pycache_path):
        for file in os.listdir(pycache_path):
            os.remove(os.path.join(pycache_path, file))
        os.rmdir(pycache_path)