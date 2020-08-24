# Secret (Reverse Engineering)

In this we were given a `.pyc` file which is a clear sign for python binary.

Interesting thing with python binaries are that we can de-compile them pretty easily.


## Step 1

I used `uncompyle6` to decompile the binary ..

we get the following source code :

```python
def kraitrot(input, d):
    Lf = input[0:d]
    Ls = input[d:]
    return Ls + Lf


def cobraverse(s):
    g = ''
    g += s[1::2]
    g += s[0::2]
    return g


def vipershift(s):
    g = ''
    for i in range(len(s)):
        a = hex(ord(s[i]) + 20)[2:]
        g += a

    return g


s3rc3t = input("Enter the secret to get access to python's cave : ")
if len(s3rc3t) < 28:
    print('Add little more weight :::\n')
else:
    if vipershift(cobraverse(kraitrot(s3rc3t, 15))) == '867387738d7c8284688f454745737c4488894784884491575a807a738787':
        print("\nWhy does Python live on land?\nBecause it's above C-level . XD!! \nCongrats for the flag anyways")
    else:
        print('Maybe a python bit you , better luck next time :((')

```


### Understanding Functions.

In this instead of creating a one shot script, I solved this by reversing the logic one by one in the python3 interpreter.

let's see the functions 


#### kraitrot(str,int)

Given :

```python
def kraitrot(input, d):
    Lf = input[0:d]
    Ls = input[d:]
    return Ls + Lf

```

this functions splits the input from the position given and then reverse the whole block

eg:

```
input str => abcdef
input int => 2

output str => cdefab

```

so that's easy to reverse just change `input int`  to `len(str)-input int` so this will give us the original string.
eg:

```
input str => cdefab
input int => 6-2=4

output str => abcdef
``` 

So that's easy enough.

#### cobraverse(s)

```python
def cobraverse(s):
    g = ''
    g += s[1::2]
    g += s[0::2]
    return g
```

so this is also easy, it's using `step` in `extended string splice` in python3 so this means this is first taking 2nd char and then concat. all the chars in 2nd step.

eg : `abcdef -> bdf`

and then do the same with remaining by setting the initial pointer at 0th element i.e 1st char

so overall working :

```
input string => abcdefgh

output string => bdfhaceg
```

This is also easy to reverse and I did this by dividing the elements in 2 different array and then concatinating their alternate elements

```python
def reversecobra(a,b):
    for i in range(0,len(a)):
        print(b[i],end='')
        print(a[i],end='')
```

#### vipershift(s)

this function takes string, then takes each char and then adds `20` to it and then convert the overall result to hex and remove the `0x` part with `[2:]` split.

so this is also simple to reverse,

just do

```python3
chr(int(hexblock,base=16)-20)
```

### FLAG

by using all the small snipnets above we can reverse the comparision string given in the code.

`vipershift(cobraverse(kraitrot(flag, 15))) = 867387738d7c8284688f454745737c4488894784884491575a807a738787`

reverse will be 

`kraitrot(reversecobra(reverseviper('867387738d7c8284688f454745737c4488894784884491575a807a738787')),int(30)-15) = pCTF{l1f3_1s_sh0rt_us3_pyth0n} "`

so flag = **pCTF{l1f3\_1s\_sh0rt\_us3\_pyth0n}**


DIY :)  Download the same binary [HERE](./_docs)
