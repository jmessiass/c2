from colorama import Fore, Back, Style
import socket
import sys

# Created by Jonathan Messias - jmcybers@gmail.com
# GitHub https://github.com/jmessiass


class Server(object):

    def __init__(self):
        self.__host = '0.0.0.0'
        try:
            if sys.argv[1] == '-help' or sys.argv[1] == '--help':
                self.info()
                sys.exit()
            elif sys.argv[1] == '-p' and int(sys.argv[2]):
                self.__port = int(sys.argv[2])
            else:
                print(Back.RED + '[*] unknown option %s' % sys.argv[1] + Style.RESET_ALL)
                self.exit_script(example=True)
        except ValueError:
                print(Back.RED + '[*] invalid port %s' % sys.argv[2] + Style.RESET_ALL)
                self.exit_script(example=True)
        except IndexError:
                print('[*] set a port')
                sys.exit('[*] usage: python server.py -p port')

    def create(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            server_socket.bind((self.__host, self.__port))
            return server_socket
        except PermissionError:
            sys.exit(Back.RED + '[*] This port require permission from sudo' + Style.RESET_ALL)
        except OSError:
            sys.exit(Back.RED + '[*] Port %s in use' % sys.argv[2] + Style.RESET_ALL)

    def listen(self, server_socket):
        server_socket.listen(5)  # maximo de 5 conexoes na fila por vez
        print(Fore.GREEN + '\n[ Info ]' + Fore.BLUE + ' Listening on localhost:' + str(self.__port) + Style.RESET_ALL)

    def connect(self, server_socket):
        client_socket, (client_ip, client_port) = server_socket.accept()  # aceita a conexao do cliente
        print(Style.BRIGHT + Fore.YELLOW + '[ Pwd ]' + Fore.CYAN + ' Connection established from ' + client_ip + '\n' + Style.RESET_ALL)

        while True:
            command = input(Style.BRIGHT + '$ ' + Style.RESET_ALL)
            client_socket.sendall(command.encode())

            if command == '':
                continue
            elif command == 'quit' or command == 'exit' or command == 'q':
                print(Fore.GREEN + '\n[ Info ]' + Fore.BLUE + ' Session ended\n' + Style.RESET_ALL)
                break

            data = client_socket.recv(1024)
            print(data.decode())

        client_socket.close()

    def info(self):
        print(Style.BRIGHT + '''
-p    > specify the port that you will listen
-help > show help
example: python server.py -p port
        ''')

    def exit_script(self, example=False):
        if example:
            return sys.exit(Fore.GREEN + '[*] usage: python server.py -p port' + Style.RESET_ALL)
        else:
            return sys.exit()


if __name__ == '__main__':
    server = Server()
    sock = server.create()
    server.listen(sock)
    server.connect(sock)
