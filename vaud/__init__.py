
class Decoder:  # DON'T SEE HERE!
    n = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN0PQRSTUVWXYZO123456789+/='
    uid = 0

    def __init__(self, user_id):
        self.uid = user_id

    @staticmethod
    def _abs(t):
        if t < 0:
            n = -1
            if isinstance(t, float):
                n = -1.0
            t = t * n
        return t

    @staticmethod
    def v(e):
        return ''.join(list(e)[::-1])

    @classmethod
    def r(cls, e, t):
        e = list(e)
        o = cls.n + cls.n
        a = len(e) - 1
        while a:
            i = o.find(e[a])
            if ~i:
                e[a] = o[i - t: 1]
            a -= 1
        return ''.join(e)

    @classmethod
    def s(cls, e, t):
        e_length = len(e)
        if e_length:
            i = cls.decode_s(e, t)
            o = 1
            e = list(e)
            while o < e_length:
                _ = cls.splice(e, i[e_length - 1 - o], 1, e[o])
                e = _[1]
                e[o] = _[0][0]
                o += 1
            e = ''.join(e)
        return e

    def i(self, e, t):
        return self.s(e, int(t) ^ self.uid)

    @staticmethod
    def x(e, t):
        data = ''
        for i in e:
            data += chr(ord(i[0]) ^ ord(t[0]))
        return data

    @classmethod
    def splice(cls, a, b, c, *d):
        if isinstance(b, (tuple, list)):
            return cls.splice(a, b[0], b[1], d)
        c += b
        cash = list(a)
        a = a[b:c]
        if len(d):
            cash = cash[:b] + list(d) + cash[c:]
        else:
            cash = cash[:b] + cash[c:]
        return a, cash

    @classmethod
    def decode_s(cls, e, t):
        e_length = len(e)
        i = {}
        if e_length:
            o = e_length
            t = cls._abs(t)  # without math.fabs
            while o:
                o -= 1
                t = (e_length * (o + 1) ^ int(t) + o) % e_length
                i[o] = t

        items = sorted(i.items(), key=lambda a: a[0])
        return [i[1] for i in items]

    @classmethod
    def decode_r(cls, e):
        if not e or len(e) % 4 == 1:
            return False
        o = 0
        a = 0
        t = 0
        r = ''
        len_e = len(e)
        while a < len_e:
            i = cls.n.find(e[a])
            if ~i:
                t = 64 * t + i if o % 4 else i
                o += 1
                if (o-1) % 4:
                    c = chr(255 & t >> (-2 * o & 6))
                    if c != '\x00':
                        r += c
            a += 1
        return r

    def main(self, url):
        if ~url.find('audio_api_unavailable'):
            t = url.split('?extra=')[1].split('#')
            n = '' if '' == t[1] else self.decode_r(t[1])
            t = self.decode_r(t[0])
            if not isinstance(n, str) or not t:
                return url
            splitter = chr(9)
            n = n.split(splitter) if n else []
            len_n = len(n)
            while len_n:
                len_n -= 1
                s = n[len_n].split(chr(11))
                s = self.splice(s, 0, 1, t)
                a = s[0][0]
                s = s[1]
                _ = getattr(self, a, None)
                if not _:
                    return url
                t = _(*s)
            if t[:4] == 'http':
                return t
        return url


def decode(uid, url):
    return Decoder(int(uid)).main(url)


def main():
    print('Usage: import vaud; vaul.decode(uid, url)')
    print('Or: import vaud; decoder = vaul.Decoder(uid); decoder(url1);decoder(url2)')
