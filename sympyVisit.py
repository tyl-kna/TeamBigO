import ast
from ForMath import *

global multiplier
global total

multiplier = str(1) ## For nested 'For' loops
total = str(0)

def findS(nodeVal):
    if (isinstance(nodeVal, ast.Constant)):
        s = nodeVal.value
    elif (isinstance(nodeVal, ast.Name)):
        s = nodeVal.id
    else:
        s = 1
    return s

def Calculate(start, stop, step): # Temporary function, stand-in for real SymPy function
    if (stop-start) % step == 0:
        return ( (stop-start) // step ) + 1
    else: # Remainder > 0
        return ( (stop-start) // step ) + 2

class Visitor(ast.NodeVisitor):
    
    def visit_Call(self,node):
        print('Node type: Call')
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Name(self,node):
        global total
        global multiplier
        print('Node type: Name [ {} ]'.format(node.id))
        #print("ctx: ", node.ctx)
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Module(self,node):
        print('Node type: Module')
        ast.NodeVisitor.generic_visit(self, node)

    def visit_ClassDef(self,node):
        global total
        global multiplier
        print('Node type: Class Definition')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
    
    def visit_Import(self,node):
        global total
        global multiplier
        print('Node type: Import')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
    
    def visit_FunctionDef(self,node):
        global total
        global multiplier
        print('Node type: Function Definition')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
    
    def visit_Expr(self,node):
        print('Node type: Expression')
        ast.NodeVisitor.generic_visit(self, node)
        
    def visit_For(self,node):
        global total
        global multiplier
        print('Node type: For Loop')
        #ast.NodeVisitor.generic_visit(self, node)
        if( len(node.iter.args) == 1 ):
            start = 0
            stop = findS(node.iter.args[0])
            step = 1
        elif( len(node.iter.args) == 2):
            start = findS(node.iter.args[0])
            stop = findS(node.iter.args[1])
            step = 1
        else:
            start = findS(node.iter.args[0])
            stop = findS(node.iter.args[1])
            step = findS(node.iter.args[2])
        tempComplexity = ForComplexity([start, stop, step])
        
        print("Previous Multiplier: ", multiplier)
        multiplier = MulExp(multiplier, SubVal(tempComplexity, "1"))
        #multiplier *= (tempComplexity - 1)
        print("Current Multiplier: ", multiplier)
        
        for x in node.body:
            ast.NodeVisitor.visit(self, x)

        multiplier = DivExp(multiplier, SubVal(tempComplexity, "1"))
        # multiplier /= (tempComplexity - 1)
        print("Multiplier after loop: ", multiplier)
        
        print("Total before loop: ", total)
        total = AddExp(total, MulExp(tempComplexity, multiplier))
        #total += (tempComplexity * multiplier)
        print("Total after loop: ", total)
    
    def visit_BinOp(self,node):
        global total
        global multiplier
        print('Node type: Binary Operator')
        print('Left: ', node.left, '\nOperator: ', node.op ,'\nRight: ', node.right)
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
    
    def visit_While(self,node):
        # WhileFlag = True
        pass
        """print('Node type: While Loop\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)"""
            
    def visit_If(self,node):
        global total
        global multiplier
        print('Node type: If Statement')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Break(self,node):
        global total
        global multiplier
        print('Node type: Break')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Continue(self,node):
        global total
        global multiplier
        print('Node type: Continue')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Return(self,node):
        global total
        global multiplier
        print('Node type: Return Statement')
        print("Previous total: ", total)
        total = AddExp(total, "1")
        #total += 1
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Delete(self,node):
        global total
        global multiplier
        print('Node type: Delete Statement')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_AugAssign(self,node):
        global total
        global multiplier
        print('Node type: Augmented Assignement')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_With(self,node):
        global total
        global multiplier
        print('Node type: With Block')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Try(self,node):
        global total
        global multiplier
        print('Node type: Try Block')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Assert(self,node):
        global total
        global multiplier
        print('Node type: Assert Statement')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Raise(self,node):
        global total
        global multiplier
        print('Node type: Raise Exception')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Pass(self,node):
        global total
        global multiplier
        print('Node type: Pass Statement')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_BoolOp(self,node):
        global total
        global multiplier
        print('Node type: Boolean Operation')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_UnaryOp(self,node):
        global total
        global multiplier
        print('Node type: Unary Operation')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Dict(self,node):
        global total
        global multiplier
        print('Node type: Dictionary')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Set(self,node):
        global total
        global multiplier
        print('Node type: Set')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
    
    def visit_Compare(self,node):
        global total
        global multiplier
        print('Node type: Comparison')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Subscript(self,node):
        global total
        global multiplier
        print('Node type: Subscript')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_List(self,node):
        global total
        global multiplier
        print('Node type: List')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Tuple(self,node):
        global total
        global multiplier
        print('Node type: Tuple')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Slice(self,node):
        global total
        global multiplier
        print('Node type: Slice')
        print("Previous total: ", total)
        total = AddExp(total, multiplier)
        #total += multiplier
        print("Current total: ", total)
        ast.NodeVisitor.generic_visit(self, node)