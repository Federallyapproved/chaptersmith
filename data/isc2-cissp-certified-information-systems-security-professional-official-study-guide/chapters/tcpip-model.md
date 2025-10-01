---
{
  "id": "chapter-124",
  "title": "TCP/IP Model",
  "order": 124,
  "source": {
    "href": "c11.xhtml",
    "anchor": "head-2-197"
  },
  "est_tokens": 402,
  "slug": "tcpip-model",
  "meta": {
    "nav_title": "TCP/IP Model",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## TCP/IP Model

The TCP/IP model (also called the DARPA model or the DOD model ) consists of only four layers, as opposed to the OSI reference model's seven. The four layers of the TCP/IP model are Application (also known as Process ), Transport (also known as Host-to-Host ), Internet (sometimes Internetworking ), and Link (although Network Interface and sometimes Network Access are also used). Figure 11.5 shows how they compare to the seven layers of the OSI model. The TCP/IP protocol suite was developed before the OSI Reference Model was created.

Since the TCP/IP model layer names and the OSI model layer names can be used interchangeably, it is important to know which model is being addressed in various contexts. Unless informed otherwise, always assume that the OSI model provides the basis for discussion because it's the most widely used network reference model.

The TCP/IP model was derived directly from the TCP/IP protocol suite or stack comprising hundreds of individual protocols. TCP/IP is a platform-independent protocol based on open standards. TCP/IP can be found in just about every available operating system, but it consumes a significant amount of resources and is relatively easy to hack, because it was originally designed for ease of use and interoperability rather than for security.

FIGURE 11.5 Comparing the OSI model with the TCP/IP model

FIGURE 11.5 Comparing the OSI model with the TCP/IP model

TCP/IP's vulnerabilities are numerous. Improperly implemented TCP/IP stacks in various operating systems are vulnerable to buffer overflows, SYN flood attacks, various denial-of-service (DoS) attacks, fragment attacks, oversized packet attacks, spoofing attacks, man-in-the-middle attacks (on-path attacks), hijack attacks, and coding error attacks.

TCP/IP (as well as most protocols) is also subject to passive attacks via monitoring or sniffing. Eavesdropping and other attacks are discussed in more detail at the end of Chapter 12 .
