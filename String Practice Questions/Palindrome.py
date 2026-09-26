def is_palindrome(s):
  if not s:
    return True

  s = s.lower().replace(" ","")
  return s == s[::-1]


print(is_palindrome("A man a plan a canal Panama"))

