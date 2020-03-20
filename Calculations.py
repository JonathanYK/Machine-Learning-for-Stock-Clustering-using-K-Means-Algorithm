import pandas as pd
from statistics import stdev
from os import listdir


# Method to get all the share files in ShareData Package
def find_csv_filename( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]


def avg_and_stdev_per_day_per_share():

    # set the correct path according to the project location    V
    all_files = find_csv_filename("D:\Coding\Python\PyCharm\PyCharm\ShareData")
    # print(all_files)  debugging - delete

    avgArr = []
    stdevArr = []

    for f in all_files:
        # print(f)  debugging - delete
        market = pd.read_csv('ShareData/' + f)
        rowCount = market.iloc[2:, 2].astype(float)
        closingSum = rowCount.sum()
        openingSum = market.iloc[2:, 4].astype(float).sum()
        avg = (closingSum + openingSum) / (rowCount.size * 2) # Calculating the whole average
        avgArr.append(avg)
        stdevArr.append(stdev(rowCount))

    finished = {'Name of the Share': all_files, 'Average': avgArr, 'Standard Deviation': stdevArr}
    calc = pd.DataFrame(finished)
    calc.to_csv('avg_and_stdev_per_day_per_share.csv')

    print(calc)