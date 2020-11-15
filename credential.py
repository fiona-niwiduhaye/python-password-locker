
class Credential:
    '''
    Class that generates instances of a users credentials
    '''
    # Empty list of credentials
    credential_list = []

    def __init__(self, user_password, credential_name, credential_password):
        '''
        __init__ method to define the properties of a User object
        Args:

            credential_name : name of an account
            user_password : password of the user
            credential_password : password for the user account
        '''
        self.user_password = user_password
        self.credential_name = credential_name
        self.credential_password = credential_password

         def save_credential(self):
        '''
        Method that saves a user's credentials to credential list
        '''
        Credential.credential_list.append(self)
@classmethod
    def display_credential(cls,password):
        '''
        Method that returns the credential list
        Args:
            password : the user password
        '''
        user_credential_list = []

        for credential in cls.credential_list:
            if credential.user_password == password:
                user_credential_list.append(credential)

        return user_credential_list


    @classmethod
    def credential_exist(cls, name):
        
        '''
        Method that checks if a credential exists in the credential list
        
        Args:
            name: name of the credential to search
            
        Returns:
            Boolean: true or false depending if the contact exists
            
        '''
        
        for credential in cls.credential_list:
            if credential.credential_name == name:
                return True
            
        return False