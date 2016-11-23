# Import the pandas library.
import pandas as pd
import matplotlib.pyplot as plt
#!/usr/bin/env python
#mvcoding: utf-8
#from sklearn.cluster import KMeans

from igraph import *


# Read in the data.
event1 = pd.read_csv("NOV 12 Hembygdsbal.csv")
event2 = pd.read_csv("OCT 1 Generationsmiddag a Uplands nation.csv")
print(event1["Name"])


print "event1"
print len(event1)

print "event2"
print len(event2)


event1 = event1[event1.Status == "Going"]
#event1["event"] = "Hembygdsbal"
event1['event'] = pd.Series("Hembygdsbal", index=event1.index)

event2 = event2[event2.Status == "Going"]
event2['event'] = pd.Series("Generationsmiddag", index=event2.index)

print "event1"
print len(event1)

print "event2"
print len(event2)

result = pd.concat([event1, event2])

print result

result.sort_values(by=["Name"])

'''




event1_graph = Graph();

event1_graph = Graph.Full(len(event1["Name"]), directed=False, loops=False)

#print("file length")
#print(len(event1["Name"]))

#event1_graph.add_vertices(len(event1["Name"]))

event1_graph.vs["name"] = event1["Name"]
event1_graph.vs["status"] = event1["Status"]


vertex = event1_graph.vs[0]
print(vertex)
print(len(event1_graph.vs))
event1_graph.delete_vertices(0)
print(len(event1_graph.vs))

to_delete_ids = [v.index for v in event1_graph.vs if v["status"] != "Going"]
event1_graph.delete_vertices(to_delete_ids)

for person in event1_graph.vs:
	print(person)


print("vertex list")
for person in event1_graph.vs:
	print person["name"]
	print person["status"]

event1_graph.vs["label"] = event1_graph.vs["name"]
layout = event1_graph.layout("kk")
#plot(event1_graph, layout = layout, margin = 20)
print(len(event1_graph.vs))


for name in event1["Name"]:

g = Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])

g.vs["name"] = ["Alice", "Bob", "Claire", "Dennis", "Esther", "Frank", "George"]
g.vs["age"] = [25, 31, 18, 47, 22, 23, 50]
g.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
g.es["is_formal"] = [False, False, True, True, True, False, True, False, False]

layout = g.layout("kk")

g.vs["label"] = g.vs["name"]
color_dict = {"m": "blue", "f": "pink"}
g.vs["color"] = [color_dict[gender] for gender in g.vs["gender"]]
plot(g, layout = layout, bbox = (300, 300), margin = 20)

'''