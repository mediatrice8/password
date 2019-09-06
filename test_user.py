import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test case of user features
    Args:
        unittest.TestCase: class helps to create the test of class"
    '''
    def setUp(self):
        '''
        set up method torun before each test case.
        '''
        self.new_user = User("media","0000")