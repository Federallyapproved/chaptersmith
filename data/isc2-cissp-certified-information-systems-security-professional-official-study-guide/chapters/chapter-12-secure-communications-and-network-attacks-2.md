---
{
  "id": "chapter-274",
  "title": "Chapter 12: Secure Communications and Network Attacks",
  "order": 274,
  "source": {
    "href": "b02.xhtml",
    "anchor": "head-2-35"
  },
  "est_tokens": 902,
  "slug": "chapter-12-secure-communications-and-network-attacks-2",
  "meta": {
    "nav_title": "Chapter 12: Secure Communications and Network Attacks",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Chapter 12: Secure Communications and Network Attacks

- Transport mode links or VPNs are anchored or end at the individual hosts connected together. Let's use IPsec as an example. In transport mode, IPsec provides encryption protection for just the payload and leaves the original message header intact. This type of VPN is also known as a host-to-host VPN or an end-to-end encrypted VPN, since the communication remains encrypted while it is in transit between the connected hosts. Tunnel mode links or VPNs are anchored or end at VPN devices on the boundaries of the connected networks (or one remote device). In tunnel mode, IPsec provides encryption protection for both the payload and message header by encapsulating the entire original LAN protocol packet and adding its own temporary IPsec header. Tunnel mode VPNs can be used to connect two networks across the internet (aka site-to-site VPN) or to allow distant clients to connect into an office local area network (LAN) across the internet (aka remote access VPN).

- Network address translation (NAT) allows the identity of internal systems to be hidden from external entities. Often NAT is used to translate between RFC 1918 private IP addresses and leased public addresses. NAT serves as a one-way firewall because it allows only inbound traffic that is a response to a previous internal query. NAT also allows a few leased public addresses to be used to grant internet connectivity to a larger number of internal systems.

- Circuit switching is usually associated with physical connections. The link itself is physically established and then dismantled for the communication. Circuit switching offers known fixed delays, supports constant traffic, is connection oriented, is sensitive only to the loss of the connection rather than the communication, and is most often used for voice transmissions. Packet switching is usually associated with logical connections because the link is just a logically defined path among possible paths. Within a packet-switching system, each system or link can be employed simultaneously by other circuits. Packet switching divides the communication into segments, and each segment traverses the circuit to the destination. Packet switching has variable delays because each segment could take a unique path, is usually employed for bursty traffic, is not physically connection oriented but often uses virtual circuits, is sensitive to the loss of data, and is used for any form of communication.

- Email is inherently insecure because it is primarily a plaintext communication medium and employs nonencrypted transmission protocols. This allows email to be easily spoofed, spammed, flooded, eavesdropped on, interfered with, and hijacked. Defenses against these issues primarily include having stronger authentication requirements and using encryption to protect the content while in transit.

- The RFC 1918 private IP address ranges are as follows: 10.0.0.0–10.255.255.255 (a full Class A range); 172.16.0.0–172.31.255.255 (16 Class B ranges); and 192.168.0.0–192.168.255.255 (256 Class C ranges). APIPA assigns each failed DHCP client with an IP address from the range of 169.254.0.1 to 169.254.255.254 along with the default Class B subnet mask of 255.255.0.0. Technically, the entire 127.0.0.0/8 network is reserved for loopback use in IPv4. However, only the 127.0.0.1 address is widely used.

- Many facts about VLANs are included in this chapter. Answers can include any of the following options. A virtual local area network (VLAN) is a hardware-imposed network segmentation created by switches. VLANs can be defined/assigned/created based on ports, device MAC address, IP subnetting, specified protocols, or authentication. VLANs are used for traffic management because they are a form of network segmentation. VLAN routing can be provided either by an external router or by the switch's internal software (one reason for the terms L3 switch and multilayer switch ). VLANs control and restrict broadcast traffic and reduce a network's vulnerability to sniffers because a switch treats each VLAN as a separate network division. The members of a private VLAN or a port-isolated VLAN can interact only with each other and over the predetermined exit port or uplink port. The trunk link allows the switches to talk to each other directly, direct traffic between hosts, and stretch VLAN definitions across multiple physical switches.
