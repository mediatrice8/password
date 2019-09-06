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
    credential_list = []
# ------------------------save credential---------------
    def save_credential(self):
        """
        save_credential method saves credential objects into the credential_list
        """
        Credential.credential_list.append(self)
# -----------------------method to display---------------
    @classmethod
    def display_credentials(cls):
        """
        method that  returns the credential list
        """
        return cls.credential_list


        