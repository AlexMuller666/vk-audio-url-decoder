import unittest
from vaud.al_audio import AlAudio


class TestAudio(unittest.TestCase):
    cookie = {}

    def test_vk(self):
        aa = AlAudio(165962770, self.cookie)
        print(aa.decode())
        pass
