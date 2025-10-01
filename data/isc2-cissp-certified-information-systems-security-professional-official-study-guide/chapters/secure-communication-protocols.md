---
{
  "id": "chapter-131",
  "title": "Secure Communication Protocols",
  "order": 131,
  "source": {
    "href": "c11.xhtml",
    "anchor": "head-2-206"
  },
  "est_tokens": 645,
  "slug": "secure-communication-protocols",
  "meta": {
    "nav_title": "Secure Communication Protocols",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Secure Communication Protocols

Protocols that provide security services for application-specific communication channels are called secure communication protocols. Examples include the following:

- IPsec Internet Protocol Security (IPsec) uses public key cryptography to provide encryption, access control, nonrepudiation, and message authentication, all using IP-based protocols. The primary use of IPsec is for virtual private networks (VPNs), so IPsec can operate in either transport or tunnel mode. IPsec is a standard of IP security extensions used as an add-on for IPv4 and integrated into IPv6. IPsec is discussed further in Chapter 12 .

- Kerberos Kerberos offers a single sign-on (SSO) solution for users and provides protection for logon credentials. Modern implementations of Kerberos use hybrid encryption to provide reliable authentication protection. Kerberos is discussed further in Chapter 14 , “Controlling and Monitoring Access.”

- SSH Secure Shell (SSH) is a good example of an end-to-end encryption technique. This security tool can be used to encrypt numerous plaintext utilities (such as rcp , rlogin , and rexec ), serve as a protocol encrypter (such as with SFTP), and function as a transport mode VPN (i.e., host to host and link encryption only). SSH is discussed further in Chapter 12 .

`rcp`

`rlogin`

`rexec`

- Signal Protocol This is a cryptographic protocol that provides end-to-end encryption for voice communications, videoconferencing, and text message services. The Signal Protocol is nonfederated and is a core element in the messaging app named Signal.

- Secure Remote Procedure Call (S-RPC) S-RPC is an authentication service for cross-network service communications and is simply a means to prevent unauthorized execution of code on remote systems.

- Transport Layer Security (TLS) This is an encryption protocol that operates at OSI layer 4 (by encrypting the payload of TCP communications). Though it is primarily known to be used to encrypt web communications as HTTPS, it can encrypt any Application layer protocol. Transport Layer Security (TLS) replaced Secure Sockets Layer (SSL) , which was officially deprecated in 2015. Features of TLS include the following: Supports secure client-server communications across an insecure network while preventing tampering, spoofing, and eavesdropping. Supports one-way authentication. Supports two-way authentication using digital certificates. Often implemented as the initial payload of a TCP package, allowing it to encapsulate all higher-layer protocol payloads. Can be used to encrypt User Datagram Protocol (UDP) and Session Initiation Protocol (SIP) connections. (SIP is a protocol associated with Voice over IP [VoIP].)

- Supports secure client-server communications across an insecure network while preventing tampering, spoofing, and eavesdropping.

- Supports one-way authentication.

- Supports two-way authentication using digital certificates.

- Often implemented as the initial payload of a TCP package, allowing it to encapsulate all higher-layer protocol payloads.

- Can be used to encrypt User Datagram Protocol (UDP) and Session Initiation Protocol (SIP) connections. (SIP is a protocol associated with Voice over IP [VoIP].)
