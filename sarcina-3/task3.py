# Fisiere txt
originale = open('./originale.txt', 'r') 
really_shuffled = open('./really_shuffled.txt', 'r')

# Citire line by line
Lines = originale.readlines()
Lines2 = really_shuffled.readlines()


#Array cu fiecare cuvant din fisiere
originale_array=[]
really_shuffled_array = []
answer_array = []
#Parsing txts

for line in Lines: 
    originale_array.append(line.strip())

for line in Lines2: 
    really_shuffled_array.append(line.strip())

#Compare elements with each other

for y in really_shuffled_array:
    for x in originale_array:
        x_letters =  ''.join(sorted(list(x)))
        y_letters = ''.join(sorted(list(y)))

        if(x_letters == y_letters):
            print('Match Found:', x, y)
            answer_array.append(x)


seen = set()
result = []
for item in answer_array:
    if item not in seen:
        seen.add(item)
        result.append(item)


len(answer_array) != len(set(answer_array))
print(''.join(result))
