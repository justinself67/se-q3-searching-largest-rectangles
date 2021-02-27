def rect():
  res = []
  x = [2,3,4,5,6,7,8,9]
  y = [2,3,4,5,6,7,8,9]
  for v1 in x:
    for v2 in y:
      if (v2, v1) not in res:
        res.append((v1, v2))
  r = sorted(res, key=lambda x: (x[0]-1)*(x[1]-1), reverse=True)
  return r