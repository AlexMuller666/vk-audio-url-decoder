import unittest
import vaud
from os import path
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
            with open(_path, 'rb') as f:
                data = f.read()
                try:
                    data = data.decode()
                except Exception:
                    pass
        else:
            # data = super(MockAlAudio, self)._post(url, data)
            # with open(_path, 'wb') as f:
            #     f.write(data.encode())
            data = ''
        return data


class TestAudio(unittest.TestCase):
    __uid = 253093876
    __cookies = {
        'remixstid': '',
        'remixflash': '0.0.0',
        'remixscreen_depth': '24',
        'remixdt': '0',
        'remixlang': '3',
        'remixsid': '',
        'remixseenads': '1',
        'tmr_detect': ''
    }

    def test_decode_item(self):
        aa = MockAlAudio(self.__uid, self.__cookies)
        items = aa.main()

        self.assertTrue(len(items) + len(aa._list_unparsed_tracks) == len(aa._playlist))
        self.assertTrue(isinstance(items[-1], dict))

        self.assertFalse(~vaud.decode(self.__uid, items[0]['url']).find('audio_api_unavailable'))
        self.assertFalse(~vaud.decode(self.__uid, items[-1]['url']).find('audio_api_unavailable'))

    def test_decode_item_as_tuple(self):
        aa = MockAlAudio(self.__uid, self.__cookies)
        items = aa.main(True)

        self.assertTrue(isinstance(items[0], tuple))

        self.assertFalse(~vaud.decode(self.__uid, items[0][0]).find('audio_api_unavailable'))
        self.assertFalse(~vaud.decode(self.__uid, items[-1][0]).find('audio_api_unavailable'))

    def test_decode_limit(self):
        aa = MockAlAudio(self.__uid, cookies=self.__cookies)
        aa.offset = 6
        aa.limit = 20
        items = aa.main()

        aa = MockAlAudio(self.__uid, cookies=self.__cookies)
        aa.offset = 0
        aa.limit = 30
        without_offset_items = aa.main()

        self.assertTrue(len(items) == 20)
        self.assertTrue(items[0]['id'] == without_offset_items[6]['id'])
