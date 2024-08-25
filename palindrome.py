def is_palindrome(s):
  start = 0
  end = len(s) - 1
  
  
  while start <= end :
    if s[start] == s[end] :
      start += 1
      end -= 1
      print(start)
      print(end)
      continue
    else :
      return False
  return True
