import unittest
from vaud import Decoder, decode


class TestUrls(unittest.TestCase):
    __uid = 165962770
    __urls = [
        'https://m.vk.com/mp3/audio_api_unavailable.mp3?extra=C1LOz3q4mxHUrZHjte5xn3zzmO1hzMGXyxzeqZjPCZjdt3uXlwn6nhn5lvLJm3m9yJHMAhrYDLffvLnkof9boc9Tyu5LAej4yMrQtf9kwv8Vv29ozenVyuCOAOXPnI1Owc54lM9kl2iYl3runZuYvNzIqY12q3PJDgfbwgP6A2vFng9JoNfWtNjHwLHKzwuWn3vbyvHtEKu/z3fvDhbmsfvPAc5NmxvLngLeq2vSwNjlowfYtJbMyMjiyvDnr3jUDvLWwNLvwMDVsxvNnG#AqSZnZe',
        'https://m.vk.com/mp3/audio_api_unavailable.mp3?extra=AhC2mKffANvTl3vvswS3vdDjsZ1ftY9tCvPymNP0thPNC1HOmMTUy3PJugWYywe3p3rWugv4n3bjDOXRCO5ZmOrUngLOr2DfAffMlxHXz3jRzhGYlMWXsNziyKTfAvmUne9NC2Xdy3D5oMTmntzHzM1RyNnNDei1CennqMfKyuH6zg9WmOuYywLLouzZAgjVmJz5v2LMnvn3n2iVzwHyzxqWCJbxuhnbn1LSv3zbBNnhDNaVwwnsmwLRlMvLt3bTDerSvtjqqZHeluzVCa#AqS3nJG',
        'https://m.vk.com/mp3/audio_api_unavailable.mp3?extra=CeHXAgfYufnZDhy3twvZEvfIuZy4Cu03CeDYC1bUovbRrdPNstH1D2SVwhuWzLzyChy5AI94AKSYnZeZy2HRwK4ZDgjTvha3mZflB1yTmuXIlMHmvMqTCZyVtJzRrtfqq3nIDgSZyLHOmevNsgPxlLjywwHtl25boveYouX1uMK/A29wm3rYuJeYowLHngnQrgLKs3nKD2vdzu9hsJLsvNzHlY42t3i4swXineP6mZzbmJjfrhu4zuDvutrVDuv1CfHFtZOVB3vWmtnwyOK3DuCWD2fLnLrJng5cnuK#AqS3odC',
    ]

    def test_urls(self):
        decoder = Decoder(self.__uid)

        for url in self.__urls:
            decoded_url = decoder.decode(url)
            self.assertFalse(~decoded_url.find('audio_api_unavailable'))

    def test_url(self):
        decoded_url = decode(self.__uid, self.__urls[0])
        self.assertFalse(~decoded_url.find('audio_api_unavailable'))

    def test_fail_url1(self):
        decoded_url = decode(self.__uid, self.__urls[0] + 'abc')
        self.assertTrue(~decoded_url.find('audio_api_unavailable'))

    def test_fail_url2(self):
        decoded_url = decode(self.__uid, self.__urls[0][:-5])
        self.assertTrue(~decoded_url.find('audio_api_unavailable'))

    def test_assert1(self):
        try:
            decode()
            result = False
        except TypeError:
            result = True
        self.assertTrue(result)

    def test_assert2(self):
        try:
            decode('asd')
            result = False
        except TypeError:
            result = True
        self.assertTrue(result)

    def test_assert3(self):
        try:
            decode('asd', 'abc')
            result = False
        except TypeError:  # python 3.*
            result = True
        except ValueError:  # python 2.7
            result = True
        self.assertTrue(result)

    def test_assert4(self):
        try:
            decoder = Decoder()
            result = False
        except TypeError:
            result = True
        self.assertTrue(result)

    def test_assert5(self):

        try:
            decoder = Decoder(0)
            result = False
        except AttributeError:
            result = True
        self.assertTrue(result)

    def test_r(self):
        decoder = Decoder(1)
        self.assertTrue('Y++69:PP6R9+VSZ4.T53P' == decoder.r('https://pastebin.com/', 22))

    def test_v(self):
        decoder = Decoder(1)
        self.assertTrue('abc' == decoder.v('cba'))

    def test_x(self):
        decoder = Decoder(1)
        p = decoder.x('https://pastebin.com/', '22')
        e = u'ZFFBA\u0008\u001d\u001dBSAFWP[\\\u001cQ]_\u001d'  # py2 crunch
        self.assertTrue(e == p)


# if __name__ == '__main__':
#     unittest.main()
