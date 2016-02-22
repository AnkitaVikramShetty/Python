from collections import deque

input_file=open("/Users/AnkitaShetty/Documents/sem2/AI/Input.txt","r").readlines()
#print input_file

#Initializations
g=dict()
c={}
child_list=[]
explored= []
path=[]
depth = dict()

#method to get path from source to destination
def get_path(explored,graph):
    if source == dest:
        return "Source is the destination"
    else:
        p = {}
        p[source] = source + ', '
        while len(explored) > 0:
            current = explored[0]
            del explored[0]
            if current in graph.keys():
                for neighbor in graph.get(current).keys():
                    if neighbor not in p:
                        if neighbor == dest:
                            p[neighbor] = p[current] + neighbor
                        else:
                            p[neighbor] = p[current] + neighbor + ', '
                       # print p[neighbor]
                        if neighbor == dest:
                            return p[neighbor]
        return "NO PATH"

#method to calculate cost of path
def get_cost(finalpath,g):
    if source == dest:
        return 0
    else:
        place = finalpath.split(", ")
        cost = 0
        i=0
        j=1
        while len(place)>j:
            if place[j] in g[place[i]]:
                x = g[place[i]]
                for k in x:
                    if k == place[j]:
                        cost = cost + int(x[k])
                i=i+1
                j=j+1

        return cost

#obtain child nodes of a parent node
def obtain_child_nodes(parent_node,graph):
    child_list=[]
    if parent_node in graph.keys():
        x=graph[parent_node]
        for k in x:
            child_list.append(k)
    return child_list

#check if given queue is empty
def is_empty(name):
    if name == deque([]):
        return True
    if name == []:
        return True
    else:
        return False

#check for goal
def goal_test(x):
    if x == dest:
       # explored.append(x)
        finalpath=[]
        finalpath = get_path(explored,graph)
        print 'Path  from ', source, ' to ', dest, ' is:'
        print finalpath
        finalcost = get_cost(finalpath,graph)
        print 'The total cost is ',finalcost
        return True
    else: return False

#print all the places on the map
def get_all_places():
    all_places = []
    for line in input_file:
        words = line.split(", ")
        for word in words:
            if '\n' not in word:
                if word not in all_places:
                    all_places.append(word)
    return all_places

all_places = get_all_places()

#constructs a graph
def construct_graph(input_file):
    for line in input_file:
        words = line.split(", ")

        if (words[1] and words[0] in words) and words[0] in g.keys():
            g[words[0]][words[1]] = words[2]
        else:
            c={}
            c[words[1]] = words[2]
            g[words[0]] = c

        if(words[1] and words[0] in words) and words[1] in g.keys():
            g[words[1]][words[0]] = words[2]
        else:
            c = {}
            c[words[0]] = words[2]
            g[words[1]] = c

    return g

#prints the graph
def print_graph(g):
    for k in g:
        print k, ':', g[k]

graph = construct_graph(input_file)
#print_graph(g)

#BFS method
def bfs(source,dest,graph):
    depth=0
    path={}
    queue = deque([source])
    path[source]=source
    while True:
        if is_empty(queue) == True:
            print 'Failure'
            break

        popped_item = queue.popleft()
        if popped_item not in explored:
            explored.append(popped_item)
        if goal_test(popped_item) is True:
            break
        else:
            child_list=obtain_child_nodes(popped_item,graph)
            for y in child_list:
                if y not in queue:
                    queue.append(y)
        child_list=[]

#DFS method
def dfs(source,dest,graph):
    path={}
    stack = [source]
    path[source]=source
   # explored = []
    while True:
      #  print 'stack', stack
        if is_empty(stack) == True:
            print 'Failure'
            break
        else:
            popped_item = stack.pop()
            if popped_item in explored:
                continue
            explored.append(popped_item)
            if goal_test(popped_item) is True:
                break
            child_list=obtain_child_nodes(popped_item,graph)
            for y in child_list:
                if y not in stack:
                    stack.append(y)

def dlstry(source, dest, graph, limit):
    return rec_dls(source, dest, graph, limit)

def rec_dls(source, dest, graph, limit):
    if source not in explored:
            explored.append(source)
    if goal_test(source) is True:
        return source
    elif limit == 0:
        return 'cutoff'
    else:
        flag = False
        child_list=obtain_child_nodes(source,graph)
        for y in child_list:
            result = rec_dls(y, dest, graph, limit-1)
            if result == 'cutoff':
                flag = True
            elif result!='Failure':
                return result
        if flag == True:
            return 'cutoff'
        else:
            return 'Failure'

def ids(source, dest, graph, val):
    dep = 0
    while True:
       result = dlstry(source, dest, graph, dep)
       if result != 'cutoff':
           return result
       dep = dep + 1


#Take user input

while True:
    g=dict()
    c={}
    child_list=[]
    explored= []
    path=[]
    depth = dict()
    source=[]
    dest=[]
    search=[]
    print ''
    print 'Choose an option 1,2,3,4: '
    print '1. Search'
    print '2. Display entire graph'
    print '3. Display list of nodes'
    print '4. exit'

    value = 0

    value = raw_input("Enter value: ")

    if value == str(1):
        source = raw_input("Enter source: ")
        source = source.lower()
        source = source.title()
        if source not in all_places:
            print 'Given source does not exist in the map'
            break

        dest = raw_input("Enter destination: ")
        dest = dest.lower()
        dest = dest.title()
        if dest not in all_places:
            print 'Given destination does not exist in the map'
            break
        search = raw_input("Enter search method (BFS) (DFS) (ID): ")
        search = search.upper()

        if search != 'BFS' and search != 'DFS' and search != 'ID':
            print 'Illegal input. Choose from the given search methods.'
            break

        if search == 'BFS':
            bfs(source,dest,graph)
        if search == 'DFS':
            dfs(source,dest,graph)
        if search == 'ID':
            'Enter'
            ids(source,dest,graph,1)

    elif value == str(2):
        graph = construct_graph(input_file)
        print_graph(g)

    elif value == str(3):
        print all_places

    elif value == str(4):
        break

    else:
        print 'Invalid selection. Try again'



