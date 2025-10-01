---
{
  "id": "chapter-126",
  "title": "Common Application Layer Protocols",
  "order": 126,
  "source": {
    "href": "c11.xhtml",
    "anchor": "head-2-199"
  },
  "est_tokens": 865,
  "slug": "common-application-layer-protocols",
  "meta": {
    "nav_title": "Common Application Layer Protocols",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Common Application Layer Protocols

In the Application layer of the OSI model reside numerous application- or service-specific protocols:

- Telnet , TCP Port 23 This is a terminal emulation network application that supports remote connectivity for executing commands and running applications but does not support transfer of files. Telnet should not be used; replace it with SSH.

- File Transfer Protocol (FTP) , TCP Ports 20 (Active Mode Data Connection)/Ephemeral (Passive Mode Data Connection) and 21 (Control Connection) This is a network application that supports an exchange of files that requires anonymous or specific authentication. FTP should not be used; replace it with SFTP or FTPS.

- Trivial File Transfer Protocol (TFTP), UDP Port 69 This is a network application that supports an exchange of files that does not require authentication. Used to host network device configuration files and can support multicasting. TFTP should not be used.

- Simple Mail Transfer Protocol (SMTP), TCP Port 25 This is a protocol used to transmit email messages from a client to an email server and from one email server to another. Only use if encrypted with TLS to create SMTPS.

- Post Office Protocol (POP3) , TCP Port 110 This is a protocol used to pull email messages from an inbox on an email server down to an email client (aka client archiving). Only use if encrypted with TLS to create POPS.

- Internet Message Access Protocol (IMAP4), TCP Port 143 This is a protocol used to pull email messages from an inbox on an email server down to an email client. IMAP offers the ability to retrieve only headers from an email server as well as to delete messages directly off the email server (i.e., server archiving). Only use if encrypted with TLS to create IMAPS.

- Dynamic Host Configuration Protocol (DHCP), UDP Ports 67 (server) and 68 (client) DHCP provides for centralized control of TCP/IP configuration settings assigned to systems upon bootup.

- Hypertext Transfer Protocol (HTTP), TCP Port 80 This is the protocol used to transmit web page elements from a web server to web browsers in cleartext.

- Hypertext Transfer Protocol Secured (HTTPS) TCP Port 443 This is the TLS-encrypted version of HTTP. (HTTPS with TLS does support use of TCP port 80—but only for server-to-server communications.)

- Line Printer Daemon (LPD), TCP Port 515 This is a network service that is used to spool print jobs and send print jobs to printers. Consider enclosing in a VPN for use.

- X Window, TCP Ports 6000–6063 This is a GUI API for command-line operating systems. Consider enclosing in a VPN for use.

- Network File System (NFS), TCP Port 2049 This is a network service used to support file sharing between dissimilar systems. Consider enclosing in a VPN for use.

- Simple Network Management Protocol (SNMP), UDP Port 161 (UDP Port 162 for Trap Messages) This is a network service used to collect network health and status information from a central monitoring station. Use the secure SNMPv3 only.

For more examples of secure protocols, see the later section “Secure Communication Protocols.”

# SNMPv3

Simple Network Management Protocol (SNMP) is a standard network-management protocol supported by most network devices and TCP/IP-compliant hosts. These include routers, switches, WAPs, firewalls, VPNs, printers, and so on. From a management console, you can use SNMP to interact with various network devices to obtain status information, performance data, statistics, and configuration details. Some devices support the modification of configuration settings through SNMP.

Early versions of SNMP relied on plaintext transmission of community strings as authentication. Communities are named collections of network devices. The original default community names were public and private. The latest version of SNMP allows for encrypted communications, as well as robust authentication protection.

UDP port 161 is used by the SNMP agent (that is, network device) to receive requests, and UDP port 162 is used by the management console to receive responses and notifications (also known as trap messages ). Trap messages inform the management console when an event or threshold violation occurs on a monitored system.
