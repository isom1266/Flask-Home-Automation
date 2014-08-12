# Wake-On-LAN
#
# Copyright (C) 2002 by Micro Systems Marc Balmer
# Written by Marc Balmer, marc@msys.ch, http://www.msys.ch/
# This code is free software under the GPL

import struct, socket

def WakeOnLan(ip, ethernet_address):

  # Construct a six-byte hardware address

  addr_byte = ethernet_address.split(':')
  hw_addr = struct.pack('BBBBBB', int(addr_byte[0], 16),
    int(addr_byte[1], 16),
    int(addr_byte[2], 16),
    int(addr_byte[3], 16),
    int(addr_byte[4], 16),
    int(addr_byte[5], 16))

  # Build the Wake-On-LAN "Magic Packet"...

  msg = '\xff' * 6 + hw_addr * 16

  # ...and send it to the broadcast address using UDP

  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  #s.sendto(msg, ('', 9))
  s.sendto(msg, (ip, 9))
  s.close()

# Example use
#WakeOnLan('192.168.2.101','f4:6d:4:93:11:82')
# WakeOnLan('192.168.1.15','64:66:b3:0f:c5:b6') # RPi
if __name__ == "__main__":
  WakeOnLan('192.168.1.100','f4:6d:4:93:11:82')