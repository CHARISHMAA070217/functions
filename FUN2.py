///
def fun1():
    print("AAA")
def fun2():
    print("BBB")
def fun3(a,b):
    print("CCC")
    print(a)
    print(b)
fun1()
fun2()
fun3(fun1,fun2)

    OUTPUT:
AAA
BBB
CCC
<function fun1 at 0x05B5B610>
<function fun2 at 0x05B5B658>
///
