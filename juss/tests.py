from django.test import TestCase
from juss import get_setting

def Test(TestCase):
    def test(self):
        res = get_setting()
        self.assertTrue(res)
