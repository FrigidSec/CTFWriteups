# MEOWNETWORK

---
> A hacker managed to get into meownetwork and leaked sensitive files of their respected board members. The hacker uses ancient floppy disk technology, however our security team managed to get a disk image of the files he leaked. Can you find out what really leaked?

> Points: 300
---

The author seems to be obsessed with cats, as the title suggests.. XD
	
So we were given a disk image of the system, the size of that disk image was pretty less around 29 MB. 

As whenever we get the disk image we blindly fire up volatility...but wait this time we was just trapped..!! the volatility tool could not find a profile image...

Then we choose randomly some of the profiles from web to get some info about disk image but all my efforts were in vain. I was stuck for around half n hour...

Then I thought of extracting files from the disk image, searched for various tools, came across various tools both in linux and windows but all just failed miserably!!
Then I came across the tool "bulk_extractor" a inbuilt tool in kali for extracting files from disk images along with associated emails and all stuffs..

It extracted some files from disk image but all were empty.. :(

Then I did some research again, came across tool “foremost” which also does the same thing along with it also extracts deleted files!
This time I was successful, it extracted a folder with jpg files in it, as I mentioned earlier, the author seems to be obsessed with cats, all the extracted images contained cats!!!

![]()
![]()

and 3 more like these.

Once again I used steghide to extract embedded things, but this time there was no passphrase required for that.. we got *5 text files* containing long encoded strings in each of it.. :(

It seemed liked base64 but didn’t know what to do next. So one of our teammates suggested that the encoded strings from all the text files should be combined and then decode it as base64, and damn that worked ! :)

We got 1 more cat image :D -

![]()

Once more steghide maybe and Yep! it had something embedded..
I remembered the dialogue:"draw me like one of your French girls" From Titanic... so tried titanic as the passphrase, but it was wrong!

So I fired up stegcracker, till then kept researching on the film titanic..
But stegcracker did the work the passphrase was ***labeba***
and we got the flag after dealing with CATS!! 

ASCWG{F10ppy_d1$k!!_th@t'$_s0m3_n0$t@1g!a_stuFF}

