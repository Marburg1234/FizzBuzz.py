#5&3の倍数=FizzBuzz
#5の倍数=Fizz
#3の倍数=Buzz

input_number = input('任意の数字を入力してください： ')
number = int(input_number)

if number % 15 == 0:
    print('FizzBuzz')
elif number % 5 == 0:
    print('Fizz')
elif number % 3 == 0:
    print('Buzz')
else:
    print('5と3どちらでも割り切れない数字です')


money = 1000
items = {"みかん": 500, "りんご": 500}

print(items)

for item in items:
    input_count = input('個数を選んでください： ')
    count = int(input_count)
    price = count * items[item]
    print(f"金額は{price}円です")
    if money >= price: 
        money -= price
        print('購入しました')
        print(f"残りの所持金は{money}円です")
    elif money == price:
        money -= price
        print("所持金は0円になりました")
    else:
        print("所持金が足りず購入できませんでした")
