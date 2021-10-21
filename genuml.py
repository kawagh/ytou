import ast
import subprocess

from process_stmt import handle_assign


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
                vname, vvalue = handle_assign(stmt)
                f.write(f":{vname}={vvalue};\n")
            else:
                raise NotImplementedError()

        f.write("stop\n")
        f.write("@enduml")
    subprocess.call(["plantuml", output_file])


if __name__ == "__main__":
    main()
