import socket   
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   
print("Your Computer Name is:"+hostname)   
print("Your Computer IP Address is:"+IPAddr) 

# import ifaddr

# def get_local_wlan_ip():
#     adapters = ifaddr.get_adapters()

#     for adapter in adapters:
#         if 'wlan' in adapter.nice_name.lower():
#             for ip in adapter.ips:
#                 if ip.is_IPv4:
#                     return ip.ip

#     return None

# local_ip = get_local_wlan_ip()

# if local_ip:
#     print("Local WLAN IP Address:", local_ip)
# else:
#     print("Unable to retrieve local WLAN IP address.")

# import netifaces

# def get_local_wlan_ip():
#     interfaces = netifaces.interfaces()

#     for interface in interfaces:
#         if 'wlan' in interface:
#             addresses = netifaces.ifaddresses(interface)
#             if netifaces.AF_INET in addresses:
#                 ip_info = addresses[netifaces.AF_INET][0]
#                 ip_address = ip_info['addr']
#                 return ip_address

#     return None

# local_ip = get_local_wlan_ip()

# if local_ip:
#     print("Local WLAN IP Address:", local_ip)
# else:
#     print("Unable to retrieve local WLAN IP address.")


# import netifaces

# def get_local_ip():
#     interfaces = netifaces.interfaces()

#     for interface in interfaces:
#         if 'wlan' in interface:
#             addresses = netifaces.ifaddresses(interface)
#             if netifaces.AF_INET in addresses:
#                 ip_info = addresses[netifaces.AF_INET][0]
#                 ip_address = ip_info['addr']
#                 return ip_address

#     return None

# local_ip = get_local_ip()
# if local_ip:
#     print("Local WLAN IP address:", local_ip)
# else:
#     print("Local WLAN IP address not found.")



# import netifaces as ni

# def get_local_ip_address() -> str:
#     ip_address = 'Not found'
#     interface_name = 'Wi-Fi'
#     try:
#         ip = ni.ifaddresses(interface_name)[ni.AF_INET][0]['addr']
#         # Exclude localhost
#         if ip != '127.0.0.1':
#             ip_address = ip
#     except (KeyError, ValueError):
#         pass

#     print(f"Local IP address: {ip_address}")
#     return ip_address

# if __name__ == "__main__":
#     get_local_ip_address()