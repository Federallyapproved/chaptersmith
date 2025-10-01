---
{
  "id": "chapter-87",
  "title": "Select Controls Based on Systems Security Requirements",
  "order": 87,
  "source": {
    "href": "c08.xhtml",
    "anchor": "head-2-150"
  },
  "est_tokens": 1808,
  "slug": "select-controls-based-on-systems-security-requirements",
  "meta": {
    "nav_title": "Select Controls Based on Systems Security Requirements",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Select Controls Based on Systems Security Requirements

Those who purchase information systems for certain kinds of applications—for example, national security agencies whose sensitive information may be extremely valuable (or dangerous in the wrong hands) or central banks or securities traders that have certain data that may be worth billions of dollars—often want to understand the security strengths and weaknesses of systems prior to acquisition. Such buyers are often willing to consider only systems that have been subjected to formal evaluation processes in advance and have received some kind of security rating.

Often trusted third parties are used to perform security evaluations; the most important result from such testing is their “seal of approval” that the system meets all essential criteria.

### Common Criteria

The Common Criteria (CC) defines various levels of testing and confirmation of systems' security capabilities, and the number of the level indicates what kind of testing and confirmation has been performed. Nevertheless, it's wise to observe that even the highest CC ratings do not equate to a guarantee that such systems are completely secure or that they are entirely devoid of vulnerabilities or susceptibilities to exploit. The Common Criteria was designed as a dynamic subjective product evaluation model and replaced previous static systems, such as the U.S. Department of Defense's Trusted Computer System Evaluation Criteria (TCSEC) and the EU's Information Technology Security Evaluation Criteria (ITSEC).

A document titled “Arrangement on the Recognition of Common Criteria Certificates in the Field of IT Security” was signed by representatives from government organizations in Canada, France, Germany, the United Kingdom, and the United States in 1998, making the document an international standard. Since then, 23 additional countries have signed the arrangement. The original arrangement documentation has been formally adopted as a standard and published as ISO/IEC 15408-1, -2, and -3 and primarily labeled as “Information technology — Security techniques — Evaluation criteria for IT security.”

There is a revision of ISO/IEC 15408 currently underway (as of fall 2020, it was labeled as ISO/IED 15408-1 (-2, or -3):2020), which may be published by the time this book is published. The latest versions of ISO/IEC standards are available at standards.iso.org/ittf/PubliclyAvailableStandards/index.html .

The objectives of the CC guidelines are as follows:

- To add to buyers' confidence in the security of evaluated, rated IT products

- To eliminate duplicate evaluations (among other things, this means that if one country, agency, or validation organization follows the CC in rating specific systems and configurations, others elsewhere need not repeat this work)

- To keep making security evaluations more cost-effective and efficient

- To make sure evaluations of IT products adhere to high and consistent standards

- To promote evaluation and increase availability of evaluated, rated IT products

- To evaluate the functionality (in other words, what the system does) and assurance (in other words, how much can you trust the system) of the target of evaluation (TOE)

The Common Criteria process is based on two key elements: protection profiles and security targets. Protection profiles (PPs) specify for a product that is to be evaluated (the TOE) the security requirements and protections, which are considered the security desires, or the “I want,” from a customer. Security targets (STs) specify the claims of security from the vendor that are built into a TOE. STs are considered the implemented security measures, or the “I will provide,” from the vendor. In addition to offering security targets, vendors may offer packages of additional security features. A package is an intermediate grouping of security requirement components that can be added to or removed from a TOE (like the option packages when purchasing a new vehicle). This system of the PP and ST allows for flexibility, subjectivity, and customization of an organization's specific security functional and assurance requirements over time.

An organization's PP is compared to various STs from the selected vendor's TOEs. The closest or best match is what the client purchases. The client initially selects a vendor based on published or marketed evaluation assurance levels (EALs) for currently available systems. Using Common Criteria to choose a vendor allows clients to request exactly what they need for security rather than having to use static fixed security levels. It also allows vendors more flexibility on what they design and create. A well-defined set of Common Criteria supports subjectivity and versatility, and it automatically adapts to changing technology and threat conditions. Furthermore, the EALs provide a method for comparing vendor systems that is more standardized (like the old TCSEC).

Table 8.4 summarizes EALs 1 through 7. For a complete description of EALs, consult the CC standard documents.

TABLE 8.4 Common Criteria evaluation assurance levels

TABLE 8.4 Common Criteria evaluation assurance levels

Though the CC guidelines are flexible and accommodating enough to capture most security needs and requirements, they are by no means perfect. As with other evaluation criteria, the CC guidelines do nothing to make sure that how users act on data is also secure. The CC guidelines also do not address administrative issues outside the specific purview of security. As with other evaluation criteria, the CC guidelines do not include evaluation of security in situ —that is, they do not address controls related to personnel, organizational practices and procedures, or physical security. Likewise, controls over electromagnetic emissions are not addressed, nor are the criteria for rating the strength of cryptographic algorithms explicitly laid out. Nevertheless, the CC guidelines represent some of the best techniques whereby systems may be rated for security.

Common Criteria documentation is available at www.commoncriteriaportal.org/ccra . Visit this site to get information on the current version of the CC guidelines and guidance on using the CC along with lots of other useful, relevant information.

International Organization for Standardization (ISO) is a worldwide standards-setting group of representatives from various national standards organizations. ISO defines standards for industrial and commercial equipment, software, protocols, and management, among others. It issues six main products: International Standards, Technical Reports, Technical Specifications, Publicly Available Specifications, Technical Corrigenda, and Guides. ISO standards are widely accepted across many industries and have even been adopted as requirements or laws by various governments. For more information on ISO, please visit the website at iso.org .

### Authorization to Operate

For many environments, it is necessary to obtain an official approval to use secured equipment for operational objectives. This is often referred to as an Authorization to Operate (ATO) . ATO is the current term for this concept as defined by the Risk Management Framework (RMF) (see Chapter 2 ,“Personnel Security and Risk Management Concepts”), which replaces the previous term of accreditation. An ATO is an official authorization to use a specific collection of secured IT/IS systems to perform business tasks and accept the identified risk. The assessment and assignment of an ATO is performed by an Authorizing Official (AO) . An AO is an authorized entity who can evaluate an IT/IS system, its operations, and its risks, and potentially issue an ATO. Other terms for AO include designated approving authority (DAA), Approving Authority (AA), Security Control Assessor (SCA), and Recommending Official (RO).

NIST maintains an excellent glossary with references at csrc.nist.gov/glossary .

A typical ATO is issued for 5 years (although assigned time frames vary and the AO can adjust the time frame even after issuing an ATO) and must be reobtained whenever one of the following conditions occurs:

- The ATO time frame has expired.

- The system experiences a significant security breach.

- The system experiences a significant security change.

The AO has the discretion to determine which breaches or security changes result in a loss of ATO. Either a modest intrusion event or the application of a substantial security patch could cause the negation of an ATO.

An AO can issue four types of authorization decisions:

- Authorization to Operate This decision is issued when risk is managed to an acceptable level.

- Common Control Authorization This decision is issued when a security control is inherited from another provider and when the risk associated with the common control is at an acceptable level and already has a ATO from the same AO.

- Authorization to Use This decision is issued when a third-party provider (such as a cloud service) provides IT/IS servers that are deemed to have risk at an acceptable level; it is also used to allow for reciprocity in accepting another AO's ATO.

- Denial of Authorization This decision is issued when risk is unacceptable.

Please see NIST SP 800-37r2 for more on the Risk Management Framework and authorization.

The RMF ATO concept replaces the previous certification and accreditation (C&A) process. There are a few remaining references to C&A in NIST documents, but they are mostly from older publications or are marked as C.F.D., which stands for “Candidates for Deletion.”
