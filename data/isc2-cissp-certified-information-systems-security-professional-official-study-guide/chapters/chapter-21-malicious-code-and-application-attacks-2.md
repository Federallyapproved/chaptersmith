---
{
  "id": "chapter-283",
  "title": "Chapter 21: Malicious Code and Application Attacks",
  "order": 283,
  "source": {
    "href": "b02.xhtml",
    "anchor": "head-2-44"
  },
  "est_tokens": 244,
  "slug": "chapter-21-malicious-code-and-application-attacks-2",
  "meta": {
    "nav_title": "Chapter 21: Malicious Code and Application Attacks",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Chapter 21: Malicious Code and Application Attacks

- Viruses and worms both travel from system to system attempting to deliver their malicious payloads to as many machines as possible. However, viruses require human intervention, such as sharing a file, network resource, or email message, to propagate. Worms, on the other hand, seek out vulnerabilities and spread from system to system under their own power, thereby greatly magnifying their reproductive capability, especially in a well-connected network.

- If possible, antivirus software may try to disinfect an infected file, removing the virus's malicious code. If that fails, it might either quarantine the file for manual review or automatically delete it to prevent further infection.

- Data integrity assurance packages like Tripwire compute hash values for each file stored on a protected system. If a file infector virus strikes the system, this would result in a change in the affected file's hash value and would therefore trigger a file integrity alert.

- Defending against SQL injection vulnerabilities requires a defense-in-depth approach. It may include the use of whitelisting and/or blacklisting input validation, stored procedures/parameterized queries, web application security scans, web application firewalls, and other controls.
