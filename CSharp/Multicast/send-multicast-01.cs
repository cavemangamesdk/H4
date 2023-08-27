// See https://aka.ms/new-console-template for more information
using System.Net;
using System.Net.Sockets;
using System.Text;

const int Port = 4567; // 58008;

Console.WriteLine("Hello, World!");

string localIPAddress = GetLocalIPAddress();

var socket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);

var multicastAddress = IPAddress.Parse("224.1.1.1");

// Join multicast group
socket.SetSocketOption(SocketOptionLevel.IP, SocketOptionName.AddMembership, new MulticastOption(multicastAddress));

// TTL
socket.SetSocketOption(SocketOptionLevel.IP, SocketOptionName.MulticastTimeToLive, 2);

// Create an endpoint
IPEndPoint ipep = new IPEndPoint(multicastAddress, Port);

// Connect to the endpoint
socket.Connect(ipep);

// Scan message
while (true)
{
    byte[] buffer = new byte[1024];
    buffer = Encoding.ASCII.GetBytes(localIPAddress);
    socket.Send(buffer, buffer.Length, SocketFlags.None);

    Thread.Sleep(1000);
}

// Close socket
//socket.Close();

static string GetLocalIPAddress()
{
    var hostname = Dns.GetHostName();

    var ip = Dns.GetHostEntry(Dns.GetHostName()).AddressList
        .First(ips => ips.AddressFamily == AddressFamily.InterNetwork)
        .ToString();

    Console.WriteLine(hostname);
    Console.WriteLine(ip);
    return ip;
}