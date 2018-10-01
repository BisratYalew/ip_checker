#!/usr/bin/env python

# import re module
from re import findall

class ip_checker(object):
    def __init__(self, ipaddress):
        self.ip_address = ipaddress

    ## This method return Boolean "True or False" by checking wheter the given ip address is valid or not
    def is_valid(self):
        if not findall( "(?i)^(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5])$" ,self.IP):
            return False
        else:
            return True 

    
    ## This method checks whether the given ipaddress is private or public & returns True or False
    def is_private(self):
        if findall( "(?i)^192.168.(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5])$", self.ip_address ):
            return True
        else if findall( '(?i)^127.\d{1,3}.\d{1,3}.\d{1,3}$',self.ip_address):
            return True
        else if findall( '(?i)^10.(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5])$', self.IP):
            return True
        else if findall( '(?i)^172.(1[6-9]|2[0-9]|3[0-1]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5])$', self.IP):
            return True
        else return False