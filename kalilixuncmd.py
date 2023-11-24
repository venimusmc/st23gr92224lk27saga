import subprocess
import platform
from pystyle import *
import colorama
from colorama import Fore
import requests
from tqdm import tqdm, trange
from time import sleep
import pyperclip
import base64

System.Title("Terminal")

print(f"{Fore.MAGENTA}")
progressbar = tqdm([1, 4, 6, 8, 10, 20, 50], leave=False)
for item in progressbar:
    sleep(2)
    progressbar.set_description(' Loading: ')


sudo_cmd = ("Not available yet try after a long time :D")

discord_cmd = (colorama.Fore.CYAN + f"""
$$-----------List Of the Discord Commands-----------$$
1: dc@tok$(id)    6: more soon    
2: web@spam$(url) 7: more soon    
3: help$nul       8: more soon    
4: dm@spam$(id)   9: more soon    
5: more soon      10: more soon   

""")

command_List = (colorama.Fore.CYAN + f"""
$$-----------List Of the Commands-----------$$
1: sudo help    6: ip help      11: more soon
2: git help     7: term help    12: more soon
3: help$nul     8: ddos help    13: more soon
4: discord      9: doxx help    14: more soon
5: server help  10: info help   15: more soon

""")

server = ("178.147.49.229")


def run_command(command):
    try:
        # Execute the command and capture the output
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        # Handle errors
        return f"Error: {e.output}"


def windows_terminal():
    while True:
        # Get user input
        user_input = input(
            colorama.Fore.LIGHTGREEN_EX + f"server" + "." + colorama.Fore.YELLOW + f"User" + ":" + colorama.Fore.LIGHTBLUE_EX + f"nul" + colorama.Fore.MAGENTA + f"$" + colorama.Fore.RED + f" ").strip()

        # Exit loop if the user enters "exit" or "quit"
        if user_input.lower() in ['exit', 'quit']:
            break

        # Handle custom commands
        elif user_input.lower() == 'help':
            print(command_List)

        elif user_input.lower().startswith('dc@tok$'):
            discord_id = user_input.split(' ')[-1]
            try:
                check = int(discord_id)
                print('')
                print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Valid ID!')
                data = f'{discord_id}'
                encodedBytes = base64.b64encode(data.encode("utf-8"))
                encodedStr = str(encodedBytes, "utf-8")
                print('')
                print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] {encodedStr}')
                print('')
                copy = input(
                    f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Do you want to copy this text? (y/n) {Fore.WHITE}')

                if copy.lower() == "y":
                    pyperclip.copy(encodedStr)
                    print('')
                    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Text Copied!')
                else:
                    print('')
                    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Press enter to exit')
                    input()

            except ValueError:
                print('')
                print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Invalid ID!')

        elif user_input.lower() == 'sudo help':
            print(sudo_cmd)

        elif user_input.lower() == 'discord':
            print(discord_cmd)

        # Execute other commands using the subprocess module, but don't allow Windows commands
        elif user_input and platform.system().lower() == 'windows':
            print("This command is not valid (Note: Windows commands don't work :D).")
        elif user_input:
            result = run_command(user_input)
            print(result)


if __name__ == "__main__":
    windows_terminal()
