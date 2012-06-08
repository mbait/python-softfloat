#!/usr/bin/env python

from softfloat import Float


def assertEquals(given, expected):
    if given != expected:
        msg = "got: '%s', expected: '%s'" % (repr(given), repr(expected))
        raise AssertionError(msg)


def assertEqualStr(given, expected):
    if str(given) != expected:
        raise AssertionError("got: '%s', expected: '%s'" % (given, expected))


def testCreateFromString():
    assertEqualStr(Float().from_string('42'), '42')
    assertEqualStr(Float().from_string('1.5234'), '1.5234')


def testCreateFromBinarySingle():
    assertEqualStr(Float().from_float_bits(1069547520), '1.5')


def testCreateFromBinaryDouble():
    assertEqualStr(Float().from_double_bits(4609434218613702656L), '1.5')


def testCreateFromInt():
    assertEqualStr(Float().from_int(10), '10')


def testConvertToDouble():
    a = Float().from_string('1.5')
    assertEquals(a.to_double_bits(), 4609434218613702656L)


def testConvertToStringWithRounding():
    assertEquals(Float().from_string('1.5678').to_s(2), '1.57')


def testAddFloat():
    a = Float()
    a.from_string('1.5')
    b = Float()
    b.from_string('-0.6')
    a.addf(b)
    assertEquals(a, Float().from_string('0.9'))


def testAddInteger():
    a = Float().from_string('1.5')
    a.addi(5)
    assertEquals(a, Float().from_string('5.5'))


def testSubtractFloat():
    a = Float().from_string('1.5')
    b = Float().from_string('-0.6')
    a.subf(b)
    assertEqualStr(a, '2.1')


def testSubtractInteger():
    a = Float().from_string('1.5')
    a.subi(2)
    assertEqualStr(a, '-0.5')


def testMultiplyFloat():
    a = Float().from_string('1.5')
    b = Float().from_string('-0.6')
    assertEquals(a.mulf(b), Float().from_string('-6.30'))

def testMultiplyInteger():
    a = Float().from_string('1.5')
    assertEquals(a.muli(3), Float().from_string('4.5'))


def testDivideFloat():
    a = Float().from_string('1.5')
    b = Float().from_string('-0.6')
    assertEquals(a.divf(b), Float().from_string('-2.5'))


def testDivideInteger():
    a = Float().from_string('1.5')
    b = Float().from_string('6')
    assertEquals(a.divi(b), Float().from_string('0.25'))


def testPowerFloat():
    a = Float().from_string('1.21')
    b = Float().from_string('-0.5')
    assertEquals(a.powf(b), Float().from_string('0.909090909090909'))


def testPowerInteger():
    a = Float().from_string('1.5')
    assertEquals(a.powi(2), Float().from_string('-2.25'))


if __name__ == '__main__':
    tests = filter(lambda name: name.startswith('test'), dir())
    test_width = max(map(len, tests))
    width = 0

    counts = [0, 0, 0]

    for t in tests:
        result = 'OK'

        try:
            apply(locals()[t])
            counts[0] += 1
        except Exception as e:
            if isinstance(e, AssertionError):
                result = 'FAIL # %s' % e
                counts[1] += 1

            else:
                result = 'ERR  # %s' % e
                counts[2] += 1

        msg = '%s%s' % (t[4:].ljust(test_width + 4, '.'), result)
        width = max(width, len(msg))
        print msg

    print ''.ljust(width, '-')
    print 'SUCCESSFUL: %d, FAILED: %d, ERRORS: %d' % tuple(counts)

# vim: set sw=4 :
# vim: set ts=4 : 
# vim: set expandtab :
