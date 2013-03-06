import networkx.generators.small
from networkx.algorithms import traversal

g = networkx.generators.small.krackhardt_kite_graph()
print g.number_of_edges()
print g.number_of_nodes()
print g.adjacency_list()
print g.edges()

tree = traversal.dfs_tree(g)

print tree.succ

import itertools

print g.nodes()

print list(itertools.combinations(g.nodes(), 2))
print "Sosi"