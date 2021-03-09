import unittest
from flask import current_app
from app import create_app


class OpenLogFile():
    def openLogFile():
        with open ("request.log", 'r') as f:
            data = f.read()
        return data


class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def testGetBasic(self):
        rv = self.client.get('/get')  
        self.assertTrue(rv, {'1': "helloworld"})

    def testLogFile(self):
        if current_app.config['LOG_REQUEST'] == True or current_app.config['LOG_RESPONSE'] == True:
            self.assertIsNotNone(OpenLogFile.openLogFile())
    
    def testHideHeader(self):
        if current_app.config['Host'] == False:
            self.assertNotIn("Host", OpenLogFile.openLogFile())

    def testHideCookie(self):
        if current_app.config["Cookie"] == False:
            self.assertNotIn("Cookie", OpenLogFile.openLogFile())

    def testResponse(self):
        if current_app.config['LOG_RESPONSE'] == True:
            self.assertIn("RESPONSE header", OpenLogFile.openLogFile())
            self.assertIn("RESPONSE payload", OpenLogFile.openLogFile())

if __name__ == '__main__':
    unittest.main()