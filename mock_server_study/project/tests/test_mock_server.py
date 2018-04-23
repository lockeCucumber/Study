# Third-party imports...
from nose.tools import assert_true 
import json
import requests
 
from project.tests.mocks import get_free_port, start_mock_server, MockServerRequestHandler

class TestMockServer(object):
    @classmethod
    def setup_class(cls):
        # Configure mock server.
        cls.mock_server_port = get_free_port()
        start_mock_server(cls.mock_server_port)

    def test_get_response(self):
        url = 'http://localhost:{port}/users'.format(port=self.mock_server_port)

        # Send a request to the mock API server and store the response.
        response = requests.get(url)

        # Confirm that the request-response cycle completed successfully.
        print(response)
        assert_true(response.ok)

    def test_post_response(self):
        url = 'http://localhost:{port}/api'.format(port=self.mock_server_port)

        # Send a request to the mock API server and store the response.
        response = requests.post(url, json={"2":"d"})

        print json.loads(response.content)

        assert json.loads(response.content) == {"w":"we"}
