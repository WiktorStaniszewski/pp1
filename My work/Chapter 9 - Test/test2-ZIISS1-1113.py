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
        self.assertEqual(p1.f("2+3"),5)
        self.assertEqual(p1.f("0-0+1-9+0"),-8)

    def test_p2(self):
        import p2
        self.assertEqual(p2.f("+-+++-+---"),0)
        self.assertEqual(p2.f("+++++---"),2)
        self.assertEqual(p2.f("+-+-+-+++++++"),7)

    def test_p3(self):
        import p3
        self.assertEqual(str(p3.f("AT43")),"27")
        self.assertEqual(str(p3.f("2QKJ9")),"41")

    def test_p4(self):
        import p4
        self.assertEqual(p4.f([2,3,4,2,3,4,5,6,7]),3)
        self.assertEqual(p4.f([8,8,7,7,6,5,5,4,4,3,2,2,1,1]),2)

    def test_p5(self):
        import p5
        self.assertEqual(p5.f([[1,1],[5,25],[-4,16]]),3)
        self.assertEqual(p5.f([[1,1],[5,-25],[-4,-16]]),1)
        self.assertEqual(p5.f([[1,1],[5,24],[-4,15],[-6,36]]),2)
 
    def test_p6(self):
        import p6
        self.assertEqual(p6.f("32 hello test5 3ok"),40)
        self.assertEqual(p6.f("a1000 b20c30 d40e"),1090)

    def test_p7(self):
        import p7
        self.assertEqual(p7.f({"D":False,"a":True,"xx":False},True),2)
        self.assertEqual(p7.f({"D":False,"a":False,"xx":False},True),3)
        self.assertEqual(p7.f({"D":False,"a":False,"xx":False},False),0)


if __name__ == '__main__':
    sys.stderr = open('results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)
