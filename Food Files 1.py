#food files 1

#food
file = open("foods.txt", "r")
lines_list = []
for line in file:
    stripped_line = line.strip()
    lines_list.append(stripped_line)

food = [ele for ele in lines_list if ele.strip() ]
food.pop(29)
print(food)
file.close()







#fiber
file = open("highfiber.txt", "r")
lines_list = []
for line in file:
    stripped_line = line.strip()
    lines_list.append(stripped_line)

fiber = [ele for ele in lines_list if ele.strip() ]
fiber.pop(29)
fiber = [x.lower() for x in fiber]
print(fiber)
file.close()



#glycemic
file = open("low-glycemic-index.txt", "r")
lines_list = []
for line in file:
    stripped_line = line.strip()
    lines_list.append(stripped_line)

glycemic = [ele for ele in lines_list if ele.strip() ]
glycemic.pop(29)
glycemic = [x.lower() for x in glycemic]
print(glycemic)

file.close()


#lowfat
file = open("lowfat.txt", "r")
lines_list = []
for line in file:
    stripped_line = line.strip()
    lines_list.append(stripped_line)

lowfat = [ele for ele in lines_list if ele.strip() ]
lowfat.pop(29)
lowfat = [x.lower() for x in lowfat]
print(lowfat)
file.close()

finalList = []

dict1 = {}
dict1.update({food[0]:food[1],fiber[0]:fiber[1],glycemic[0]:glycemic[1],lowfat[0]:lowfat[1]})

print(dict1)