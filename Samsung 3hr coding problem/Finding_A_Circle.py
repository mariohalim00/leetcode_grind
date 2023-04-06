def isThereACycle(adj):
    visited = []
    stack = [1]
    # for i in range(1, len(adj)):
    while stack:
      current_idx = stack.pop()
      if(current_idx in visited): return True
      visited.append(current_idx)
      # get all neighbors
      for i in range(1, len(adj[current_idx])):
        if adj[current_idx][i] == 1:
          stack.append(i)
    return False

def main():
    n, m = [int(i) for i in input().split()]
    paths = []
    for i in range(m):
      a, b = [int(i) for i in input().split()]
      paths.append([a, b])
    
    adj = [[0 for i in range(n + 1)] for i in range(n + 1)]
    for path in paths:
      a, b = path
      adj[a][b] = 1

    res = "Yes" if (isThereACycle(adj))  else "No"
    print(res)    

if __name__ == "__main__":
  main()