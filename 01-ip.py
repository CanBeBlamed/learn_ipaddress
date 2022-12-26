from ipaddress import IPv4Address, AddressValueError

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

def main():

    try:
        input_ip = input('IP address: ')
        ip_object = ipValid(input_ip)

        while not ip_object:
            print('Invalid IP address')
            input_ip = input('IP address: ')
            ip_object = ipValid(input_ip)

        if ip_object.is_global:
            print('Public IP address')
        elif ip_object.is_private:
            print('Private IP address')
        elif ip_object.is_loopback:
            print('Loopback address')
        elif ip_object.is_reserved:
            print('Reserved address')
        elif ip_object.is_link_local:
            print('Link local address')
        elif ip_object.is_multicast:
            print('Multicast address')
        else:
            print('Unknown address')

    except KeyboardInterrupt:
        exit('\nBye!')

if __name__ == '__main__':
    main()
