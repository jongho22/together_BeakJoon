word_list = []

for _ in range(5) :
    line = []
    words = input()
    for char in words :
        line.append(char)
    word_list.append(line)

#print(word_list)
max = len(word_list[0])
for i in word_list :
    if len(i)>max :
        max = len(i)
    #print(len(i))

for i in range(max) :
    for list in word_list :
        try :
            print(list[i],end="")
        except :
            pass
