newHeight = 100
initHeight = 100
totalHeight = 0
for i in range(10):
  newHeight /= 2
  totalHeight = initHeight
  initHeight += newHeight*2
print(totalHeight)
print(newHeight)
