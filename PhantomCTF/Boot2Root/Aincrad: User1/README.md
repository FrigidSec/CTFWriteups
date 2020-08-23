### Aincrad: User1
###### Description: Hello Hackers We are RATH we got an old sao server running .Hack you way in.

###### aincrad.cybsec.in

###### NOTE:- 22PORT IS OUT OF SCOPE SO DONT WASTE TIME PLEASE NO DIRBUST AND BRUTEFORCE. IT IS NOT REQUIRED. THE MACHINE IS JUST EXPERIMENTAL SO IT WILL RESET EVERY 1 HOUR JUST VOTE IN THE RESPECTIVE DISCORD FOR RESETS.

---
Once we got the shell using one of the 2 methods described in the Aincrad: Foothold writeup, we could just enumerate a little bit. Going to `/home/` showed us home directories for 2 users: `argenestel` and `kirito`.

Trying to `cd` into argenestel's home directory did not work. We didn't have the permissions.
However, we could `cd` into kirito's home directory.

Going into his `Desktop` folder, we noticed 2 files, `creds.txt` and `kirito.txt`.

`cat kirito.txt` gave us the flag:

**pCTF{N3v3r_l3v3e_pa4ss}**
