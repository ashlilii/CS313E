#  File: Boxes.py

#  Description: Program finds the largest subset of boxes that nest inside each other

import sys

subsets = []

def sub_sets (a, b, idx):
  global subsets
  # when the program has checked every box, add to the subset
  if (idx == len(a)):
    subsets.append(b)
    return
  else:
    c = b[:]
    b.append (a[idx])
    sub_sets (a, c, idx + 1)
    if len(b) > 1:
      box1 = b[len(b) - 2]
      box2 = b[len(b) - 1]
      # if box1 is smaller than box2, continue to add to the subset
      if box_fit(box1, box2) is True:
        sub_sets(a, b, idx + 1)
    else:
      sub_sets (a, b, idx + 1)

def box_fit(box1, box2):
    # sees if box1 is smaller than box2
    if box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]:
        return True

def read_file():
    all_box = []
    line = sys.stdin.readline()
    line = line.strip()
    num_boxes = int(line)

    for i in range(num_boxes):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        box = [int(x) for x in line]
        # sort dimensions into ascending order
        box.sort()
        all_box.append(box)
    all_box.sort()
    return all_box

def main():
  boxes = []
  box_dimensions = read_file()

  sub_sets(box_dimensions, boxes, 0)

  # constraint that to be considering nesting, it must have two boxes
  largest = 2
  for i in subsets:
    if len(i) > largest:
      largest = len(i)
  print(largest)
  
  counter = 0
  for i in sorted(subsets):
    if len(i) == largest:
      counter += 1
  print(counter)

if __name__ == "__main__":
  main()
