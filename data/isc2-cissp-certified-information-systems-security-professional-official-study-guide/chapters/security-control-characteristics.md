---
{
  "id": "chapter-156",
  "title": "Security Control Characteristics",
  "order": 156,
  "source": {
    "href": "c12.xhtml",
    "anchor": "head-2-244"
  },
  "est_tokens": 416,
  "slug": "security-control-characteristics",
  "meta": {
    "nav_title": "Security Control Characteristics",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Security Control Characteristics

When you're selecting or deploying security controls for network communications, you need to evaluate numerous characteristics in light of your circumstances, capabilities, and security policy. Key characteristics are the protection of confidentiality and integrity. Since those issues are handled by encryption and hashing, please see Chapters 6 and 7 for those topics. Other important characteristics are transparency, logging, and error management.

### Transparency

Just as the name implies, transparency is the characteristic of a service, security control, or access mechanism that ensures that it is unseen by users. Transparency is often a desirable feature for security controls. The more transparent a security mechanism is, the less likely a user will be able to circumvent it or even be aware that it exists. With transparency, there is a lack of direct evidence that a feature, service, or restriction exists, and its impact on performance is minimal.

In some cases, transparency may need to function more as a configurable feature than as a permanent aspect of operation, such as when an administrator is troubleshooting, evaluating, or tuning a system's configurations.

### Transmission Management Mechanisms

Transmission logging is a form of auditing focused on communications. Transmission logging records the particulars about source, destination, time stamps, identification codes, transmission status, number of packets, size of message, and so on. These pieces of information may be useful in troubleshooting problems and tracking down unauthorized communications or used against a system as a means to extract data about how it functions.

Transmission error correction is a capability built into connection- or session-oriented protocols and services. If it is determined that a message, in whole or in part, was corrupted, altered, or lost, a request can be made for the source to resend all or part of the message. Retransmission controls determine whether all or part of a message is retransmitted in the event that a transmission error correction system discovers a problem with a communication. Retransmission controls can also determine whether multiple copies of a hash total or CRC (cyclic redundancy check) value are sent and whether multiple data paths or communication channels are employed.
