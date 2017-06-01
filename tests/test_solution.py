from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        import pandas as pd
        from random import  randint
        num1 = randint(0,100)
        ds = pd.Series([num1])
        res = solution(ds)

        self.assertTrue(isinstance(res, list))
        self.assertEqual(num1, res[0])