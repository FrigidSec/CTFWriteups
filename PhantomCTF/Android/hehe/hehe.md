# hehe.apk (Android)

This was one of the baby android challenges. We can solve this in just 5 min.

### Step 1
We get an APK file in the challenge zip.

![](./_docs/a1.png)

### Step 2 
Decompile the apk with apktool

![](./_docs/a2.png)


###  Step 3
This can vary depending on the challenge, but we just searched for any string matching "flag" and got interesting results

![](./_docs/a3.png)


### Step 4

After quick analysis of the [SMALI](https://stackoverflow.com/questions/30837450/what-is-smali-code-android) file we can see that the app is using base64 on a hardcoded string we can try to just decode it


![](./_docs/a4.png)
### Step 5 

Searching for the string in the file and then decoding it, gave us the flag.

![](./_docs/a5.png)

![](./_docs/a6.png)
**pCTF{7hr0w_4aPpl3_fr0m_w1nDoW}**
