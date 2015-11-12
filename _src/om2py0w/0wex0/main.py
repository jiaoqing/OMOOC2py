import os
#导入模块名 os.py 

def main():
	print "hello world"
	print "这是Alice\的问候"
    print '这是 Bob\' 的问候'

    foo(5,10) #调用函数，函数的声明在后面

    print '='*10   #字符可乘 等于 ’===============‘
    print '这将直接执行'+os.getcwd()  #调用了 os 模块中得函式

    counter = 0  
    counter +=1 #变量得先实例化才可进一步计算

    food = ['苹果','杏子'，'李子'，'梨子']
    for i in food:
    	print '我就爱吃'+i
    #单行语句块，其实不可以换行的，但是，建议清晰起点，规范点：另起一行， 缩进一级。

    print "数到10"
    for i in range(1,10):
    	print i  
    #range()内置函式，返回类似[0,1,2,3,4,5,6,7,8,9] 的数字列表，注意for in 循环语句使用冒号声明



    def foo(param1, secondParam):  # 函数式声明，注意使用冒号结束x声明
    	res = param1 + secondParam 
    	print '%s 加 %s 等于 %s'%(param1, secondParam, param1+secondParam)
    if res < 50: 
    	print '这个'
    elif (res >= 50) and((param1 == 42) or (secondParam == 24)):
    	print '那个'
    else:
    	print "嗯......"
    return res    
    ''' 这个是多行
    注释''' 

  代码分支


    	