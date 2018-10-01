#!/usr/bin/env python

# import re module
from re import findall

class ip_checker(object):
    def __init__(self, ipaddress):
        self.ip_address = ipaddress

    ## This method return Boolean "True or False" by checking the given ip address
    def is_valid(self):
        if not findall( "(?i)^(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5]).(\d|\d\d|1[0-9][0-9]|2[0-9][0-5])$" ,self.IP):
            return False
        else:
            return True