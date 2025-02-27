def fun():
    print("AAA")
    def f():
        print("CCC")
    print("BBB")
    return f
print(fun())
