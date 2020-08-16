---
layout: post
title: ASCWG CTF Check Writeup  
tags:
  - CTF Writeups
  - CTF
  - FrigidSec
---

<div class="message">
Writeup of Reverse Engineering Challenge of Arab Security Cyber WarGames.

Points : 300
</div>

### Background
Just a file `check` with no discription. Who gives discription for reverse challanges anyways?

that being said let's dive into writeup.

This was fairly easy challange.

### Solving

First we just did `strings` but found nothing and will see why that's the case with this chal later.

#### Running for first time

![](/assets/images/check/1.png)

ok that being done let's move to next part.

#### IDA Static Analysis

Just searching for the strings `checking machine...` we got our main function.


![](/assets/images/check/2.png)

here we can see lots of strings being stored in the stack. okay let's trace more..


![](/assets/images/check/3.png)

So now we see some new data being loaded to the stack and then passing at arguments to some function..


![](/assets/images/check/4.png)

#### The XOR function
![]()
So the above function is just an xor function which XORs the passed data with preset key, in our case `87h` which can be seen here :


![](/assets/images/check/5.png)

yes i have renamed the variables to make it easy to understand..

then the function returns back to main... so let's follow...

#### XOR minefield
The whole main function is then followed by the same scheme,

1. Load data
2. XOR with preset key 

and all the functions are also simple like above.

so let's keep this in mind and moveon...

#### `_getenv` 
this name is enough to understand what this is trying to do...

![](/assets/images/check/6.png)

So now you see what it does?

Lemme explain...

1. Take DATA 
2. XOR with key 
3. GET SYSTEM ENVIORNMENT VARIABLE with same decoded name
4. then XOR one more value 
5. Check this value with the obtained value from envvar
6. Do this for 2 different env. vars and if they match then show the flag.

the flag is loaded as a chunk of data in the start, and yes it's also XORed with `92h` as key.

#### Get the flag.

so there are now three ways to get the flag.

1. Decode the env. var and values and then run the binary
2. Decode flag directly from stack
3. JUST DO BINARY PATCHING AND CHANGE LAST 2 `if statement` to change the program flow

##### Decode everythin' XORmayhem

Here is a small python script to do what program is doing

```python
env1a=[0xd3,0xd4,0xc8,0xcf]
env1a.reverse()
env1b=[0xc2,0xca,0xc6,0xc9]
env1b.reverse()
env1=env1a+env1b

env2=[0xc3,0xd4,0xc2,0xc4]
env2.reverse()

envvar1valueA=[0xfe,0xf5,0xf7,0xdb]
envvar1valueA.reverse()
envvar1valueB=[0xf3,0xf8,0xff]
envvar1valueB.reverse()
envvar1value=envvar1valueA+envvar1valueB

envvar2valueA=[0xf7,0xfc,0xfc,0xeb]
envvar2valueA.reverse()
envvar2valueB=[0xfc,0xf7,0xfe,0xf0]
envvar2valueB.reverse()

envvar2value=envvar2valueA+envvar2valueB

flagA=[0xd6,0xdc,0xc4,0xc3]
flagB=[0xa5,0xf6,0xa2,0xc4]
flagC=[0xa0,0xa7,0xa0,0xdf]
flagD=[0xa2,0xcb,0xa1,0xca]
flagE=[0xf4,0xc4,0xf8,0xf1]
flagF=[0xe8,0xdb,0xda,0xdc]
flagG=[0xa3,0xc7,0xa1,0xca]
flagH=[0xa3,0xc8,0xa0,0xdf]
flagI=[0xaf,0xa2,0xda,0xf0]

flagA.reverse()
flagB.reverse()
flagC.reverse()
flagD.reverse()
flagE.reverse()
flagF.reverse()
flagG.reverse()
flagH.reverse()
flagI.reverse()

flag=flagA+flagB+flagC+flagD+flagE+flagF+flagG+flagH+flagI

print("envVar1 = ",end=' ')
for i in env1:
    print(chr(int(i)^int('87',base=16)),end="")

print()

print("envVar1 Value = ",end=' ')
for i in envvar1value:
    print(chr(int(i)^int('96',base=16)),end="")

print()


print("envVar2 = ",end=' ')
for i in env2:
    
    print(chr(int(i)^int('91',base=16)),end="")
    
print()


print("envVar2 Value = ",end=' ')
for i in envvar2value:
    
    print(chr(int(i)^int('99',base=16)),end="")

print()
print("flag = ",end=' ')
for i in flag:
    print(chr(int(i)^int('92',base=16)),end="")

print()
```
The above script will give you all the enviornment variables and the flag too as it is also XORed lol....


![](/assets/images/check/7.png)

and then just export these values in the env. vars to get the flag.

![](/assets/images/check/8.png)


#### My FAV binary patching ! (solve in 5 min)

Just see this ... 


![](/assets/images/check/9.png)

`74` -> `75` i.e. `JZ` -> `JNZ` just do this in two places and the program will give you all its secrets without any pain...


![](/assets/images/check/10.png)


Binary patching can be intimidating for some... check these articles out for some idea and how to do it at basic level as you should be good to go for this one. :)

[Use VIM as HEX editor like a boss](/article/2020/08/16/use-VIM-as-HEX-Editor.html)

[Taking over a software by Instruction Rewriting.](/article/2019/11/25/Taking-over-a-software-by-Instruction-Rewriting.html)


### Conclusion 

So we have the flag in `base64` format, by any of the above method.

we just need to decode it and it's pretty easy with is neat pipe trick:

`echo "QVNDV0d7M252X3Y0cjVfNHIzX3U1M2Z1bH0=" | base64 -d -` 

This will give the flag

**ASCWG{3nv\_v4r5\_4r3\_u53ful}**

---

