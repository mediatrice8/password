import unittest
from credentials import Credential


class TestCredential(unittest.TestCase):
    '''test class for credential class
     Args:
         TestCase class that helps in creating test 
    '''
    
    def setUp(self):
        '''
        set up function to run before each test case
        '''
        self.new_credential = Credential("Instagram","mediay37","5555")
    def tearDown(self):
        '''
        tearDown method that does clean up after each test has run
        '''
        Credential.credential_list = []
    def test_init(self):
        '''
        test to initialize the object
        '''
        self.assertEqual(self.new_credential.account_type,"Instagram")
        self.assertEqual(self.new_credential.user_name,"mediay37")
        self.assertEqual(self.new_credential.password,"5555")