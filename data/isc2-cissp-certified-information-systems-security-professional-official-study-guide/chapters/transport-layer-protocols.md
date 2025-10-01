---
{
  "id": "chapter-127",
  "title": "Transport Layer Protocols",
  "order": 127,
  "source": {
    "href": "c11.xhtml",
    "anchor": "head-2-201"
  },
  "est_tokens": 713,
  "slug": "transport-layer-protocols",
  "meta": {
    "nav_title": "Transport Layer Protocols",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Transport Layer Protocols

When a connection is established via the Transport layer, it is done using ports. Since port numbers are 16-digit binary numbers, the total number of ports is 2^16, or 65,536, numbered from 0 through 65,535. Ports allow a single IP address to be able to support multiple simultaneous communications, each using a different port number (i.e., multiplexing over IP). The combination of an IP address and a port number is known as a socket .

The first 1,024 of these ports (0–1,023) are called the well-known ports or the service ports . These ports are reserved for use exclusively by servers.

Ports 1,024 to 49,151 are known as the registered software ports . These are ports that have one or more networking software products specifically registered with the International Assigned Numbers Authority (IANA) at iana.org .

Ports 49,152 to 65,535 are known as the random , dynamic , or ephemeral ports because they are often used randomly and temporarily by clients as a source port. However, most OSs allow for any port from 1,024 to be used as a dynamic client source port as long as it is not already in use on that local system.

The two primary Transport layer protocols of TCP/IP are TCP and UDP. Transmission Control Protocol (TCP) is a full-duplex connection-oriented protocol, whereas User Datagram Protocol (UDP) is a simplex connectionless protocol.

Transmission Control Protocol (TCP) supports full-duplex communications, is connection oriented, and employs reliable sessions. TCP is connection oriented because it employs a handshake process between two systems to establish a communication session. The three-way handshake process ( Figure 11.6 ) is as follows:

- The client sends a SYN (synchronize) flagged packet to the server.

- The server responds with a SYN/ACK (synchronize and acknowledge) flagged packet back to the client.

- The client responds with an ACK (acknowledge) flagged packet back to the server.

FIGURE 11.6 The TCP three-way handshake

FIGURE 11.6 The TCP three-way handshake

When a communication session is complete, there are two methods to disconnect the TCP session. First, and most common, is the use of FIN (finish) flagged packets to gracefully initiate session shutdown. Second is the use of an RST (reset) flagged packet, which causes an immediate and abrupt session termination.

TCP should be employed when the delivery of data is required. In the event that all packets of a transmission window were not received, no acknowledgment is sent. After a timeout period, the sender will resend the entire transmission window set of packets again. TCP guarantees delivery because it will continue to resend any unacknowledged window of segments until it receives an acknowledgment, it receives an RST, the local application terminates the network communication attempts, or power is removed from the system.

User Datagram Protocol (UDP) also operates at layer 4 (the Transport layer) of the OSI model. It is a connectionless “best-effort” communications protocol. It offers no error detection or correction, does not use sequencing, does not use flow control mechanisms, does not use a preestablished session, and is considered unreliable. UDP has very low overhead and thus can transmit data quickly. However, UDP should be used only when the delivery of data is not essential. UDP is often employed by real-time or streaming communications for audio and/or video.
