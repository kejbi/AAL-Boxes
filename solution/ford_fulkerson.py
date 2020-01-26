# code from https://github.com/bigbighd604/Python/blob/master/graph/Ford-Fulkerson.py
# little editions needed to algorithm

class Edge(object):
  def __init__(self, u, v, w):
    self.source = u
    self.target = v
    self.capacity = w

  def __repr__(self):
    return "%s->%s:%s" % (self.source, self.target, self.capacity)


class FlowNetwork(object):
  def  __init__(self):
    self.adj = {}
    self.flow = {}

  def AddVertex(self, vertex):
    self.adj[vertex] = []

  def GetEdges(self, v):
    return self.adj[v]

  def AddEdge(self, u, v, w = 0):
    if u == v:
      raise ValueError("u == v")
    edge = Edge(u, v, w)
    redge = Edge(v, u, 0)
    edge.redge = redge
    redge.redge = edge
    self.adj[u].append(edge)
    self.adj[v].append(redge)
    # Intialize all flows to zero
    self.flow[edge] = 0
    self.flow[redge] = 0

  def FindPath(self, source, target, path):
    if source == target:
      return path
    for edge in self.GetEdges(source):
      residual = edge.capacity - self.flow[edge]
      if residual > 0 and not (edge, residual) in path:
        result = self.FindPath(edge.target, target, path + [(edge, residual)])
        if result != None:
          return result

  def MaxFlow(self, source, target):
    path = self.FindPath(source, target, [])
    # print(f'path after enter MaxFlow: {path}')
    # for key in self.flow:
      # print(f'{key}:{self.flow[key]}')
    # print('-' * 20)
    while path != None:
      flow = min(res for edge, res in path)
      for edge, res in path:
        self.flow[edge] += flow
        self.flow[edge.redge] -= flow
      # for key in self.flow:
        # print(f'{key}:{self.flow[key]}')
      path = self.FindPath(source, target, [])
      # print(f'path inside of while loop: {path}') 
    # for key in self.flow:
      # print(f'{key}:{self.flow[key]}')

    volume = 0
    stacks = []
    for vertex in self.adj.keys():
      if vertex[0] == 'u':
        lonely = True

        for edge in self.adj[vertex]:
          if edge.target[0] == 'v' and self.flow[edge] == 1:
            lonely = False
            for stack in stacks:
              if stack[-1] == edge.target[1]:
                stack.append(vertex[1])
                break
            break
        
        if lonely:
          stacks.append([vertex[1]])
          volume += vertex[1][3]

    return stacks, volume  
    #return sum(self.flow[edge] for edge in self.GetEdges(source))