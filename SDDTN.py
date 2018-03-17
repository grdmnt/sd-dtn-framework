from abc import ABCMeta, abstractmethod 

class SDDTN:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.flow_tables = {}
        
    @abstractmethod
    def boot(self):
        pass
    
    @abstractmethod
    def packet_in(self):
        pass

    @abstractmethod
    def alive(self):
        pass

    def add_flow(self, ip_address, flow):
        self.__validate_ip_address(ip_address)
        self.__validate_flow(flow)

        if not ip_address in self.flow_tables.keys():
            self.flow_tables[ip_address] = []

        self.flow_tables[ip_address].append(flow)

    def get_flow_table(self, ip_address):
        try:
            return self.flow_tables[ip_address]
        except KeyError:
            print('IP Address ' + ip_address + ' does not exist in flow tables')
    
    def __validate_flow(self, flow):
        pass

    def __validate_ip_address(self, ip_address):
        if not type(ip_address) == str:
            raise TypeError('IP Address should be a string')

        ip_address = ip_address.split('.')

        if len(ip_address) != 4:
            raise ValueError('IP Address format is invalid, IP Address given: ' + '.'.join(ip_address))

        for section in ip_address:
            if len(section) < 1 or len(section) > 3:
                raise ValueError('IP Address format is invalid, IP Address given: ' + '.'.join(ip_address))

    
            