#複数のデータを扱おう→Pythonではリストと呼ぶ Rubyの配列のこと
foods = ['pasta', 'curry', 'sushi']
print(foods)

print('0番を出力')
print(foods[0])
print('好きな食べ物は' + foods[2] + 'です')

#リストの要素を更新しよう
print('0番をUdonに更新し出力する')
foods[0] = 'Udon'
print(foods)

#リストに要素を追加しよう
print('リストに要素を追加する append')
foods.append('pizza')
print(foods)

#繰り返し処理 for文を使ってみよう
print('forで繰り返し処理してみよう')
for food in foods:
    print(food + 'が大好きです')

#辞書について
#Pythonの辞書とは、複数のデータをまとめて管理できる キーと値が1セットになったもの
print('Rubyのハッシュを、Pythonでは辞書と言う')
print('Rubyの配列を、Pythonではリストと言う')

user = {'name': 'Suzuki', 'age': 18, 'country': 'Japan'}
print(user)

user['region'] = 'Tokyo'
user['name'] = 'Yamada'
print(user)

#辞書の要素をすべて取得しよう
fruits = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
for fruit in fruits:
    print(fruit + 'の色は' + fruits[fruit] + 'です')


#while文 指定した条件に合致するまで処理を実行する
x = 1
while x <= 5: #末尾の:コロンを忘れずに
    print(x)
    x += 1

#指定した条件になったとき強制終了する break
numbers = [159, 249, 777, 157, 9999]
for number in numbers:
    print(number)

print('breakを使い777が出たら処理をとめる')
for number in numbers:
    print(number)
    if number == 777:
        break

#ある条件の時に繰り返し処理をスキップすることもできる continue
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 3 == 0:
        continue
    print(number)

#お買い物プログラムを作っていこう
#商品メニューを用意する
money = 1000
items = {'apple': 100, 'banana': 200, 'orange':400}

print(items['apple'])
print(items)
for item_name, item_price in items.items():
    print(f"{item_name}は{item_price}円です") #f"~" は、文字列に自動で変換してくれる
    

#メニュー内容を1つずつ取り出す
for item_name in items:
    print("--------------------------")
    print(item_name + "は1個" + str(items[item_name]) + "円です")

#個数を入力してもらうのと支払い金額まで表示する
    #個数入力機能を作る
    input_count = input('購入する' + 'item_name' + 'の個数を入力してください： ')
    print('購入する' + item_name + 'の個数は' + input_count + '個です')
    #支払い金額を表示する
    total_price = int(input_count) * items[item_name]
    print('小計：' + str(total_price))

    #支払い金額の計算と表示は以下でも可能
    count = int(input_count)
    total_price = count * items[item_name]
    print('合計金額は' + str(total_price) + '円です')

    #所持金のmoney変数を追加　計算して足りるときと、たりないときで表示内容を変える
    if money >= total_price:
        print(item_name + 'を' + str(items[item_name]) + '個買いました') 
        money = money - total_price #所持金(money)から金額を引いて、所持金(money)の値を更新する
        if money == 0:
            print('財布が空になりました')    
    else:
        print('お金が足りず、' + item_name + 'を買えません')
    print('残金は' + str(money) + '円です')
