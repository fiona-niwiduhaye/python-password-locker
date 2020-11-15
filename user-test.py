import unittest # Importing the unittest module

from user import User # Importing the user class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User Class behaviours
    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

def setUp(self):
        '''
        Set up method to run before each test case
        '''

        # Create user object
        self.new_user = User("fiona","niwiduhaye")
 def test_init(self):
        '''
        Test case to test if the object is initialised properly
        '''

        self.assertEqual( self.new_user.user_name, "fiona" )
        self.assertEqual( self.new_user.user_password, "niwiduhaye" )


    def tearDown(self):
        '''
        tearDown method that cleans up after each test case is run
        '''

        User.user_list = []

        def test_save_user(self):
        
        '''Test case to test if the user object is saved into the user list'''
          # Saving the new user
        self.new_user.save_user()

        self.assertEqual( len(User.user_list), 1 )

    def test_save_multiple_users(self):
        '''
        Test case to test if you can save multiple objects to user list
        '''
         
        # Save the new user
        self.new_user.save_user()

        test_user = User("fiona","niwiduhaye")

        test_user.save_user()

        self.assertEqual( len(User.user_list), 2)

        def test_log_in(self):
        '''
        Test case to test if a user can log into their credentials
        '''

        # Save the new user
        self.new_user.save_user()

        test_user = User("fiona","niwiduhaye")

        test_user.save_user()

        found_credential = User.log_in("fiona", "niwiduhaye")

        self.assertEqual( found_credential,  Credential.credential_list )   
     def test_display_user(self):
        '''
        Test case to test if a user can see a list of all the users saved
        '''
        
        self.assertEqual( User.display_user() , User.user_list )
        
         def test_user_exist(self):
        
        '''
        Test to check if we can return a boolean if we can't find the user
        '''
          # Save the new user
        self.new_user.save_user()

        test_user = User("fiona","niwiduhaye")

        test_user.save_user()
        
        # use contact exist method
        user_exists = User.user_exist("fiona")
        
        self.assertTrue(user_exists)

if __name__ == '__main__':
    unittest.main()