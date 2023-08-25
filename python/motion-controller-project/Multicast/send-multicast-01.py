import socket
import psutil

def get_local_ip_address(interface):
    interface_addrs = psutil.net_if_addrs().get(interface) or []
    for snicaddr in interface_addrs:
            if snicaddr.family == socket.AF_INET:
                    return snicaddr.address
    #return False

print(get_local_ip_address("wlan0"))