import netifaces

interfaces = netifaces.interfaces()
for interface in interfaces:
    addresses = netifaces.ifaddresses(interface)
    ip_info = addresses.get(netifaces.AF_INET)
    if ip_info:
        for ip in ip_info:
            ip_address = ip['addr']
            if ip_address != '127.0.0.1':
                print("Available local address:", ip_address)
                break
