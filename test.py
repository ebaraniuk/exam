import unittest
from progression import Progression


class TestProgression(unittest.TestCase):
    test = Progression(20)
    test2 = Progression(90)
    test3 = Progression(3)
    test4 = Progression(25)
    test_error = Progression(-1)



    def test_summa(self):
        self.assertRaises(ValueError,self.test_error.summa)
        self.assertEqual(self.test.summa(), 610)
        self.assertTrue(self.test.summa(), isinstance(self.test.summa(), int))
        self.assertEqual(self.test2.summa(), 12195)
        self.assertEqual(self.test3.summa(), 15)
        self.assertEqual(self.test4.summa(), 950)






if __name__ == '__main__':
    unittest.main()
