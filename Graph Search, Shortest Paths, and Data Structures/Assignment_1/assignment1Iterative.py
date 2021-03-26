
input_file = ""
def inputGenerator(input_file):
    """Get the Input"""
    with open(input_file, 'r') as data:
        line = data.read().strip().split("\n")
    graphDict = {} #we will store information on the node in the index, i.e. index 0 = node 1
    maximum = 0
    for element in line:
        line_list = list(map(int, element.strip().split(" ")))
        if line_list[0] in graphDict:
            graphDict[line_list[0]].append(line_list[1])
            if line_list[1] > maximum: #get maximum for later
                maximum = line_list[1]
        else:
            graphDict[line_list[0]] = [line_list[1]]
            if line_list[0] > maximum or line_list[1] > maximum:
                maximum = max(line_list[0], line_list[1])

    return graphDict, maximum
    
G, maximum = inputGenerator(input_file) #We want the maximum to know over which range we should iterate without hard coding this variable


def graphTranspose(G):
    gTransposed = {}
    for node in G:
        for edge in G[node]:
            if edge in gTransposed:
                gTransposed[edge].append(node)
            else:
                gTransposed[edge] = [node]
    return gTransposed
      
#implement all under same function for easier handling of variable scope              
def kosaraju(G):
    #First iteration to get magical order
    looper, nonExploredNode, L = range(maximum, 0 , -1), [0] + [1] * (maximum), []
    for node in looper:
        if nonExploredNode[node]:
            nonExploredNode[node], s = False, [node]
            while s:
                done = True
                if s[-1] not in G:
                    L.append(s.pop())
                    continue #add it to the list of nodes as this node is a sunk node, no need to loop on it below as it'll fail
                for edge in G[s[-1]]:
                    if nonExploredNode[edge]:
                        nonExploredNode[edge], done = False, False
                        s.append(edge)
                        break
                if done:
                    L.append(s.pop())
    GT = graphTranspose(G) 

    #iterating again using magical order
    result, temp = [], 0
    while L:
        v = (L.pop())
        s = [v]
        if not nonExploredNode[v]:
            nonExploredNode[v] = True
            result.append(1)
        while s:
            done = True
            if s[-1] not in GT:
                if nonExploredNode[s[-1]]: #check if already counted above
                    s.pop()
                    break #if yes pop it without double counting
                else:
                    result.append(1)
                    s.pop()
                    break
            for edge in GT[s[-1]]:
                if not nonExploredNode[edge]:
                    nonExploredNode[edge], done = True, False
                    s.append(edge)
                    result[-1]+=1
                    break
            if done:
                s.pop()
    print(sorted(result, reverse=True))
kosaraju(G)
