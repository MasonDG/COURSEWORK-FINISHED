class Vertex:
    #when an object is instaniated, it is given a label which is the nodes name.
    def __init__(self,label):
        self.label = label
        

class Graph:
    #adjList is the method I show my data graph structure, with the node as a dictionary linking to a list of neighboring nodes.
    adjList = { }

    def addNode(self,node):
        #if the node being entered already exists, ignore it. Else, add the node as a Vertex object with a value of an empty list.
            if node.label in self.adjList:
                pass
            else:
                self.adjList[node.label] = []


    def addEdge(self,fromNode,toNode):
        #First check if the two nodes being used to add an edge exists.
        if fromNode in self.adjList:
            if toNode in self.adjList:
                #when both nodes have been found, append each of the node's dictionary key to include each other within their values.
                self.adjList[fromNode].append(toNode)
                self.adjList[toNode].append(fromNode)
                             
    def returnGraph(self):
        #return the adjecency list data graph for the object being passed.
        return(self.adjList)

    def dfs(graph,startNode):
        #start with a empty stack and visited list, the visited list will keep a record of nodes that have been visited already.
        stack = [ ]
        visited = [ ]
        #append the provided node to the stack then start a while loop conditional for if the stack has a node inside.
        stack.append(startNode)
        #while the stack is not empty
        while stack:
            #pop the first unvisited node linked to the current before continuing.
            edge = stack.pop()
            #if the node currently being visited was not visited before, add it into the existing list in visited
            #then update the stack list before adding the rest of the edges before moving onto the next node.
            if edge not in visited:
                visited.extend(edge)
                #Traverse to the first unvisited node linked to the previous popped node, stop once all connected nodes are in the visited list.
                stack = stack + graph.adjList[edge]
        #create a text file in the same folder as the script, write the start node passed then how the nodes were visited.
        text_file = open("outputtedWork.txt", "w")
        text_file.write("DFS Result of " + str(startNode + str(visited)))
        text_file.close()
        return visited

    def bfs(graph,startNode):
        #Similar process to DFS except when it finds its first available node
        stack = [ ]
        visited = [ ]
        stack.append(startNode)
        while stack:
            edge = stack.pop(0)
            if edge not in visited:
                visited.extend(edge)
                stack = stack + graph.adjList[edge]
        text_file = open("outputtedWork.txt", "w")
        text_file.write("BFS Result of " + str(startNode) + str(visited))
        text_file.close()
        return visited
#graph will be an object of Graph class which I use to conduct the necessary tasks                            
graph = Graph()
#Simple fixed array of 10 elements to be used as nodes
nodes = ['0','1','2','3','4','5','6','7','8','9']
#Adds each element of the node function into a graph format by calling the addNode function with the argument being the node's position as a Vertex object.
for i in range(0,len(nodes)):
    graph.addNode(Vertex(nodes[i]))
#Example code to add edges inbetween existing nodes
graph.addEdge('0','2')
graph.addEdge('2','3')
graph.addEdge('3','4')
graph.addEdge('3','5')
graph.addEdge('5','6')

#Brief pseudo code provided from lecture slides to help me understand
#CLASS VERTEX
    #LABEL <--- 0
    # EDGES < ---- [ ]

    #example <--- new VERTEX ( example = Vertex(24,3)
    #example.label <--- 24 (24 IS A NODE)
    #example.edges.add(3) <------ 3 is the node it is going to



