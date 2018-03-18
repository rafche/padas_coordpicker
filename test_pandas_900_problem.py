from pandas_900_problem import getvalues
import pandas as pd
import pytest

class TestClass(object):

    @pytest.mark.coordmerge
    def test_getvalues(self):
        sums = {'T1': pd.Series([0, 6, 12, 18, 24, 30],
                 index=['1', '2', '3', '4', '5', '6']),
                'T2': pd.Series([1, 7, 13, 19, 25, 31],
                 index=['1', '2', '3', '4', '5', '6']),
                'T3': pd.Series([2, 8, 14, 20, 26, 32],
                 index=['1', '2', '3', '4', '5', '6']),
                'T4': pd.Series([3, 9, 15, 21, 27, 33],
                 index=['1', '2', '3', '4', '5', '6']),
                'T5': pd.Series([4, 10, 16, 22, 28, 34],
                 index=['1', '2', '3', '4', '5', '6']),
                'T6': pd.Series([5, 11, 17, 23, 29, 35],
                 index=['1', '2', '3', '4', '5', '6'])
                }
        df = pd.DataFrame(sums)
        for i in range(0,36):
            assert getvalues(i,df) == i