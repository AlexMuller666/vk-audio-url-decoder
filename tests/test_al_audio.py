import unittest
import vaud
from os import path, name
current_dir = path.dirname(path.realpath(__file__))


class MockAlAudio(vaud.AlAudio):
    _sleep_time = 0

    def _post(self, url, data):
        _path = '%s/data/%s_%s.txt' % (
            current_dir,
            data.get('act', '---'),
            data.get('offset', data.get('ids', '---'))
        )
        if path.isfile(_path):
            try:
                if name == 'nt':
                    with open(_path, 'rb') as f:
                        data = f.read().decode()
                else:
                    with open(_path, 'r') as f:
                        data = f.read()
            except Exception:
                data = ''
        else:
            # _openssl.SSL_do_handshake  Very long
            data = ''  # super(MockAlAudio, self)._post(url, data)
        return data


class TestAudio(unittest.TestCase):
    __uid = 165962770

    def test_decode_item(self):
        aa = MockAlAudio(self.__uid, cookies={})
        items = aa.main()

        self.assertTrue(len(items) > 100)
        self.assertTrue(isinstance(items[-1], dict))

        self.assertFalse(~vaud.decode(self.__uid, items[0]['url']).find('audio_api_unavailable'))
        self.assertFalse(~vaud.decode(self.__uid, items[-1]['url']).find('audio_api_unavailable'))

    def test_decode_item_as_tuple(self):
        aa = MockAlAudio(self.__uid, cookies={})
        items = aa.main(True)

        self.assertTrue(isinstance(items[0], tuple))

        self.assertFalse(~vaud.decode(self.__uid, items[0][0]).find('audio_api_unavailable'))
        self.assertFalse(~vaud.decode(self.__uid, items[-1][0]).find('audio_api_unavailable'))
