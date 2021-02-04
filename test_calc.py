import unittest
import calc

class testAddition(unittest.TestCase):
    def test1(self):
        self.assertEqual(calc.addition(5,5),10)
    def test2(self):
        self.assertEqual(calc.addition(-1,2),1)
    def test3(self):
        self.assertEqual(calc.addition(-2,-2),-4)
    def test4(self):
        self.assertEqual(calc.addition(1.1,1.4),2.5)

class testSubtraction(unittest.TestCase):
    def test1(self):
        self.assertEqual(calc.subtraction(5,1),4)
    def test2(self):
        self.assertEqual(calc.subtraction(3,-1),4)
    def test3(self):
        self.assertEqual(calc.subtraction(-2,-3),1)
    def test4(self):
        self.assertEqual(calc.subtraction(3,1.5),1.5)

class testMultiplication(unittest.TestCase):
    def test1(self):
        self.assertEqual(calc.multiplication(5,5),25)
    def test2(self):
        self.assertEqual(calc.multiplication(5,-1),-5)
    def test3(self):
        self.assertEqual(calc.multiplication(-2,-2),4)
    def test4(self):
        self.assertEqual(calc.multiplication(5,0.5),2.5)

class testDivision(unittest.TestCase):
    def test1(self):
        self.assertEqual(calc.division(10,2),5)
    def test2(self):
        self.assertEqual(calc.division(10,-1),-10)
    def test3(self):
        self.assertEqual(calc.division(-5,-5),1)
    def test4(self):
        self.assertEqual(calc.division(5,-2.5),-2)
    def test5(self):
        with self.assertRaises(ZeroDivisionError):
            calc.division(2,0)

if __name__ == '__main__':
    unittest.main(verbosity=2)