# Memory 2

![](https://github.com/FrigidSec/CTFWriteups/blob/master/FwordCTF/Forensics/Memory/Images/Memory2.png)

**KEYNOTE: Read the CHALLENGE DESCRIPTION CAREFULLY**

**I also need to follow this above KEYNOTE**  :)

So when I read the first line of the decription I directly hoped over for volatility using **chromehistory** plugin because I knew that there was **googlechrome.exe**!!

**I didn't bothered to read the next line of challenge description which had consequences later :(**

Okay I didn't had the **chromehistory** plugin for volatility so I cloned it from [here](https://github.com/superponible/volatility-plugins)

![](https://github.com/FrigidSec/CTFWriteups/blob/master/FwordCTF/Forensics/Memory/Images/5.png)

We can see the **GO File Link** : **https://gofile.io/d/k2RkIS**! So I just went to the website there was one zip file, I downloaded it! The ZIP file was password 
protected! I extracted the password hash using **zip2john** and fired up the **JTR** to crack the hash!!

**OKAY here is the twist!! As I said I should also follow the KEYNOTE I messed up with the challenge description!!**

We were needed to find the channel on which they were chatting....**So gentle reminder again! Please read the challenge description carefully**

Okay again going through the chromehistory I found the website where they were chatting : **https://webchat.freenode.net/**

**Now how to get the channel name???** Then I thought of dumping the internet cache so I came across the **yarascan** plugin of **volatility**. 
YARA is a rule name, where these rules consist of sets of strings and a boolean expression.As we know the expression of the flag **FwordCTF{** we could actually use this
to get the channel name. We knew the time stamps for **webchat** so we should dump the **chrome cache** whose **process id** was around that **timestamp**

![](https://github.com/FrigidSec/CTFWriteups/blob/master/FwordCTF/Forensics/Memory/Images/6.png)

So we got the channel name as our flag:

**FwordCTF{top_secret_channel}**
