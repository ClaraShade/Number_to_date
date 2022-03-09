# Number_to_date
This is a small script to extract a date from serial number of the product,
designed by my previous workplace.
The serial number must be in a form of 'YYMMDDXXX', where the last three digits corresponds to
the ID in the LOT.
It takes the .xlsx file with bunch of serial numbers in the first column and creates the .xlsx file with corresponding
dates in the firs column.

PIP installation required: openpyxl