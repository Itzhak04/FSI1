First of all, there are 3 python files of importance in this repository: 
- run.py 
	- used for running the tests, the results printed through this file contain: 
	(route taken) + (number of generated nodes) + (number of visited nodes) + (time the test has lasted in nanoseconds) + (cost of the route taken)
	additionally to separate each test there is a line of hyphens.


- search.py
	- There are various classes and a few classless functions on this file, some of them unmodified compared to the files files we
   were given for this practice, these are:
		- The "Problem" abstract class which represents a formal problem where there is an initial state and a goal, it also
    helps with expanding the problem,s graph.
		
		- The "Graph" class which is in charge of making and being the graph for the problem, in order to create the graph, 
		we use the help of various functions like the "RandomGraph", and the help of another class in this file "GPSProblem".
    Toghether all of them make the graph so that we can focus on the problem of this practice.
		
		- The "Node" class which defines the nodes for the problem associated with the graph.

	- The functions worthy of note that we have changed are:
		-added: "ramificacion_search" which has been added for the associated problem, it takes a problem and uses the
     corresponding list type for that problem.
		-added: "subestimacion_search" which has also been added for the associated problem, as before it takes a problem
     and uses the corresponding list type for that problem.
		-modified: "graph_search" has been modified, before it simply searched the graph for the solution using the initial node,
     now with the help of the "Result" class it also saves additional information.
	- The only class that we have added in this file is "Result":
		- The "Result" class is used to store the information relating to the problem, or in other words additional problem information, 
		the object from this class is initially created in the modified "graph_search" function which then starts the timer
    for the problem, so that we can know the amount of time the problem was being processed. Then, while inside the same "graph_search" function,
    the object from the class is modified for example by increasing the values of the visited nodes attribute, by increasing the number of
    generated nodes, to set the goal node and to finally end the timer for the problem.

-utils.py
	-Since it has a lot of classes and functions, we will only mention the modifications:
		-added: "PriorityQueue" class it serves as the queue for the "ramificacion" problem. It is used to find a solution for a problem.
		-added: "PriorityQueue2" class it serves as the queue for the "subestimacion" problem. It is used to find the best solution for a problem.
