# with open("textfile.txt") as file:
#     print(file)
# I dont have clarity about files concept.so I tried in another way to print the words which are less than 5 charecters.


str = input("enter a sentence: ")
#str = "python is a programming language"
list= str.split()
print(list)
length = len(list)
#print(length)
for i in list:
     
    if len(i)<5:
        print(i)