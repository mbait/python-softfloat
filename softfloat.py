class Float:
    """Byte order for x86 is little. Assume it during development.

    TODO: find out the byte order of the target platform

    """
    BITS_LEN = 64

    def __init__(self):
        self._s = 0
        self._a = 0
        self._q = 0

    def __eq__(self, obj):
        return self._s == obj._s and self._a == obj._a and self._q == obj._q

    def __ne__(self, obj):
        return not self.__eq__(obj)

    def __str__(self):
        return ''

    def __repr__(self):
        return str(long((-1 ** self._s) << 63 | (self._a) << 11 | self._q))

    def _count_zeros(self, sig):
        p = 1

        while p <= self.BITS_LEN:
            if sig & 1 << (self.BITS_LEN - p):
                break
            else:
                p += 1

        return p - 1


    def _normalize(self, sig):
        shift = self._count_zeros(sig) - 11
        return sig << shift, 1 - shift

    def to_s(self, p):
        return str(self)

    def from_string(self, s):
        i = 0
        j = -1
        n = len(s)
        sig = ''

        if s[0] == '+' or s[0] == '-':
            i = 1

        while i < n:
            if s[i] == '.':
                if j == -1:
                    j = i + 1
                else:
                    raise ValueError('Invalid froating-point string')
            else:
                sig += s[i]

            i += 1

        if s[0] == '-':
            self._s = 1
        else:
            self._s = 0

        self._q, self._a = self._normalize(long(sig))
        
        return self

    def from_int(self, num):
        return self

    def from_float_bits(self, bits):
        return self

    def from_double_bits(self, bits):
        self._s = bits >> 31
        self._a = bits << 1 >> 12
        self._q = bits << 53 >> 53;

        return self

    def to_double_bits(self):
        return long(self._s << 31 | self._a << 11 | self._q)

    def addf(self, obj):
        return self

    def addi(self, obj):
        return self

    def subi(self, num):
        return self

    def subf(self, obj):
        return self

    def muli(self, num):
        return self

    def mulf(self, obj):
        return self

    def divi(self, num):
        return self

    def divf(self, obj):
        return self

    def powi(self, num):
        return self

    def powf(self, num):
        return self

# vim: set sw=4 :
# vim: set ts=4 :
# vim: set expandtab :
