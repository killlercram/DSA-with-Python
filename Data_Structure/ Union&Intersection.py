def UandI(set1, set2):
  union = set1 | set2
  intersection = set1 & set2

  print("Union: ",union )
  print("Intersection: ",intersection )

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

unionAndIntersection = UandI(set1,set2)
