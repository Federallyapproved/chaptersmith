---
{
  "id": "chapter-23",
  "title": "Threat Modeling",
  "order": 23,
  "source": {
    "href": "c01.xhtml",
    "anchor": "head-2-52"
  },
  "est_tokens": 2446,
  "slug": "threat-modeling",
  "meta": {
    "nav_title": "Threat Modeling",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Threat Modeling

Threat modeling is the security process where potential threats are identified, categorized, and analyzed. Threat modeling can be performed as a proactive measure during design and development or as a reactive measure once a product has been deployed. In either case, the process identifies the potential harm, the probability of occurrence, the priority of concern, and the means to eradicate or reduce the threat.

Threat modeling isn't meant to be a single event. Instead, it's meant to be initiated early in the design process of a system and continue throughout its lifecycle. For example, Microsoft uses a Security Development Lifecycle (SDL) ( www.microsoft.com/en-us/securityengineering/sdl ) with the motto of “Secure by Design, Secure by Default, Secure in Deployment and Communication” (also known as SD3+C). It has two goals in mind with this process:

- To reduce the number of security-related design and coding defects

- To reduce the severity of any remaining defects

A defensive approach to threat modeling takes place during the early stages of systems development, specifically during initial design and specifications establishment. This method is based on predicting threats and designing in specific defenses during the coding and crafting process. In most cases, integrated security solutions are more cost-effective and more successful than those shoehorned in later. While not a formal term, this concept could be considered a proactive approach to threat management.

Unfortunately, not all threats can be predicted during the design phase, so a reactive approach to threat management is still needed to address unforeseen issues. This concept is often call threat hunting or may be referred to as an adversarial approach .

An adversarial approach to threat modeling takes place after a product has been created and deployed. This deployment could be in a test or laboratory environment or to the general marketplace. This technique of threat hunting is the core concept behind ethical hacking, penetration testing, source code review, and fuzz testing. Although these processes are often useful in finding flaws and threats, they unfortunately result in additional effort in coding to add in new countermeasures, typically released as patches. This results in less effective security improvements (over defensive threat modeling) at the cost of potentially reducing functionality and user-friendliness.

Fuzz testing is a specialized dynamic testing technique that provides many different types of input to software to stress its limits and find previously undetected flaws. See Chapter 15 for more on fuzz testing.

### Identifying Threats

There's an almost infinite possibility of threats, so it's important to use a structured approach to accurately identify relevant threats. For example, some organizations use one or more of the following three approaches:

- Focused on Assets This method uses asset valuation results and attempts to identify threats to the valuable assets.

- Focused on Attackers Some organizations are able to identify potential attackers and can identify the threats they represent based on the attacker's motivations, goals, or tactics, techniques, and procedures (TTPs).

- Focused on Software If an organization develops software, it can consider potential threats against the software.

It's common to pair threats with vulnerabilities to identify threats that can exploit assets and represent significant risks to the organization. An ultimate goal of threat modeling is to prioritize the potential threats against an organization's valuable assets.

When attempting to inventory and categorize threats, it is often helpful to use a guide or reference. Microsoft developed a threat categorization scheme known as the STRIDE threat model. STRIDE is an acronym standing for the following:

- Spoofing : An attack with the goal of gaining access to a target system through the use of a falsified identity. When an attacker spoofs their identity as a valid or authorized entity, they are often able to bypass filters and blockades against unauthorized access.

- Tampering : Any action resulting in unauthorized changes or manipulation of data, whether in transit or in storage.

- Repudiation : The ability of a user or attacker to deny having performed an action or activity by maintaining plausible deniability. Repudiation attacks can also result in innocent third parties being blamed for security violations.

- Information disclosure : The revelation or distribution of private, confidential, or controlled information to external or unauthorized entities.

- Denial of service (DoS) : An attack that attempts to prevent authorized use of a resource. This can be done through flaw exploitation, connection overloading, or traffic flooding.

- Elevation of privilege : An attack where a limited user account is transformed into an account with greater privileges, powers, and access.

Process for Attack Simulation and Threat Analysis (PASTA) is a seven-stage threat modeling methodology. PASTA is a risk-centric approach that aims at selecting or developing countermeasures in relation to the value of the assets to be protected. The following are the seven steps of PASTA:

- Stage I: Definition of the Objectives (DO) for the Analysis of Risks

- Stage II: Definition of the Technical Scope (DTS)

- Stage III: Application Decomposition and Analysis (ADA)

- Stage IV: Threat Analysis (TA)

- Stage V: Weakness and Vulnerability Analysis (WVA)

- Stage VI: Attack Modeling & Simulation (AMS)

- Stage VII: Risk Analysis & Management (RAM)

Each stage of PASTA has a specific list of objectives to achieve and deliverables to produce in order to complete the stage. For more information on PASTA, please see Risk Centric Threat Modeling: Process for Attack Simulation and Threat Analysis (Wiley, 2015), by Tony UcedaVelez and Marco M. Morana.

Visual, Agile, and Simple Threat (VAST) is a threat modeling concept that integrates threat and risk management into an Agile programming environment on a scalable basis (see Chapter 20 , “Software Development Security,” regarding Agile).

These are just a few in the vast array of threat modeling concepts and methodologies available from community groups, commercial entities, government agencies, and international associations.

# Be Alert for Individual Threats

Competition is often a key part of business growth, but overly adversarial competition can increase the threat level from individuals. In addition to criminal hackers and disgruntled employees, adversaries, contractors, employees, and even trusted partners can be a threat to an organization if relationships go sour.

Potential threats to your business are broad and varied. A company faces threats from nature, technology, and people. Always consider the best and worst possible outcomes of your organization's activities, decisions, and interactions. Identifying threats is the first step toward designing defenses to help reduce or eliminate downtime, compromise, and loss.

### Determining and Diagramming Potential Attacks

The next step in threat modeling is to determine the potential attack concepts that could be realized. This is often accomplished through the creation of a diagram of the elements involved in a transaction along with indications of data flow and privilege boundaries ( Figure 1.4 ). This image shows each major component of a system, the boundaries between security zones, and the potential flow or movement of information and data.

This is a high-level overview and not a detailed evaluation of the coding logic. However, for more complex systems, multiple diagrams may need to be created at various focus points and at varying levels of detail magnification.

Once a diagram has been crafted, identify all of the technologies involved. Next, identify attacks that could be targeted at each element of the diagram. Keep in mind that all forms of attacks should be considered, including logical/technical, physical, and social. This process will quickly lead you into the next phase of threat modeling: reduction analysis.

### Performing Reduction Analysis

The next step in threat modeling is to perform reduction analysis. Reduction analysis is also known as decomposing the application, system, or environment. The purpose of this task is to gain a greater understanding of the logic of the product, its internal components, as well as its interactions with external elements. Whether an application, a system, or an entire environment, it needs to be divided into smaller containers or compartments. Those might be subroutines, modules, or objects if you're focusing on software, computers, or operating systems; they might be protocols if you're focusing on systems or networks; or they might be departments, tasks, and networks if you're focusing on an entire business infrastructure. Each identified element should be evaluated in order to understand inputs, processing, security, data management, storage, and outputs.

FIGURE 1.4 An example of diagramming to reveal threat concerns

FIGURE 1.4 An example of diagramming to reveal threat concerns

In the decomposition process, you must identify five key concepts:

- Trust Boundaries Any location where the level of trust or security changes

- Dataflow Paths The movement of data between locations

- Input Points Locations where external input is received

- Privileged Operations Any activity that requires greater privileges than of a standard user account or process, typically required to make system changes or alter security

- Details about Security Stance and Approach The declaration of the security policy, security foundations, and security assumptions

Breaking down a system into its constituent parts makes it much easier to identify the essential components of each element as well as take notice of vulnerabilities and points of attack. The more you understand exactly how a program, system, or environment operates, the easier it is to identify threats to it.

Once threats are identified, they should be fully documented by defining the means, target, and consequences of a threat. Consider including the techniques required to implement an exploitation as well as list potential countermeasures and safeguards.

### Prioritization and Response

After documentation, the next step is to rank or rate the threats. This can be accomplished using a wide range of techniques, such as Probability × Damage Potential ranking, high/medium/low rating, or the DREAD system.

The ranking technique of Probability × Damage Potential produces a risk severity number on a scale of 1 to 100, with 100 the most severe risk possible. Each of the two initial values can be assigned numbers between 1 and 10, with 1 being lowest and 10 the highest. These rankings can be somewhat arbitrary and subjective, but since the same person or team will be assigning the numbers for their own organization, it should still result in assessment values that are accurate on a relative basis.

The high/medium/low (1/2/3 or green/yellow/red) rating process is even simpler. It creates a basic risk matrix or heat map ( Figure 1.5 ). As with any means of risk assessment, the purpose is to help establish criticality prioritization. Using a risk matrix, each threat can be assigned a probability and a damage level. Then when these two values are compared, the result is a combined value somewhere in the nine squares. Those threats in the HH (high probability/high damage) area are of the highest priority and concern, whereas those in the LL (low probability/low damage) area are of least priority and concern.

FIGURE 1.5 A risk matrix or risk heat map

FIGURE 1.5 A risk matrix or risk heat map

The Disaster, Reproducibility, Exploitability, Affected Users, and Discoverability (DREAD) rating system is designed to provide a flexible rating solution that is based on the answers to five main questions about each threat:

- Damage Potential How severe is the damage likely to be if the threat is realized?

- Reproducibility How complicated is it for attackers to reproduce the exploit?

- Exploitability How hard is it to perform the attack?

- Affected Users How many users are likely to be affected by the attack (as a percentage)?

- Discoverability How hard is it for an attacker to discover the weakness?

Once threat priorities are set, responses to those threats need to be determined. Technologies and processes to remediate threats should be considered and weighted according to their cost and effectiveness. Response options should include making adjustments to software architecture, altering operations and processes, and implementing defensive and detective components.

This process is similar to the risk assessment process discussed in Chapter 2 . The difference is that threats are the focus of threat modeling, whereas assets are the focus of risk assessment.
