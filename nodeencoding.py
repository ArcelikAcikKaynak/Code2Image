# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:35:45 2019

@author: ebilzek

This script encodes tokens into numerical tuples.
"""

def map(a):
    if a.__class__.__name__ == 'FuncDef' :
        return [255, 0, 0] 
    elif a.__class__.__name__ == 'Decl' :
        return [0, 255, 0]
    elif a.__class__.__name__ == 'FuncDecl' :
        return [15, 0, 0]
    elif a.__class__.__name__ == 'TypeDecl' :
        return [128, 128, 128]
    elif a.__class__.__name__ == 'IdentifierType' :
        if a.names == ['string']:
            return [25, 110, 0]
        elif a.names == ['char']:
            return [25, 120, 0]
        elif a.names == ['int']:
            return [25, 130, 0] 
        elif a.names == ['float']:
            return [25, 140, 0]
        elif a.names == ['short'] :
            return [25, 100, 10]
        elif a.names == ['short','int']:
            return [25, 130, 10]
        elif a.names == ['unsigned','short','int']:
            return [25, 90, 10]
        elif a.names == ['unsigned', 'short'] :
            return [25, 90, 10]
        elif a.names == ['long']:
            return [25, 100, 20]
        elif a.names == ['long','int']:
            return [25, 130, 20]
        elif a.names == ['unsigned', 'long', 'int']:
            return [25, 90, 20]
        elif a.names == ['unsigned', 'long']:
            return [25, 90, 20]
        elif a.names == ['signed', 'long', 'int']:
            return [25, 160, 20]
        elif a.names == ['long','long']:
            return [25, 160, 60]
        elif a.names == ['long','long','int']:
            return [25, 160, 60]
        elif a.names == ['unsigned', 'int']:
            return [25, 90, 15]
        elif a.names == ['void']:
            return [25, 128, 128]
        elif a.names == ['unsigned','char']:
            return [25, 90, 30]
        elif a.names == ['unsigned','string']:
            return [25, 90, 40]
        elif a.names == ['unsigned','float']:
            return [25, 90, 50]
        elif a.names == ['signed', 'float']:
            return [25, 160, 50]
        elif a.names == ['signed','char']:
            return [25, 160, 30]
        elif a.names == ['signed','string']:
            return [25, 160, 40]
        elif a.names == ['signed', 'int']:
            return [25, 160, 70]
        elif a.names == ['unsigned','int']:
            return [25, 90, 70]
        elif a.names == ['signed', 'short']:
            return [25, 160, 10]
        elif a.names == ['signed', 'long']:
            return [25, 160, 20] 
        else:
            return [25, 80, 80]
    elif a.__class__.__name__ == 'Compound' :
        return [0, 0, 255]
    elif a.__class__.__name__ == 'Constant' :
        try:
            if a.type == "string":
                return [35, 10, 0]
            elif a.type == "char":
                return [35, 20, 0]
            elif a.type == "int":
                return [35, 30, min(int(a.value), 255)] 
            elif a.type == "float":
                return [35, 40, min(int(a.value), 255)]  
            elif a.type == "unsigned short" or a.type == "unsigned short int":
                return [35, 90, min(int(a.value), 255)]                  
            elif a.type == "short" or a.type == "short int" or a.type == "signed short int":
                return [35, 160, min(int(a.value), 255)]
            elif a.type == "unsigned long" or a.type == "unsigned long int":
                return [35, 70, min(int(a.value), 255)] 
            elif a.type == "long" or a.type == "long int" or a.type == "signed long int":
                return [35, 80, min(int(a.value), 255)] 
            elif a.type == "long long" or a.type == "long long int":
                return [35, 100, min(int(a.value), 255)]
            elif a.type == "unsigned int":
                return [35, 90, min(int(a.value), 255)] 
            else:
                return [35, 110, 0] 
        except ValueError :
            return [35, 120, 0]             
    elif a.__class__.__name__ == 'FuncCall'  :
        return [40, 128, 0] 
    elif a.__class__.__name__ == 'ID'  :
        if a.name == 'NULL':
            return [45, 10, 128] 
        elif a.name == 'printf':
            return [45, 20, 128] 
        else:
            return [45, 0, 128]  
    elif a.__class__.__name__ == 'ArrayDecl'  :
        return [50, 0, 0]  
    elif a.__class__.__name__ == 'ArrayRef' :
        return [55, 0, 0]  
    elif a.__class__.__name__ == 'Assignment'  :
        if a.op == '=':
            return [60, 20, 0]  
        elif a.op == '+=':
            return [60, 40, 0] 
        elif a.op == '-=':
            return [60, 60, 0] 
        elif a.op == '*=':
            return [60, 80, 0] 
        elif a.op == '/=':
            return [60, 100, 0] 
        elif a.op == '%=':
            return [60, 120, 0] 
        elif a.op == '<<=':
            return [60, 140, 0] 
        elif a.op == '>>=':
            return [60, 160, 0] 
        elif a.op == '&=':
            return [60, 180, 0] 
        elif a.op == '^=':
            return [60, 200, 0] 
        elif a.op == '|=':
            return [60, 220, 0]
        else:
            return [60, 240, 0] 
    elif a.__class__.__name__ == 'BinaryOp'  :
        if a.op == '<':
            return [65, 0, 10]
        if a.op == '>':
            return [65, 0, 20]
        if a.op == '<=':
            return [65, 0, 30]
        if a.op == '>=':
            return [65, 0, 40]
        if a.op == '==':
            return [65, 0, 50]
        if a.op == '!=':
            return [65, 0, 60]
        if a.op == '-':
            return [65, 0, 70]
        if a.op == '+':
            return [65, 0, 80]
        if a.op == '*':
            return [65, 0, 90]
        if a.op == '/':
            return [65, 0, 100]
        if a.op == '%':
            return [65, 0, 110]
        if a.op == '<<':
            return [65, 0, 120]
        if a.op == '>>':
            return [65, 0, 130]
        if a.op == '&':
            return [65, 0, 140]
        if a.op == '|':
            return [65, 0, 150]
        if a.op == '^':
            return [65, 0, 160]
        if a.op == '&&':
            return [65, 0, 170]
        if a.op == '||':
            return [65, 0, 180]
        else:
            return [65, 0, 190]
    elif a.__class__.__name__ == 'Break' :
        return [70, 0, 0] 
    elif a.__class__.__name__ == 'Case'  :
        return [75, 0, 0]  
    elif a.__class__.__name__ == 'Cast' :
        return [80, 0, 0]  
    elif a.__class__.__name__ == 'CompoundLiteral'  :
        return [85, 0, 0] 
    elif a.__class__.__name__ == 'Continue' :
        return [90, 0, 0] 
    elif a.__class__.__name__ == 'DeclList'  :
        return [95, 0, 0]   
    elif a.__class__.__name__ == 'Default'  :
        return [100, 0, 0] 
    elif a.__class__.__name__ == 'DoWhile'  :
        return [105, 0, 0]  
    elif a.__class__.__name__ == 'EllipsisParam'  :
        return [110, 0, 0] 
    elif a.__class__.__name__ == 'EmptyStatement'  :
        return [115, 0, 0]  
    elif a.__class__.__name__ == 'Enum'  :
        return [120, 0, 0]  
    elif a.__class__.__name__ == 'Enumerator'  :
        return [125, 0, 0]   
    elif a.__class__.__name__ == 'EnumeratorList'  :
        return [130, 0, 0]   
    elif a.__class__.__name__ == 'For' :
        return [135, 0, 0]   
    elif a.__class__.__name__ == 'Goto'  :
        return [140, 0, 0]   
    elif a.__class__.__name__ == 'If'  :
        return [145, 0, 0]   
    elif a.__class__.__name__ == 'InitList'  :
        return [150, 0, 0]  
    elif a.__class__.__name__ == 'Label'  :
        return [155, 0, 0]   
    elif a.__class__.__name__ == 'NamedInitializer'  :
        return [160, 0, 0] 
    elif a.__class__.__name__ == 'ParamList'  :
        return [165, 0, 0]   
    elif a.__class__.__name__ == 'PtrDecl'  :
        return [170, 0, 0]   
    elif a.__class__.__name__ == 'Return'  :
        return [175, 0, 0]   
    elif a.__class__.__name__ == 'Struct'  :
        return [180, 0, 0]   
    elif a.__class__.__name__ == 'Switch'  :
        return [185, 0, 0]   
    elif a.__class__.__name__ == 'TernaryOp'  :
        return [190, 0, 0]  
    elif a.__class__.__name__ == 'Typedef'  :
        return [195, 0, 0]  
    elif a.__class__.__name__ == 'Typename'  :
        return [200, 0, 0]   
    elif a.__class__.__name__ == 'UnaryOp'  :
        if a.op == '-':
            return [205, 20, 0]  
        elif a.op == '*':
            return [205, 40, 0]   
        elif a.op == '!':
            return [205, 60, 0]  
        elif a.op == '++':
            return [205, 80, 0]  
        elif a.op == '--':
            return [205, 100, 0]  
        elif a.op == '&':
            return [205, 120, 0]  
        elif a.op == 'p++':
            return [205, 140, 0]  
        elif a.op == 'p--':
            return [205, 160, 0]  
        else:
            return [205, 180, 0]   
    elif a.__class__.__name__ == 'Union'  :
        return [210, 0, 0]  
    elif a.__class__.__name__ == 'While'  :
        return [215, 0, 0]  
    elif a.__class__.__name__ == 'Pragma' :
        return [220, 0, 0]   
    elif a.__class__.__name__ == 'ExprList' :
        return [225, 0, 0]   
    elif a.__class__.__name__ == 'StructRef' :
        if a.type == '->':
            return [230, 25, 0]  
        elif a.type == '.':
            return [230, 50, 0]  
        else:
            return [230, 75, 0]  
    else:
        return [235, 0, 0] 