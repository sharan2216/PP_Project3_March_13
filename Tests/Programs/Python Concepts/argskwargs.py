# def meth(*args):
#     tot = 0
#     for i in args:
#         tot = tot + i
#     print(tot)
#
#
# meth(11)

def meth2(**kwargs):
    res=[]
    for key,value in kwargs.items():
        res.append("{} has {}".format(key,value))

    print(res)

meth2(google="java",micro="python")