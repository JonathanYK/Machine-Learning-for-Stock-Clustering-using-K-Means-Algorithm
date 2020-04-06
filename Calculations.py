# Calculations.py

import pandas as pd
import numpy as np
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
        closingRowData = market.iloc[2:, 2].astype(float)
        closingSum = closingRowData.sum()
        openingSum = market.iloc[2:, 4].astype(float).sum()
        avg = (closingSum + openingSum) / (closingRowData.size * 2) # Calculating the whole average
        avgArr.append(avg)
        stdevArr.append(stdev(closingRowData))

    finished = {'Name of the Share': all_files, 'Average': avgArr, 'Standard Deviation': stdevArr}
    calc = pd.DataFrame(finished)
    calc.to_csv('avg_and_stdev_per_day_per_share.csv')

   # print(calc)  debugging - delete


def avg_and_beta_per_day_per_share():
    # set the correct path according to the project location    V
    all_files = find_csv_filename("D:\Coding\Python\PyCharm\PyCharm\ShareData")

    # print(all_files)  debugging - delete

    avgArr = []
    tempBetaArr = []
    betaArr = []

    for f in all_files:
        # print(f)  debugging - delete
        market = pd.read_csv('ShareData/' + f)
        closingRowData = market.iloc[2:, 2].astype(float)
        closingSum = closingRowData.sum()
        openingSum = market.iloc[2:, 4].astype(float).sum()
        avg = (closingSum + openingSum) / (closingRowData.size * 2)  # Calculating the whole average
        avgArr.append(avg)

        for i in range(2, closingRowData.size-1):
            betaRow = (closingRowData[i] / closingRowData[i+1]) -1
            tempBetaArr.append(betaRow)

        betaArr.append(np.average(tempBetaArr))

    finished = {'Name of the Share': all_files, 'Average': avgArr, 'Beta': betaArr}
    calc = pd.DataFrame(finished)
    calc.to_csv('avg_and_beta_per_day_per_share.csv')

# print(calc)  debugging - delete




def returns_per_year_per_share():
    all_files = find_csv_filename("D:\Coding\Python\PyCharm\PyCharm\ShareData")

    yearArr = [2013, 2014, 2015, 2016, 2017, 2018]
    tempRetArr = []
    retaArr = []

    for f in all_files:
        # print(f)  debugging - delete
        market = pd.read_csv('ShareData/' + f)

        closingRowData = market.iloc[2:, 2].astype(float)

        for i in range(2, closingRowData.size - 1):
            betaRow = (closingRowData[i] / closingRowData[i + 1]) - 1
            tempRetArr.append(betaRow)

        retaArr.append(np.average(tempRetArr))



        finished = {'Name of the Share': all_files, 'Return': retaArr, 'Year': yearArr}
        calc = pd.DataFrame(finished)
        calc.to_csv('avg_and_beta_per_day_per_share.csv')