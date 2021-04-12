from house import House
from quilt import Quilt

q = Quilt()
for row in range(10):
    for column in range(10):
        h = House("A", "B", "C", "D")
        q.set_house(row, column, h)

print(q.is_complete())

print(q)
