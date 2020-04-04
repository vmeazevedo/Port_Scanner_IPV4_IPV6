#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

import socket
import time

t = 3

print('\nEsse teste serve para nalisar se alguma porta pode estar aberta, e irá realizar uma varedura pela porta 1 até a 9999.')
input('Digite enter para iniciar o scan.\n')
print('Processando...')
time.sleep(t)

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

for port in range(1,9999):
    result = portscan(port)
    if(result):
        print('A porta {} está aberta!'.format(port))
    else:
        print('A porta {} está fechada!'.format(port))

