import ast

from icecream import ic


def main():

    with open("./src.py", "r") as f:
        c = f.read()
        print(c)
        p = ast.parse(c)
        d = ast.dump(p, indent=4)

    print(d)

    for stmt in p.body:
        print(stmt)
        if isinstance(stmt, ast.Assign):
            vname, vvalue = handle_assign(stmt)
            ic(vname, vvalue)
            # ic(stmt.value.__dict__["value"])
            # var_value = stmt.value.__dict__["value"]
            # ic(stmt.__dict__)
            # var_name = stmt.__dict__["targets"][0].__dict__["id"]
            # print(var_name, var_value)
        else:
            raise NotImplementedError()


def handle_assign(stmt):
    """
    単一代入文
    """
    var_value = stmt.value.__dict__["value"]
    var_name = stmt.__dict__["targets"][0].__dict__["id"]
    return var_name, var_value


if __name__ == "__main__":
    main()
