import pandas as pd

def getvalues(coord, df):
    '''
    :param coord: coordinate from table
    :param df: data frame which holds the data
    :return: the Value of the coord
    example: the value of the coord 8 = 7
    +----+----+----+----+----+----+----+
    | IX | T1 | T2 | T3 | T4 | T5 | T6 |
    +----+----+----+----+----+----+----+
    |  1 |  1 |  1 |  1 |  4 |  1 |  1 |
    |  2 |  1 | [7]|  9 |  1 |  1 |  1 |
    |  3 |  1 |  4 |  8 |  1 |  1 |  1 |
    | .. | .. | .. | .. | .. | .. | .. |
    +----+----+----+----+----+----+----+
    '''
    colnr = df.shape[1]
    row = coord // colnr
    column = coord % colnr
    return df.iloc[row,column]


if __name__ == '__main__':
    data = {'T1': pd.Series([1, 1, 1, 1, 2, 31, 1],
             index=['1', '2', '3', '4', '5', '6','7']),
            'T2': pd.Series([1, 4, 1, 2, 6, 2, 1],
             index=['1', '2', '3', '4', '5', '6','7']),
            'T3': pd.Series([1, 7, 1, 2, 7, 3, 1],
             index=['1', '2', '3', '4', '5', '6','7']),
            'T4': pd.Series([1, 1, 1, 1, 4, 4, 1],
             index=['1', '2', '3', '4', '5', '6','7']),
            'T5': pd.Series([1, 1, 1, 2, 1, 3, 1],
             index=['1', '2', '3', '4', '5', '6','7']),
            'T6': pd.Series([1, 2, 1, 2, 1, 3, 1],
             index=['1', '2', '3', '4', '5', '6','7'])
            }

    df = pd.DataFrame(data)
    print(getvalues(33,df))











