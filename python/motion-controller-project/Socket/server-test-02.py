import socket

subnet = '192.168.109.'
mask = '255.255.255.0'
port = 12345  # Replace with the port number you want to use

subnet_octets = subnet.split('.')
mask_octets = mask.split('.')

# Check if the subnet and mask strings are correctly formatted
if len(subnet_octets) != 2 or len(mask_octets) != 4:
    print("Invalid subnet or mask format. Please make sure they are correctly formatted.")
    exit()

try:
    # Calculate the network address
    network_octets = [str(int(subnet_octets[i]) & int(mask_octets[i])) for i in range(2, 4)]
    network_address = subnet + '.'.join(network_octets)

    # Calculate the number of available host addresses
    available_hosts = 2 ** sum([bin(int(octet)).count('1') for octet in mask_octets]) - 2

    # Iterate through the host addresses and check availability
    for i in range(1, available_hosts + 1):
        host = network_address + '.' + str(i)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex((host, port))
            if result != 0:
                print(f"Available local address: {host}")
                break
except ValueError:
    print("Invalid subnet or mask format. Please make sure they are correctly formatted.")
