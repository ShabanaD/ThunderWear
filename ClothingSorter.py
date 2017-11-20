import indicoio
import math
import json
import operator
import os

indicoio.config.api_key = '4db161e811d460e7173d6dbb19384330'

# Create 5 json files, tops, jackets/coats, bottoms and dresses
jackets = ["coat", "snowsuit", "jacket", "windbreaker", "windcheater", "sweater", "cardigan", "vest"]
dresses = ["dress", "gown"]
tops = ["button", "blouse", "shirt", "top"]
bottoms = ["pants", "skirt", "trousers", "denim", "jeans", "shorts", "slacks"]

clothing = []
i=0
for root, dirs, files in os.walk("imgs"):
    for image in files:
        if image.endswith("jpg"):
            clothing.append(os.path.join(root, image))
            i+=1

            if i == 500:
                break
            
clothes = indicoio.image_recognition(clothing)
j = open('jackets.txt', 'w')
d = open('dresses.txt', 'w')
t = open('tops.txt', 'w')
b = open('bottoms.txt', 'w')

i=0
for cloth in clothes:
    sortC = sorted(cloth.items(), key=operator.itemgetter(1), reverse=True)
    print(sortC[0][0])
    if any(s in sortC[0][0] for s in jackets):
        j.write(clothing[i]+"!"+sortC[0][0]+"?")
    elif any(s in sortC[0][0] for s in dresses):
        d.write(clothing[i]+"!"+sortC[0][0]+"?")
    elif any(s in sortC[0][0] for s in tops):
        t.write(clothing[i]+"!"+sortC[0][0]+"?")
    elif any(s in sortC[0][0] for s in bottoms):
        b.write(clothing[i]+"!"+sortC[0][0]+"?")
    i+=1

j.close()
d.close()
t.close()
b.close()
