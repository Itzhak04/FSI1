# Search methods

import search

points = [('A', 'B'), ('O', 'E'), ('G', 'Z'), ('N', 'D'), ('M', 'F')]

# Loop over each pair of points
for start, end in points:
    ab = search.GPSProblem(start, end, search.romania)


    a = search.depth_first_graph_search(ab)
    b = search.breadth_first_graph_search(ab)
    c = search.ramificacion_search(ab)
    d = search.subestimacion_search(ab)


    print(b.node.path(), b.generatedNode, b.visitNode, b.timing, b.node.path_cost)
    print(a.node.path(), a.generatedNode, a.visitNode, a.timing, a.node.path_cost)
    print(c.node.path(), c.generatedNode, c.visitNode, c.timing, c.node.path_cost)
    print(d.node.path(), d.generatedNode, d.visitNode, d.timing, d.node.path_cost)
    print("------------------------------------------------------------------------")

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
