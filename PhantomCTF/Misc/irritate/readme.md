# Irritate (Misc.)

We get a 7z archive with as file named same as the challenge (~77 MB)


### Step 1

The file is a long chunk of string to printing all would mess up terminal so we can use `head and tail` to see start and end of the string

### Step 2

`cat irritate | head` Gave us :

```sh
x64mayhem$ cat irritate | head
Vm0wd2QyUXlVWGxWV0d4V1YwZDRWMVl3WkRSV01WbDNXa1JTVjAxV2JETlhhMUpUVmpBeFYySkVU
bGhoTVVwVVZtcEJlRll5U2tWVQpiR2hvVFZWd1ZWWnRjRUpsUmxsNVUydFdWUXBpUjJodlZGWldk
MVpXV25SalJVcHNVbXhzTlZVeWRGZFdVWEJwVWpKb2RsWkdXbGRrCk1WcFhWMjVTYWxKVmNITlZi
WGh6VGxaVmVXUkdaRmRWV0VKd1ZXcEtiMlJzV2tkWGJHUnJDazFXY0ZoV01qVlRZV3hLVm1OSVRs
WmkKV0doNlZHeGFWbVZYVWtkYVJtUldWMFZLZDFaWGNFdGlNbEp6VjJ0a1dHSkhVbkpEYXpGWFkw
Wm9WMDFxVmxSWlYzaExWbTFPU1ZScwpXbWtLVjBkb05sWkhlR0ZXYlZaWVZXdGtZVkp0VWxkV01G
WkxaREZhV0dORmRHbE5iRXA2VmpKMGExZEhTa2hWYmtwRVlYcEdXRmt3CldtOVdNREZ4Vm14U1ds
WXphRXhXYlRGUFUxWlNjd3BYYld0TFZqQmtiMDVzV2tobFIwWlhZbFphV1ZaWGRHdFpWa3AwVld4
a1YwMUcKV2t4YVJFWmhWMGRPUm1SSGJFNWlSWEEyVm1wS01HRXhaRWhUYTJoV1ltdHdSVmxZY0Vk
WFJtdDNDbGR0T1ZkTlJFWjRWbTE0VTFkcwpXWHBoUlhoWFlsUkdVRlV4V2xOamQzQllZbGQwVEZa
x64mayhem$ 
``` 
`cat irritate | tail` Gave us:

```sh
x64mayhem$ cat irritate | tail
a3B3ClZXcEdTMWxXWkZWUmJYUnBUVlpXTkZkclZtOWhSa3AwWlVac1YySlVSbE5hUkVaclZqRndS
MXBIY0U1aE0wSkhWbXBLTkZSM2NHaFYKV0VKVVZGWldkMDVHV1hnS1drUkNhVTFWVmpSV1IzUnJW
MGRLYzFOdVJtRldNMUpvVmpGYVYyUkhVa2xhUm1ST1ZqTlJlbFp0TUhkTwpWbGwzVFZoS2FsSlhh
RmRVVnpWU1RVWmtWMWRzY0d4aVJrcDRWbGQ0YXdwVWJFcDFVV3N4VjJGcldtaERiVkY0VTI1S1Qx
WnRVbTlWCmJYTXhWMVpXYzFadVpGWmhNRFY2VmpJMVUxUnNXa1pUYkdoRVlsVlpNbFZ0ZUc5WGJV
VjRZMGhLV2xZemFFeGFSV1JIQ2xOV1RuTlgKYld4VFRXMW9WbFp0ZUZkV01WRjVWRmhzVkZkSVFu
QlVWV2hUVmpGYWNWUnRPRXRaTW5oWFkyeHdSbHBGT1dsU1ZuQTBWbTB4TkdFeApXWGROU0dSVVlY
cEdXRmxzVWtZS1RVWldObE5yT1dwTldFSktWVzE0VTJGV1NuVlJiRlpZVm14S1NGcEhNVmRXTVdS
elYxVjBWMDF1ClVuSlpWRXBMVW14T2MxUnNjR2xpVkd0NlZsUk9hMlJuY0ZGVlZ6ZzVRMmM5UFFv
PQo=
x64mayhem$ 

```

> Note that `=` pad at the end.. seems like this is a base64 or 32 encoded data.


### Step 3 

Decoding the data with `cat irritate | base64 -d -` gave us one more base64 string.

> So this is Recursive base64 data.

### Step 4

For this I made the following python3 script to do this..

Logic is to keep decoding until we get a `BaseError` this will tell us that it cannot be decoded further and then print that data

```python
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
```

running this gave us the flag

```sh
x64mayhem$ python3 crack.py 
b'pCTF{1s_it_5t1ll_h4ck4ble}\n'

```

### FLAG

**pCTF{1s\_it\_5t1ll\_h4ck4ble}**

##### NOTE 
All the are available in [\_docs](./_docs) folder.


