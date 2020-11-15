import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the Credential Class behaviours
    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''
     def setUp(self):
        '''
        Set up method to run before each test case
        '''
        # Create credential object
        
        self.new_credential = Credential("fiona","gmail","gmail2020")

    def tearDown(self):
        '''
        tearDown method that cleans up after each test case is run
        '''

        Credential.credential_list = []

         def test_init(self):
        '''
        Test case to test if the object is initialised properly
        '''
        self.assertEqual( self.new_credential.user_password, "fiona")
        self.assertEqual( self.new_credential.credential_name, "gmail" )
        self.assertEqual( self.new_credential.credential_password, "gmail2020" )
        #method to test saving 
        def test_save_credential(self):
        '''
        Test case to test if the user object is saved into the user list
        '''
# Save the new credential

        self.new_credential.save_credential()

        self.assertEqual( len(Credential.credential_list), 1 )

    def test_save_multiple_credentials(self):
        '''
        Test case to test if you can save multiple objects to credential list
        '''