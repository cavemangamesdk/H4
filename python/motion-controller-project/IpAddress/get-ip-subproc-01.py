# 1
# import os
# print(os.system('ipconfig'))
# print(os.system('hostname'))

# 2
# import socket
# hostname = socket.gethostname()
# print(hostname)
# ip_address = socket.gethostbyname(hostname)
# print(ip_address)

# 3
# from netifaces import interfaces, ifaddresses, AF_INET
# for ifaceName in interfaces():
#     addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
#     print(' '.join(addresses))

# 4
# import subprocess
# import re
# def get_ip_address():
#     ipconfig_result = subprocess.run(['ipconfig'], stdout=subprocess.PIPE).stdout.decode('utf-8')
#     ip_address = re.search(r'IPv4 Address.*: (.*)', ipconfig_result).group(1)
#     return ip_address

# print(get_ip_address())

# 5
import socket
 
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('192.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
 
local_ip = get_local_ip()
print(local_ip)