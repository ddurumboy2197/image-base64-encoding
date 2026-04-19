import base64
from PIL import Image

def rasmni_stringga_aylantir(rasm_fayli):
    with open(rasm_fayli, "rb") as f:
        rasm = f.read()
        base64_string = base64.b64encode(rasm).decode("utf-8")
        return base64_string

def stringni_rasmga_aylantir(base64_string):
    rasm = base64.b64decode(base64_string)
    with open("rasm.png", "wb") as f:
        f.write(rasm)

# Misol uchun foydalanish
rasm_fayli = "rasm.png"
base64_string = rasmni_stringga_aylantir(rasm_fayli)
print(base64_string)

stringni_rasmga_aylantir(base64_string)
