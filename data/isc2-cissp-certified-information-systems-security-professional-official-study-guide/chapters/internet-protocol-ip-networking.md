---
{
  "id": "chapter-129",
  "title": "Internet Protocol (IP) Networking",
  "order": 129,
  "source": {
    "href": "c11.xhtml",
    "anchor": "head-2-204"
  },
  "est_tokens": 2068,
  "slug": "internet-protocol-ip-networking",
  "meta": {
    "nav_title": "Internet Protocol (IP) Networking",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Internet Protocol (IP) Networking

Another important protocol in the TCP/IP protocol suite operates at the Network layer of the OSI model, namely, Internet Protocol (IP) . IP provides route addressing for data packets. It is this route addressing that is the foundation of global internet communications because it provides a means of identity and prescribes transmission paths. Similar to UDP, IP is connectionless and is an unreliable communication service. IP does not offer guarantees that packets will be delivered or that packets will be delivered in the correct order, and it does not guarantee that packets will be delivered only once. However, it was designed to perform “best effort” in finding a path or route to a destination, in spite of a damaged or corrupted network structure. Thus, you must employ TCP with IP to gain reliable and controlled communication sessions.

### IPv4 vs. IPv6

IPv4 is the version of Internet Protocol that is most widely used around the world. However, IPv6 is being rapidly adopted for both private and public network use. IPv4 uses a 32-bit addressing scheme, whereas IPv6 uses 128 bits for addressing. IPv6 offers many new features that are not available in IPv4. Some of IPv6's new features are scoped addresses, autoconfiguration, and quality of service (QoS) priority values. Scoped addresses give administrators the ability to group and then block or allow access to network services, such as file servers or printing. Autoconfiguration removes the need for both DHCP and network address translation (NAT). QoS priority values allow for traffic management based on prioritized content. Also, IPsec is native to IPv6, but it is an add-on for IPv4.

IPv4 has an equivalent concept to that of IPv6's QoS which is named Type of Service (ToS). However, it seemed to go unused and was converted into the Differentiated Services (DS) by later specification. The DS field offers a variety of definable characteristics that can be used to manage traffic flow. However, it still does not seem to have widespread use or support by network devices, which would perform such management. There is promise that IPv6 networks will include more common support and actually provide for traffic prioritization based on IPv6 header values.

IPv6 is supported by most operating systems released since 2000, either natively or via an add-in. However, IPv6 has been slowly adopted. Most of the IPv6 networks are currently located in private networks such as those in large corporations, research laboratories, and universities. For a glimpse into the status of IPv4 to IPv6 conversion on the internet from Google's perspective, see the IPv6 statistics at www.google.com/intl/en/ipv6/statistics.html .

The transition or migration to IPv6 raises several security concerns. One issue is that with the larger 128-bit address space, there are many more addresses that attackers can use as source addresses; thus, IP filtering and block lists will be less effective as attackers can just use a different address to get past the filter.

A second issue is that secure deployment of IPv6 requires that all security filtering and monitoring products be upgraded to fully support IPv6 prior to enabling the protocol on the production network. Otherwise, IPv6 will serve as a covert channel, as it will be unmonitored and unfiltered.

A third concern with IPv6 is the loss or lack of NAT (see Chapter 12 ). IPv4 required the use of NAT to support a growing number of client systems in light of a dwindling number of public IP addresses. With IPv6, the number of addresses is astronomical (340,282,366,920,938,463,463,374,607,431,768,211,456), so NAT is not only not necessary, it is not addressed in the specification. Some argue that this reduces security; the reality is that it mostly reduces privacy. The real security perceived as being from NAT is actually provided on purpose by a stateful inspection firewall, which most networks were already using in addition to NAT. Privacy is lost or reduced without NAT since a system's locally assigned IP address is not masked by NAT to a public address. With future IPv6 addresses being hard-coded to a NIC, it may be difficult to hide the identity of a source system, whether that is an attacker or an individual in need of a private and/or untraceable online transaction (such as a whistleblower or someone seeking assistance due to domestic abuse).

The means by which IPv6 and IPv4 can coexist on the same network is to use one or more of three primary options: dual stack , tunneling, or NAT-PT. Dual stack means having systems operate both IPv4 and IPv6 and using the appropriate protocol for each conversation. Tunneling allows most systems to operate a single stack of either IPv4 or IPv6 and use an encapsulation tunnel to access systems of the other protocol. Network Address Translation-Protocol Translation (NAT-PT) (RFC-2766) can be used to convert between IPv4 and IPv6 network segments similar to how NAT converts between internal and external addresses.

Both IPv4 and IPv6 have a header field that is used to control or limit infinite transmission. The time to live (TTL) field of IPv4 and the hop limit field of IPv6 are decremented by routers until it reaches zero (0). Once that occurs, the packet is discarded and an ICMP Type 11 Timeout Exceeded error message is sent back to the origin.

### IP Classes

Basic knowledge of IPv4 addressing and IPv4 classes is a must for any security professional. If you are rusty on IPv4 addressing, subnetting, classes, and other related topics, take the time to refresh your knowledge.

Table 11.1 and Table 11.2 provide a quick overview of the key details of classes and default subnets. A full Class A subnet supports 16,777,214 hosts; a full class B subnet supports 65,534 hosts; and a full Class C subnet supports 254 hosts. Class D is used for multicasting, whereas Class E is reserved for future use.

TABLE 11.1 IP classes

TABLE 11.1 IP classes

Note that the entire Class A network of 127 was set aside for the loopback address , although only a single address is actually needed for that purpose. A Class A network of 0 is defined as the blackhole network where traffic is routed in order to be thrown away and discarded.

The loopback address for IPv4 is any address in the Class A subnet of 127.0.0.1–127.255.255.254, even though only the address of 127.0.0.1 is typically used. When an interface is configured for loopback, a subnet mask is not defined; it will use 255.255.255.255 by default, although some will document this as 127.0.0.0/8. Also note that under IPv4, the first address of a subnet is reserved as the network address (i.e., 127.0.0.0) and the last for the directed broadcast (i.e., 127.255.255.255) and therefore not directly usable as a host address (or in this case a loopback address). The IPv6 loopback is not a specific address—it is a notation: ::1/128.

TABLE 11.2 IP classes' default subnet masks

TABLE 11.2 IP classes' default subnet masks

The original class-based grouping of IPv4 addresses is not strictly adhered to any longer. Instead, a more flexible system has been adopted based on variable length subnet masking (VLSM) and Classless Inter-Domain Routing (CIDR) . CIDR provides for a subnet masking notation that uses mask bit counts rather than a full dotted-decimal notation subnet mask. Thus, instead of 255.255.0.0, a CIDR notation is added to the IP address after a slash, as in 172.16.1.1/16, for example. One significant benefit of CIDR over traditional subnet-masking techniques is the ability to combine multiple noncontiguous sets of addresses into a single subnet. For example, it is possible to combine several Class C subnets into a single larger subnet grouping. If CIDR piques your interest, see IETF's RFC for CIDR at tools.ietf.org/html/rfc4632 .

### ICMP

Internet Control Message Protocol (ICMP) is used to determine the health of a network or a specific link. ICMP is utilized by ping , traceroute , pathping , and other network management tools. The ping utility employs ICMP echo packets and bounces them off remote systems. Thus, you can use ping to determine whether the remote system is online, whether the remote system is responding promptly, whether the intermediary systems are supporting communications, and the level of performance efficiency at which the intermediary systems are communicating. The ping utility includes a redirect function that allows the echo responses to be sent to a different destination than the system of origin.

`ping`

`traceroute`

`pathping`

`ping`

`ping`

`ping`

Unfortunately, the features of ICMP were often exploited in various forms of bandwidth-based denial-of-service (DoS) attacks, such as ping of death, Smurf attacks, and ping floods. This fact has shaped how networks handle ICMP traffic today, resulting in many networks limiting the use of ICMP or at least limiting its throughput rates.

### IGMP

Internet Group Management Protocol (IGMP) allows systems to support multicasting. Multicasting is the transmission of data to multiple specific recipients. RFC 1112 discusses the requirements to perform IGMP multicasting ( tools.ietf.org/html/rfc1112 ). IGMP is used to manage a host's dynamic multicast group membership. With IGMP, a single initial signal is multiplied at the router if divergent pathways exist to the intended recipients. Multicasting can be assisted by a Trivial File Transfer Protocol (TFTP) system to host or cache content that is to be sent to the multiple recipients.
