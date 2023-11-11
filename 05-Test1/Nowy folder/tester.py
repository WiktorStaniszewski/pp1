'''
1. Place this program in the same folder as your programs.
2. To assess your programs, run this program.
3. Your results will be saved to the results.txt file.
'''

import sys
import unittest

class Test(unittest.TestCase):
    def test_p1(self):
        import p1
        self.assertEqual(p1.f("590111222333"),False)
        self.assertEqual(p1.f("5901112223334"),True)
        self.assertEqual(p1.f("5801112223334"),False)

    def test_p2(self):
        import p2
        self.assertEqual(p2.f(17),987)

    def test_p3(self):
        import p3
        self.assertEqual(p3.f(88077066),42)

    def test_p4(self):
        import p4
        self.assertEqual(p4.f(99887766),"9+9+8++8++7+7+6++6")

    def test_p5(self):
        import p5
        self.assertEqual(p5.f(20,15),"20,19,18,17,16,15")

    def test_p6(self):
        import p6
        self.assertEqual(p6.f(1234,987654),True)
        self.assertEqual(p6.f(1234,98765),False)


if __name__ == '__main__':
    sys.stderr = open('results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)