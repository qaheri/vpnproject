import subprocess
import random
import string
import os
import datetime

sudo_password=""
u=input("enter username: ")
e=int(input("enter expire: "))
def create_user(username,expire):
    # inn = str(input("username,password:\n"))
    letters = string.digits
    result_str = ''.join(random.choice(letters) for i in range(8))
    
    password = result_str
    print(f"password: {password}")
    # command = "useradd -p "+password+" "+username+" --shell=/bin/false"
    # command = command.split()

    # cmd1 = subprocess.Popen(['echo',sudo_password], stdout=subprocess.PIPE)
    # cmd2 = subprocess.Popen(['sudo'] + command, stdin = cmd1.stdout, stdout = subprocess.PIPE)
    # output = cmd2.stdout.read().decode()
    # print(output)

    subprocess.run(['sudo', 'useradd', username, '--shell=/bin/false'])

    expiration_date = datetime.date.today() + datetime.timedelta(days=expire)

    expiration_date_str = expiration_date.strftime('%Y-%m-%d')

    p = subprocess.Popen(['sudo', 'passwd', username], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(input=bytes(password + '\n' + password + '\n', 'utf-8'))

    print(output.decode('utf-8'))
    print(err.decode('utf-8'))

    result = subprocess.run(['sudo', 'chage', '-E', expiration_date_str, username])

    if result.returncode == 0:
        print(f"Successfully disabled account '{username}' after {expire} days.")
    else:
        print(f"Failed to disable account '{username}':")
        print(result.stderr)


create_user(username=u,expire=e)