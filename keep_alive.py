import socket
from xml.dom import minidom
import codecs
import sys
import time

decode_hex = codecs.getdecoder("hex_codec")

HandShake = {b'U\xaa\x00\x06\x05\x02\x00\x00\x0c\x19U\xaa': b'U\xaa\x00\x06\x06\x02\x00\x00\x01\x0fU\xaa',
             b'U\xaa\x00\x06\x05\x03\x00\x00\x16$U\xaa': b'U\xaa\x01\x16\x06\x01\x00\x00\x03\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x00@@@@@@@@\x01\x01#U\xaa',
             b'U\xaa\x00\x08\x05\x04\x00\x00\x15\xd3\xb5\xaeU\xaa': b'U\xaa\x00\x1b\x06\x01\x00\x00\x16Ver 04.11.00|DS 05.02/U\xaa',
}

while True:

    IFSEI = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    IFSEI.settimeout ( 3 )
    IFSEI_address = ( '192.168.1.202', 25200 )

    try:

        for k in HandShake.keys():
            print (k)
            sent = IFSEI.sendto(k, IFSEI_address)
            data, server = IFSEI.recvfrom(512)
            print (data)
        while True:
            for k in HandShake.keys():
                print (k)
                sent = IFSEI.sendto(k, IFSEI_address)
                data, server = IFSEI.recvfrom(512)
                print (data)
                if data != HandShake [k]:
                    raise Exception ("2")
                break
            IFSEI.close
            time.sleep (60)
            IFSEI = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            IFSEI.settimeout ( 3 )
            IFSEI_address = ( '192.168.1.202', 25200 )
       
    except:
            
        IFSEI.close






