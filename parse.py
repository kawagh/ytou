import ast

d = ast.dump(ast.parse("for i in range(10): print(i)"))
print(d)
print(type(d))
