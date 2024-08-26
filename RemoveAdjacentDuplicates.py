def remove_duplicates(s):
  stack = []
  for item in s :
    if len(stack) > 0 and item == stack[len(stack)-1] :
      stack.pop()
    else :
      stack.append(item)
  return "".join(x for x in stack)
