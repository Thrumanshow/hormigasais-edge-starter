import sys
import shutil

required_tools = ["bash", "python3", "git"]
missing = [tool for tool in required_tools if shutil.which(tool) is None]

if missing:
    print(f"FAIL: Faltan herramientas requeridas: {', '.join(missing)}")
    sys.exit(1)

print("OK: Entorno de laboratorio compatible (Bash, Python3, Git detectados).")
sys.exit(0)
