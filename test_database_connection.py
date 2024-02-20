import unittest
import threading
from unittest.mock import patch
from weather_app_sergey import connect_to_database

class TestDatabaseConnection(unittest.TestCase):    
    connection_checked = False

    @classmethod
    def setUpClass(cls):        
        if not cls.connection_checked:
            cls.connection_checked = True
            cls.check_connection()

    @classmethod
    def check_connection(cls):       
        with patch('weather_app_sergey.create_engine') as mock_create_engine:
            mock_engine = mock_create_engine.return_value
            mock_metadata = mock_engine.return_value
            result = connect_to_database()
            cls.assertEqual(result, mock_metadata)

    def test_dummy(self):        
        pass

    def test_timeout(self):        
        timer = threading.Timer(10, self.fail_test)
        timer.start()
        timer.join()

    def fail_test(self):        
        self.fail("Тест завершился по таймауту")

if __name__ == '__main__':
    unittest.main()
