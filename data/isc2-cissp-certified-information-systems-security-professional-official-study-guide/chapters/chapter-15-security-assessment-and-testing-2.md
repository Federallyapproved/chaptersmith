---
{
  "id": "chapter-277",
  "title": "Chapter 15: Security Assessment and Testing",
  "order": 277,
  "source": {
    "href": "b02.xhtml",
    "anchor": "head-2-38"
  },
  "est_tokens": 484,
  "slug": "chapter-15-security-assessment-and-testing-2",
  "meta": {
    "nav_title": "Chapter 15: Security Assessment and Testing",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Chapter 15: Security Assessment and Testing

- TCP SYN scanning sends a single packet to each scanned port with the SYN flag set. This indicates a request to open a new connection. If the scanner receives a response that has the SYN and ACK flags set, this indicates that the system is moving to the second phase in the three-way TCP handshake and that the port is open. TCP SYN scanning is also known as “half-open” scanning. TCP connect scanning opens a full connection to the remote system on the specified port. This scan type is used when the user running the scan does not have the necessary permissions to run a half-open scan.

- The three possible port status values returned by nmap are as follows: Open—The port is open on the remote system and there is an application that is actively accepting connections on that port. Closed—The port is accessible on the remote system, meaning that the firewall is allowing access, but there is no application accepting connections on that port. Filtered—Nmap is unable to determine whether a port is open or closed because a firewall is interfering with the connection attempt.

- Open—The port is open on the remote system and there is an application that is actively accepting connections on that port.

- Closed—The port is accessible on the remote system, meaning that the firewall is allowing access, but there is no application accepting connections on that port.

- Filtered—Nmap is unable to determine whether a port is open or closed because a firewall is interfering with the connection attempt.

- Static software testing techniques, such as code reviews, evaluate the security of software without running it by analyzing either the source code or the compiled application. Dynamic testing evaluates the security of software in a runtime environment and is often the only option for organizations deploying applications written by someone else.

- Mutation (dumb) fuzzing takes previous input values from actual operation of the software and manipulates (or mutates) it to create fuzzed input. It might alter the characters of the content, append strings to the end of the content, or perform other data manipulation techniques. Generational (intelligent) fuzzing develops data models and creates new fuzzed input based on an understanding of the types of data used by the program.

Generational (intelligent) fuzzing develops data models and creates new fuzzed input based on an understanding of the types of data used by the program.
