# waSTEGate

**Description: A CCTV near a wastegate has captured the image of the hacker behind the twitter scandal. FBI image forensic team has sent you the following attachment. Analyze and find the culprit.**

We were given a zip file which contained a png  file inside it. You can find the file [here](https://google.com)

After extracting the png, when we try to open it it popped up error: **Fatal error reading PNG image file : Not a PNG file**

**Blooper: First we thought that it had corrupted PNG headers, so we were fixing the headers of PNG, but it was not the case so!**

We wasted almost 15 minutes in just fixing the headers. So I checked the file format using the **file** command it gave this result:
**png.png: Zip archive data, at least v?[0x314] to extract** So it was a zip file!! :(

This time we fixed the corrupted header with the zip headers and changed the file extension to **zip**!! LOL!

The new zip file contained a directory in which there were two files: **cctv.jpeg and flagishere.txt**

We opened the **flagishere.txt**, but it was a **prank** it contained :**fakeflag{ju$7_k!d<>din}**

Now we were left with the **cctv.jpeg**, ran **steghide** without passphrase to extract the hidden file: **notflag.txt** which contained the flag!!

**pCTF{cL4rk_1v4N_<3_$}**


As we knew the Flag format **pCTF{}** so we just used **strings utility** to just dump all the strings present then piped it with **grep**to find the particular Flag format. This was just enough to get the flag out of that pcap file.


**pCTF{sh4rk_1n_th3_w1r3}**

