class Float:
    BITS_LEN = 64

    def __init__(self):
        self._s = 0L
        self._a = 0L
        self._q = 0L

    def __eq__(self, obj):
        return self._s == obj._s and self._a == obj._a and self._q == obj._q

    def __ne__(self, obj):
        return self._s != obj._s or self._a != obj._a or self._q != obj._q

    def __str__(self):
        return ''

    def __repr__(self):
        int64 = (self._s << 63) | (self._e << 52) | self._a
        return str(int64 & 0xffffffffffffffffL)

    def _count_zeros(self, sig):
        p = 1

        while p <= self.BITS_LEN:
            if sig & 1 << (self.BITS_LEN - p):
                break
            else:
                p = p + 1

        return p - 1


    def _normalize(self, sig):
        shift = self._count_zeros(sig) - 11
        return 1 - shift, sig << shift

    def to_s(self, p):
        return str(self)

    def from_string(self, s):
        n = len(s)
        i = 0

        while i < n and s[i] != '.':
            i = i + 1

        sig = long(s[:i] + s[i + 1:])
        sign = 0

        if sig < 0:
            sign = 1
            sig = -sig

        e = 0

        return self

    def from_int(self, num):
        return self

    def from_float_bits(self, bits):
        self._s = bits >> 31
        self._q = bits >> 23 & 0xff
        self._a = bits & 0x007FFFFFL

        return self

    def from_double_bits(self, bits):
        self._s = bits >> 63
        self._q = bits >> 52 & 0x7ff
        self._a = bits & 0x000FFFFFFFFFFFFFL

        return self

    def to_double_bits(self):
        return long(self._s << 31 | self._a << 11 | self._q)

    def addf(self, obj):
        """
        flag aSign, bSign;

        aSign = extractFloat64Sign( a );
        bSign = extractFloat64Sign( b );
        if ( aSign == bSign ) {
            return addFloat64Sigs( a, b, aSign );
        }
        else {
            return subFloat64Sigs( a, b, aSign );
        }
        """

        return self

    def addi(self, obj):
        return self

    def subi(self, num):
        return self

    def subf(self, obj):
        """
        flag aSign, bSign;

        aSign = extractFloat64Sign( a );
        bSign = extractFloat64Sign( b );
        if ( aSign == bSign ) {
            return subFloat64Sigs( a, b, aSign );
        }
        else {
            return addFloat64Sigs( a, b, aSign );
        }
        """

        return self

    def muli(self, num):
        return self

    def mulf(self, other):
        """
        flag aSign, bSign, zSign;
        int16 aExp, bExp, zExp;
        bits64 aSig, bSig, zSig0, zSig1;

        aSig = extractFloat64Frac( a );
        aExp = extractFloat64Exp( a );
        aSign = extractFloat64Sign( a );
        bSig = extractFloat64Frac( b );
        bExp = extractFloat64Exp( b );
        bSign = extractFloat64Sign( b );
        zSign = aSign ^ bSign;

        if ( aExp == 0x7FF ) {
            if ( aSig || ( ( bExp == 0x7FF ) && bSig ) ) {
                return propagateFloat64NaN( a, b );
            }
            if ( ( bExp | bSig ) == 0 ) {
                float_raise( float_flag_invalid );
                return float64_default_nan;
            }
            return packFloat64( zSign, 0x7FF, 0 );
        }
        if ( bExp == 0x7FF ) {
            if ( bSig ) return propagateFloat64NaN( a, b );
            if ( ( aExp | aSig ) == 0 ) {
                float_raise( float_flag_invalid );
                return float64_default_nan;
            }
            return packFloat64( zSign, 0x7FF, 0 );
        }
        if ( aExp == 0 ) {
            if ( aSig == 0 ) return packFloat64( zSign, 0, 0 );
            normalizeFloat64Subnormal( aSig, &aExp, &aSig );
        }
        if ( bExp == 0 ) {
            if ( bSig == 0 ) return packFloat64( zSign, 0, 0 );
            normalizeFloat64Subnormal( bSig, &bExp, &bSig );
        }
        zExp = aExp + bExp - 0x3FF;
        aSig = ( aSig | LIT64( 0x0010000000000000 ) )<<10;
        bSig = ( bSig | LIT64( 0x0010000000000000 ) )<<11;
        mul64To128( aSig, bSig, &zSig0, &zSig1 );
        zSig0 |= ( zSig1 != 0 );
        if ( 0 <= (sbits64) ( zSig0<<1 ) ) {
            zSig0 <<= 1;
            --zExp;
        }

        return roundAndPackFloat64( zSign, zExp, zSig0 );
        """

        if self._q == 0x7ff:
            pass

        if other._q == 0x7ff:
            pass

        if self._q == 0:
            pass

        if other._q == 0:
            pass

        q = self._q + other._q - 0x3ff
        a1 = (self._a | 0x0010000000000000L) << 10
        a2 = (other._a | 0x0010000000000000L) << 10
        a = a1 * a2

        if 0 <= a:
            s = s << 1
            q = q - 1

        self._round_and_pack(s, q, a)

        return self

    def divi(self, num):
        return self

    def divf(self, obj):
        """
        flag aSign, bSign, zSign;
        int16 aExp, bExp, zExp;
        bits64 aSig, bSig, zSig;
        bits64 rem0, rem1;
        bits64 term0, term1;

        aSig = extractFloat64Frac( a );
        aExp = extractFloat64Exp( a );
        aSign = extractFloat64Sign( a );
        bSig = extractFloat64Frac( b );
        bExp = extractFloat64Exp( b );
        bSign = extractFloat64Sign( b );
        zSign = aSign ^ bSign;
        if ( aExp == 0x7FF ) {
            if ( aSig ) return propagateFloat64NaN( a, b );
            if ( bExp == 0x7FF ) {
                if ( bSig ) return propagateFloat64NaN( a, b );
                float_raise( float_flag_invalid );
                return float64_default_nan;
            }
            return packFloat64( zSign, 0x7FF, 0 );
        }
        if ( bExp == 0x7FF ) {
            if ( bSig ) return propagateFloat64NaN( a, b );
            return packFloat64( zSign, 0, 0 );
        }
        if ( bExp == 0 ) {
            if ( bSig == 0 ) {
                if ( ( aExp | aSig ) == 0 ) {
                    float_raise( float_flag_invalid );
                    return float64_default_nan;
                }
                float_raise( float_flag_divbyzero );
                return packFloat64( zSign, 0x7FF, 0 );
            }
            normalizeFloat64Subnormal( bSig, &bExp, &bSig );
        }
        if ( aExp == 0 ) {
            if ( aSig == 0 ) return packFloat64( zSign, 0, 0 );
            normalizeFloat64Subnormal( aSig, &aExp, &aSig );
        }
        zExp = aExp - bExp + 0x3FD;
        aSig = ( aSig | LIT64( 0x0010000000000000 ) )<<10;
        bSig = ( bSig | LIT64( 0x0010000000000000 ) )<<11;
        if ( bSig <= ( aSig + aSig ) ) {
            aSig >>= 1;
            ++zExp;
        }
        zSig = estimateDiv128To64( aSig, 0, bSig );
        if ( ( zSig & 0x1FF ) <= 2 ) {
            mul64To128( bSig, zSig, &term0, &term1 );
            sub128( aSig, 0, term0, term1, &rem0, &rem1 );
            while ( (sbits64) rem0 < 0 ) {
                --zSig;
                add128( rem0, rem1, 0, bSig, &rem0, &rem1 );
            }
            zSig |= ( rem1 != 0 );
        }
        return roundAndPackFloat64( zSign, zExp, zSig );
        """

        return self

    def powi(self, num):
        return self

    def powf(self, num):
        return self

# vim: set sw=4 :
# vim: set ts=4 :
# vim: set expandtab :
