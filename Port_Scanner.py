import socket
from IPy import IP


# 192.168.184.128

class PortScan():
    banners = []
    openPort = []

    def __init__(self, target, portNumber):
        self.targets = target
        self.portNumber = portNumber

    def scan(self):
        for port in range(1, self.portNumber):
            self.scanPort(port)

    def check_ip(self):
        try:
            return IP(self.targets)
        except ValueError:
            return socket.gethostbyname(self.targets)

    def scanPort(self, port):
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip, port))
            self.openPort.append(port)
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
            except:
                self.banners.append(" ")
            sock.close()
        except:
            pass
