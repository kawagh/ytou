import ast
import subprocess

from process_stmt import handle_assign, handle_if

OPERATOR_MAP: dict[ast.AST, str] = {ast.Eq: "=="}


def main():
    with open("./src.py", "r") as f:
        c = f.read()

    p = ast.parse(c)
    print(c)
    output_file = "out.pu"
    with open(output_file, "w") as f:

        f.write("@startuml\n")
        f.write("start\n")

        for stmt in p.body:
            if isinstance(stmt, ast.Assign):
                handle_assign(stmt, f)
            elif isinstance(stmt, ast.If):
                handle_if(stmt, f)
            else:
                raise NotImplementedError()

        f.write("stop\n")
        f.write("@enduml")
    subprocess.call(["plantuml", output_file])


if __name__ == "__main__":
    main()
