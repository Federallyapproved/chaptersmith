---
{
  "id": "chapter-171",
  "title": "Implementing Authentication Systems",
  "order": 171,
  "source": {
    "href": "c14.xhtml",
    "anchor": "head-2-263"
  },
  "est_tokens": 4529,
  "slug": "implementing-authentication-systems",
  "meta": {
    "nav_title": "Implementing Authentication Systems",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Implementing Authentication Systems

Authentication systems simplify the management of authentication on the internet and in internal networks. Chapter 13 discusses federated identity management (FIM) and single sign-on (SSO) concepts in more depth, but as a reminder, FIM allows different organizations to use federations for SSO. For example, after an employee logs on to Company A's network, they can then access resources on Company B's network without logging on again.

### Implementing SSO on the Internet

Beyond federated identity management systems, many sites support SSO to simplify the user experience. They also provide security to users by ensuring their credentials on one site are not shared with other sites.

Imagine you want to transfer money from Bank A to Bank B. You could give Bank B your credentials to Bank A and have them transfer the money. Sound scary? You bet. You should never be required to give your credentials to any third party. Solutions such as SAML, OAuth, OpenID, and OIDC help solve this problem. They share authentication, authorization, or profile information about a user, and some solutions share all three.

#### XML

Extensible Markup Language (XML) goes beyond describing how to display the data by actually describing the data. XML can include tags to describe data as anything desired. For example, the following tag identifies the data as the results of taking an exam: <ExamResults>Passed</ExamResults> .

`<ExamResults>Passed</ExamResults>`

Databases from multiple vendors can import and export data to and from an XML format, making XML a common language used to exchange information. Many specific schemas exist, and if companies agree on what schema to use, they can easily share information. Many cloud-based providers use XML-based languages to share information for authentication and authorization. They don't use XML as it is but instead use other languages based on XML.

#### SAML

Security Assertion Markup Language (SAML) is an open XML-based standard commonly used to exchange authentication and authorization (AA) information between federated organizations. It provides SSO capabilities for browser access.

The Organization for the Advancement of Structured Information Standards (OASIS), a nonprofit consortium that encourages open standards development, adopted SAML 2.0 as an OASIS standard in 2005 and has maintained it since then. SAML 2.0 is a convergence of SAML 1.1, the Liberty Alliance Identity Federation Framework (ID-FF) 1.2, and Shibboleth 1.3.

The SAML 2.0 specification utilizes three entities: the principal, the service provider, and the identity provider. For example, imagine Sally is accessing her investment account at ucanbeamillionaire.com . The site requires her to log on to access her account, and the site uses SAML.

- Principal or User Agent For simplicity, think of Sally as the principal. She's trying to access her investment account at ucanbeamillionaire.com .

- Service Provider (SP) In this scenario, the ucanbeamillionaire.com site is providing the service and is the service provider.

- Identity Provider (IdP) This is a third party that holds the user authentication and authorization information.

When Sally accesses the site, it prompts her to enter her credentials. When she does, the site sends her credentials to the IdP. The IdP then responds with XML messages validating (or rejecting) Sally's credentials and indicating what she is authorized to access. The site then grants her access to her account.

The IdP can send three types of XML messages known as assertions:

- Authentication Assertion This provides proof that the user agent provided the proper credentials, identifies the identification method, and identifies the time the user agent logged on.

- Authorization Assertion This indicates whether the user agent is authorized to access the requested service. If the message indicates access is denied, it indicates why.

- Attribute Assertion Attributes can be any information about the user agent.

Clearly, there is much more going on here. If you want to dig into the details, the www.oasis-open.org/standards site has more details on SAML 2.0.

Many cloud service providers include SAML in their solutions because it simplifies the services for their customers. SAML provides authentication assertion, attribute assertion, and authorization assertion.

SAML is a popular SSO standard on the internet. It is used to exchange authentication and authorization (AA) information.

#### OAuth

OAuth 2.0 (implying open authorization) is an authorization framework described in RFC 6749 and maintained by the Internet Engineering Task Force (IETF). Many companies on the internet use it to share account information with third-party websites.

For example, imagine you have a Twitter account, and you download an app called Acme that can interact with your Twitter account and schedule Tweets in advance. When you try to use the feature in the Acme app, it redirects you to Twitter. Twitter prompts you to log on, shows you what permissions the Acme app will access, and then asks if you want to authorize the Acme app to access your Twitter app. If you approve, Twitter sends the Acme app an authorization token. The app may accept and enter the authorization token directly, or you may need to enter it into the app's settings. When the app accesses the Twitter account, it sends an API message and includes the token. Note that this doesn't provide authentication. Instead, it authorizes access to the account. A primary benefit is that you never provide your Twitter credentials to the Acme app. Even if the Acme app is compromised, it does not expose your credentials.

Many online sites support OAuth 2.0 but not OAuth 1.0, and OAuth 2.0 is not backward compatible with OAuth 1.0.

OAuth is an authorization framework, not an authentication protocol. It exchanges API messages and uses a token to show that access is authorized.

#### OpenID

OpenID is also an open standard, but it is maintained by the OpenID Foundation rather than as an RFC standard. It provides decentralized authentication, allowing users to log into multiple unrelated websites with one set of credentials maintained by a third-party service referred to as an OpenID provider.

When users go to an OpenID-enabled website (also known as a relying party ), they are prompted to provide their OpenID identity as a URI. The OpenID-enabled website and an OpenID provider exchange data and create a secure channel. The user is then redirected to the OpenID provider and is prompted to provide the password. If correct, the user is redirected back to the OpenID-enabled site.

To see how this works, check out this site: openidexplained.com/use . The site doesn't support HTTPS so use HTTP. One thing you'll see is that it's always obvious when you're using OpenID because you have to enter your OpenID identifier. For example, if your OpenID identifier is bobsmith2021.myopenid.com , that's what you have to enter. In contrast, other methods exchange data behind the scenes, so it isn't as obvious what method is being used.

#### OIDC

OpenID Connect (OIDC) is an authentication layer using the OAuth 2.0 authorization framework. A key point is that it provides both authentication and authorization. Like OpenID, it is maintained by the OpenID Foundation.

It builds on the technologies created with OpenID but uses a JavaScript Object Notation (JSON) Web Token (JWT), also called an ID token. OpenID Connect uses a web service to retrieve the JWT. In addition to providing authentication, the JWT can also include profile information about the user.

Most of this occurs behind the scenes, but you can see it in action by logging onto eBay with a Google account. These processes and interfaces change over time, but the general steps are as follows:

- If you don't have a Google account, create one first.

- Ensure you're logged out of eBay and Google, go to ebay.com , and click Sign In.

- Click Continue With Google. A dialog box opens, prompting you to enter your Google email. It also indicates what Google will share with ebay.com .

- Enter your email address and press Enter.

- Enter your password and click Next.

- If you've enabled 2-Step Verification on your Google account, you'll be prompted to get the code and enter it.

You don't need to complete the creation of an eBay account with your Google account. However, if you choose to do so, click the Create Account button. You'll now be logged on to eBay using your Google account. If you log out of eBay and try to log on again, all you need to do is click Sign In and then click Continue with Google. As long as you're still logged on with Google, you'll be logged into eBay without any more steps.

OAuth and OIDC are used with many web-based applications to share information without sharing credentials. OAuth provides authorization. OIDC uses the OAuth framework for authorization and builds on the OpenID technologies for authentication. OIDC uses JSON Web Tokens.

#### Comparing SAML, OAuth, OpenID, and OIDC

It's easy to mix up the differences between SAML, OAuth, OpenID, and OIDC. This section summarizes key points of each one and points out some of the differences.

The following bullets outline the key points about SAML:

- SAML 2.0 is an open XML-based standard.

- OASIS adopted it as a standard in 2005.

- It utilizes three entities: a principal (such as a user), a service provider (such as a website), and an identity provider (a third party that holds the authentication and authorization information).

- It can provide authentication, authorization, and attribute information on the principal.

The following bullets outline the key points about OAuth:

- It's an authorization framework, not an authentication protocol.

- RFC 6749 describes OAuth 2.0.

- It exchanges information using APIs.

- An app obtains an access token from an identity provider.

- Later, the app includes the access token for authorization.

The following bullets outline the key points about OpenID:

- OpenID is an authentication standard.

- It is maintained by the OpenID Foundation.

- An OpenID provider provides decentralized authentication.

- Users enter their Open ID identifier (such as bobsmith2021.myopenid.com ) on a site and the OpenID provider verifies the identifier.

The following bullets outline the key points about OIDC:

- OIDC is an authentication layer using OAuth 2.0.

- It builds on the OpenID authentication standard.

- It provides both authentication and authorization.

- It builds on OpenID but uses a JSON Web Token.

### Implementing SSO on Internal Networks

SSO solutions are also used on internal networks. Kerberos is the most common, and it's an important authentication system to know for the CISSP exam. Network access methods allow users to access internal networks from remote locations (such as at home). Two common remote access protocols are RADIUS and TACACS+. In addition to supporting SSO, RADIUS and TACAS+ provide authentication, authorization, and accounting.

#### AAA Protocols

Several protocols provide authentication, authorization, and accounting and are referred to as AAA protocols. These provide centralized access control with remote access systems such as virtual private networks (VPNs) and other types of network access servers. They help protect internal LAN authentication systems and other servers from remote attacks. If you are using a separate system for remote access, a successful attack on the system only affects the remote access users. In other words, the attacker won't have access to internal accounts.

These AAA protocols use the access control elements of identification, authentication, authorization, and accountability as described in Chapter 13 . They ensure that users have valid credentials to authenticate and verify that they are authorized to connect to the remote access server based on the user's proven identity. Additionally, the accounting element can track the user's network resource usage, which can be used for billing purposes. Some common AAA protocols are covered next.

#### Kerberos

Ticket authentication is a mechanism that employs a third-party entity to prove identification and provide authentication. The most common and well-known ticket system is Kerberos . The primary purpose of Kerberos is authentication. After users authenticate and prove their identity, Kerberos uses their proven identity to issue tickets, and user accounts present these tickets when accessing resources.

The Kerberos name is borrowed from Greek mythology. A three-headed dog named Kerberos, sometimes referred to as Cerberus, guards the gates to the underworld. The dog faces inward, preventing escape rather than denying entrance.

Kerberos offers a single sign-on solution for users and protects logon credentials. Kerberos version 5 relies on symmetric-key cryptography (also known as secret-key cryptography) using the Advanced Encryption Standard (AES) symmetric encryption protocol. Kerberos provides confidentiality and integrity for authentication traffic using end-to-end security and helps protect against eavesdropping and replay attacks. Chapter 6 , “Cryptography and Symmetric Key Algorithms,” covers symmetric key encryption in greater depth.

Many of the Kerberos roles are on a single server, but they can be installed on different servers. Larger networks sometimes separate them to increase performance, but smaller networks typically have one Kerberos server performing all of the different roles.

Kerberos uses several different elements that are important to understand:

- Key Distribution Center The Key Distribution Center is the trusted third party that provides authentication services. Kerberos uses symmetric-key cryptography to authenticate clients to servers. All clients and servers are registered with the KDC, and it maintains the secret keys for all network members.

- Kerberos Authentication Server The authentication server hosts the functions of the KDC: a ticket-granting service (TGS) and an authentication service (AS). However, it is possible to host the ticket-granting service on another server. The authentication service verifies or rejects the authenticity and timeliness of tickets. This server is often called the KDC.

- Ticket A ticket is an encrypted message that provides proof that a subject is authorized to access an object. It is sometimes called a service ticket (ST). Subjects (such as users) request tickets to access objects (such as files), and if they have authenticated and are authorized to access the object, Kerberos issues them a ticket. Kerberos tickets have specific lifetimes and usage parameters. Once a ticket expires, a client must request a renewal or a new ticket to continue communications with any server.

- Ticket-Granting Ticket A ticket-granting ticket (TGT) provides proof that a subject has authenticated through a KDC and is authorized to request tickets to access other objects. A TGT is encrypted and includes a symmetric key, an expiration time, and the user's IP address. Subjects present the TGT when requesting tickets to access objects.

- Kerberos Principal Kerberos issues tickets to Kerberos principals. A Kerberos principal is typically a user but can be any entity that can request a ticket.

- Kerberos Realm Generically, a realm is an area controlled or ruled by something. A Kerberos realm is a logical area (such as a domain or network) ruled by Kerberos. Principals within the realm can request tickets from Kerberos, and Kerberos can issue tickets to principals in the realm.

Kerberos requires a database of accounts, typically stored in a directory service such as Microsoft's Active Directory (AD). It exchanges tickets between clients, network servers, and the KDC to prove identity and provide mutual authentication. This allows a client to request resources from the server, with both the client and server having assurances of the identity of the other. These encrypted tickets also ensure that login credentials, session keys, and authentication messages are never transmitted in cleartext.

The Kerberos login process works as follows:

- The user types a username and password into the client.

- The client encrypts the username with AES for transmission to the KDC.

- The KDC verifies the username against a database of known credentials.

- The KDC generates a symmetric key that will be used by the client and the Kerberos server. It encrypts this with a hash of the user's password. The KDC also generates an encrypted timestamped TGT.

- The KDC then transmits the encrypted symmetric key and the encrypted timestamped TGT to the client.

- The client installs the TGT for use until it expires. The client also decrypts the symmetric key using a hash of the user's password.

Note that the client's password is never transmitted over the network, but it is verified. The server encrypts a symmetric key using a hash of the user's password, and it can only be decrypted with a hash of the user's password. As long as the user enters the correct password, this step works. However, it fails if the user enters the incorrect password.

When a client wants to access an object, such as a resource hosted on the network, it must request a ticket through the Kerberos server. The following steps are involved in this process:

- The client sends its TGT back to the KDC with a request for access to the resource.

- The KDC verifies that the TGT is valid and checks its access control matrix to verify that the user has sufficient privileges to access the requested resource.

- The KDC generates a service ticket and sends it to the client.

- The client sends the ticket to the server or service hosting the resource.

- The server or service hosting the resource verifies the validity of the ticket with the KDC.

- Once identity and authorization are verified, Kerberos activity is complete. The server or service host then opens a session with the client and begins communications or data transmission.

Kerberos is a versatile authentication mechanism that works over local LANs, remote access, and client/server resource requests. However, Kerberos presents a single point of failure—the KDC. If the KDC is compromised, the secret key for every system on the network is also compromised. Also, if a KDC goes offline, no subject authentication can occur.

It also has strict time requirements, and the default configuration requires that all systems be time-synchronized within 5 minutes of each other. If a system is not synchronized or the time is changed, a previously issued TGT will no longer be valid, and the system will not be able to receive any new tickets. In effect, the client will be denied access to any protected network resources.

Administrators often configure a time synchronization system within a network. In an Active Directory domain, one domain controller (DC) synchronizes its time with an external Network Time Protocol (NTP) server. All other DCs synchronize their time with the first DC. All other systems synchronize their time with one of the DCs when they log on.

#### RADIUS

Remote Authentication Dial-in User Service (RADIUS) centralizes authentication for remote access connections, such as with VPNs or dial-up access. It is typically used when an organization has more than one network access server (or remote access server). A user can connect to any network access server, which then passes on the user's credentials to the RADIUS server to verify authentication and authorization and to track accounting. In this context, the network access server is the RADIUS client, and a RADIUS server acts as an authentication server. The RADIUS server also provides AAA services for multiple remote access servers.

Many internet service providers (ISPs) use RADIUS for authentication. Users can access the ISP from anywhere, and the ISP server then forwards the user's connection request to the RADIUS server.

Organizations can also use RADIUS, and organizations often implement it with location-based security. For example, if the user connects with an IP address, the system can use geolocation technologies to identify the user's location. Although it isn't as common today, some users still have Integrated Services Digital Network (ISDN) dial-up lines and use them to connect to VPNs. The RADIUS server can use callback security for an extra layer of protection. Users call in, and after authentication, the RADIUS server terminates the connection and initiates a call back to the user's predefined phone number. If a user's authentication credentials are compromised, the callback security prevents an attacker from using them.

RADIUS uses the User Datagram Protocol (UDP) by default and encrypts only the password's exchange. It doesn't encrypt the entire session, but RADIUS can use other protocols to encrypt the data session. The current version is defined in RFC 2865. RFC 6614, designated as Experimental, defines how RADIUS can use Transport Layer Security (TLS) over Transmission Control Protocol (TCP).

When using TLS, RADIUS uses TCP port 2083. RADIUS uses UDP port 1812 for RADIUS messages and UDP port 1813 for RADIUS Accounting messages.

# RADIUS/TLS or RadSec

RFC 6614 documents how to secure RADIUS traffic with RADIUS/TLS. It is based on how Open System Consultants used their Radiator RADIUS product with the internally designed RadSec protocol. Interestingly, an early draft of RADIUS/TLS was called TLS encryption for RADIUS over TCP (RadSec). However, RFC 6614 omitted the parenthetical RadSec. Radiator Software still sells Radiator and refers to RadSec as “secure, reliable RADIUS proxying.”

When taking the CISSP exam, you should know that RADIUS encrypts only the password's exchange by default, but it is possible to use RADIUS/TLS to encrypt the entire session. Because authoritative documents don't refer to RADIUS/TLS as RADSEC, it's unlikely that you'll see this on the exam.

RADIUS provides AAA services between network access servers and a shared authentication server. The network access server is the client of the RADIUS authentication server.

#### TACACS+

Cisco developed Terminal Access Controller Access Control System Plus (TACACS+) and later released it as an open standard. It provides several improvements over the earlier versions and over RADIUS.

It separates authentication, authorization, and accounting into separate processes, which can be hosted on three different servers if desired. Additionally, TACACS+ encrypts all of the authentication information, not just the password, as RADIUS does. TACACS+ uses TCP port 49, providing a higher level of reliability for the packet transmissions.
