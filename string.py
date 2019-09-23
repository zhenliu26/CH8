def is_reverse(word1,word2):
    if(len(word1)==len(word2)):
        i=0
        j=len(word2)-1
        while(j>-1):
            if word1[i]!=word2[j]:
                return False
            i=i+1
            j=j-1
        return True
    else:
        return False
'''
fruit="apple"
print len(fruit)
print fruit[1:-1]
greeting="hello"
letter=greeting[:]
print(letter)


str="banana"
index=0
while index<len(str):
    print(str[index])
    index=index+1


letter="LB"
suffix="ike"
for i in letter:
    print(i+suffix)

for jelly in range(5):# stop at 0,1,2,3
    print(jelly)
list1=('monday',5,list('asda'))
for i in list1:
    print i

print str(65)

str1="Mary"
str2="mac"
str2="hello"
print(str1.lower()<str2.lower())
greeting= "hello, world"# string is immutable
newgreeting='J'+greeting[1:]
print newgreeting
'''


word='Zanzibar'
count=0
for letter in word.lower():
    if letter =='z':
        count=count+1
print count

