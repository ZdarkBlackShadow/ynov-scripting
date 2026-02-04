import tempfile
import os
import time

def function_name():
    with tempfile.NamedTemporaryFile(mode="w+", delete=True, encoding="utf-8") as fp:
        print(f"Fichier crée : {fp.name}\n")

        fp.write("test\ntest")

        fp.seek(0)
        time.sleep(600)
        print("test")
        print(f"> {fp.read()}\n")

function_name()