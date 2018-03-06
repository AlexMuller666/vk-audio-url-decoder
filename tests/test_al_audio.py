import unittest
import vaud
from os import path
current_dir = path.dirname(path.realpath(__file__))


class MockAlAudio(vaud.AlAudio):
    def _post(self, url, data):
        _path = '%s/data/%s_%s.txt' % (
            current_dir,
            data.get('act', '---'),
            data.get('offset', data.get('ids', '---'))
        )
        if path.isfile(_path):
            try:
                with open(_path, 'r') as f:
                    data = f.read()
            except Exception:
                data = ''
        else:
            data = super(MockAlAudio, self)._post(url, data)
        return data


class TestAudio(unittest.TestCase):
    __uid = 165962770

    def test_vk(self):
        aa = MockAlAudio(self.__uid, cookies={})
        items = aa.decode()

        self.assertTrue(len(items) > 100)
        self.assertTrue(isinstance(items[-1], tuple))
        self.assertTrue(~items[-1][0].find('audio_api_unavailable'))

    def test_decode_item(self):
        aa = MockAlAudio(self.__uid, cookies={})
        items = aa.decode()
        self.assertFalse(~vaud.decode(self.__uid, items[0][0]).find('audio_api_unavailable'))
        self.assertFalse(~vaud.decode(self.__uid, items[-1][0]).find('audio_api_unavailable'))
