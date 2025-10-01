---
{
  "id": "chapter-84",
  "title": "Secure Design Principles",
  "order": 84,
  "source": {
    "href": "c08.xhtml",
    "anchor": "head-2-142"
  },
  "est_tokens": 5527,
  "slug": "secure-design-principles",
  "meta": {
    "nav_title": "Secure Design Principles",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Secure Design Principles

Security should be a consideration at every stage of a system's development. Programmers, developers, engineers, and so on should strive to build security into every application or system they develop, with greater levels of security provided to critical applications and those that process sensitive information. It's extremely important to consider the security implications of a development project in the early stages because it's much easier to build security into a system during development than it is to add security to an existing system. Developers should research, implement, and manage engineering processes using secure design principles.

In addition to the secure design principles of CISSP Objective 3.1, there are other common lists of such principles. These include the US-CERT list at us-cert.cisa.gov/bsi/articles/knowledge/principles/design-principles .

### Objects and Subjects

Controlling access to any resource in a secure system involves two entities. The subject is the active entity that makes a request to access a resource. A subject is commonly a user, but it can also be a process, program, computer, or organization. The object is the passive entity that the subject wants to access. An object is commonly a resource, such as a file or printer, but it can also be a user, process, program, computer, or organization. You want to keep a broad understanding of the terms of subject and object, rather than only considering users and files. Access is the relationship between a subject and object, which could include reading, writing, changing, deleting, printing, moving, backing up, and many other operations or activities.

Keep in mind that the actual entities referenced by the terms subject and object are specific to an individual access request. The entity serving as the object in one access event could serve as the subject in another. For example, process A may ask for data from process B. To satisfy process A's request, process B must ask for data from process C. In this example ( Table 8.1 ), process B is the object of the first request and the subject of the second request.

TABLE 8.1 Subjects and objects

TABLE 8.1 Subjects and objects

This also serves as an example of transitive trust. Transitive trust is the concept that if A trusts B and B trusts C, then A inherits trust of C through the transitive property ( Figure 8.1 )—which works like it would in a mathematical equation: if a = b and b = c, then a = c. In the previous example, when A requests data from B and then B requests data from C, the data that A receives is essentially from C. Transitive trust is a serious security concern because it may enable bypassing of restrictions or limitations between A and C, especially if A and C both support interaction with B. An example of this would be when an organization blocks access to Facebook or YouTube to increase worker productivity. Thus, workers (A) do not have access to certain internet sites (C). However, if workers are able to have access to a web proxy, virtual private network (VPN), or anonymization service, then this can serve as a means to bypass the local network restriction. In other words, if workers (A) are accessing VPN service (B), and the VPN service (B) can access the blocked internet service (C), then A is able to access C through B via a transitive trust exploitation.

FIGURE 8.1 Transitive trust

FIGURE 8.1 Transitive trust

### Closed and Open Systems

Systems are designed and built according to one of two differing philosophies. A closed system is designed to work well with a narrow range of other systems, generally all from the same manufacturer. The standards for closed systems are often proprietary and not normally disclosed. Open systems , on the other hand, are designed using agreed-upon industry standards. Open systems are much easier to integrate with systems from different manufacturers that support the same standards or that use compatible application programming interfaces (APIs) .

An API is a defined set of interactions allowed between computing elements, such as applications, services, networking, firmware, and hardware. An API defines the types of requests that can be made, the exact means to make the requests, the data forms of the exchange, and other related requirements (such as authentication and/or session encryption). APIs make interoperability of computing elements possible. Without APIs, computing components would be unable to directly interact and information sharing would not be easy. APIs are what make modern computing and the internet possible. The app on your smartphone talks to the phone's operating system via an API; the phone's operating system talks over the telco or Wi-Fi network via an API to reach the cloud service's API in order to submit a request and receive a response.

Closed systems are harder to integrate with unlike systems, but this “feature” could make them more secure. A closed system is often composed of proprietary hardware and software that does not incorporate industry standards or offer an open API. This lack of integration ease means that attacks that typically focus on generic system components either will not work or must be customized to be successful. In many cases, attacking a closed system is harder than launching an attack on an open system, since a unique exploit of a unique vulnerability would be required. In addition to the lack of known vulnerable components on a closed system, it is often necessary to possess more in-depth knowledge of the specific target system to launch a successful attack.

Open systems are generally far easier to integrate with other open systems. It is easy, for example, to create a local area network (LAN) with a Microsoft Windows Server machine, a Linux machine, and a Macintosh machine. Although all three computers use different operating systems and could represent up to three different hardware architectures, each supports industry standards and open APIs, which makes it easy for network (or other) communications to occur. This ease of interoperability comes at a price, however. Because standard communications components are incorporated into each of these three open systems, there are far more predictable entry points and methods for launching attacks. In general, their openness makes them more vulnerable to attack, and their widespread availability makes it possible for attackers to find plenty of potential targets. Also, open systems are more popular and widely deployed than closed systems and thus attract more attention from attackers. An attacker who develops basic attacking skills will find more targets that are open systems than closed ones. Inarguably, there's a greater body of shared experience and knowledge on how to attack open systems than there is for closed systems. The security of an open system is therefore more dependent on the use of secure and defensive coding practices and a thoughtful defense-in-depth deployment strategy (see Chapter 1 ).

# Open Source vs. Closed Source

It's also helpful to keep in mind the distinction between open source and closed source systems. An open source solution is one where the source code, and other internal logic, is exposed to the public. A closed source solution is one where the source code and other internal logic is hidden from the public. Open source solutions often depend on public inspection and review to improve the product over time. Closed source solutions are more dependent on the vendor/programmer to revise the product over time. Both open source and closed source solutions can be available for sale or at no charge, but the term commercial typically implies closed source. However, closed source code is sometimes revealed through either vendor compromise or through decompiling or disassembly. The former is always a breach of ethics and often the law, whereas the latter is a standard element in ethical reverse engineering or systems analysis.

It is also the case that a closed source program can be either an open system or a closed system, and an open source program can be either an open system or a closed system. Since these terms are so similar, it is essential to read questions carefully. Additional coverage of open source and other software issues is included in Chapter 20 , “Software Development Security.”

CISSP Objective 3.1 lists 11 secure design principles. Six of them are covered in this chapter (i.e., secure defaults, fail securely, keep it simple, zero trust, privacy by design, and trust but verify); the other five are covered in other chapters where they integrate best with broader coverage of similar topics. For threat modeling and defense in depth see Chapter 1 , for least privilege and separation of duties see Chapter 16 ; and for shared responsibility see Chapter 9 .

### Secure Defaults

You have probably heard the phrase “the tyranny of the default.” But do you really know what this means? Tyranny has several definitions, but the one that applies here is “a rigorous condition imposed by some outside agency or force” (attributed to American historian Dixon Wecter). Many assume that the settings that are present in a software or hardware product when it is first installed are the optimal settings. This is based on the assumption that the designers and developers of a product know the most about that product and so the settings they made are likely the best ones. However, this assumption overlooks the fact that often the default settings of a product are selected to minimize installation problems to avoid increased load on the technical support services. For example, consider the fact that most devices have a default password, which minimizes the costs of support when installing or using the product for the first time. Unfortunately, default settings often make discovery and exploitation of equipment trivial for attackers.

Never assume that the default settings of any product are secure. They typically are not, because secure settings would likely get in the way of existing business tasks or system operations. It is always up to the system's administrator and/or company security staff to alter a product's settings to comply with the organization's security policies. Unless your organization hired the developer, that developer did not craft the code or choose settings specifically for your organization's use of their product.

A much better assumption is that the default settings of a product are the worst possible options for your organization. Therefore, you need to review each and every setting to determine what it does and what you need it to be configured to do in order to optimize security while supporting business operations.

Fortunately, there is some movement toward more secure defaults . As mentioned in Chapter 1 , Microsoft's Security Development Lifecycle (SDL) has a motto named SD3+C, which includes the phrase “Secure by Default.” Some products, especially security products, may now be designed with their most secure settings enabled by default. However, such a locked-down product will have fewer enabled capabilities and will likely be less user friendly. Thus, while being more secure, secure defaults may be an obstacle for those who only want their systems to function.

If you are a developer, then it is your responsibility to create detailed explanations of each of the configuration options of your product. You can't assume that customers know everything about your product, especially what the configuration settings are and what each option does to alter its features, operations, communications, and so forth. You may be required to have default settings to make the product as easy to install as possible, but you may be able to provide one or more configurations in either written instructional form or in a file that can be imported or applied. This will go a long way to assist customers with gaining the most advantage from your product while minimizing the security risks.

### Fail Securely

System failures can occur due to a wide range of causes. Once the failure event occurs, how the system or environment handles the failure is important. The most desired result is for an application to fail securely . The first type of failure management is programmatic error handling (aka exception handling ). This is the process where a programmer codes in mechanisms to anticipate and defend against errors in order to avoid the termination of execution. Error handling is the inclusion of code that will attempt to handle errors when they arise before they can cause harm or interrupt execution.

One such mechanism, which is supported by many languages, is a try..catch statement. This logical block statement is used to place code that could result in an error on the try branch, and then code that will be executed if there is an error on the catch branch. This is similar to if..then..else statements, but it is designed to deftly handle errors.

`try..catch`

`try`

`catch`

`if..then..else`

Other mechanisms are to avoid or prevent errors, especially as related to user input. Input sanitization, input filtering, or input validation are some of the terms used to refer to this concept. This often includes checking the input for length, filtering against a block list of unwanted input, and escaping metacharacters. See more about secure coding practices in Chapter 9 ; Chapter 15 , “Security Assessment and Testing,” and Chapter 20 .

There are several similar terms that can be confusing and thus require a bit of focus to comprehend. These terms are fail-soft, fail-secure, fail-safe, fail-open, and fail-closed. Typically, the confusion occurs when not understanding the context where these terms are used. The two primary contexts are the physical world and the digital environment. In the physical world, entities primarily prioritize the protection of people. However, there are some circumstances where assets are protected in priority over people. In the digital world, entities focus on protecting assets but the type of protection may vary amongst the CIA triad.

When a program fails securely, it was able to do so only because it was designed and programmed to. When secure failure is integrated into a system, the designer must make a few difficult choices about what the results of a failure event will be. The first question to be resolved is whether the system can operate in a fail-soft mode. To fail-soft is to allow a system to continue to operate after a component fails. This is an alternative to having a failure cause a complete system failure. An example is a typical multitasking operating system that can support numerous simultaneous applications. If one application fails, the others can typically continue to operate.

If fail-soft isn't a viable option, then the designer needs to consider the type of product, its deployment scenarios, and the priorities related to failure response. In other words, when the product fails without a fail-soft design, it will fail completely. The designer/developer needs to decide what type of complete failure to perform and what to protect or sacrifice to achieve the planned failure result. There are numerous scenarios to consider. The initial distinction is whether the product is something that affects the physical world, such as a door locking mechanism, or is it primarily a digital asset focused product, such as a firewall. If a product can affect the physical world, then the life and safety of humans needs to be considered and likely prioritized. This human protection prioritization is called fail-safe . The idea is that when a failure occurs, the system, device, or product will revert to a state that protects the health and safety of people. For example, a fail-safe door will open easily in an emergency in order to allow people to escape a building. But this implies that the protection of assets may be sacrificed in favor of personnel safety.However, in some physical world situations, a product could be designed and intended to protect assets in priority above people, such as a bank vault, medical lab, or even data center. A fail-secure system prioritizes the physical security of assets over any other consideration. For example, a vault door may automatically close and lock when the building enters a state of emergency. This prioritization of asset protection may occur at the potential cost of harming personnel who could be trapped inside. Obviously, the prioritization of physical world products needs to be considered carefully. In the context of the physical world, the terms fail-open is a synonym to fail-safe and fail-closed is a synonym of fail-secure.

If the product is primarily digital, then the focus of security is completely on digital assets. That means the designer must then decide upon the security aspect to prioritize—namely, availability or confidentiality and integrity. If the priority is for maintaining availability, then when the product fails, the connection or communication is allowed to continue. This is known as fail-open. If the priority is for maintaining confidentiality and integrity, then when the product fails, the connection or communication is cut off. This is known as fail-secure, fail-closed, and/or fail-safe (again, in the context of a digital environment). (Note: the IETF recommends avoiding the use of the term fail-safe when discussing digital only issues as it introduces the concept of human safety which is not a concern in a digital context and thus causes unnecessary confusion). Take note that when the context switches from the physical world to the digital world, the definition of fail-safe changes. An example could be a firewall, which if designed to fail-open would allow communications without filtering, whereas if implement a fail-secure, fail-closed, or fail-safe solution would cut off communications. The fail-open state protects availability through the sacrifice of confidentiality and integrity, whereas the fail-closed state sacrifices availability in order to protect confidentiality and integrity. Another example of a digital environment event following a fail-secure, fail-closed, and/or fail-safe procedure is when an operating system encounters a processing or memory isolation violation, it terminates all executions, then initiates a reboot. This mechanism is known as a stop error, or the Blue Screen of Death (BSoD) in Windows.

A condensed summary of the context and protection priority of these terms is presented in Table 8.2 .

TABLE 8.2 Fail terms definitions related to physical and digital products

TABLE 8.2 Fail terms definitions related to physical and digital products

### Keep It Simple

Keep it simple is a shortened form of the classic statement of “keep it simple, stupid” or “keep it stupid simple.” This is sometimes called the KISS principle. In the realm of security, this concept is the encouragement to avoid overcomplicating the environment, organization, or product design. The more complex a system, the more difficult it is to secure. The more lines of code, the more challenging it is to thoroughly test it. The more parts there are, the more places there are for things to go wrong. The more features and capabilities, the larger the attack surface.

There are many other concepts that have a similar or related emphasis, such as the following:

- “Don't Repeat Yourself” (DRY) The idea of eliminating redundancy in software by not repeating the same code in multiple places, which would increase the difficulty if changes are needed.

- Computing Minimalism Crafting code so that it uses the least necessary hardware and software resources possible; this is also the goal of the program evaluation and review technique (PERT), which is discussed in Chapter 20 .

- Rule of Least Power Use the least powerful programming language that is suitable for the needed solution.

- “Worse Is Better” (aka New Jersey Style) The quality of software does not necessarily increase with an increase in capabilities and functions; there is often a worse software state (i.e., fewer functions), which is the better (i.e., preferred, maybe more secure) option.

- “You Aren't Gonna Need It” (YAGNI) Programmers should not add capabilities and functions until they are actually necessary, so rather than create it when you think of it, instead create it only when you actually need it.

It is easy to get caught up in adding complexity to a system, whether that system is a software program or an organizational IT security structure. The KISS principle encourages us all to avoid the overly complex in favor of the streamlined, optimized, and reduced solution. Simpler solutions are easier to secure, easier to troubleshoot, and easier to verify.

### Zero Trust

Zero trust is a security concept where nothing inside the organization is automatically trusted. There has long been an assumption that everything on the inside is trusted and everything on the outside is untrusted. This has led to a significant security focus on endpoint devices, the locations where users interact with company resources. An endpoint device could be a user's workstation, a tablet, a smartphone, an Internet of Things (IoT) device, an industrial control system (ICS), an edge computing sensor, or any public-facing servers in a screened subnet or extranet. The idea that a security perimeter exists between the safe inside and the harmful outside is problematic. There have been too many occurrences of security breaches caused by insiders as well as external hacker breaches that gained the freedom to perform lateral movement internally once they breached the security barrier. The concept of a security perimeter is further complicated by the use of mobile devices, the cloud, and the proliferation of endpoint devices. For most organizations, there is no longer a clearly defined line between inside and outside.

Zero trust is an alternate approach to security where nothing is automatically trusted. Instead, each request for activity or access is assumed to be from an unknown and untrusted location until otherwise verified. The concept is “never trust, always verify.” Since anyone and anything could be malicious, every transaction should be verified before it is allowed to occur. The zero trust model is based around “assume breach,” meaning that you should always assume a security breach has occurred and that whoever or whatever is making a request could be malicious. The goal is to have every access request be authenticated, authorized, and encrypted prior to the access being granted to a resource or asset. The implementation of a zero trust architecture does involve a significant shift from historical security management concepts. This shift typically requires internal microsegmentation and strong adherence to the principle of least privilege. This approach prevents lateral movement so that if there is a breach or even a malicious insider, their ability to move about the environment is severely restricted.

Microsegmentation is dividing up an internal network into numerous subzones. Each zone is separated from the others by internal segmentation firewalls (ISFWs), subnets, or VLANs. Zones could be as small as a single device, such as a high-value server or even a client or endpoint device. Any and all communications between zones are filtered, may be required to authenticate, often require session encryption, and may be subjected to allow list and block list control.

Zero trust is implemented using a wide range of security solutions, including internal segmentation firewalls (ISFWs), multifactor authentication (MFA), identity and access management (IAM), and next-generation endpoint security (see Chapter 9 ). A zero trust approach to security management can only be successful if a means to continuously validate and monitor user activities is implemented. If a one-time validation mechanism is used, then the opportunity to abuse the system remains since threats, users, and connection characteristics are always subject to change. Thus, zero trust networking can only work if real-time vetting and visibility into user activities is maintained.

In some situations, complete isolation may be needed instead of controlled and filtered interaction. This type of isolation is achieved using an air gap. An air gap is a network security measure employed to ensure that a secure system is physically isolated from other systems. Air gap implies that neither cabled nor wireless network links are available.

In order to implement a zero trust system, an organization must be capable of and willing to abandon some long-held assumptions about security. First and foremost, it must be understood that there is no such thing as a trusted source. No entity, asset, or subject—internal or external—is to be trusted by default. Instead, always assume attackers are already on the inside, on every system. From this new “no assumed trust” position, it is obvious that traditional default access controls are insufficient. Each and every subject, each and every time, needs to be authenticated, authorized, and encrypted. From there, a continuous real-time monitoring system needs to be established to look for violations and suspicious events. But even with zero trust integrated into the IT architecture, it is only an element of a holistic security strategy that is integrated into the entire organization's management processes.

Zero trust has been formalized in NIST SP 800-207, “Zero Trust Architecture.” Please consult this document to learn more about this revolution in security design.

### Privacy by Design

Privacy by Design (PbD) is a guideline to integrate privacy protections into products during the early design phase rather than attempting to tack it on at the end of development. It is effectively the same overall concept as “security by design” or “integrated security,” where security is to be an element of design and architecture of a product starting at initiation and being maintained throughout the software development lifecycle (SDLC).

As described in Ann Cavoukian's paper “Privacy by Design – The 7 Foundational Principles: Implementation and Mapping of Fair Information Practices” ( collections.ola.org/mon/24005/301946.pdf ), the PbD framework is based on seven foundational principles:

- Proactive not reactive; preventive not remedial

- Privacy as the default

- Privacy embedded into design

- Full functionality – positive-sum, not zero-sum

- End-to-end security – full lifecycle protection

- Visibility and transparency

- Respect for user privacy

The goal of PbD is to have developers integrate privacy protections into their solutions in order to avoid privacy violations in the first place. The overall concept focuses on preventions rather than remedies for violations.

PbD is also the driving factor behind an initiative to have privacy protections integrated throughout an organization, not just by developers. That business operations and systems design can also integrate privacy protections into their core functions. This in turn has led to the Global Privacy Standard (GPS) , which was crafted to create a single set of universal and harmonized privacy principles. GPS is to be adopted by countries to use as a guide in developing privacy legislation, used by organizations to integrate privacy protection into their operations, and used by developers to integrate privacy into the products they produce. There is some integration of a few of the principles of PbD in the EU's GDPR (see gdpr-info.eu/issues/privacy-by-design and Chapter 4 , “Laws, Regulations, and Compliance”).

For more on PbD and GPS, please visit gpsbydesign.org , review the Cavoukian paper mentioned earlier, and read an additional paper, “Privacy by Design in Law, Policy and Practice,” at collections.ola.org/mon/25008/312239.pdf . Learn more about privacy in Chapter 4 and about software development security in Chapter 20 .

### Trust but Verify

The phrase “trust, but verify” (which is a quote from a Russian proverb) was made famous by former president Ronald Reagan when discussing U.S. relations with the Soviet Union. However, our focus on this phrase is on its use in the security realm. A more traditional security approach of trusting subjects and devices within the company's security perimeter (i.e., internal entities) automatically can be called “ trust but verify .” This type of security approach leaves an organization vulnerable to insider attacks and grants intruders the ability to easily perform lateral movement among internal systems. Often the trust but verify approach depended on an initial authentication process to gain access to the internal “secured” environment, and then relied on generic access control methods. Due to the rapid growth and changes in the modern threatscape, the trust but verify model of security is no longer sufficient. Most security experts now recommend designing organizational security around the zero trust model.
