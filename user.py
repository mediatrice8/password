class User:
    '''
    A class for the users
    '''
    user_names = []
    def __init__(self,user_name,password):
        '''
        method to initialize the object
        Args:
            user_name: New user usename.
            password : New user password.
        '''
        self.user_name=user_name
        self.password=password
    def save_user(self):
        '''
        method to save the object into usernames
        '''
        User.user_names.append(self)
        
#  ---------exit------------------------
    @classmethod
    def user_exist(cls,user_name):
        '''
        method used to check if user exit from usernames
        '''
        for user in cls.user_names:
            if user.user_name == user_name:
                return True
        return False