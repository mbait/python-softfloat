#!/usr/bin/env python

from softfloat import Float


def assertEquals(given, expected):
    if given != expected:
        msg = '\ngot: {}, expected: {}\n'.format(repr(given), repr(expected))
        raise AssertionError(msg)


def assertEqualStr(given, expected):
    if str(given) != expected:
        raise AssertionError('\ngot: {}, expected: {}\n'.format(given, expected))


def testCreateFromString():
    assertEqualStr(Float().from_string('1.5234'), '1.5234')


def testCreateFromBinarySingle():
    assertEqualStr(Float().from_float_bits(1069547520), '1.5')


def testCreateFromBinaryDouble():
    assertEqualStr(Float().from_double_bits(4609434218613702656), '1.5')


def testCreateFromInt():
    assertEqualStr(Float().from_int(10), '10')


def testConvertToDouble():
    assertEquals(Float().from_string('1.5').to_double_bits(), 4609434218613702656)


def testConvertToStringWithRounding():
    assertEquals(Float().from_string('1.5678').to_s(2), '1.57')


def testAddFloat():
    a = Float()
    a.from_string('1.5')
    b = Float()
    b.from_string('-0.6')
    a.fadd(b)
    assertEquals(a, Float().from_string('0.9'))


def testAddInteger():
    a = Float().from_string('1.5')
    a.add(5)
    assertEqualStr(a, '5.5')


def testSubtractFloat():
    a = Float().from_string('1.5')
    b = Float().from_string('-0.6')
    a.fsub(b)
    assertEqualStr(a, '2.1')


def testSubtractInteger():
    a = Float().from_string('1.5')
    a.sub(2)
    assertEqualStr(a, '-0.5')


def testMultiplyFloat():
    a = Float().from_string('1.5')
    b = Float().from_string('-0.6')
    a.fmul(b)

def testMultiplyInteger():
    a = Float().from_string('1.5')
    b = Float().from_string('-0.6')
    a.mul(3)


def testDivideFloat():
    a = Float().from_string('1.5')
    b = Float().from_string('-0.6')
    a.fdiv(b)


def testDivideInteger():
    a = Float().from_string('1.5')
    b = Float().from_string('-0.6')
    a.div(2)


def testPowerFloat():
    a = Float().from_string('1.5')
    b = Float().from_string('-0.6')
    a.fpow(b)


def testPowerInteger():
    a = Float().from_string('1.5')
    b = Float().from_string('-0.6')
    a.pow(10)


if __name__ == '__main__':
    tests = filter(lambda name: name.startswith('test'), dir())
    name_width = max(map(len, tests))
    width = 0

    counts = [0, 0, 0]

    for t in tests:
        result = 'OK'

        try:
            apply(locals()[t])
            counts[0] += 1
        except Exception as e:
            if isinstance(e, AssertionError):
                result = 'FAIL\n{}'.format(e)
                counts[1] += 1

            else:
                result = 'ERR # {}'.format(e)
                counts[2] += 1

        msg = '%-*s  %s' % (name_width, t, result)
        width = max(width, len(msg))
        print msg

    #apply(print_stat, 
    #stat = zip(['SUCCESSFUL', 'FAILED', 'ERRORS'], counts)
    #print ''.ljust(width, '-')
    #print ', '.join(map(lambda x: x[0] + ': ' + str(x[1]), stat))

# vim: set sw=4 :
# vim: set ts=4 : 
# vim: set expandtab :
