---
{
  "id": "chapter-49",
  "title": "Compliance",
  "order": 49,
  "source": {
    "href": "c04.xhtml",
    "anchor": "head-2-95"
  },
  "est_tokens": 614,
  "slug": "compliance",
  "meta": {
    "nav_title": "Compliance",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Compliance

Over the past decade, the regulatory environment governing information security has grown increasingly complex. Organizations may find themselves subject to a wide variety of laws (many of which were outlined earlier in this chapter) and regulations imposed by regulatory agencies or contractual obligations.

### Real World Scenario

### Payment Card Industry Data Security Standard

The Payment Card Industry Data Security Standard (PCI DSS) is an excellent example of a compliance requirement that is not dictated by law but by contractual obligation. PCI DSS governs the security of credit card information and is enforced through the terms of a merchant agreement between a business that accepts credit cards and the bank that processes the business's transactions.

PCI DSS has 12 main requirements.

- Install and maintain a firewall configuration to protect cardholder data.

- Do not use vendor-supplied defaults for system passwords and other security parameters.

- Protect stored cardholder data.

- Encrypt transmission of cardholder data across open, public networks.

- Protect all systems against malware and regularly update antivirus software or programs.

- Develop and maintain secure systems and applications.

- Restrict access to cardholder data by business need-to-know.

- Identify and authenticate access to system components.

- Restrict physical access to cardholder data.

- Track and monitor all access to network resources and cardholder data.

- Regularly test security systems and processes.

- Maintain a policy that addresses information security for all personnel.

Each of these requirements is spelled out in detail in the full PCI DSS standard, which can be found at pcisecuritystandards.org . Organizations subject to PCI DSS may be required to conduct annual compliance assessments, depending on the number of transactions they process and their history of cybersecurity breaches.

Dealing with the many overlapping, and sometimes contradictory, compliance requirements facing an organization requires careful planning. Many organizations employ full-time IT compliance staff responsible for tracking the regulatory environment, monitoring controls to ensure ongoing compliance, facilitating compliance audits, and meeting the organization's compliance reporting obligations.

Organizations that are not merchants but that store, process, or transmit credit card information on behalf of merchants must also comply with PCI DSS. For example, the requirements apply to shared hosting providers who must protect the cardholder data environment.

Organizations may be subject to compliance audits, either by their standard internal and external auditors or by regulators or their agents. For example, an organization's financial auditors may conduct an IT controls audit designed to ensure that the information security controls for an organization's financial systems are sufficient to ensure compliance with the Sarbanes–Oxley Act (SOX). Some regulations, such as PCI DSS, may require the organization to retain approved independent auditors to verify controls and provide a report directly to regulators.

In addition to formal audits, organizations often must report regulatory compliance to a number of internal and external stakeholders. For example, an organization's board of directors (or, more commonly, that board's audit committee) may require periodic reporting on compliance obligations and status. Similarly, PCI DSS requires organizations that are not compelled to conduct a formal third-party audit to complete and submit a self-assessment report outlining their compliance status.
