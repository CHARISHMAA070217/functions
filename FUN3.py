///
def fun1():
    print("AAA")
def fun2():
    print("BBB")
def fun3(a,b):
    print("CCC")
    a()
    b()
fun3(fun1,fun2)

    OUTPUT:
CCC
AAA
BBB
///
