word1 = input()
word2 = input()

# Please write your code here.
is_same='Yes'
if len(word1)!=len(word2):
    is_same='No'
else:
    sort_word1 = sorted(list(word1))
    sort_word2 = sorted(list(word2))
    for i in range(len(word1)):
        if sort_word1[i]!=sort_word2[i]:
            is_same='No'
            break
print(is_same)