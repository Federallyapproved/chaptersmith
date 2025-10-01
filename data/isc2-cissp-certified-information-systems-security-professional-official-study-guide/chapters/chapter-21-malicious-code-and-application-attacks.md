---
{
  "id": "chapter-262",
  "title": "Chapter 21: Malicious Code and Application Attacks",
  "order": 262,
  "source": {
    "href": "b01.xhtml",
    "anchor": "head-2-23"
  },
  "est_tokens": 1410,
  "slug": "chapter-21-malicious-code-and-application-attacks",
  "meta": {
    "nav_title": "Chapter 21: Malicious Code and Application Attacks",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Chapter 21: Malicious Code and Application Attacks

- D. User and entity behavior analytics (UEBA) tools develop profiles of individual behavior and then monitor users for deviations from those profiles that may indicate malicious activity and/or compromised accounts. This type of tool would meet Dylan's requirements. Endpoint detection and response (EDR) tools watch for unusual endpoint behavior but do not analyze user activity. Integrity monitoring is used to identify unauthorized system/file changes. Signature detection is a malware detection technique.

- B. All of these technologies are able to play important roles in defending against malware and other endpoint threats. User and entity behavior analysis (UEBA) looks for behavioral anomalies. Endpoint detection and response (EDR) and next-generation endpoint protection (NGEP) identify and respond to malware infections. However, only managed detection and response (MDR) combines antimalware capabilities with a managed service that reduces the burden on the IT team.

- C. If Carl has backups available, that would be his best option to recover operations. He could also pay the ransom, but this would expose his organization to legal risks and incur unnecessary costs. Rebuilding the systems from scratch would not restore his data. Installing antivirus software would be helpful in preventing future compromises, but these packages would not likely be able to decrypt the missing data.

- A. Although an advanced persistent threat (APT) may leverage any of these attacks, they are most closely associated with zero-day attacks due to the cost and complexity of the research required to discover or purchase them. Social engineering, Trojans (and other malware), and SQL injection attacks are often attempted by many different types of attackers.

- B. Buffer overflow vulnerabilities exist when a developer does not properly validate user input to ensure that it is of an appropriate size. Input that is too large can “overflow” a data structure to affect other data stored in the computer's memory. Time-of-check to time-of-use (TOCTTOU) attacks exploit timing differences that lead to race conditions. Cross-site scripting (XSS) attacks force the execution of malicious scripts in the user's browser. Cross-site request forgery (XSRF) attacks exploit authentication trust between browser tabs.

- B. TOC/TOU is a type of timing vulnerability that occurs when a program checks access permissions too far in advance of a resource request. Backdoors are code that allows those with knowledge of the backdoor to bypass authentication mechanisms. Buffer overflow vulnerabilities exist when a developer does not properly validate user input to ensure that it is of an appropriate size. Input that is too large can “overflow” a data structure to affect other data stored in the computer's memory. SQL injection attacks include SQL code in user input in the hopes that it will be passed to and executed by the backend database.

- D. The try…catch clause is used to attempt to evaluate code contained in the try clause and then handle errors with the code located in the catch clause. The other constructs listed here ( if…then , case…when , and do…while ) are all used for control flow.

`try…catch`

`try`

`catch`

`if…then`

`case…when`

`do…while`

- C. In this case, the .. operators are the telltale giveaway that the attacker was attempting to conduct a directory traversal attack. This particular attack sought to break out of the web server's root directory and access the /etc/passwd file on the server. SQL injection attacks would contain SQL code. File upload attacks seek to upload a file to the server. Session hijacking attacks require the theft of authentication tokens or other credentials.

`..`

`/etc/passwd`

- A. Logic bombs wait until certain conditions are met before delivering their malicious payloads. Worms are malicious code objects that move between systems under their own power, whereas viruses require some type of human intervention. Trojan horses masquerade as useful software but then carry out malicious functions after installation.

- D. The single quote character ( ' ) is used in SQL queries and must be handled carefully on web forms to protect against SQL injection attacks.

`'`

- B. Developers of web applications should leverage parameterized queries to limit the application's ability to execute arbitrary code. With stored procedures, the SQL statement resides on the database server and may only be modified by database developers or administrators. With parameterized queries, the SQL statement is defined within the application and variables are bound to that statement in a safe manner.

- C. Although any malware may be leveraged for financial gain, depending on its payload, cryptomalware is specifically designed for this purpose. It steals computing power and uses it to mine cryptocurrency. Remote access Trojans (RATs) are designed to grant attackers remote administrative access to systems. Potentially unwanted programs (PUPs) are any type of software that is initially approved by the user but then performs undesirable actions. Worms are malicious code objects that move between systems under their own power.

- A. Cross-site scripting attacks are often successful against web applications that include reflected input. This is one of the two main categories of XSS attack. In a reflected attack, the attacker can embed the attack within the URL so that it is reflected to users who follow a link.

- A, B, D. A programmer can implement the most effective way to prevent XSS by validating input, coding defensively, escaping metacharacters, and rejecting all script-like input.

- B. Input validation prevents cross-site scripting attacks by limiting user input to a predefined range. This prevents the attacker from including the HTML <SCRIPT> tag in the input.

`<SCRIPT>`

- A. The use of the <SCRIPT> tag is a telltale sign of a cross-site scripting (XSS) attack.

`<SCRIPT>`

- B. Backdoors are undocumented command sequences that allow individuals with knowledge of the backdoor to bypass normal access restrictions. Privilege escalation attacks, such as those carried out by rootkits, seek to upgrade normal user accounts to administrative access rights. Buffer overflows place excess input in a field in an attempt to execute attacker-supplied code.

- D. Elasticity provides for automatic provisioning and deprovisioning of resources to meet demand. Scalability only requires the ability to increase (but not decrease) available resources. Load balancing is the ability to share application load across multiple servers, and fault tolerance is the resilience of a system in the face of failures.

- D. The <SCRIPT> tag is used to indicate the beginning of an executable client-side script and is used in reflected input to create a cross-site scripting attack.

`<SCRIPT>`

- C. Trojan horses masquerade as useful programs (such as a game) but really contain malicious code that runs in the background. Logic bombs contain malicious code that is executed if certain specified conditions are met. Worms are malicious code objects that spread under their own power, while viruses spread through some human intervention.
