### SherlocK
###### Description: This is an easy one. Have fun and read carefully. Evening is coming fast. Kids are playing. Enjoy the sun setting at the horizon. Your friends are right before you. I think they can be useful. Shirts wont help. Pants wont either, but their caps can. Enjoy with your friends. Please do the needful. Papa will be happy. Eventually, i also think words are your friends. Rest is your wish!

###### eGIU{kfdhydfjwigastz}

---

Looking at the initial letter of every word in the description, we get this-
```
T  his is an easy one.
H  ave fun and read carefully.
E  vening is coming fast.

K  ids are playing.
E  njoy the sun setting at the horizon.
Y  our friends are right before you.

I   think they can be useful. 
S  hirts wont help.

P  ants wont either, but their caps can.
E  njoy with your friends. 
P  lease do the needful. 
P  apa will be happy. 
E  ventually, i also think words are your friends. 
R  est is your wish!
```

So the key is pepper. But what cipher is it? It's obviously a substitution cipher since the given string still looks very much like a flag.
We didn't have to try too long. We found out that it's Vigenère cipher. Decoding it with the key 'pepper', we get the flag-

**pCTF{goodjobsherlock}**
