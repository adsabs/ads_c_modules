import os
import unittest
import doctest

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'stubdata/test_map.dat')

class DeviceTest(unittest.TestCase):
    # This is a simple test that just tries to load the module
    def runTest(self):
        try:
            import ctrigram
        except ImportError, e:
            self.Fail(str(e))

class MethodTest(unittest.TestCase):
    # Test that the module actually works
    def runTest(self):
        from utils import Trigdict
        # Attempt to instantiate the dictionary
        try:
            d = Trigdict()
        except Exception, e:
            self.Fail(str(e))
        # Build the dictionary with stubdata
        with open(TESTDATA_FILENAME) as fh:
            for line in fh:
                abbrev, name = line.strip().split('\t')
                d[name] = abbrev
        # Is it working?
        # Testing for matching
        self.assertEqual(d['Z. Astrophys.'],[(1.0, 'ZA.......')])         
        # Testing for best matches
        expected = [(0.5833333730697632, 'A&A......'), 
                    (0.6666666269302368, 'A&ARv....'), 
                    (0.7222222089767456, 'A&ARv....'), 
                    (0.8333333134651184, 'A&ARv....')]
        self.assertEqual(d.bestmatches("A&A Rv",4), expected)
