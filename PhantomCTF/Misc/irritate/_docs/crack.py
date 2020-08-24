#X64MAYHEM
import base64 as bsf


data=""
with open("irritate","r") as f:
    data=f.read()

while(True):
    try:
        data=bsf.b64decode(data)
    except Exception:
        break;

print(data)


