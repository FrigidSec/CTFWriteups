# Memory 3


![](https://github.com/FrigidSec/CTFWriteups/blob/master/FwordCTF/Forensics/Memory/Images/Memory3.png)

**This time I have read the description carefully :)**

**The main thing is that the hardwork I did for previous challenge for finding the ZIP file was not wasted LOL**

So we don't have to do any bruteforce for finding the ZIP Password

**Where to look for password??** I did filescan on that disk image to find if any important file where the zip password could be..but I couldn't find anything useful.

Then I thought of checking the web chats of the channel! so this time I just used **strings** on disk image and used **grep** to print only strings related to :
**FwordCTF{top_secret_channel}** and BOOM! we got the zip password : **fw0rdsecretp4ss**
Unlocked the ZIP and got the flag!!

![](https://github.com/FrigidSec/CTFWriteups/blob/master/FwordCTF/Forensics/Memory/Images/flag1.png)
