def greet():
    print("こんにちは")


f = greet   # ( ) を付けないので、関数そのものを f に入れる
f()         # f を呼び出すと greet が実行される
