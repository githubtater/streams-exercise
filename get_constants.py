#!/usr/bin/env python3
import socket
from pprint import pprint

def get_constants(prefix):
    """filtered mapping of socket module constants to their names"""
    return {
        getattr(socket, name): name
        for name in dir(socket) if name.startswith(prefix)
    }

def get_address_info(host, port):
    for response in socket.getaddrinfo(host, port):
        family, s_type, protocol, name, address = response
        print('family: {}'.format(family))
        print('type: {}'.format(s_type))
        print('protocol: {}'.format(protocol))
        print('canonical name: {}'.format(name))
        print('socket address: {}'.format(address))
        print('')


pprint(get_constants('AF'))
pprint(get_constants('SOCK'))
pprint(get_constants('IPPROTO_'))
get_address_info(socket.gethostname(), 'https')