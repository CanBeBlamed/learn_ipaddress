from ipaddress import IPv4Address, AddressValueError, IPv4Network, NetmaskValueError

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
        ip_address = input('IP address: ')
        ip_object = ipValid(ip_address)
        print(ip_object)

        # while loop, asks for IP address until valid IP address entered
        while not ip_object:
            print('Invalid IP address!')
            ip_address = input('IP address: ')
            ip_object = ipValid(ip_address)
            
        net_cidr = input('CIDR: ')
        net_object = netValid(net_cidr)
        
        # while loop, asks for CIDR until valid CIDR entered
        while not net_object:
            print('Invalid CIDR!')
            net_cidr = input('CIDR: ')
            net_object = netValid(net_cidr)

        if net_object.network_address == ip_object:
            print('In subnet (Network address)')
        elif net_object.broadcast_address == ip_object:
            print('In subnet (Broadcast address)')
        elif net_object.network_address < ip_object < net_object.broadcast_address:
            print('In subnet')
        else:
            print('Not in subnet')


    except KeyboardInterrupt:
        exit('\nBye!')

if __name__ == '__main__':
    main()

