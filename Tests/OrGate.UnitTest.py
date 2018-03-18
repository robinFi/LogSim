import unittest 
from OrGate import OrGate
class OrGateUnitTest(unittest.TestCase):
    def testcase_01(self): 
        a = OrGate(False, False)
        a.execute() 
        self.assertEqual(False, a._output, "Test 01 fehlgeschlagen.") 

    def testcase_02(self): 
        a = OrGate(True, False) 
        a.execute() 
        self.assertEqual(True, a._output, "Test 02 fehlgeschlagen.") 

    def testcase_03(self): 
        a = OrGate(False, True)
        a.execute() 
        self.assertEqual(True, a._output, "Test 03 fehlgeschlagen.") 

    def testcase_04(self): 
        a = OrGate(True, True)
        a.execute() 
        self.assertEqual(True, a._output, "Test 04 fehlgeschlagen.") 

if __name__ == "__main__": 
    unittest.main()