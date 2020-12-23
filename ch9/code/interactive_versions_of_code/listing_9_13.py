import pandas
import seaborn
import numpy
from matplotlib import pyplot

malware = pandas.read_csv("malware_data.csv")
axis = seaborn.jointplot(x=numpy.log10(malware['size']),
                         y=malware['positives'],
                         kind="kde")
axis.set_axis_labels("Bytes in malware file (log base-10)",
                     "Number of engines detecting malware (out of 57)")
pyplot.show()
