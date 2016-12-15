import inspect
def get_current_function_name():
    # print(inspect.stack())
    for va in inspect.stack() :
        for v in va:
            if inspect.isframe(v):
                print(v.f_locals)
            # else:
            #     print('v == ',v)
    return inspect.stack()[1][3]

# class MyClass:
#     def function_one(self):
#         print("%s.%s invoked"%(self.__class__.__name__, get_current_function_name()))
# if __name__ == "__main__":
#     myclass = MyClass()
#     myclass.function_one()
#
#     print(dir(inspect))
import sys
def add(x:int,y:int):
    z = x+y
    w=10
    get_current_function_name()
    # print(dir(sys))
    # print(sys.thread_info)
    return z
add(4,2)