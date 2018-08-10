# Backdoor

Example of a server and a client keep communication using sockets in python. First of all change the IP from HOST in client.py.


Steps:


clone the project

```sh
$ git clone https://github.com/jmessiass/backdoor.git
```
install requirements and execute the server using python 3.
```sh
$ cd backdoor
$ pip install -r requirements.txt
$ python3 server.py -p 12345 (choose any port)
```
in another machine, execute the client (don't forget of using the same port from server)

```sh
$ python client.py
```
if everything occurred good you gain access in computer from victim.
