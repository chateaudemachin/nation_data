# Import the pandas library.
import pandas
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# Read in the data.
event = pandas.read_csv("NOV 12 Hembygdsbal.csv")
#plt.hist(event["Name"])


print(event.columns)
#plt.show()

