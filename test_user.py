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
    def test_save_user(self):
        '''
        test to see if the user name is saved into usernames
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_names),1)
# ------------------third test-------------
    def test_save_multiple_user(self):
        '''
        test to check if we can save mulptile usernames
        '''
        self.new_user.save_user()
        test_user = User("Hope","0000")
        test_user.save_user()
        self.assertEqual(len(User.user_names),2)
# -------------four test-------------
    def test_user_exists(self):
        '''
        test for checking if we can return a boolean ,if we are not found the user
        '''
        self.new_user.save_user()
        test_user=User("Hope","0000")
        test_user.save_user()
        
        user_exists = User.user_exist("Hope")
        self.assertTrue(user_exists)
        
        
if __name__ == '__main__':
    unittest.main()
        
        