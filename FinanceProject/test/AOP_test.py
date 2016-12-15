class pyAOP(type):
    def nop(cls):
        print('test')
    beforeop = nop
    afterop  = nop

    @classmethod
    def setbefore(cls,func):
        pyAOP.beforeop = func
    @classmethod
    def setafter(cls,func):
        pyAOP.afterop = func
    def __new__(mcl,name,bases,dict):
        from types import FunctionType
        obj = object()
        def AOP(func):
            def wrapper(*args,**kwargs):
                pyAOP.beforeop(obj)
                value = func(*args,**kwargs)
                pyAOP.afterop(obj)
                return value
            return wrapper
        for attr,value in dict.iteritems():
            if isinstance(value,FunctionType):
                dict[attr] = AOP(value)
        obj = super(pyAOP,mcl).__new__(mcl,name,bases,dict)
        return obj


class A(object):
    __metaclass__ = pyAOP
    def foo(self):
        total = 0
        for i in range(100000):
            total += 1
        print(total)
    def foo2(self):
        from time import sleep
        total = 0
        for i in range(1000):
            total += 1
            sleep(0.0001)
        print(total)

def beforep():
    print('before')
def afterp():
    print('after')
if __name__ == '__main__':
    pyAOP.setbefore(beforep)
    pyAOP.setafter(afterp)
    a = A()
    a.foo()
    a.foo2()
