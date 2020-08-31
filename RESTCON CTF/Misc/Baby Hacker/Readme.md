# Baby Hacker

![](./Images/BabyHacker.png)


After reading the description with hint mentioned, I started looking for some blogs about the recent crypto scams! I came across various blogs but it didn't helped me much..

So I kept going through the description for about 3-5 times..then I focused on the point mentioned in the description **also a member of ResetHacker Community** so I started going through the discord server,I found some interesting username **smile_hacker_** which just gave the idea of the hacker mentioned in the description **hacker who will make you smile** Gotcha!

So I started looking for **smile_hacker_** over the various social media..I came across the twitter handler **_smile_hacker_** !

![](./Images/smilehackertwitter.png)

You can see that he also has his own website [smilehacker.me](http://smilehacker.me/)

After going through the website,I didn't find anything interesting..so I jumped on to the website's source code and boom I encountered with some **cipher** in the comment!

I can't paste that cipher over here as it was very much long.It starts with something like this **LVstLS0tLS0tPis8XT4rLisrKysrKysrLi0tLS0tLS4tLS0tLi0uK1srKz4tLS0tLTxdPisuKysrK......**

This cipher includes series of different cipher decrytptions..
**Base64 -> BrainFuck -> Base32 -> Base64 -> BrainFuck**

Finally you will get something like this : **QDRSBNM{j33O^^G4bj!mF_jDDDDDo_rlHKdddmF}** It looks like we need to rotate it ..
After rotating for 27 rounds we will get our Flag!

**RESTCON{k33P^^H4ck!nG_kEEEEEp_smILeeenG}**


