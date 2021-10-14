def valid_ISBN10(isbn):
    x = 1
    s = 0
    l = [str(i) for i in isbn]    #生成l为isbn拆分为单个str格式
    if len(l)!=10:
        return False
    else:
        l = ['10' if i=='X' else i for i in l]   #列表中的把X替换为10
        test1 = [i.isdigit() for i in l]    #判断l中是否全为数字
        if sum(test1) == len(test1):    #判断l中是否全为数字
            test2 = [int(i) <= 9 for i in l[:-1]]    #判断前9位是否不含X
            if sum(test2) == len (test2):
                for i in l:
                    s = s+ int(i)*x
                    x+=1
                return s % 11 == 0
            else:
                return False
        else:
            return False

isbn = '1112223339'
print(valid_ISBN10(isbn))