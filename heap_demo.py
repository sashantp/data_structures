# heap demo
from heapq import *

h = []

heappush(h, (2, 'sashant'))
heappop(h)

l = []

heappush(l,4)
heappush(l,2)
heappush(l,3)
heappush(l,1)

print heappop(l)
print heappop(l)


