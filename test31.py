#!/usr/bin/python3



from scapy.all import *

ip = IP(src="10.0.2.18", dst="10.0.2.21")

tcp = TCP(sport=1070, dport=80)

tcp.flag=2

payload = 'A' * 80

pkt = ip/tcp/payload
send(pkt, varbose=0)