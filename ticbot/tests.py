from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch, MagicMock

from utils import send_slack_message


class TICBotTestCase(TestCase):
    @patch('utils.requests.post')
    def test_send_slack_message(self, mock_request):
        magic_mock = MagicMock()
        magic_mock.status_code = HTTPStatus.OK
        magic_mock.text = 'ok'
        mock_request.return_value = magic_mock

        send_slack_message({'text': 'test message'})

    @patch('utils.requests.post')
    def test_send_slack_message_failed_without_text(self, mock_request):
        '''data에 text가 포함되지 않으면 에러 발생하는지'''
        magic_mock = MagicMock()
        magic_mock.status_code = HTTPStatus.BAD_REQUEST
        magic_mock.text = 'no_text'
        mock_request.return_value = magic_mock

        with self.assertRaisesRegex(ValueError, 'must have "text"'):
            send_slack_message({'invalid_text': 'invalid_value'})
