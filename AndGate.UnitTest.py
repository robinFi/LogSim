import unittest 
from AndGate import AndGate
class AndGateUnitTest(unittest.TestCase):
    def testcase_01(self): 
        a = AndGate(False, False)
        a.execute() 
        self.assertEqual(False, a._output, "Test 01 fehlgeschlagen.") 

    def testcase_01(self): 
        a = AndGate(True, False) 
        a.execute() 
        self.assertEqual(False, a._output, "Test 02 fehlgeschlagen.") 

    def testcase_01(self): 
        a = AndGate(False, True)
        a.execute() 
        self.assertEqual(False, a._output, "Test 03 fehlgeschlagen.") 

    def testcase_01(self): 
        a = AndGate(True, True)
        a.execute() 
        self.assertEqual(True, a._output, "Test 04 fehlgeschlagen.") 

if __name__ == "__main__": 
    unittest.main()