from .al_audio import AlAudio
from .decoder import Decoder

__version__ = '0.2.3'


def decode(uid, url):
    return Decoder(uid).decode(url)
