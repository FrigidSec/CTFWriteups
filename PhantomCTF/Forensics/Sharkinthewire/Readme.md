# Sharkinthewire

**Description: We intercepted unencrypted com and dont have any guy to analyse it please find for us**

We were given a tar file which had a pcap file inside it. You can find the file [here](https://google.com)

**Golden Tip: Don't just fireup wireshark everytime when you have the pcap file. Many challenges can be solved without any Network Packet Analyzer**

As we knew the Flag format **pCTF{}** so we just used **strings utility** to just dump all the strings present then piped it with **grep**to find the particular Flag format. This was just enough to get the flag out of that pcap file.


**pCTF{sh4rk_1n_th3_w1r3}**

