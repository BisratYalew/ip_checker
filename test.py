import unittest
from ip_checker import ip_checker

ip_obj = ip_checker('123.111.23.1')

class IP_ADDRESS_VALIDITY_CHECKER(unittest.TestCase):
    def test(self):
        self.assertEqual(ip_obj.is_valid(), True)

class CHECK_IF_IP_ADDRESS_IS_PRIVATE(unittest.TestCase):
    def test(self):
        self.assertEqual(ip_obj.is_private(), False)

class CHECK_IF_IP_ADDRESS_IS_PUBLIC(unittest.TestCase):
    def test(self):
        self.assertEqual(ip_obj.is_public(), True)