import unittest
from credentials import Credential
import random


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
#--------------------first test-----------------------
    def test_init(self):
        '''
        test to initialize the object
        '''
        self.assertEqual(self.new_credential.account_type,"Instagram")
        self.assertEqual(self.new_credential.user_name,"mediay37")
        self.assertEqual(self.new_credential.password,"5555")
#-------------------second test----------------------
    def test_save_credential(self):
        """
        test save credential test case to test if the contact object is saved into the credential_list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)
