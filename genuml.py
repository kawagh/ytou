import subprocess

SOURCE_CODE = """
print("Hi")
print("Hey")
"""

output_file = "out.pu"
with open(output_file, "w") as f:
    f.write("@startuml\n")
    f.write("start\n")
    f.write(":Hi;\n")
    f.write(":Hey;\n")
    f.write("stop\n")
    f.write("@enduml")
subprocess.call(["plantuml", output_file])
