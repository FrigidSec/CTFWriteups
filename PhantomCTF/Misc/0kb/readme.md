# 0kb (Misc)

Here we get a rar archive.

## Step 1

Extracting the rar file gives us the `modibaba.txt` file which is zero KB file and actually do not contain anything.

## Step 2

on close inspection we see that the `7z x ` command in linux gives us an error that there is a problem with the archive and it cannot extract `modibaba.txt:hidden` file.

And this is our biggest clue on what's actually the case with this file.

## Step 3 

This file is actually created by good 'ol notepad trick from late 2000 i think.

Last time i read about it was in 2010 and it was fun...

actually there is a command that we can pass in windows that will cerate a new file discriptor and channel for the file and the actual data is written there.

to get the flag :

* open this in windows VM
* issue following command
`type modibaba.txt:hidden`
* and we will get our flag

## Flag

 
flag{baba\_jika\_thullu\_flag} 

 
