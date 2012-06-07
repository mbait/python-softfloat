class Float:
    """Byte order for x86 is little. Assume it during development.

    TODO: find out the byte order of the target platform

    """
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
        return str(long((-1 ** self._s) << 63 & (self._a) << 11 & self._q))

    def to_s(self, p):
        return str(self._rep)

    def from_string(self, s):
        self.from_float_bits(hex(float(s).hex()))
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
        return long(self._s << 31 & self._a << 11 & self._q)

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
