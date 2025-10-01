---
{
  "id": "chapter-258",
  "title": "Chapter 17: Preventing and Responding to Incidents",
  "order": 258,
  "source": {
    "href": "b01.xhtml",
    "anchor": "head-2-19"
  },
  "est_tokens": 1416,
  "slug": "chapter-17-preventing-and-responding-to-incidents",
  "meta": {
    "nav_title": "Chapter 17: Preventing and Responding to Incidents",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Chapter 17: Preventing and Responding to Incidents

- B, C, D. Detection, reporting, and lessons learned are valid incident management steps. Prevention is done before an incident. Creating backups can help recover systems, but it isn't one of the incident management steps. The seven steps (in order) are detection, response, mitigation, reporting, recovery, remediation, and lessons learned.

- A. Your next step is to isolate the computer from the network as part of the mitigation phase. You might look at other computers later, but you should try to mitigate the problem first. Similarly, you might run an antivirus scan, but later. The lessons learned phase is last and will analyze an incident to determine the cause.

- D. The first step is detection. The seven steps (in order) are detection, response, mitigation, reporting, recovery, remediation, and lessons learned.

- A, C, D. The three basic security controls listed are 1) keep systems and applications up to date, 2) remove or disable unneeded services or protocols, and 3) use up-to-date antimalware software. SOAR technologies implement advanced methods to detect and automatically respond to incidents. It's appropriate to place a network firewall at the border (between the internet and the internal network), but web application firewalls (WAF) should only filter traffic going to a web server.

- B. Audit trails provide documentation on what happened, when it happened, and who did it. IT personnel create audit trails by examining logs. Authentication of individuals is also needed to ensure that the audit trails provide proof of identities listed in the logs. Identification occurs when an individual claims an identity, but identification without authentication doesn't provide accountability. Authorization grants individuals access to resources based on their proven identity. Confidentiality ensures that unauthorized entities can't access sensitive data and is unrelated to this question.

- B. The first step should be to copy existing logs to a different drive so that they are not lost. If you enable rollover logging, you are configuring the logs to overwrite old entries. It's not necessary to review the logs before copying them. If you delete the oldest log entries first, you may delete valuable data.

- A. Fraggle is a denial of service (DoS) attack that uses UDP. Other attacks, such as a SYN flood attack, use TCP. A smurf attack is similar to a fraggle attack, but it uses ICMP. SOAR is a group of technologies that provide automated responses to common attacks, not a protocol.

- A. A zero-day exploit is an attack that exploits a vulnerability that doesn't have a patch or fix. A newly discovered vulnerability is only a vulnerability until someone tries to exploit it. Attacks on unpatched systems aren't zero-day exploits. A virus is a type of malware that delivers its payload after a user launches an application.

- C. This is a false positive. The IPS falsely identified normal web traffic as an attack and blocked it. A false negative occurs when a system doesn't detect an actual attack. A honeynet is a group of honeypots used to lure attackers. Sandboxing provides an isolated environment for testing and is unrelated to this question.

- D. An anomaly-based IDS requires a baseline, and it then monitors traffic for any anomalies or changes when compared to the baseline. It's also called behavior based and heuristics based. Pattern-based detection (also known as knowledge-based detection and signature-based detection) uses known signatures to detect attacks.

- B. An NIDS will monitor all traffic and raise alerts when it detects suspicious traffic. A HIDS only monitors a single system. A honeynet is a network of honeypots used to lure attackers away from live networks. A network firewall filters traffic, but it doesn't raise alerts on suspicious traffic.

- A. This describes an NIPS. It is monitoring network traffic, and it is placed in line with the traffic. An NIDS isn't placed in line with the traffic, so it isn't the best choice. Host-based systems only monitor traffic sent to specific hosts, not network traffic.

- D. A drawback of some HIDSs is that they interfere with a single system's normal operation by consuming too many resources. The other options refer to applications that aren't installed on user systems.

- B. An IDS is most likely to connect to a switch port configured as a mirrored port. An IPS is placed in line with traffic, so it is placed before the switch. A honeypot doesn't need to see all traffic going through a switch. A sandbox is an isolated area often used for testing and would not need all traffic from a switch.

- B. A false negative occurs when there is an attack but the IDS doesn't detect it and raise an alarm. In contrast, a false positive occurs when an IDS incorrectly raises an alarm, even though there isn't an attack. The attack may be a UDP-based fraggle attack or an ICMP-based smurf attack, but the attack is real, and since the IDS doesn't detect it, it is a false negative.

- B. An anomaly-based IDS (also known as a behavior-based IDS) can detect new security threats. A signature-based IDS only detects attacks from known threats. An active IDS identifies the response after a threat is detected. A network-based IDS can be both signature based and anomaly based.

- B. A security information and event management (SIEM) system is a centralized application that monitors multiple systems. Security orchestration, automation, and response (SOAR) is a group of technologies that provide automated responses to common attacks. A host-based intrusion detection system (HIDS) is decentralized because it is on one system only. A threat feed is a stream of data on current threats.

- D. A network-based data loss prevention (DLP) system monitors outgoing traffic (egress monitoring) and can thwart data exfiltration attempts. Network-based intrusion detection systems (NIDSs) and intrusion protection systems (IPSs) primarily monitor incoming traffic for threats. Firewalls can block traffic or allow traffic based on rules in an access control list (ACL), but they can't detect unauthorized data exfiltration attacks.

- A. Threat hunting is the process of actively searching for infections or attacks within a network. Threat intelligence refers to the actionable intelligence created after analyzing incoming data, such as threat feeds. Threat hunters use threat intelligence to search for specific threats. Additionally, they may use a kill chain model to mitigate these threats. Artificial intelligence (AI) refers to actions by a machine, but the scenario indicates administrators are doing the work.

- A. Security orchestration, automation, and response (SOAR) technologies provide automated responses to common attacks, reducing an administrator's workload. A security information and event management (SIEM) system is a centralized application that monitors log entries from multiple sources. A network-based intrusion detection system (NIDS) raises the alerts. A data loss prevention (DLP) system helps with egress monitoring and is unrelated to this question.
