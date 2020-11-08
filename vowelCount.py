checkingSentence = input('Enter the sentence you want to check : ').lower()
list1 = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in checkingSentence :
    if i in list1 :
        count += 1
print('Vowels Letter in the given sentence is', count)