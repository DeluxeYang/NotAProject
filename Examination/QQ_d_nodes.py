input_temp = input().split(" ")
deep = int(input_temp[0])
three_nodes = [int(x) for x in input_temp[1:]]
_number = 0
top = deep*deep
buttom = 0
flag = False
while True:
  mid = (top + buttom) / 2
  is_more = 0
  is_less = 0
  for node in three_nodes:
    if node > mid:
      is_more += 1
    elif node < mid:
      is_less += 1
    else:
      _number = mid
      flag = True
  if is_more == 3:
    buttom = mid
  elif is_less == 3:
    top = mid
  else:
    _number = mid
    flag = True
  if flag:
    break
print(_number)
