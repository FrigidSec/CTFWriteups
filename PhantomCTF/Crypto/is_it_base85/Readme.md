# is_it_base85(Crypto)
The file for this challenge u can find it [here](https://github.com/FrigidSec/CTFWriteups/blob/master/PhantomCTF/Crypto/is_it_base85/is_it_base85)

The name of this challenge suggested that the cipher is base85 encoded. But take a moment to think .. that the organizers would make that look so easy? No !!It is not a Sanity check or welcome challenge!!

So I went through the ctf-katana Framework, where it stated that Malbolge(an esoteric language) looks like base85 encoded.

I copied that cipher and pasted in this [Malbolge decoder](http://www.malbolge.doleczek.pl/) which popped out the flag:

**pCTF{Its_r3411y_D4nt3s_H3ll}**

