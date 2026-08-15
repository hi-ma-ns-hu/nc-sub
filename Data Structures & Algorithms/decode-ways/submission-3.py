class Solution:
  def numDecodings(self, s: str) -> int:
    a, b = 0, 0
    res = 1 # default for lens(s) = 1
    
    for i in range(len(s)-1, -1, -1):
      if s[i] == '0':
        a = 0
      else:
        a = res

      if (i+1) < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456'):
        a += b
      
      a, b, res = 0, res, a
      
    return res