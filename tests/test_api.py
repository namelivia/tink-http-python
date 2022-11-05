# from tink_http_python.api import ApiV2, ApiV1
# from requests.models import Response
# from mock import patch


class TestApi:
    pass


# TODO: This patch is not working for some reason I don't know


"""
    @patch("requests.post")
    def test_post_api_v1(self, m_post):
        m_post.return_value = Response()
        ApiV1.post("some_url", {"header": "value"}, {"data": "value"})
        m_post.assert_called_once_with()

    @patch("requests.post")
    def test_post_api_v2(self, m_post):
        m_post.return_value = Response()
        ApiV2().post("some_url", {"header": "value"}, {"data": "value"})
        m_post.assert_called_once_with()

    @patch("requests.get")
    def test_get_api_v1(self, m_get):
        m_get.return_value = Response()
        ApiV1().post("some_url", {"header": "value"}, {"data": "value"})
        m_get.assert_called_once_with()

    @patch("requests.get")
    def test_get_api_v2(self, m_get):
        m_get.return_value = Response()
        ApiV2().post("some_url", {"header": "value"}, {"data": "value"})
        m_get.assert_called_once_with()
"""
