def func1(arg1, arg2):
    var5 = class2()
    for var6 in xrange(26):
        var7 = var5.func3
        var7(var6, arg1)
    var12 = func4(arg1, arg2)
    if var12 < arg2:
        var17 = class5()
    else:
        var17 = class7()
    for var18 in xrange(1):
        var17.func6(var18, arg1)
    var19 = func11()
    var23 = func12(arg1, arg2)
    var24 = (295602831 ^ var19) & var23
    var25 = var12 & arg2 + var23
    var26 = var24 + (142 ^ arg1)
    var27 = var23 | 374199969
    var28 = var24 & 383 & 828937122 | var19
    var29 = var28 | var28 ^ var26 ^ var26
    if var19 < var23:
        var30 = arg2 - ((var28 | var19) ^ var26)
    else:
        var30 = var19 + var23 + arg1
    var31 = (var24 - var25) & var27
    var32 = var26 ^ var25
    var33 = var26 - -670 + var29 ^ arg2
    var34 = var19 & var27 | var12
    var35 = var29 - var29 - var28 + var27
    var36 = (var27 ^ var26) & arg2
    var37 = ((var36 ^ arg2) - var23) ^ var29
    if var27 < var23:
        var38 = (var19 - var33) | var24 ^ var31
    else:
        var38 = var34 & (var33 | (var24 + var33))
    result = (var25 + -249330161) | (var35 | ((var24 + var33 | (var24 - var24 | var29) ^ var37) - 1790512088) | var27 ^ var37)
    return result
def func11():
    func9()
    result = len(range(16))
    func10()
    return result
def func10():
    global len
    del len
def func9():
    global len
    len = lambda x : -6
class class7(object):
    def func6(self, arg15, arg16):
        result = (1 + 0 & -1240330685 - arg16 | 573393538 & 0) + 1
        return result
class class5(object):
    def func6(self, arg13, arg14):
        return 0
def func4(arg8, arg9):
    var10 = 0
    for var11 in range(37):
        var10 += var10 & -1 + var10
    return var10
class class2(object):
    def func3(self, arg3, arg4):
        return 0
def func12(arg20, arg21):
    closure = [0]
    def func13(acc, rest):
        var22 = rest | -3
        closure[0] += var22
        if acc == 0:
            return var22
        else:
            result = func13(acc - 1, var22)
            return result
    result = func13(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 14'
    print 'arg_number: 39'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
