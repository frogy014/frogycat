n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def lcd(n):
    if n==1:
        return arr[0]
    a = lcd_a = lcd(n-1)
    while True:
        if lcd_a% arr[n-1]==0:
            return lcd_a
        lcd_a+=a    
print(lcd(n))