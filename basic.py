import subprocess
import random
import string
import os

sudo_password="32388261Aa"

def create_user(username, expire):
    # inn = str(input("username,password:\n"))
    letters = string.digits
    result_str = ''.join(random.choice(letters) for i in range(8))
    
    password = result_str
    
    command = "useradd -p "+password+" "+username+" --shell=/bin/false"
    command = command.split()

    cmd1 = subprocess.Popen(['echo',sudo_password], stdout=subprocess.PIPE)
    cmd2 = subprocess.Popen(['sudo'] + command, stdin = cmd1.stdout, stdout = subprocess.PIPE)

    output = cmd2.stdout.read().decode()
    print(output)
    os.system(f'sudo chage -E $(date -d "+{expire} days" +%Y-%m-%d) {username}')
    
create_user(username=input("enter username: ", expire=input("enter expire: ")))