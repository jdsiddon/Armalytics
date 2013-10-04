import csv

txt_file = r"data.txt"
csv_file = r"data.csv"

# use 'with' if the program isn't going to immediately terminate
# so you don't leave files open
# the 'b' is necessary on Windows
# it prevents \x1a, Ctrl-z, from ending the stream prematurely
# and also stops Python converting to / from different line terminators
# On other platforms, it has no effect

""" "rU" opens the targeted text file as a text file
and allows \n, \r, \r\n to be used as new line characters"""

in_txt = csv.reader(open(txt_file, "rU"), delimiter = ',') 
out_csv = csv.writer(open(csv_file, 'wb'))

out_csv.writerows(in_txt)