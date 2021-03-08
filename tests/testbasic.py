import unittest
from flask import request, current_app
from app import create_app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        # self.client = current_app.test_client()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()
        

    def testBasic(self):
        rv = self.client.get('/get')  
        self.assertTrue(rv, {'1': "hello"})

    def test_log_file(self):
        current_app.config['LOG_REQUEST'] = True
        with open "logging.log" as f:
            data = f.read()

if __name__ == '__main__':
    unittest.main()