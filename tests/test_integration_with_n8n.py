import unittest
import requests
from agent_integration import AgentOpenCloud
import config


class TestIntegrationWithN8N(unittest.TestCase):
    VALID_DATA = {'field1': 'value1', 'field2': 'value2'}

    def test_happy_path(self):
        agent = AgentOpenCloud('https://httpbin.org/post')
        status_code, response = agent.send_payload(self.VALID_DATA)

        self.assertEqual(status_code, 200)
        self.assertIsNotNone(response)

    def test_happy_path_with_api_key(self):
        agent = AgentOpenCloud('https://httpbin.org/post', api_key='test-key')
        status_code, response = agent.send_payload(self.VALID_DATA)

        self.assertEqual(status_code, 200)
        self.assertIsNotNone(response)
        self.assertEqual(response['headers']['Authorization'], 'Bearer test-key')

    def test_server_error(self):
        agent = AgentOpenCloud('https://httpbin.org/status/500')
        status_code, response = agent.send_payload(self.VALID_DATA)

        self.assertEqual(status_code, 500)
        self.assertIsNone(response)

    def test_timeout(self):
        agent = AgentOpenCloud('https://httpbin.org/delay/20', timeout=1)
        status_code, response = agent.send_payload(self.VALID_DATA)

        self.assertEqual(status_code, 500)
        self.assertIsNone(response)

    def test_invalid_payload(self):
        agent = AgentOpenCloud('https://httpbin.org/status/400')
        status_code, response = agent.send_payload({'invalid_field': 'invalid_value'})

        self.assertEqual(status_code, 400)
        self.assertIsNone(response)


if __name__ == '__main__':
    unittest.main()
