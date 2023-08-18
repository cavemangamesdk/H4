from zeroconf import Zeroconf, ServiceInfo
import socket

# Get local IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_address = s.getsockname()[0]
print(ip_address)
s.close()

# Setup Zeroconf service
zeroconf = Zeroconf()
service_info = ServiceInfo(
    "_http._tcp.local.",
    "My WebSocket._http._tcp.local.",
    addresses=[socket.inet_aton(ip_address)],
    port=8000,
    properties={'path': '/ws'},
    server="myserver.local.",
)
zeroconf.register_service(service_info)
