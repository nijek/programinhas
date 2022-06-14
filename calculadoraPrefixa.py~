#TODO: verificar os inputs, verificar o caso () e tratar as exceções, colocar a possibilidade de definir variáveis e funções 



operators = {'+' : lambda x, y: x + y, '-' : lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y, '^' : lambda x, y: x ** y} 

def read_expr ():
    s = input("> ")
    aux = []  
    s = list(s)
    i = 0
    while i in range (len(s)):
        if s[i].isdigit():
            #negativos
            if s[i - 1] == '-':
                num = aux.pop() + s[i]
            else:    
                num = s[i]
            i = i + 1
            while s[i].isdigit() or s[i] == '.':
                num = num + s[i]
                i = i + 1    
            aux.append(num)    
        
        elif s[i] != ' ':
            aux.append(s[i])
            i = i + 1
        else: 
            i = i + 1
    return analize(aux)


def analize(expr):
    
    hasPar = True #tem Parentesis  
    while hasPar:
        left, right, i = 0, 0, 0
        hasPar = False
        for ch in expr:
            if ch == '(':
                hasPar = True
                left = i
            elif ch == ')':
                right = i
                result = calculate(expr[left + 1:right])    
                expr = (expr[0:left]) + [result] + expr[right + 1:]
                break
            i = i + 1
    return(expr)

def calculate(expr):
    operands = []
    if expr[0] and expr[0] in operators.keys():
        operatorFun = operators[expr[0]]
        expr = expr[1:]
    else:
        return expr[0] 
    return operate(expr, operatorFun)

def operate (nums, operator):
    res = float(nums[0])
    for num in nums[1:]:
        res = operator(res, float(num))
    return res
    
while True:
    print(read_expr())




