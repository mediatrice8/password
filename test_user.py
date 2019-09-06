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
    def tearDown(self):
        '''
        tearDown method to clean up after test runs
        '''
         User.user_names=[]
#------------------first test-------------------
    def  test_init(self):
        '''
        test_init used to test if the object is initialized well
        '''
        self.assertEqual(self.new_user.user_name,"media")
        self.assertEqual(self.new_user.password,"0000")
# -----------------second test---------------------
        