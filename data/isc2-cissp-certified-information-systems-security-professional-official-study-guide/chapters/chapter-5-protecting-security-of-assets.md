---
{
  "id": "chapter-246",
  "title": "Chapter 5: Protecting Security of Assets",
  "order": 246,
  "source": {
    "href": "b01.xhtml",
    "anchor": "head-2-7"
  },
  "est_tokens": 1668,
  "slug": "chapter-5-protecting-security-of-assets",
  "meta": {
    "nav_title": "Chapter 5: Protecting Security of Assets",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Chapter 5: Protecting Security of Assets

- B. Data classifications provide strong protection against the loss of confidentiality and are the best choice of the available answers. Data labels and proper data handling are based on first identifying data classifications. Data degaussing methods apply only to magnetic media.

- D. Backup media should be protected with the same level of protection afforded the data it contains, and using a secure offsite storage facility would ensure this. The media should be marked, but that won't protect it if it is stored in an unstaffed warehouse. A copy of backups should be stored offsite to ensure availability if a catastrophe affects the primary location. If copies of data are not stored offsite or offsite backups are destroyed, security is sacrificed by risking availability.

- B. Destruction is the final stage in the lifecycle of backup media. Because the backup method is no longer using tapes, they should be destroyed. Degaussing and declassifying the tape is done if you plan to reuse it. Retention implies you plan to keep the media, but retention is not needed at the end of its lifecycle.

- C. The data owner is the person responsible for classifying data. A data controller decides what data to process and directs the data processor to process the data. A data custodian protects the integrity and security of the data by performing day-to-day maintenance. Users simply access the data.

- A. The data custodian is responsible for the tasks of implementing the protections defined by the security policy and senior management. A data controller decides what data to process and how. Data users are not responsible for implementing the security policy protections. A data processor controls the processing of data and only does what the data controller tells them to do with the data.

- D. The company can implement a data collection policy of minimization to minimize the amount of data they collect and store. If they are selling digital products, they don't need the physical address. If they are reselling products to the same customers, they can use tokenization to save tokens that match the credit card data, instead of saving and storing credit card data. Anonymization techniques remove all personal data and make the data unusable for reuse on the website. Pseudonymization replaces data with pseudonyms. Although the process can be reversed, it is not necessary.

- B. Security labeling identifies the classification of data such as sensitive, secret, and so on. Media holding sensitive data should be labeled. Similarly, systems that hold or process sensitive data should also be marked. Many organizations require the labeling of all systems and media, including those that hold or process nonsensitive data.

- B. A data subject is a person who can be identified by an identifier such as a name, identification number, or other PII. All of these answers refer to the General Data Protection Regulation (GDPR). A data owner owns the data and has ultimate responsibility for protecting it. A data controller decides what data to process and how it should be processed. A data processor processes the data for the data controller.

- B. Personnel did not follow the record retention policy for the backups sent to the warehouse. The scenario states that administrators purge onsite emails older than six months to comply with the organization's security policy, but the leak was from emails sent over three years ago. Personnel should follow media destruction policies when the organization no longer needs the media, but the issue here is the data on the tapes. Configuration management ensures that systems are configured correctly using a baseline, but this does not apply to backup media. Versioning applies to applications, not backup tapes.

- D. Record retention policies define the amount of time to keep data, and laws or regulations often drive these policies. Data remanence is data remnants on media, and proper data destruction procedures remove data remnants. Laws and regulations do outline requirements for some data roles, but they don't specify requirements for the data user role.

- D. Purging is the most reliable method among the given choices. Purging overwrites the media with random bits multiple times and includes additional steps to ensure that data is removed. It ensures there isn't any data remanence. Erasing or deleting processes rarely remove the data from media but instead mark it for deletion. Solid-state drives (SSDs) do not have magnetic flux, so degaussing an SSD doesn't destroy data.

- A. Overwriting the disks multiple times will remove all existing data. This is called purging, and purged media can then be used again. Formatting the disks isn't secure because it doesn't typically remove the previously stored data. Degaussing the disks often damages the electronics but doesn't reliably remove the data. Defragmenting a disk optimizes it, but it doesn't remove data.

- D. Systems with an EOS date that occurs in the following year should be a top priority for replacement. The EOS date is the date that the vendor will stop supporting a product. The EOL date is the date that a vendor stops offering a product for sale, but the vendor continues to support the product until the EOS date. Systems used for data loss prevention or to process sensitive data can remain in service.

- D. Purging memory buffers removes all remnants of data after a program has used it. Asymmetric encryption (along with symmetric encryption) protects data in transit. The data is already encrypted and stored in the database. The scenario doesn't indicate that the program modified the data, so there's no need to overwrite the existing data in the database. Data loss prevention methods prevent unauthorized data loss but do not protect data in use.

- A. Symmetric encryption methods protect data at rest, and data at rest is any data stored on media, such as a server. Data in transit is data transferred between two systems. Data in use is data in memory that is used by an application. Steps are taken to protect data from the time it is created to the time it is destroyed, but this question isn't related to the data lifecycle.

- B. Scoping is a part of the tailoring process and refers to reviewing a list of security controls and selecting the security controls that apply. Tokenization is the use of a token, such as a random string of characters, to replace other data and is unrelated to this question. Note that scoping focuses on the security of the system and tailoring ensures that the selected controls align with the organization's mission. If the database server needs to comply with external entities, it's appropriate to select a standard baseline provided by that entity. Imaging is done to deploy an identical configuration to multiple systems, but this is typically done after identifying security controls.

- A. Tailoring refers to modifying a list of security controls to align with the organization's mission. The IT administrators identified a list of security controls to protect the web farm during the scoping steps. Sanitization methods (such as clearing, purging, and destroying) help ensure that data cannot be recovered and is unrelated to this question. Asset classification identifies the classification of assets based on the classification of data the assets hold or process. Minimization refers to data collection. Organizations should collect and maintain only the data they need.

- A. A cloud access security broker (CASB) is software placed logically between users and cloud-based resources, and it can enforce security policies used in an internal network. Data loss prevention (DLP) systems attempt to detect and block data exfiltration. CASB systems typically include DLP capabilities. Digital rights management (DRM) methods attempt to provide copyright protection for copyrighted works. End-of-life (EOL) is generally a marketing term and indicates when a company stops selling a product.

- B. Network-based data loss prevention (DLP) systems can scan outgoing data and look for specific keywords and/or data patterns. DLP systems can block these outgoing transmissions. Antimalware software detects malware. Security information and event management (SIEM) provides real-time analysis of events occurring on systems throughout an organization but doesn't necessarily scan outgoing traffic. Intrusion prevention systems (IPSs) scan incoming traffic to prevent unauthorized intrusions.

- B, C, D. Persistent online authentication, automatic expiration, and a continuous audit trail are all methods used with digital rights management (DRM) technologies. Virtual licensing isn't a valid term within DRM.
