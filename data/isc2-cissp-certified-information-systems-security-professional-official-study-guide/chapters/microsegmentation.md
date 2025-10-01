---
{
  "id": "chapter-133",
  "title": "Microsegmentation",
  "order": 133,
  "source": {
    "href": "c11.xhtml",
    "anchor": "head-2-209"
  },
  "est_tokens": 584,
  "slug": "microsegmentation",
  "meta": {
    "nav_title": "Microsegmentation",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Microsegmentation

Networks are not typically configured as a single large collection of systems. Usually, networks are segmented or subdivided into smaller organizational units. These smaller units, groupings, segments, or subnetworks (i.e., subnets) can be used to improve various aspects of the network:

- Boosting Performance Network Network segmentation can improve performance through an organizational scheme in which systems that often communicate are located in the same segment. Also, dividing broadcast domains can significantly improve performance for larger networks.

- Reducing Communication Problems Network segmentation often reduces congestion and contains communication problems, such as broadcast storms.

- Providing Security Network segmentation can also improve security by isolating traffic and user access to those segments where they are authorized.

Segments can be created by using switch-based VLANs, routers, or firewalls, individually or in combination. A private LAN or intranet, a screened subnet, and an extranet are all types of network segments.

Another often-overlooked network segmentation concept is the creation of an out-of-band pathway . This is often performed to create a separate and distinct network structure for traffic that would otherwise interfere with the production network or that may itself be put at risk if placed on the production network. Secondary (or additional) network paths or segments may be created to support data storage traffic (such as with SANs), VoIP, backup data, patch distribution, and management operations.

An evolution of the concept of network segmentation is microsegmentation. Microsegmentation is dividing an internal network into numerous subzones, potentially as small as a single device, such as a high-value server or even a client or endpoint device. Each zone is separated from the others by internal segmentation firewalls (ISFWs), subnets, VLANs, or other virtual networking solutions. Any and all communications between zones are filtered, may be required to authenticate, often require session encryption, and may be subjected to allow list and block list control. In some cases, in order to communicate with entities external to the local segment, the communication must be encapsulated for egress. This is similar to using a VPN to access a remote network. Microsegmentation is a key element in implementing zero trust (see Chapter 8 , “Principles of Security Models, Design, and Capabilities”).

Virtual eXtensible LAN (VXLAN) is an encapsulation protocol that enables VLANs (see Chapter 12 ) to be stretched across subnets and geographic distances. VLANs are typically restricted to layer 2 network areas and are not able to include members from other networks that are accessible only through a router portal. Additionally, VXLAN allows for up to 16 million virtual networks to be created, whereas traditional VLANs are limited to only 4,096. VXLAN can be used as a means to implement microsegmentation without limiting segments to local entities only. VXLAN is defined in RFC 7348.
