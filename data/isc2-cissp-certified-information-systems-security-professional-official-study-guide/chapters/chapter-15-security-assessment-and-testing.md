---
{
  "id": "chapter-256",
  "title": "Chapter 15: Security Assessment and Testing",
  "order": 256,
  "source": {
    "href": "b01.xhtml",
    "anchor": "head-2-17"
  },
  "est_tokens": 822,
  "slug": "chapter-15-security-assessment-and-testing",
  "meta": {
    "nav_title": "Chapter 15: Security Assessment and Testing",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Chapter 15: Security Assessment and Testing

- A. Nmap is a network discovery scanning tool that reports the open ports on a remote system and the firewall status of those ports. OpenVAS is a network vulnerability scanning tool. Metasploit Framework is an exploitation framework used in penetration testing. lsof is a Linux command used to list open files on a system.

`lsof`

- D. Only open ports represent potentially significant security risks. Ports 80 and 443 are expected to be open on a web server. Port 1433 is a database port and should never be exposed to an external network. Port 22 is used for the Secure Shell protocol (SSH), and the filtered status indicates that nmap can't determine whether it is open or closed. This situation does require further investigation, but it is not as alarming as a definitely exposed database server port.

- C. The sensitivity of information stored on the system, difficulty of performing the test, and likelihood of an attacker targeting the system are all valid considerations when planning a security testing schedule. The desire to experiment with new testing tools should not influence the production testing schedule.

- C. Security assessments include many types of tests designed to identify vulnerabilities, and the assessment report normally includes recommendations for mitigation. The assessment does not, however, include actual mitigation of those vulnerabilities.

- A. Security assessment reports should be addressed to the organization's management. For this reason, they should be written in plain English and avoid technical jargon.

- C. Vulnerability scanners are used to test a system for known security vulnerabilities and weaknesses. They are not active detection tools for intrusion, they offer no form of enticement, and they do not configure system security. In addition to testing a system for security weaknesses, they produce evaluation reports and make recommendations.

- B. The server is likely running a website on port 80. Using a web browser to access the site may provide important information about the site's purpose.

- B. The SSH protocol uses port 22 to accept administrative connections to a server.

- D. Authenticated scans can read configuration information from the target system and reduce the instances of false positive and false negative reports.

- C. The TCP SYN scan sends a SYN packet and receives a SYN ACK packet in response, but it does not send the final ACK required to complete the three-way handshake.

- D. SQL injection attacks are web vulnerabilities, and Matthew would be best served by a web vulnerability scanner. A network vulnerability scanner might also pick up this vulnerability, but the web vulnerability scanner is specifically designed for the task and more likely to be successful.

- C. PCI DSS requires that Badin rescan the application at least annually and after any change in the application.

- B. Metasploit Framework is an automated exploit tool that allows attackers to easily execute common attack techniques. Nmap is a port scanning tool. OpenVAS is a network vulnerability scanner and Nikto is a web application scanner. While these other tools might identify potential vulnerabilities, they do not go as far as to exploit them.

- C. Mutation fuzzing uses bit flipping and other techniques to slightly modify previous inputs to a program in an attempt to detect software flaws.

- A. Misuse case testing identifies known ways that an attacker might exploit a system and tests explicitly to see if those attacks are possible in the proposed code.

- B. User interface testing includes assessments of both graphical user interfaces (GUIs) and command-line interfaces (CLIs) for a software program.

- B. During a white-box penetration test, the testers have access to detailed configuration information about the system being tested.

- B. Unencrypted HTTP communications take place over TCP port 80 by default.

- B. There are only two types of SOC report: Type I and Type II. Both reports provide information on the suitability of the design of security controls. Only a Type II report also provides an opinion on the operating effectiveness of those controls over an extended period of time.

- B. The backup verification process ensures that backups are running properly and thus meeting the organization's data protection objectives.
