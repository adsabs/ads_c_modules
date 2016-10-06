import unittest
import doctest

class DeviceTest(unittest.TestCase):
    # This is a simple test that just tries to load the module
    def runTest(self):
        try:
            import ldw
        except ImportError, e:
            self.Fail(str(e))

class MethodTest( unittest.TestCase ):
    # Test that the module actually works
    def runTest(self):
        import ldw
        self.assertEqual(ldw.ldw('abcd','cadb'), 4)
