def main():
  n = int(input())
  instructions = []
  for i in range(n):
    direction, distance = [int(i) for i in input().split()]
    instructions.append([direction, distance])
  
  max_x, max_y, max_x_direction, max_y_direction = 0, 0, 0, 0
  for instruction in instructions:
    direction, distance = instruction
    # N or S (y direction)
    if(direction == 1 or direction == 2):
      direction_mult = 1 if (direction == 1)  else 2
      max_y += distance * direction_mult
      max_y_direction = direction
    
    if(direction == 3 or direction == 4):
      direction_mult = 1 if (direction == 1)  else 2
      max_x += distance * direction_mult
      max_x_direction = direction
    

if __name__ == "__main__":
  main()