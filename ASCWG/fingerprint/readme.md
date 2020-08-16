# FINGERPRINT [FORENSIC]

We were provided with 7 images which included 6 jpg and 1 png format.

There wasn’t any clue in the images, so lets dig into actual forensics 	part.

First of all, I checked all the jpg images with steghide and the png 	image with zteg to check whether something is embedded in the images 	or not? All the images contained some embedded things in it, which 	required a passphrase to discover.. :(

Then just manually checked all the images with strings utility, hoping to 	get something interesting out of the images. YEP! I got an encoded 	string out of the image named 3.jpg.
	
The padding at the end of the string pointed to direction of base64 	encoding. 

The base64 decoding of the string, gave a hex encoded output, then decoded that hex to get a string which indicated it as rar file, so I saved it as rar file.	 


The rar file we saved was password protected!! There was no clue for the password in any of the metadata or strings in any of the images..

So extracted the password protected rar hash using rar2john, then fired up JTR to crack the password hash using the rockyou.txt wordlist and boom the password was cracked: “komputer” and we got the flag! 

"ASCWG{F0Ren$ics_I$_Fun_;)}" - Yeah its fun!!!


