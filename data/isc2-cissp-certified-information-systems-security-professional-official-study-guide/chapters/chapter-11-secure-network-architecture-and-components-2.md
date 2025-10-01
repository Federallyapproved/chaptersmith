---
{
  "id": "chapter-273",
  "title": "Chapter 11: Secure Network Architecture and Components",
  "order": 273,
  "source": {
    "href": "b02.xhtml",
    "anchor": "head-2-34"
  },
  "est_tokens": 535,
  "slug": "chapter-11-secure-network-architecture-and-components-2",
  "meta": {
    "nav_title": "Chapter 11: Secure Network Architecture and Components",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Chapter 11: Secure Network Architecture and Components

- Application (7), Presentation (6), Session (5), Transport (4), Network (3), Data Link (2), and Physical (1).

- Problems with cabling and their countermeasures include attenuation (use repeaters or don't violate distance recommendations), using the wrong category of cable (check the cable specifications against throughput requirements, and err on the side of caution), crosstalk (use shielded cables, place cables in separate conduits, or use cables of different twists per inch), interference (use cable shielding, use cables with higher twists per inch, or switch to fiber-optic cables), and eavesdropping (maintain physical security over all cable runs or switch to fiber-optic cables).

- Some of the frequency spectrum-use technologies are spread spectrum, Frequency Hopping Spread Spectrum (FHSS), Direct Sequence Spread Spectrum (DSSS), and Orthogonal Frequency-Division Multiplexing (OFDM).

- Methods to secure 802.11 wireless networking include updating firmware; changing the default administrator password to something unique and complex; enabling WPA2 or WPA3 encryption; disabling the SSID broadcast; changing the SSID to something unique; changing the wireless MAC address; enabling MAC filtering; considering the use of static IPs or using DHCP with reservations; treating wireless as remote; separating WAPs from the LAN with firewalls; monitoring all wireless client activity with an IDS; deploying a wireless intrusion detection system (WIDS) and a wireless intrusion prevention system (WIPS); considering requiring wireless clients to connect with a VPN to gain LAN access; implementing a captive portal; and tracking/logging all wireless activities and events.

- The applications and ports listed in this chapter you could have selected include: Telnet, TCP Port 23; File Transfer Protocol (FTP), TCP Ports 20 (Active Data Connection)/Ephemeral (Passive Data Connection) and 21 (Control Connection); Simple Mail Transfer Protocol (SMTP), TCP Port 25; Post Office Protocol (POP3), TCP Port 110; Internet Message Access Protocol (IMAP), TCP Port 143; Dynamic Host Configuration Protocol (DHCP), UDP Ports 67 and 68; Hypertext Transfer Protocol (HTTP), TCP Port 80; HTTPS with Transport Layer Security (TLS), TCP Port 443; Line Print Daemon (LPD), TCP Port 515; Network File System (NFS), TCP Port 2049; Simple Network Management Protocol (SNMP), UDP Port 161 (UDP Port 162 for Trap Messages); and Domain Name System (DNS), TCP/UDP 53.
