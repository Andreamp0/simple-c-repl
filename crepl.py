import os
import subprocess
import tempfile
import readline

st = """#include <stdio.h>
int main(void)
{
"""

en = """
}"""

ib = []

while True:
    new = (input('>>> '))
    match new:
        case ":reset":
            ib = []
            continue
        case ":pcode":
            print(st+"\n".join(ib)+en)
            continue
        case "":
            continue
        case ":quit":
            break
    ib.append(new)
    with tempfile.TemporaryDirectory() as tmp:
        comp = subprocess.run(["clang", "-Wall", "-Wextra", "-Wno-unused", "-std=c23", "-pedantic", "-o", os.path.join(tmp, "main"), "-x", "c", "-"], input=st+"\n".join(ib)+en, capture_output=True, text=True)
        print(comp.stderr)
        if comp.returncode == 0:
            results = subprocess.run([os.path.join(tmp, "main")], capture_output=True, text=True)
            print(results.stdout)
        else:
            ib.pop()
        
