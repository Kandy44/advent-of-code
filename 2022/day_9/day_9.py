def read_data():
    with open("../inputs/9.in", "r") as fp:
      return [line.strip('\n').split(' ') for line in fp]

def count_repeated_points(data,tail_length=1):
  comp = lambda a,b: 1 if a > b else -1 if a < b else 0
  update_point = lambda x,y,d: [x+{'R':1,'L':-1}.get(d,0),y+{'D':1,'U':-1}.get(d,0)]
  visited_points = {(0,0)}
  head_x,head_y=0,0
  tail_idxs = [[0,0] for _ in range(tail_length)]
  for (direction,step_count) in data:
    step_count = int(step_count)
    
    for _ in range(step_count):
      head_x,head_y = update_point(head_x,head_y,direction)
      prev_head_x,prev_head_y = head_x,head_y
      
      for i in range(tail_length):
        tail_x,tail_y = tail_idxs[i]
        if abs(prev_head_x - tail_x) == 2 or abs(prev_head_y - tail_y) == 2:
          tail_x += comp(prev_head_x,tail_x)
          tail_y += comp(prev_head_y,tail_y)
        tail_idxs[i] = [tail_x,tail_y]
        prev_head_x,prev_head_y = tail_x,tail_y
        visited_points.add(tuple(tail_idxs[-1]))
    
  return len(visited_points)

def main():
    data = read_data()
    print(count_repeated_points(data,tail_length=1))
    print(count_repeated_points(data,tail_length=9))
main()