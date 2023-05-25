# Check for missing Call Numbers

## Goal
We have extracted the Number-Part of our Call Numbers. Usually they have a sequential number, followed by a dash, followed by an upper case character (e.g. 105375-B). Throughout the years it is possible that some numbers disapear. This small program works with al list of Call Numbers and finds the missing digits.

## How it works
1. With the provided analytics query we get the Numbers out of the Alma Analytics.
    1. Note that this query is tailored to meet the needs of the JKU and would need adaptation if used in a different university.
1. Save your analytics query result as csv file with the name `input.csv` in the root folder
1. Change the following paramater as you wish:
    1. Search only a specific Call Number range:
        1. `lastCallNr2Check` to define an upper limit
        1. `firstCallNr2Check` defines the lower limit
    1. `bins` defines the "resolution" of the histogram
1. Execute callNr_checker.py

The produced output is a list of missing numbers of specified range and a graphic file of a histogram plot showing the distribution of the Call Numbers. All files are stored in the `output` folder.