class Credential:
    '''
    class that provide the instances of credential
    '''
    def __init__(self,account_type,user_name,password):
        '''
        function that helps ud to initialize the properties
          Args:
          acccount-name: the type of account-type or the kind of platform
          user_name: the username for the account.
          password: password for the account.
        '''
        self.account_type = account_type
        self.user_name = user_name
        self.password = password
    credxntial_list = []
        