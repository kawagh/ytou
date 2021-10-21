import ast
from typing import Any

from icecream import ic

OPERATOR_MAP: dict[Any, str] = {ast.Eq: "=="}


def main():

    with open("./src.py", "r") as f:
        c = f.read()
        print(c)
        p = ast.parse(c)
        d = ast.dump(p, indent=4)

    # print(d)

    for stmt in p.body:
        print(stmt)
        if isinstance(stmt, ast.Assign):
            pass
            # ic(stmt.value.__dict__["value"])
            # var_value = stmt.value.__dict__["value"]
            # ic(stmt.__dict__)
            # var_name = stmt.__dict__["targets"][0].__dict__["id"]
            # print(var_name, var_value)
        elif isinstance(stmt, ast.If):
            pass

        else:
            raise NotImplementedError()


def handle_assign(stmt, f):
    """
    単一代入文
    """
    # TOOD 複数代入の処理
    var_name = getattr(getattr(stmt, "targets")[0], "id")
    var_value = getattr(stmt.value, "value")
    f.write(f":{var_name}={var_value};\n")


def handle_if(stmt, f):
    """
    test: expr
    body: typing.List[stmt]
    orelse: typing.List[stmt]
    """
    test = getattr(stmt, "test")
    body = getattr(stmt, "body")
    orelse = getattr(stmt, "orelse")

    var_name = getattr(test.left, "id")
    ops = getattr(test, "ops")
    # ic(ops[0].__class__)
    op: str = OPERATOR_MAP[ops[0].__class__]
    compartors = getattr(test, "comparators")
    compartor_value = getattr(compartors[0], "value")

    f.write(f"if ({var_name} {op} {compartor_value}) then(true)\n")
    for body_i in body:
        if isinstance(body_i, ast.Assign):
            handle_assign(body_i, f)
        elif isinstance(body_i, ast.If):
            handle_if(body_i, f)
        else:
            raise NotImplementedError()
            # handle_body()?

    # TODO process orelse

    f.write("endif\n")


if __name__ == "__main__":
    main()
