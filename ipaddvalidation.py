import ipaddress
#ipaddress of ipv4
print(ipaddress.ip_address(u'192.3.4.50'))

print(ipaddress.ip_address(u'192.3.4.254'))

#ipaddress ipv6
print(ipaddress.ip_address(u'FFFF:9999:2000:FDE:257:0:9FAE:1120'))

print(ipaddress.ip_address(u'AAAB:9999:9000:FDE:257:0:9FAE:1120'))