# FINGERPRINT [FORENSIC]
---
> Can You Spoof My Finger Print ???

> Points : 300

---

**We were provided with 7 images which included 6 jpg and 1 png format**. You can find them [HERE](https://github.com/FrigidSec/CTFWriteups/tree/master/ASCWG/fingerprint/_docs/chal_images)

There wasn’t any clue in the images, so lets dig into actual forensics part.

First of all, we checked all the jpg images with *steghide* and the png image with *zteg* to check whether something is embedded in the images or not. 
All the images contained some embedded things in it, which required a passphrase to discover.. :(


Then just manually checked all the images with *strings* utility, hoping to get something interesting out of the images. 
> YEP! we got an B64 encoded string out of the image named 3.jpg.
	
The padding at the end of the string pointed to direction of base64 encoding. 
![](https://raw.githubusercontent.com/FrigidSec/CTFWriteups/master/ASCWG/fingerprint/_docs/ss/1.png)
The base64 decoding of the string, gave a hex encoded output, then decoded that hex to get a set of gibbris hraw output which had RAR header signature in it, so rar file it was, so we saved it as rar file.
![](https://github.com/FrigidSec/CTFWriteups/blob/master/ASCWG/fingerprint/_docs/ss/2.png)

The rar file we saved was password protected!! There was no clue for the password in any of the metadata or strings in any of the images..

So **extracted the password protected rar hash using rar2john**, then fired up *JTR to crack* the password hash using the *rockyou.txt* wordlist and boom the password was cracked: **komputer** and we got the flag! 

"**ASCWG{F0Ren$ics_I$_Fun_;)}**"
