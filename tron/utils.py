def is_between(c, a, b):
  return min(a, b) <= c and max(a, b) >= c


def is_on_line(p, a, b):
  x = p[0]
  y = p[1]
  x1 = a[0]
  y1 = a[1]
  x2 = b[0]
  y2 = b[1]
  d = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)

  return d == 0 and is_between(x, x1, x2) and is_between(y, y1, y2)
