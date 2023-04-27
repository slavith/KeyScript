from discord_webhook import DiscordWebhook
import random
import string
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import os


webhook_url = input(f"{Fore.MAGENTA}[{Fore.RED}WEBHOOK{Fore.MAGENTA}] >> {Fore.RED}")
program_path = input(f"{Fore.MAGENTA}[{Fore.RED}SCRIPT PATH{Fore.MAGENTA}] >> {Fore.RED}")


new_pw = "S4-" + "".join(random.choices(string.digits + string.ascii_letters, k=16))


result = f"""
**Your Script Key Has Been Generated**
**Key: **`{new_pw}`"""
wb = DiscordWebhook(url=webhook_url, content=result, username="KeyScript")
wb.execute()

with open(program_path, 'r') as w:
    s = w.read()
    wb1 = DiscordWebhook(url=webhook_url, content="**Getting Your Script Ready To Swap**", username="KeyScript")
    wb1.execute()
with open('key_app.py', 'w+', encoding="utf-8") as b:
    b.write(f"""

key = "{new_pw}"

key_to_enter = input("key: ")


if key_to_enter == key:
    pass
else:
    quit()

{s}
""")
wb2 = DiscordWebhook(url=webhook_url, content="**Your New Program Has Been Built! (py)**", username="KeyScript")
wb2.execute()
py_to_exe = input(f"{Fore.MAGENTA}[{Fore.RED}PY TO EXE{Fore.MAGENTA}] (y/n | need python) >> {Fore.RED}")

if py_to_exe == 'y':
    os.system("pip install pyinstaller")
    icon = input(f"{Fore.MAGENTA}[{Fore.RED}ICON PATH{Fore.MAGENTA}] >> {Fore.RED}")
    os.system(f'pyinstaller -F -i "{icon}" key_app.py')
    wb3 = DiscordWebhook(url=webhook_url, content="**Your New Program Has Been Built! (exe)**", username="KeyScript")
    wb3.execute()
    print(f"{Fore.RED}Done!")
    input("")
else:
    print(f"{Fore.RED}Done!")
    input("")


