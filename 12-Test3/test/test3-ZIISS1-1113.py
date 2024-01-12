'''
1. Place this program in same the folder as your programs.
2. To assess your programs, run this program.
3. Your results will be saved to the results.txt file.
'''

import sys
import unittest

class Test(unittest.TestCase):
    def test_p1(self):
        import p1
        self.assertEqual(p1.f(""),0)
        self.assertEqual(p1.f("+-+"),1)
        self.assertEqual(p1.f("+-+++-+---"),0)
        self.assertEqual(p1.f("+-+++++-"),4)
        self.assertEqual(p1.f("+-+-++"),2)

    def test_p2(self):
        import p2
        self.assertEqual(p2.f([5,6,6,6]),5)
        self.assertEqual(p2.f([8,8,8,8,9]),9)
        self.assertEqual(p2.f([25,25,23]),23)
        self.assertEqual(p2.f([7,7,7,7,7,5,7,7]),5)
        self.assertEqual(p2.f([10,10,9,10,10,10]),9)

    def test_p3(self):
        import p3
        self.assertEqual(p3.f([[1,2,3,4],[5,6,7,8]]),[[5,6,7,8],[1,2,3,4]])
        self.assertEqual(p3.f([[1,1],[2,2],[3,3],[4,4]]),[[4,4],[2,2],[3,3],[1,1]])
        self.assertEqual(p3.f([[1,9],[2,7]]),[[2,7],[1,9]])

    def test_p4(self):
        import p4
        self.assertEqual(p4.f("A4"),True)
        self.assertEqual(p4.f("a4"),True)
        self.assertEqual(p4.f("4a"),False)
        self.assertEqual(p4.f("bC123"),True)
        self.assertEqual(p4.f("bcd555"),False)
        self.assertEqual(p4.f("g80915"),False)
        self.assertEqual(p4.f("A1B2"),False)
        self.assertEqual(p4.f("AB12"),True)

    def test_p5(self):
        import p5
        stadium = p5.C({"A":120,"D":150,"G":90,"K":110,"E":10})
        stadium.m1("G",130)
        self.assertEqual(stadium.m2("GD"),280)
        self.assertEqual(stadium.m2("KEJ"),120)
 
    def test_p6(self):
        import p6
        res = [95,90,20,50,70] 
        fnc1 = lambda x: x>50
        fnc2 = lambda x: x>70 and x<100
        self.assertEqual(p6.f(fnc1,res),25)
        self.assertEqual(p6.f(fnc2,res),5)

    def test_p7(self):
        import p7
        self.assertEqual(p7.f(1027),0)
        self.assertEqual(p7.f(4444),16)
        self.assertEqual(p7.f(22777),25)
        self.assertEqual(p7.f(230335),9)
        self.assertEqual(p7.f(513553007),21)
        self.assertEqual(p7.f(112345),2)


if __name__ == '__main__':
    sys.stderr = open('results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)
