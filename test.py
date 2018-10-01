import unittest
from ip_checker import ip_checker

ip_obj = ip_checker('123.111.23.1')

class IpCheckerTest(unittest.TestCase):
    def test(self):
        self.assertEqual(ip_obj.is_valid(), True)
        self.assertEqual(ip_obj.is_private(), False)
        self.assertEqual(ip_obj.is_private(), True)