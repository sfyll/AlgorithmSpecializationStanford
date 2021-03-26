
input_file = "/Users/santi/Documents/Algorithm Class Stanford/Assignments/Class 2/Assignment_1/testCase.txt"
def inputGenerator(input_file):
    """Get the Input"""
    with open(input_file, 'r') as data:
        line = data.read().strip().split("\n")
    graphDict = {} #we will store information on the node in the index, i.e. index 0 = node 1
    for element in line:
        line_list = list(map(int, element.strip().split(" ")))
        if line_list[0] in graphDict:
            graphDict[line_list[0]].append(line_list[1])
        else:
            graphDict[line_list[0]] = [line_list[1]]
    return graphDict
    
G = inputGenerator(input_file)
#Global Var Instantiation
s = None
order = []
nonExploredNode = [0] + [1] * max((list(G.keys())[-1]+1), len(G))#if node not explored, equal to 1
counter = []
temp = 0

def dfs_loop(G, looper):
    global s
    for node in looper:
        if nonExploredNode[node]:
            s = node
            dfs(G, node)

def dfs(G, node):
    global order
    global nonExploredNode
    global counter
    global temp
    nonExploredNode[node] = False
    leader = s
    if node not in G:
        counter.append(1)
        order = [node] + order #sunk vertex so we append it
        return
    for edge in G[node]:
        if nonExploredNode[edge]:
            dfs(G, edge)
    order = [node] + order
    if leader == temp:
        counter[-1]+=1
    else:
        temp= s
        counter.append(1)

def graphTranspose(G):
    gTransposed = {}
    for node in G:
        for edge in G[node]:
            if edge in gTransposed:
                gTransposed[edge].append(node)
            else:
                gTransposed[edge] = [node]
    return gTransposed
                    
def kosaraju(G):
    global order
    global nonExploredNode
    global counter
    global temp
    looper = range(len(G), 0 , -1)
    dfs_loop(G, looper)
    GT = graphTranspose(G)
    counter = []
    nonExploredNode = [0] + [1] * max((list(G.keys())[-1]+1), len(G))
    temp = 0
    s = None
    print(GT, order)
    dfs_loop(GT, order)
    print(sorted(counter, reverse= True))

kosaraju(G)
