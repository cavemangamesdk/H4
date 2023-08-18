import requests
response = requests.get('https://api.ipify.org')
ip_address = response.text
print(f'Your IP Address is {ip_address}')