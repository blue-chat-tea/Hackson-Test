def add(a,b):
    return a+b

a,b=(int(x) for x in input('2つの整数をスペース区切りで入力してください:').split())

c=add(a,b)

print(str(a),'+',str(b),'=',str(c))