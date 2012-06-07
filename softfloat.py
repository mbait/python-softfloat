class Float(object):
    SINGLE_SIGN_SIZE = 23
    SINGLE_EXP_SIZE = 8
    SINGLE_USIGN_SIZE = SINGLE_SIGN_SIZE + SINGLE_EXP_SIZE

    DOUBLE_SIGN_SIZE = 52
    DOUBLE_EXP_SIZE = 11
    DOUBLE_UNSIGN_SIZE = DOUBLE_SIGN_SIZE + DOUBLE_EXP_SIZE

    def __init__(self):
        self._rep = 0L

    def __eq__(self, obj):
        return self._rep == obj._rep

    def __ne__(self, obj):
        return not self.__eq__(obj)

    def __str__(self):
        return str('%g' % self._rep)

    def __repr__(self):
        return str(self._rep)

    def to_s(self, p):
        return str(self._rep)

    def from_string(self, s):
        self._rep = float(s)
        return self

    def from_int(self, num):
        return self

    def from_float_bits(self, bits):
        self._rep = long(
                (bits >> self.SINGLE_USIGN_SIZE) << self.DOUBLE_UNSIGN_SIZE +
                 (bits >> self.SINGLE_EXP_SIZE ) << self.DOUBLE_EXP_SIZE)

        return self

    def from_double_bits(self, bits):
        self._rep = bits
        return self

    def to_double_bits(self):
        return self._rep

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

# vim : set ts=4 :
# vim : set sw=4 :
# vim : set expandtab :
