import networkx as net
import urllib

g = net.Graph()
g.add_edge('a','sosi')
g.add_edge('b','sarah')
g.add_edge('b','sosi')
net.draw(g)
print g.node['sosi']
print g['sosi']

#print "Sosi"