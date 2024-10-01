ip = '200.20.15.12'

ip = tuple(map(int, ip.split('.')))

if len(ip) != 4: raise Exception('Invalid IP address')

a = None
if ip[0] < 128:
    ip_class = 'A'
    a = 3
elif ip[0] < 192:
    ip_class = 'B'
    a = 2
elif ip[0] < 224:
    ip_class = 'C'
    a = 1
elif ip[0] < 240:
    ip_class = 'D'
else:
    ip_class = 'E'

if a is None:
    print('IP Class: ', ip_class)
    print('This IP address cannot be used to get internet access')
    exit()

b = 4 - a

network_address = ip[0:a] + (0,) * b
network_mask = (255,) * a + (0,) * b
range_addresses = 2 ** a
block_addresses = (
    ip[0 : a] + (0,)   * (b - 1) + (1,),
    ip[0 : a] + (255,) * (b - 1) + (254,)
)
broadcast_address = ip[0 : a] + (255,) * b

print()
print('IP Address: ',                          ip                 )
print('IP Class: ',                            ip_class           )
print('Network Mask: ',                        network_mask       )
print('Range of Addresses: ',                  range_addresses    )
print('Usable Addresses/Block of Addresses: ', range_addresses - 2)
print('* Network Address: ',                   network_address    )
print('* List of usable Addresses/Hosts: ',    block_addresses    )
print('* Broadcast Address: ',                 broadcast_address  )
print()

if ip[a:] == (0,) * b or ip[a:] == (255,) * b:
    print('This IP address cannot be used to get internet access')
else:
    print('This IP address can be used to get internet access')
    
print()