'''

	Simulates requesting the /kingdom_death endpoint with the unittest
	param.

'''

import unittest
from kdm-manager-api.app import API

class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        self.API = API.test_client()
        self.API.testing = True  # Set testing mode to True

    def test(self):
        # Send a GET request to the home page
        response = self.API.get('/kingdom_death')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the expected content
#        self.assertIn(b'Hello, World!', response.data)


if __name__ == '__main__':
    unittest.main()
