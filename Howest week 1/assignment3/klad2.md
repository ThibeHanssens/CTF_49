**Slide 1: The discovery**
Tor is a distributed system designed around the principle of **Segmentation of Knowledge.**.
In July 2014, the Tor Project discovered a massive, sophisticated attack on its network. Which led to a targeted effort to de-anonymize thousands of users.
(optional if time: "Which eventually led to their nickname, Dark Web")

**Slide 2: VPN vs Tor**
In a standard network, like a VPN, the provider knows both your IP address and where you are going. Tor’s entire goal is to ensure that no single entity ever possesses both of those pieces of information at the same time.
(Dus een slide met VPN vs TOR, en bij VPN zie je IP -> where you are going, en bij Tor toon je op slide dat ze nooit samen geweten worden)

**Slide 3: Volunteer network**
This TOR-system is powered by a global network of volunteers. Currently, about 7,000 relays are run by individuals and organizations worldwide. Anyone can contribute bandwidth, which makes the network resilient, but also introduces certain risks.

**Slide 4: 3 hops**
A standard Tor-connection bounces through three random hops. While there are several roles in this process, for this specific attack, we highlight 2 specific nodes: the **Entry Guard** and the **HSDir**.

**Slide 5: The Entry Guard**
The **Entry Guard** is the only node in the entire chain that knows your **real IP address**.
->  because of the network's design, the entry guard has no idea what website you are actually visiting.

**Slide 6: The HSDir**
The **HSDir**, or Hidden Service Directory, knows where a .onion site is physically located on the internet, but it doesn't know the identity of the person asking for it. -> so it has no idea who is actually visiting the site

**Slide 7: Privacy gap**
Privacy exists in the "gap" between the Entry Guard and the HSDir. As long as these two nodes aren't talking to each other, the user stays anonymous.
The attack that we're talking about, was specifically designed to bridge that gap.
(show the entry guard and the HSDir on the same slide, and design it so it's easy to explain)

**Slide 8:**
Beginning in January 2014, a mysterious group began contributing massive amounts of bandwidth to the network. They launched around **115 high-speed relays**, which was around 6,4% of the guard bandwidth of the Tor infrastructure. 

**Slide 9: The exploit**
That same group exploited a protocol involving specific **control packets** that were used for building circuits.
These attackers realized they could repurpose these control packets to send a hidden tags through the encrypted layers of the onion.

**Slide 10: Tagging the data**
When a user requested a .onion site hosted by an attacker’s HSDir, the attacker put a tag the data.
They marked the traffic with a specific pattern of control packets as it traveled back to the user. .

**Slide 11:**
Because Tor is encrypted, middle nodes couldn't see the "ink." But if that same user happened to be using one of the **Entry Guards** also hosted by an attacker, that Entry Guard could see the tag -> matching up both ends of the circuit

**Slide 12:**
By matching the tag seen at the HSDir with the tag seen at the Guard, the attackers successfully linked a specific **IP address** to a specific **.onion site**. For those users, the segmentation of knowledge was officially broken.

**Slide 13: Sybil attack**
To make this work at scale, they used a **Sybil Attack**. This is when an attacker creates a massive number of fake identities (in this case, 115 relays) to gain a disproportionate and dangerous amount of influence over the network.

**Slide 14: 6.4% capacity**
By contributing **6.4% of the network’s total capacity**, the attackers ensured they were mathematically likely to be both the Guard and the HSDir for thousands of users every single day. 

**Slide 15: patched**
The Tor Project discovered the rogue nodes in July 2014 and immediately kicked them off. They released a patch that strictly limited how those "Relay Early" control packets could be used, closing the loophole for good.

**Slide 16: But, who?**
After the discovery, a huge number of users felt exposed. They wanted to know who had spent five months spying on them. For a while, the identity of the attackers remained a total mystery. We simply didn't know.

**Slide 17: Research group**
Then, they noticed something. A talk at the **Black Hat conference** by researchers from **Carnegie Mellon University** was abruptly canceled by their legal team -> and he topic was A low-cost way to de-anonymize Tor users...

**Slide 18: drug markets**
The connection became undeniable during Operation Onymous, a massive global crackdown of **illegal Tor sites**. While Silk Road 2.0 was the biggest headline, law enforcement initially wouldn't admit how they had bypassed Tor’s layers to locate the hidden servers.
OF:
The connection became undeniable during the trials for **Silk Road 2.0**, a major illegal drug market.
Law enforcement had successfully found the site’s operators, but they initially wouldn't admit how they did it.

**Slide 19**
Eventually, court documents eventually revealed the truth: The **FBI** had paid an "academic institution" at least **$1 million** for the data.
This data was used to arrest operators of multiple illegal marketplaces across the Tor network.
OF
Eventually, court documents revealed the truth: The **FBI** had paid an "academic institution" at least $1 million for the data. This led to the seizure of hundreds of sites, including marketplaces like Cloud 9, Hydra, and Blue Sky.

**Slide 20: lesje ofz?**
Good remindeedn the strongest encryption can be defeated by logical exploits. blablabla
(ending hier schrijven, of misschien ergens anders een slide extra doen ofz indien nodig idk)