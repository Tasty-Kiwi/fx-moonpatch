import sys, json, re
from subprocess import Popen, PIPE

class CompilerError(Exception):
    """Raised if moonc compiler sends an stderr signal."""
    pass

# Based on https://regexr.com/33jqd
REGEX_FX = r"([-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*)(?:[eE][+-]?\d+)?)fx"
REGEX_FUNC = r"fx\(([-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*)(?:[eE][+-]?\d+)?)\)"

with open("config.json") as f:
    config = json.load(f)
    config_dir = config["moonc_path"]

if len(sys.argv) < 2 or sys.argv[1] == "help":
    print(
        f"Moonpatch, the fx patch for moonc",
        f"USAGE: {sys.argv[0]} FILENAME",
        '\n',
        f"moonc path: {config_dir}",
        "Change it in config.json.",

        sep='\n'
    )
else:
    filename = sys.argv[1]
    print(f"[INFO] Reading {filename}")

    with open(filename, "r") as f:
        content = f.read()

    print("[INFO] 1fx -> fx(1)")
    first_conversion = re.sub(REGEX_FX, r"fx(\1)", content)
    print("[INFO] Conversion successful.")
    #print(shit)

    #exit(0)
    p = Popen([f"{config_dir}", "--"], stdout=PIPE, stdin=PIPE, stderr=PIPE, encoding="utf8")
    stdout, stderr = p.communicate(input=first_conversion)
    if stderr:
        raise CompilerError(stderr)

    print("[INFO] moonc: compiled successfully.")

    print("[INFO] fx(1) -> 1fx")
    second_conversion = re.sub(REGEX_FUNC, r"\1fx", stdout)
    print("[INFO] Conversion successful.")

    with open(f"{filename}.lua", "w") as f:
        f.write(second_conversion)

    print("[INFO] Successfully finished.")
