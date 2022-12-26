from ipaddress import IPv4Address, AddressValueError, IPv4Network

def ipValid(ip_address):

    '''
    Validates IP address. If IP address is valid, it returns the ipadress.IPv4Address object,
    if not valid it returns None
    '''

    try:
        ip_obj = IPv4Address(ip_address)
        return ip_obj

    except AddressValueError:
        pass

def netValid(cidr):

    '''
    Validates CIDR. If CIDR address is valid, it returns the ipadress.IPv4Network object,
    if not valid it returns None
    '''

    try:
        network_object = IPv4Network(cidr, strict=False)
        return network_object

    except AddressValueError:
        pass

    except NetmaskValueError:
        pass


def main():

    try:
        net_cidr = input('CIDR: ')
        network_object = netValid(net_cidr)

        while not network_object:
            print('Invalid CIDR')
            net_cidr = input('CIDR: ')
            network_object = netValid(net_cidr)

        print('Network address: {}'.format(network_object.network_address))
        print('Broadcast address: {}'.format(network_object.broadcast_address))
        print('Subnet mask: {}'.format(network_object.netmask))
        print('Max hosts in subnet: {}'.format(network_object.num_addresses - 2))


    except KeyboardInterrupt:
        exit('\nBye!')

if __name__ == '__main__':
    main()
