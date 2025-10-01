---
{
  "id": "chapter-140",
  "title": "Exam Essentials",
  "order": 140,
  "source": {
    "href": "c11.xhtml",
    "anchor": "head-2-219"
  },
  "est_tokens": 2438,
  "slug": "exam-essentials-11",
  "meta": {
    "nav_title": "Exam Essentials",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Exam Essentials

Know the OSI model. The OSI layers are as follows: Application, Presentation, Session, Transport, Network, Data Link, and Physical.

Understand encapsulation. Encapsulation is the addition of a header, and possibly a footer, to the data received by each layer from the layer above before it's handed off to the layer below. The inverse action is deencapsulation.

Know the network container names. The network containers are: OSI layers 7–5 protocol data unit (PDU), layer 4 segment (TCP) or a datagram (UDP), layer 3 packet, layer 2 frame, and layer 1 bits.

Understand protocol analyzers. A protocol analyzer is a tool used to examine the contents of network traffic.

Understand the MAC address. Media Access Control (MAC) address is a 6-byte (48-bit) binary address written in hexadecimal notation, aka hardware address, physical address, the NIC address, and the Ethernet address. The first 3 bytes (24 bits) of the address is the organizationally unique identifier (OUI), which denotes the vendor or manufacturer.

Know routing protocols. Interior routing protocols are distance vector (Routing Information Protocol ([RIP] and Interior Gateway Routing Protocol [IGRP]) and link state (Open Shortest Path First [OSPF] and Intermediate System to Intermediate System [IS-IS]); exterior routing protocols are path vector (Border Gateway Protocol [BGP]).

Understand the TCP/IP model. Also known as DARPA or the DOD model, the model has four layers: Application (also known as Process), Transport (also known as Host-to-Host), Internet (sometimes known as Internetworking), and Link (although Network Interface and sometimes Network Access are used).

Be aware of the common application layer protocols. These include Telnet, FTP, TFTP, SMTP, POP3, IMAP, DHCP, HTTP, HTTPS (TLS), LPD, X Window, NFS, and SNMP.

Understand transport layer protocols. Be aware of the features and differences between TCP and UDP; also be familiar with ports, session management, and TCP header flags.

Understand DNS. The Domain Name System (DNS) is the hierarchical naming scheme used in both public and private networks. DNS links human-friendly fully qualified domain names (FQDNs) and IP addresses together. DNSSEC and DoH are DNS security features.

Understand DNS poisoning. DNS poisoning is the act of falsifying the DNS information used by a client to reach a desired system. It can be accomplished through a rogue DNS server, pharming, altering a hosts file, corrupting IP configuration, DNS query spoofing, and proxy falsification.

`hosts`

Understand domain hijacking. Domain hijacking, or domain theft, is the malicious action of changing the registration of a domain name without the authorization of the valid owner.

Understand typosquatting. Typosquatting is a practice employed to capture and redirect traffic when a user mistypes the domain name or IP address of an intended resource.

Know about IP. Be familiar with the features and differences between IPv4 and IPv6. Understand IPv4 classes, subnetting, and CIDR notation.

Understand network layer protocols. Be familiar with ICMP and IGMP.

Know about ARP. Address Resolution Protocol (ARP) is essential to the interoperability of logical and physical addressing schemes. ARP is used to resolve IP addresses into MAC addresses. Also know about ARP poisoning.

Be able to give examples of security communication protocols. Examples include IPsec, Kerberos, SSH, Signal protocol, S-RPC, and TLS.

Understand multilayer protocols. Benefits of multilayer protocols include the fact that they can be used at higher OSI levels and that they offer encryption, flexibility, and resiliency. Drawbacks include covert channels, filter bypass, and violation of network segment boundaries.

Know about converged protocols. Examples include FCoE, MPLS, iSCSI, VPN, SDN, cloud, virtualization, SOA, microservices, infrastructure as code (IaC), and serverless architecture.

Define VoIP. Voice over IP (VoIP) is a tunneling mechanism that encapsulates audio, video, and other data into IP packets to support voice calls and multimedia collaboration over TCP/IP network connections.

Understand the various types and purposes of network segmentation. Network segmentation can be used to manage traffic, improve performance, and enforce security. Examples of network segments or subnetworks include intranet, extranet, and screened subnet.

Know about microsegmentation. Microsegmentation is dividing up an internal network in numerous subzones, potentially as small as a single device, such as a high-value server or even a client or endpoint device. Each zone is separated from the others by internal segmentation firewalls (ISFWs), subnets, or VLANs.

Define SDN. Software-defined networking (SDN) is a unique approach to network operation, design, and management. SDN aims at separating the infrastructure layer (hardware and hardware-based settings) from the control layer (network services of data transmission management).

Understand the various wireless technologies. Cell phones, Bluetooth (802.15), and wireless networking (802.11) are all called wireless technologies, even though they are all different. Be aware of their differences, strengths, and weaknesses. Understand the basics of securing 802.11 networking. Know RFID, NFC, LiFi, satellite, narrow-band, and Zigbee.

Know about service set identifier (SSID). Examples include ESSID, BSSID, and ISSID.

Define WPA2. IEEE 802.11i defined Wi-Fi Protected Access 2 (WPA2). WPA2 supports two authentication options: preshared key (PSK) or personal (PER) and IEEE 802.1X or enterprise (ENT). WPA2 uses AES-CCMP.

Understand WPA3. Wi-Fi Protected Access 3 (WPA3) uses 192-bit AES CCMP encryption, whereas WPA3-PER remains at 128-bit AES CCMP. WPA3-PER uses Simultaneous Authentication of Equals (SAE).

Define SAE. Simultaneous Authentication of Equals (SAE) performs a zero-knowledge proof process known as Dragonfly Key Exchange, which is itself a derivative of Diffie–Hellman. The process uses a preset password and the MAC addresses of the client and AP to perform authentication and session key exchange.

Understand site surveys. A site survey is a formal assessment of wireless signal strength, quality, and interference using an RF signal detector. A site survey is performed by placing a wireless base station in a desired location and then collecting signal measurements from throughout the area.

Understand WPS attacks. Wi-Fi Protected Setup (WPS) intended to simplify the effort involved in adding new clients to a secured wireless network. It operates by automatically connecting the first new wireless client to seek the network once WPS is triggered.

Understand MAC filtering. A MAC filter is a list of authorized wireless client interface MAC addresses that is used by a WAP to block access to all nonauthorized devices.

Understand antenna types. A wide variety of antenna types can be used for wireless clients and base stations. These include omnidirectional pole antennas as well as many directional antennas, such as Yagi, cantenna, panel, and parabolic.

Understand captive portals. A captive portal is an authentication technique that redirects a newly connected client to a web-based portal access control page.

Define spread spectrum. Spectrum-use techniques manage the simultaneous use of the limited radio frequencies, including FHSS, DSSS, and OFDM.

Understand Bluetooth attacks. Attacks include bluesniffing, bluesmacking, bluejacking, bluesnarfing, and bluebugging.

Know wireless attacks. Attacks include war driving, wireless scanners/crackers, rogue access points, evil twin, disassociation, jamming, IV abuse, and replay.

Be familiar with CDNs. A content distribution network (CDN), or content delivery network, is a collection of resource services deployed in numerous data centers across the internet in order to provide low latency, high performance, and high availability of the hosted content.

Know the common network devices. Common network devices are repeater, hub, modem, bridge, switch, router, LAN extender, jumpbox, sensor, collector, and aggregator.

Define NAC. Network access control (NAC) is the concept of controlling access to an environment through strict adherence to and enforcement of security policy. Know about 802.1X, preadmission, postadmission, agent-based, and agentless.

Understand the various types of firewalls. There are several types of firewalls: static packet filtering, application-level, circuit-level, stateful inspection, NGFW, and ISFW. Also know about virtual firewall, filters/rules/ACLs/tuples, bastion host, ingress, egress, RTBH, stateless vs. stateful, WAF, SWG, TCP wrapper, DPI, and content and URL filtering.

Know about proxies. A proxy server is used to mediate between clients and servers. Proxies are most often used in the context of providing clients on a private network with internet access while protecting the identity of the clients. Know about forward, reverse, transparent, and nontransparent.

Understand endpoint security. Endpoint security is the concept that each individual device must maintain local security whether or not its network or telecommunications channels also provide security.

Know EDR. Endpoint detection and response (EDR) is a security mechanism that is an evolution of traditional antimalware products, IDS, and firewall solutions. EDR seeks to detect, record, evaluate, and respond to suspicious activities and events.

Understand MDR. managed detection and response (MDR) focuses on threat detection and mediation but is not limited to the scope of endpoints. MDR is a service that attempts to monitor an IT environment in real-time to quickly detect and resolve threats. Often an MDR solution is a combination and integration of numerous technologies, including SIEM, network traffic analysis (NTA), EDR, and IDS.

Know EPP. Endpoint protection platform (EPP) is a variation of EDR much like IPS is a variation of IDS. The focus on EPP is on four main security functions: predict, prevent, detect, and respond. Thus, EPP is the more active prevent and predict variation of the more passive EDR concept.

Understand XDR. Extended detection and response (XDR) components often include EDR, MDR, and EPP elements. Also, XDR is not solely focused on endpoints, but often includes NTA, NIDS, and NIPS functions as well.

Be aware of MSSP. Managed security service provider (MSSP) can provide XDR solutions that are centrally controlled and managed. MSSP solutions can be deployed fully on-premise, fully in the cloud, or as a hybrid structure. MSSP solutions can be overseen through a SOC which is itself local or remote. Typically, working with an MSSP to provide EDR, MDR, EPP, or XDR services can allow an organization to gain the benefits of these advanced security products and leverage the experience and expertise of the MSSP's staff of security management and response professionals.

Describe the different cabling types. This includes STP, UTP, 10Base2 coax (thinnet), 10Base5 coax (thicknet), 100BaseT, 1000BaseT, and fiber-optic. You should be familiar with UTP categories 1 through 8.

Be familiar with the common LAN technologies. The most common LAN technology is Ethernet. Also be familiar with analog vs. digital communications; synchronous vs. asynchronous communications; duplexing; baseband vs. broadband communications; broadcast, multicast, and unicast communications; CSMA, CSMA/CD, and CSMA/CA; token passing; and polling.

Know the standard network topologies. These are ring, bus, star, and mesh.
