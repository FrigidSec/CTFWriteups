# MEOWNETWORK

---
> A hacker managed to get into meownetwork and leaked sensitive files of their respected board members. The hacker uses ancient floppy disk technology, however our security team managed to get a disk image of the files he leaked. Can you find out what really leaked?

> Points: 300
---

The author seems to be obsessed with cats, as the title suggests.. XD
	
So we were given a disk image of the system, the size of that disk image was pretty less around 29 MB. 

As whenever we get the disk image we blindly fire up volatility...but wait this time we was just trapped..!! the **volatility tool could not find a profile image...**

Then we choose randomly some of the profiles from web to get some info about disk image but all of our efforts were in vain. we were stuck for around half 'n hour...

Then we thought of extracting files from the disk image, searched for various tools, came across various tools both in linux and windows but all just failed miserably!!
Then we came across the tool "bulk_extractor" a inbuilt tool in kali for extracting files from disk images along with associated emails and all stuffs..

It extracted some files from disk image but all were empty.. :(

Then we did some research again, came across tool "**foremost**" which also does the same thing along with it also extracts deleted files!
This time we was successful, it extracted a folder with jpg files in it, as we mentioned earlier, the author seems to be obsessed with cats, all the extracted images contained cats!!!

![](https://github.com/FrigidSec/CTFWriteups/blob/master/ASCWG/meownetwork/_docs/pics/1.jpg)
![](https://github.com/FrigidSec/CTFWriteups/blob/master/ASCWG/meownetwork/_docs/pics/2.jpg)

and 3 more like these.

Once again we used steghide to extract embedded things, but this time there was no passphrase required for that.. we got **5 text files containing long encoded strings in each of it**.. :(

It seemed liked base64 but didn't know what to do next. So one of our teammates suggested that the encoded strings from all the text files should be combined and then decode it as base64 as the intermediate files were starting with `/` and last file was ending with `==` padding, and damn that worked ! :)

`cat 1.txt 2.txt 3.txt 4.txt 5.txt >>newfile.txt`

`cat newfile.txt | base64 -d - >>image.jpg`

We got 1 more cat image :D -

![](https://github.com/FrigidSec/CTFWriteups/blob/master/ASCWG/meownetwork/_docs/pics/3.jpg)

Once more steghide maybe and Yep! it had something embedded..
we remembered the dialogue:"draw me like one of your French girls" From Titanic... so tried titanic as the passphrase, but it was wrong!

So we fired up **stegcracker**, till then kept researching on the film titanic..
But stegcracker did the work the passphrase was ***labeba***
and we got the flag after dealing with CATS!! 

**ASCWG{F10ppy\_d1$k!!\_th@t'$\_s0m3\_n0$t@1g!a\_stuFF}**

