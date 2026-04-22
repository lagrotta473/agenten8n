import requests


class AgentOpenCloud:
    DEFAULT_HEADERS = {'Content-Type': 'application/json'}
    DEFAULT_TIMEOUT = 10

    def __init__(self, n8n_webhook_url, api_key=None, timeout=None):
        self.n8n_webhook_url = n8n_webhook_url
        self.api_key = api_key
        self.timeout = timeout or self.DEFAULT_TIMEOUT

    def _get_headers(self):
        headers = dict(self.DEFAULT_HEADERS)
        if self.api_key:
            headers['Authorization'] = f'Bearer {self.api_key}'
        return headers

    def send_payload(self, data):
        try:
            response = requests.post(
                self.n8n_webhook_url,
                headers=self._get_headers(),
                json=data,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.status_code, response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            return getattr(http_err.response, 'status_code', None), None
        except requests.exceptions.Timeout as timeout_err:
            print(f'Request timed out: {timeout_err}')
            return 500, None
        except Exception as err:
            print(f'An error occurred: {err}')
            return None, None
