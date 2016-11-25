# if python2 unicode consider
# this is not a big data problem

import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
from numpy.random import normal

"""
Event   Person1, 2, 3, 4, ... N
1           5    4  0  0      0
2           3    5  5  0      0
3           3    0  3  3      5
"""
nlist = []
ndict = {}
is_there = {}
events = {}
# max_count = 0
for file in os.listdir('.'):
    if file.endswith('.csv'):
        date_str = file[:6].strip().lower()
        date = datetime.strptime(date_str, '%b %d')
        event_name = file[6:-4].strip().lower()
        event = {'name': event_name,
                 'date': date,
                 'date_str': date_str}
        # print event
        # parse date
        ndict[file]={}
        with open(file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            events[event_name.lower()] = {'count': 0, 
                                          'going':0, 
                                          'maybe':0,
                                          'invited':0}

            for row in reader:
                name, status = row
                # TODO remove the ','
                status = status.split(',')[-1]
                event_name=event_name.lower()
                events[event_name]['count'] += 1
                if status.lower() == 'going':
                    events[event_name]['going'] += 1
                    name = name.lower()
                    if name in is_there:
                        is_there[name]['events'].append(event)
                        is_there[name]['count'] += 1
                    else:
                        is_there[name]={
                            'events':[event],
                            'count':0
                        }
                if status.lower() == 'maybe':
                    events[event_name]['maybe'] += 1
                if status.lower() == 'invited':
                    events[event_name]['invited'] += 1
                # nlist.append(name)
                # if status not in ndict[file]:
                #     ndict[file][status]=[name]
                # else:
                #     ndict[file][status].append(name)
ordered_counts = sorted([(name, is_there[name]['count']) for name in is_there], key=lambda x: x[1])
ordered_events_count = sorted([(name, events[name]['count']) for name in events], key=lambda x: x[1])
ordered_events_going = sorted([(name, events[name]['going']) for name in events], key=lambda x: x[1])

from pprint import pprint
pprint(ordered_events_going)

print len(ordered_events_going)

'''
#show what events had the biggest reach
counts_only = [x[1] for x in ordered_events if x[1] and x[1]]
# plt.figure(1)
plt.plot(counts_only)
plt.show()


# pprint(is_there['mostafa salah'])
# print(max_count)
# pprint(ordered_counts)

# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly
# plotly.tools.set_credentials_file(username='ielouafiq', api_key='gxSMBi2oyq6nIrRxWv59')
# import numpy as np
# x = np.random.randn(500)
#
# data = [
#     go.Histogram(
#         x=x
#     )
# ]
# py.iplot(data)
#
#
# import plotly.plotly as py
# import plotly.graph_objs as go
#
# import numpy as np
# x = np.random.randn(500)
#
# data = [
#     go.Histogram(
#         x=x,
#         histnorm='probability'
#     )
# ]
# py.iplot(data)



# import random
# import numpy
# import matplotlib.pyplot as plt
# import plotly.plotly as py  # tools to communicate with Plotly's server
#
# histogram=plt.figure()
#
# x = [random.gauss(3,1) for _ in range(400)]
# y = [random.gauss(4,2) for _ in range(400)]
#
# bins = numpy.linspace(-10, 10, 100)
#
# pyplot.hist(x, bins, alpha=0.5)
# pyplot.hist(y, bins, alpha=0.5)
# pyplot.show()
#
print ordered_counts
# plot_url = py.plot_mpl(histogram, filename='docs/histogram-mpl-same')


counts_only = [x[1] for x in ordered_counts if x[1] and x[1]]
# plt.figure(1)
plt.plot(counts_only)
plt.show()

# plt.figure(2)
plt.hist(counts_only)
plt.show()

# gaussian_numbers = [x[1] for x in ordered_counts  if x[1] and x[1]]
# plt.hist(gaussian_numbers)
# plt.title("Gaussian Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()
'''

