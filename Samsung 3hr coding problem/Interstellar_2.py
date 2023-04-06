class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Wormhole:
    def __init__(self, ax, ay, bx, by, duration):
        self.gateA = Node(ax, ay)
        self.gateB = Node(bx, by)
        self.duration = duration
        
def calculateDistance(a: Node, b:Node):
    return (abs(a.x - b.x) + abs(a.y - b.y))

def isWormhole(gate: Node, wormholes: list[Wormhole]):
    for w in wormholes:
        if(w.gateA == gate or w.gateB == gate): return [True, w]
    return [False, None]

def getNextSmallestDistance(distances, visited):
    min_node, min_node_dist = None , 0
    for d in distances:
        if(d in visited): continue
        if(min_node == None):
            min_node = d
            min_node_dist = distances[min_node]
            continue
        if(distances[d] < min_node_dist):
            min_node = d
            min_node_dist = distances[min_node]
    return [min_node, min_node_dist]
    

def getLeastDistance(wormholes: list[Wormhole], start: Node, end: Node):
    if len(wormholes) == 0: return calculateDistance(start, end)

    visited = [start]
    nodes_list = [start]
    distances = {}
    for wormhole in wormholes:
        nodes_list.append(wormhole.gateA)
        nodes_list.append(wormhole.gateB)
    nodes_list.append(end)
    
    # get initial distance from start to all other nodes
    for node in nodes_list:
        distance = calculateDistance(start, node)
        distances[node] = distance
    nodes_list.remove(start)

    # smallest next node
    min_node, min_node_dist = getNextSmallestDistance(distances, visited)
    while(len(nodes_list) != 0):
        for unvisited_node in nodes_list:
            if(len(nodes_list) == 1 and min_node == end): break
            #check if current min node is wormhole
            is_wormhole, wormhole = isWormhole(min_node, wormholes)
            # check if the current unvisited node is the complementary gate
            if is_wormhole and (wormhole.gateA == unvisited_node or wormhole.gateB == unvisited_node):
                distance = min_node_dist + wormhole.duration
                if(distance < distances[unvisited_node]): 
                    distances[unvisited_node] = distance
            # distance from the current node with smallest distance to target unvisited node
            else:
              distance = calculateDistance(unvisited_node, min_node)
              distance += min_node_dist
              if(distance < distances[unvisited_node]): 
                    distances[unvisited_node] = distance
            
        visited.append(min_node)
        nodes_list.remove(min_node)
        min_node, min_node_dist = getNextSmallestDistance(distances, visited)

      


    return(distances[end])  
    
def main():
    # get T test cases
    t = int(input())

    for j in range(t):
      n = int(input())
      # get start node and end node
      sx, sy, ex, ey = [int(i) for i in input().split()]
      start = Node(sx, sy)
      end = Node(ex, ey)

      # get N wormholes
      wormholes = []
      for i in range(n):
          ax, ay, bx, by, duration = [int(i) for i in input().split()]
          wormhole = Wormhole(ax, ay, bx, by, duration)
          wormholes.append(wormhole)

      # GET least distance
      res = getLeastDistance(wormholes, start, end)
      print(f"#{j+1}", res)
        

    
if __name__ == "__main__":
    main()
    