nb_pair = list()

index = 0
while len(nb_pair) < 10:
    if index % 2 == 0:
        nb_pair.append(index)
    index += 1

print(nb_pair)  
