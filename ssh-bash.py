import argparse
import paramiko
from easygui import *

host = enterbox("Adress ")
user = enterbox("User ")
passw = passwordbox("PASSWORD:")
port = enterbox("Port ")



def create_argparse():
    p = argparse.ArgumentParser(description="login info")
    p.add_argument("--host", action="store", dest="host", default=host, help="host")
    p.add_argument("--user", action="store", dest="user", default=user, help="username")
    p.add_argument("--passw", action="store", dest="passw", default=passw, help="password")
    return p


def get_args():
    parser = create_argparse()
    return parser.parse_args()


args = get_args()

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=args.host, username=args.user, password=args.passw, port=port)

    #stdin, stdout, stderr = client.exec_command("ls")
    #print(stdout.read())

    command = "grep blank /root/* -r | cut -d: -f1 | while read file ;do sed -i -e 's/blank/input/g' ${file} ; done"
    command1 = command.replace("blank", input("search for what? "))
    print(command1)
    command2 = command1.replace("root", input("search where? "))
    print(command2)
    command3 = command2.replace("input", input("replace to what? "))
    print(command3)


    stdin, stdout, stderr = client.exec_command("%s" % command3)
    #print(stdout.read())
    #print(stderr.read())
finally:
    client.close()


