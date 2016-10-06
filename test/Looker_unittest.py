import os
import unittest
import doctest

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'stubdata/test_data.dat')

class DeviceTest(unittest.TestCase):
    # This is a simple test that just tries to load the module
    def runTest(self):
        try:
            import Looker
        except ImportError, e:
            self.Fail(str(e))

class MethodTest(unittest.TestCase):
    # Test that the module actually works
    def runTest(self):
        import Looker
        looker = Looker.Looker(TESTDATA_FILENAME).look
        self.assertEqual(len(looker("US").strip().split('\n')),29)
