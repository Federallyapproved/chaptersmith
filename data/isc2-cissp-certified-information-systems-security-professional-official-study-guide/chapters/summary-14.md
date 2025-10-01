---
{
  "id": "chapter-173",
  "title": "Summary",
  "order": 173,
  "source": {
    "href": "c14.xhtml",
    "anchor": "head-2-268"
  },
  "est_tokens": 368,
  "slug": "summary-14",
  "meta": {
    "nav_title": "Summary",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Summary

This chapter covered several different access control models. With a Discretionary Access Control (DAC) model, all objects have an owner, and the owner has full control over the object. Role-Based Access Control models use roles or groups that often match the hierarchy of an organization. Administrators place users into roles and assign privileges to the roles based on jobs or tasks. Rule-based access controls use global rules that apply to all subjects equally. Attribute-Based Access Control (ABAC) models use policies that include attributes to assign access. Mandatory Access Control (MAC) models require all objects to have labels, and access is based on subjects having a matching label. Risk-based access controls evaluate the environment and the situation, and make risk-based decisions based on security policies.

Several internet-based authentication systems provide users with single sign-on (SSO) capabilities. SAML is an XML-based standard used to exchange authentication and authorization information. OAuth 2.0 is an authorization framework, and OpenID is used for authentication. OIDC uses OAuth 2.0, and it builds on the technologies used by OpenID. It uses a JSON Web Token as an ID token.

Kerberos is a popular single sign-on authentication protocol using tickets for authentication in internal networks. It uses a database of subjects, symmetric cryptography, and time synchronization of systems to issue tickets. RADIUS and TACACS+ are authentication, authorization, and accounting (AAA) protocols commonly used for remote access protocols, such as with VPNs.

Access control attacks include privilege escalation techniques to gain more rights and permissions. Passwords are a common authentication mechanism, and several types of attacks attempt to crack passwords. Password attacks include dictionary attacks, brute-force attacks, birthday attacks, rainbow table attacks, pass-the-hash attacks, Kerberos exploitation attacks, and sniffer attacks.
