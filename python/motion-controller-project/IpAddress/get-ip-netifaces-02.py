import netifaces as ni

def get_local_ip_address() -> str:
    ip_address = 'Not found'
    interfaces = ni.interfaces()
    for interface in interfaces:
        if 'wlan' in interface:
            try:
                ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
                # Exclude localhost
                if ip != '127.0.0.1':
                    ip_address = ip
                    break
            except KeyError:
                pass

    print(f"Local IP address: {ip_address}")
    return ip_address

if __name__ == "__main__":
    get_local_ip_address()