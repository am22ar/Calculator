import ipaddress

print(ipaddress.ip_address(u'192.3.5.90')>ipaddress.ip_address(u'192.3.4.90'))

print(ipaddress.ip_address(u'192.3.4.90')==ipaddress.ip_address(u'192.3.4.90'))

print(ipaddress.ip_address(u'192.3.4.90')!=ipaddress.ip_address(u'192.3.4.90'))