#   Tile Cost Calculator v0.1
#   Thanks to karan for the idea!
#
print ("Welcome to Tile Cost Calculator")

print ("Please input the width of the floor")
width = int(input())

print ("Please input the height of the floor")
height = int(input())

print ("Please input the cost/sq ft of the tile")
cost = int(input())

total = ((width * height) * cost)
print (total)


