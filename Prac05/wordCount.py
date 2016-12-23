__author__ = 'jc451073'

string = input(" Enter your text: ")
list = string.split()
count = {}
for j in list:
    count[j]=list.count(j)

for key in count:
    print("{}: {}".format(key,count[key]))
