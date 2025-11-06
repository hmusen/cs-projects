# given a particular graph, how would you implement a Breadth-First Search that allows you to visit every vertex of the graph

marked = [False] * G.size()

def bfs(G,v):
    queue = [v] # initialise queue
    while len(queue) > 0: # while queue is not empty
        v = queue.pop(0) # put the first element of the queue into v to know the vertex we have to visit
        if not marked[v]: # if v is not marked
            visit(v) # visit v and mark it is as marked
            marked[v] = True
            for w in G.neighbours(v): # go through all the neighbours of v
                if not marked[w]: # if the neighbour is not marked
                    queue.append(w) # append it to the queue

[1]


