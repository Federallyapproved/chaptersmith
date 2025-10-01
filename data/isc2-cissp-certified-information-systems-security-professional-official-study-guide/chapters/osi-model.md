---
{
  "id": "chapter-123",
  "title": "OSI Model",
  "order": 123,
  "source": {
    "href": "c11.xhtml",
    "anchor": "head-2-193"
  },
  "est_tokens": 2966,
  "slug": "osi-model",
  "meta": {
    "nav_title": "OSI Model",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## OSI Model

Communications between computers over networks are made possible by protocols. A protocol is a set of rules and restrictions that define how data is transmitted over a network medium (e.g., twisted-pair cable, wireless transmission). The International Organization for Standardization (ISO) developed the Open Systems Interconnection (OSI) Reference Model for protocols in the late 1970s.

### History of the OSI Model

The OSI Reference Model (more commonly called the OSI model ) wasn't the first or only attempt to establish a common communications standard. In fact, the most widely used protocol today, TCP/IP (which is based on the Defense Advanced Research Projects Agency (DARPA) model, also known now as the TCP/IP model), was developed in the early 1970s. The OSI model was not developed until the late 1970s (and not formally published as standard ISO 7498 until 1984).

The OSI model was developed to establish a common communication structure or standard for all computer systems. The OSI model serves as an abstract framework, or theoretical model, for how protocols should function in an ideal world on ideal hardware. The OSI model has become a common reference point.

### OSI Functionality

The OSI model divides networking tasks into seven layers. Each layer is responsible for performing specific tasks or operations with the ultimate goal of supporting data exchange (in other words, network communication) between two computers. They are referred to by either their name or their layer number ( Figure 11.1 ). The layers are ordered specifically to indicate how information flows through the various levels of communication. Each layer communicates directly with the layer above it as well as the layer below it.

FIGURE 11.1 The OSI model

FIGURE 11.1 The OSI model

### Encapsulation/Deencapsulation

The OSI model represents a protocol stack, which is a layered collection of multiple protocols (i.e., a multilayered protocol). Communication between protocol layers occurs through encapsulation and deencapsulation. Encapsulation is the addition of a header, and possibly a footer, to the data received by each layer from the layer above before it's handed off to the layer below. As the message is encapsulated at each layer, the previous layer's header and payload become the payload of the current layer. The inverse action occurring as data moves up through the OSI model layers from Physical to Application is known as deencapsulation . (Note: the term decapsulation is sometimes used, but the term used by the Internet Engineering Task Force (IETF) is deencapsulation.) The encapsulation/deencapsulation process is as follows:

- The Application layer receives data from software. The Application layer encapsulates the message by adding information to it. Information is usually added only at the beginning of the message (called a header); however, some layers also add material at the end of the message (called a footer), as shown in Figure 11.2 . The Application layer passes the encapsulated message to the Presentation layer.

- The process of passing the message down and adding layer-specific information continues until the message reaches the Physical layer.

- At the Physical layer, the message is converted into electrical impulses that represent bits and is transmitted over the physical connection.

- The receiving computer captures the bits from the physical connection and re-creates the message in the Physical layer and sends the message up to the Data Link layer.

- The Data Link layer strips its information and sends the message up to the Network layer.

- This process of deencapsulation is performed until the message reaches the Application layer.

- When the message reaches the Application layer, the data in the message is sent to the intended software recipient.

FIGURE 11.2 OSI model encapsulation

FIGURE 11.2 OSI model encapsulation

The information removed by each layer contains instructions, checksums, and so on that can be understood only by the peer layer that originally added or created the information (see Figure 11.3 ). This is known as peer layer communication .

FIGURE 11.3 The OSI model peer layer logical channels

FIGURE 11.3 The OSI model peer layer logical channels

The data sent into the protocol stack at the Application layer (layer 7) is encapsulated into a network container. The protocol data unit (PDU) is then passed down to the Presentation layer (layer 6), which in turn passes it down to the Session layer (layer 5). This network container is known as the PDU at layers 7, 6, and 5. Once the network container reaches the Transport layer (layer 4) it is then called a segment (TCP) or a datagram (User Datagram Protocol [UDP]). In the Network layer (layer 3), it is called a packet . In the Data Link layer (layer 2), it is called a frame . In the Physical layer (layer 1), the network container is converted into bits for transmission over the physical connection medium. Figure 11.4 shows the label applied to the network container at each layer.

FIGURE 11.4 OSI model layer-based network container names

FIGURE 11.4 OSI model layer-based network container names

### OSI Layers

Understanding the functions and responsibilities of each layer of the OSI model will help you understand how network communications function, how attacks can be perpetrated, and how security can be implemented to protect network communications.

# Remember the OSI

Mnemonics can help you remember the layers of the OSI model in order: Application, Presentation, Session, Transport, Network, Data Link, and Physical (top to bottom). Examples include: “Please Do Not Teach Surly People Acronyms” (Physical layer up to the Application layer) and “All Presidents Since Truman Never Did Pot” (Application layer down to Physical layer).

#### Application Layer

The Application layer (layer 7) is responsible for interfacing user applications, network services, or the operating system with the protocol stack. The software application is not located within this layer; rather, the protocols and services required to transmit files, exchange messages, connect to remote terminals, and so on are found here.

#### Presentation Layer

The Presentation layer (layer 6) is responsible for transforming data into a format that any system following the OSI model can understand. It imposes common or standardized structure and formatting rules onto the data. The Presentation layer is also responsible for encryption and compression.

On TCP/IP networks, there is not an actual Presentation layer. There is no current need to reformat data for network transport, and protocol-stack compression only occurs in concert with some encryption operations. Encryption in relation to network communication can occur in at least five locations:

- Pre-network encryption where the software encrypts prior to sending the data into the Application layer

- Transport layer encryption typically performed by TLS

- VPN encryption, which can occur at layer 2, 3, or 4 depending on the VPN technology in use (such as L2TP, IPsec, or OpenVPN, respectively)

- Wireless encryption at the Data Link layer

- Bulk encryption at the Physical layer (provided by a device external to the NIC)

#### Session Layer

The Session layer (layer 5) is responsible for establishing, maintaining, and terminating communication sessions between two computers. It manages dialog discipline or dialog control (simplex, half-duplex, full-duplex), establishes checkpoints for grouping and recovery, and retransmits PDUs that have failed or been lost since the last verified checkpoint.

On TCP/IP networks, there is not an actual Session layer. Session layer functions are handled by TCP at the Transport layer, or not at all when UDP is in use.

Communication sessions can operate in one of three different discipline or control modes:

- Simplex: One-way communication

- Half-Duplex: Two-way communication, but only one direction can send data at a time

- Full-Duplex: Two-way communication, in which data can be sent in both directions simultaneously

#### Transport Layer

The Transport layer (layer 4) is responsible for managing the integrity of a connection and controlling the session. The Transport layer establishes communications between nodes (also known as devices) and defines the rules of a session. Session rules specify how much data each segment can contain, how to verify message integrity, and how to determine whether data has been lost. Session rules are established through a handshaking process. (Please see the section “Transport Layer Protocols,” later in this chapter, for the discussion of the SYN/ACK three-way handshake of TCP.)

The Transport layer establishes a logical connection between two devices and provides end-to-end transport services to ensure data delivery. This layer includes mechanisms for segmentation, sequencing, error checking, controlling the flow of data, error correction, multiplexing, and network service optimization. The following protocols operate within the Transport layer:

- Transmission Control Protocol (TCP)

- User Datagram Protocol (UDP)

- Transport Layer Security (TLS)

#### Network Layer

The Network layer (layer 3) is responsible for logical addressing and performing routing. Logical addressing occurs when an address is assigned and used by software or a protocol rather than being provided and controlled by hardware. The Network layer's packet header includes the source and destination IP addresses.

The Network layer is responsible for providing routing or delivery guidance, but it is not responsible for verifying guaranteed delivery. The Network layer also manages error detection and node data traffic (i.e., traffic control).

# Non-IP, or Legacy, Protocols

Non-IP protocols are protocols that serve as an alternative to IP at the OSI Network layer (3). With the dominance and success of TCP/IP, non-IP protocols (i.e., legacy protocols ) have become the purview of special-purpose networks, such as IPX, AppleTalk, and NetBEUI. Because non-IP protocols are rare, most firewalls are unable to perform packet header, address, or payload content filtering on those protocols. Also, non-IP protocols can be encapsulated in IP to be communicated across the internet. Thus, legacy protocols need to be blocked.

A router is the primary network hardware device that functions at layer 3. Routers determine the best logical path for the transmission of packets based on speed, hops, preference, and so on. Routers use the destination IP address to guide the transmission of packets.

# Routing Protocols

There are two broad categories of interior routing protocols : distance vector and link state. Distance vector routing protocols maintain a list of destination networks along with metrics of direction and distance as measured in hops (in other words, the number of routers to cross to reach the destination). Link state routing protocols gather router characteristics, such as speed, latency, error rates, and actual monetary cost for use. This information is tabulated to make a next hop routing decision. Common examples of distance vector routing protocols are Routing Information Protocol (RIP) and Interior Gateway Routing Protocol (IGRP) . Common examples of link state routing protocols are Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS) . There is also a commonly used advanced distance vector routing protocol that replaces IGRP: Enhanced Interior Gateway Routing Protocol (EIGRP) .

There is one main category of exterior routing protocols that is called path vector. Path vector routing protocols make next hop decisions based on the entire remaining path (i.e., vector) to the destination. This is distinct from interior routing protocols, which make next hop decisions based solely on information related to that next immediate hop. Interior routing protocols are myopic, whereas exterior routing protocols are far-sighted. The primary example of a path vector protocol is Border Gateway Protocol (BGP) .

Route security can be enforced by configuring routers to only accept route updates from other authenticated routers. Administrative access to a router should be limited physically and logically to only specific authorized entities. It is also important to keep router firmware updated.

#### Data Link Layer

The Data Link layer (layer 2) is responsible for formatting the packet for transmission. The proper format is determined by the hardware, topology, and the technology of the network, such as Ethernet (IEEE 802.3).

Part of the processing performed on the network container within the Data Link layer includes adding the source and destination hardware addresses to the frame. The hardware address is the Media Access Control (MAC) address , which is a 6-byte (48-bit) binary address written in hexadecimal notation (for example, 00-13-02-1F-58-F5). This address is also known as the physical address , the NIC address , and the Ethernet address . The first 3 bytes (24 bits) of the address is the organizationally unique identifier (OUI) , which denotes the vendor or manufacturer of the physical network interface. OUIs are registered with the Institute of Electrical and Electronics Engineers (IEEE), which controls their issuance. The OUI can be used to discover the manufacturer of a NIC through the IEEE website at standards.ieee.org/products-services/regauth/index.html . The last 3 bytes (24 bits) of the MAC address represent a unique number assigned to that interface by the manufacturer. Some manufacturers will encode information into these final 24 bits, which may represent the make, model, and production run along with a unique value. Thus, some devices (such as mobile devices, IoT equipment, and embedded systems) that use a unique NIC can be identified by their MAC address.

Among the protocols at the Data Link layer (layer 2) of the OSI model, you should be familiar with Address Resolution Protocol (ARP). See the section “ARP Concerns” later in this chapter.

Network hardware devices that function at layer 2, the Data Link layer, are switches and bridges. These devices support MAC-based traffic routing. Switches receive a frame on one port and send it out another port based on the destination's MAC address. MAC address destinations are used to determine whether a frame is transferred over the bridge from one network segment to another.

#### Physical Layer

The Physical layer (layer 1) converts a frame into bits for transmission over the physical connection medium, and vice versa for receiving communications.

Network hardware devices that function at layer 1, the Physical layer, are NICs, hubs, repeaters, concentrators, and amplifiers. These devices perform hardware-based signal operations, such as sending a signal from one connection port out on all other ports (a hub) or amplifying the signal to support greater transmission distances (a repeater).
