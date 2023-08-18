from zeroconf import Zeroconf, ServiceBrowser, ServiceListener
import websockets
import asyncio
import socket

class MyListener(ServiceListener):
    async def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info:
            for address in info.addresses:
                ip_address = socket.inet_ntoa(address)
                print("Found service at {}:{}".format(ip_address, info.port))
                # Connect to WebSocket server
                uri = "ws://{}:{}/ws".format(ip_address, info.port)
                async with websockets.connect(uri) as websocket:
                    # Add your code here to interact with the WebSocket server
                    pass

zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)

try:
    input("Press enter to exit...\n\n")
finally:
    zeroconf.close()
