text = input()
pattern = input()

# Please write your code here.
def inpattern():
    is_pattern=-1
    for i in range(len(text)):
        if text[i]==pattern[0]:
            is_pattern=i
            for j in range(len(pattern)):
                if text[i+j]!=pattern[j]:
                    is_pattern=-1
                    break
            if is_pattern!=-1:
                break
    return is_pattern

print(inpattern())
