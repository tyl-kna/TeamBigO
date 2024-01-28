import ast

class Visitor(ast.NodeVisitor):
    def visit_Await(self, node):
        print('Node type: Await\nFields: ', node._fields)
        self.generic_visit(node)

    def visit_Call(self,node):
        print('Node type: Call\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Name(self,node):
        print('Node type: Name [ {} ]\nFields: '.format(node.id), node._fields)
        #print("ctx: ", node.ctx)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Attribute(self,node):
        print('Node type: Attribute\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Module(self,node):
        print('Node type: Module\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_ClassDef(self,node):
        print('Node type: Class Definition\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
    
    def visit_Import(self,node):
        print('Node type: Import\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
    
    def visit_FunctionDef(self,node):
        print('Node type: Function Definition\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
    
    def visit_Expr(self,node):
        print('Node type: Expression\nFields: ', node._fields)
        print('Value: ', node.value)
        ast.NodeVisitor.generic_visit(self, node)
        
    def visit_For(self,node):
        print('Node type: For Loop\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
    
    def visit_BinOp(self,node):
        print('Node type: Binary Operator')
        print('Left: ', node.left, '\nOperator: ', node.op ,'\nRight: ', node.right)
        ast.NodeVisitor.generic_visit(self, node)
    
    def visit_While(self,node):
        pass
        """print('Node type: While Loop\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)"""
            
    def visit_If(self,node):
        print('Node type: If Statement\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Break(self,node):
        print('Node type: Break\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Continue(self,node):
        print('Node type: Continue\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_AsyncFunctionDef(self,node):
        print('Node type: Async Function Definition\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Return(self,node):
        print('Node type: Return Statement\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Delete(self,node):
        print('Node type: Delete Statement\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_AugAssign(self,node):
        print('Node type: Augmented Assignement\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_With(self,node):
        print('Node type: With Block\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Try(self,node):
        print('Node type: Try Block\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Assert(self,node):
        print('Node type: Assert Statement\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Raise(self,node):
        print('Node type: Raise Exception\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Pass(self,node):
        print('Node type: Pass Statement\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_BoolOp(self,node):
        print('Node type: Boolean Operation\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_UnaryOp(self,node):
        print('Node type: Unary Operation\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Lambda(self,node):
        print('Node type: Lambda Expresion\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Dict(self,node):
        print('Node type: Dictionary\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Set(self,node):
        print('Node type: Set\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
    
    def visit_Compare(self,node):
        print('Node type: Comparison\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Subscript(self,node):
        print('Node type: Subscript\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_List(self,node):
        print('Node type: List\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Tuple(self,node):
        print('Node type: Tuple\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
            
    def visit_Slice(self,node):
        print('Node type: Slice\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)