#!/usr/bin/env python

# import re module
from re import findall

class ip_checker(object):
    def __init__(self, ipaddress):
        self.ip_address = ipaddress

    ## This method return Boolean "True or False" by checking wheter the given ip address is valid or not
    def is_valid(self):
        if not findall( "(?i)^(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5])$" ,self.ip_address):
            return False
        else:
            return True 
            

    
    ## This method checks whether the given ipaddress is private or public & returns True or False
    def is_private(self):
        if findall( "(?i)^192.168.(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5])$", self.ip_address ):
            return True
        elif findall( '(?i)^127.\d{1,3}.\d{1,3}.\d{1,3}$',self.ip_address):
            return True
        elif findall( '(?i)^10.(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5])$', self.ip_address):
            return True
        elif findall( '(?i)^172.(1[6-9]|2[0-9]|3[0-1]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5])$', self.ip_address):
            return True
        else: return False

    ## Check if the ip address is public or not
    def is_public(self):
        if self.is_valid() and not self.is_private():
            return True
        else:
            return False