class User:
    '''
    A class for the users
    '''
    def __init__(self,user_name,password):
        '''
        method to initialize the object
        Args:
            user_name: New user usename.
            password : New user password.
        '''
        self.user_name=user_name
        self.password=password
    user_names = []