import ast
import subprocess

from process_stmt import handle_assign, handle_if, handle_stmt

OPERATOR_MAP: dict[ast.AST, str] = {ast.Eq: "=="}


def main():
    with open("./ifelsesrc.py", "r") as f:
        c = f.read()

    p = ast.parse(c)
    print(c)
    output_file = "out.pu"
    with open(output_file, "w") as f:

        f.write("@startuml\n")
        f.write("start\n")

        for stmt in p.body:
            handle_stmt(stmt, f)

        f.write("stop\n")
        f.write("@enduml")
    subprocess.call(["plantuml", output_file])


if __name__ == "__main__":
    main()
