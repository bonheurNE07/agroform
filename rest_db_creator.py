from db_creator import createDb
import unittest

# Create a test class that inherits from unittest.TestCase
class TestCreateDbFunction(unittest.TestCase):

    def test_create_valid_db(self):
        # Test creating a valid database
        db_name = "form_db"
        createDb(db_name)
        # Add additional assertions here if needed
        self.assertTrue(True)  # Placeholder assertion

    def test_create_invalid_db(self):
        # Test creating a database with an invalid name
        db_name = None
        with self.assertRaises(TypeError):
            createDb(db_name)
        
        # Add additional assertions here if needed
        self.assertTrue(True)  # Placeholder assertion

if __name__ == '__main__':
    unittest.main()