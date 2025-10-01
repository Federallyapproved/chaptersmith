---
{
  "id": "chapter-154",
  "title": "WAN Technologies",
  "order": 154,
  "source": {
    "href": "c12.xhtml",
    "anchor": "head-2-241"
  },
  "est_tokens": 838,
  "slug": "wan-technologies",
  "meta": {
    "nav_title": "WAN Technologies",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## WAN Technologies

Wide area network links are used to connect distant networks, nodes, or individual devices together. A WAN link can improve communications and efficiency, but it can also place data at risk. Proper connection management and transmission encryption is needed for a secure connection, especially over public network links. WAN links and long-distance connection technologies can be divided into two primary categories: dedicated and nondedicated.

A dedicated line (also called a leased line or point-to-point link ) is one that is continually reserved for use by a specific customer. A dedicated line is always on and waiting for traffic to be transmitted over it. The link between the customer's LAN and the dedicated WAN link is always open and established. A dedicated line connects two specific endpoints and only those two endpoints. This type of connection is often used between multiple business locations, so they can effectively communicate as a single entity.

There have been numerous types of dedicated lines over the years, ranging from the T1 (telephone line 1 with 1.54 Mbps capacity) to T3 or DS3 (Digital Service 3 with 44.7 Mbps capacity). Other options included X.25, Asynchronous Transfer Mode (ATM), and Frame Relay. These technologies have mostly been replaced by fiber optic–based solutions.

Cable TV–based internet service does not fit well into either the dedicated or the nondedicated classification. Cable internet is an always-on system, but not between two client locations. Instead, it is a link from your premises to an internet gateway. Thus, it can be labeled as a point-to-multipoint connection. Another wrinkle is that cable internet service is also typically a shared service with the other subscribers in the neighborhood. Privacy is maintained through encryption, similar to a VPN, from the cable modem deployed at your location to an exit point in the cable company's network, typically immediately connected to the internet gateway.

A nondedicated line is one that requires a connection to be established before data transmission can occur. A nondedicated line can be used to connect with any remote system that uses the same type of nondedicated line.

# Fault Tolerance with Carrier Network Connections

To obtain fault tolerance with leased lines or with connections to carrier networks, you must deploy two redundant connections. For even greater redundancy, you should purchase the connections from two different telcos or service providers. However, when you're using two different service providers, be sure they don't connect to the same regional backbone or share any major pipeline. The physical location of multiple communication lines leading from your building is also of concern because a single disaster or human error (e.g., a misguided backhoe) could cause multiple lines to fail at once. If you cannot afford to deploy an exact duplicate of your primary dedicated leased line, consider a nondedicated connection. These less expensive options may still provide partial availability in the event of a primary leased line failure.

Standard classic modems and DSL modems are examples of nondedicated lines. Digital subscriber line (DSL) is a technology that exploits the upgraded telephone network to grant consumers speeds from 144 Kbps to 20 Mbps (or more). There are numerous formats of DSL, such as ADSL, xDSL, CDSL, HDSL, SDSL, RASDSL, IDSL, and VDSL. Each format varies as to the specific downstream and upstream bandwidth provided.

Integrated Services Digital Network (ISDN) was the planned replacement for PSTN, but with the advent of DSL, cable internet, and ultimately fiber options, it did not gain widespread adoption. Most ISDN services have been discontinued.

When considering connection options, don't forget about satellite connections. Satellite connections may offer high-speed solutions even in locales that are inaccessible by cable-based, radio wave–based, and line-of-sight–based communications. Satellites are usually considered insecure because of their large surface footprint; communications over a satellite can be intercepted by anyone. But if you have strong encryption, satellite communications can be reasonably secured. Just think of satellite radio. As long as you have a receiver, you can get the signal anywhere. But without a paid service plan, you can't gain access to the content.
