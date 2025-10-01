---
{
  "id": "chapter-58",
  "title": "Understanding Data Roles",
  "order": 58,
  "source": {
    "href": "c05.xhtml",
    "anchor": "head-2-106"
  },
  "est_tokens": 2149,
  "slug": "understanding-data-roles",
  "meta": {
    "nav_title": "Understanding Data Roles",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Understanding Data Roles

Many people within an organization manage, handle, and use data, and they have different requirements based on their roles. Different documentation refers to these roles a little differently. Some of the terms you may see match the terminology used in some NIST documents, and other terms match some of the terminology used in the EU GDPR. When appropriate, we've listed the source so that you can dig into these terms a little deeper if desired.

One of the most important concepts here is ensuring that personnel know who owns information and assets. The owners have a primary responsibility of protecting the data and assets.

### Data Owners

The data owner (sometimes referred to as the organizational owner or senior manager) is the person who has ultimate organizational responsibility for data. The owner is typically the chief executive officer (CEO), president, or a department head (DH). Data owners identify the classification of data and ensure that it is labeled properly. They also ensure that it has adequate security controls based on the classification and the organization's security policy requirements. Owners may be liable for negligence if they fail to perform due diligence in establishing and enforcing security policies to protect and sustain sensitive data.

NIST SP 800-18 Rev. 1, “Guide for Developing Security Plans for Federal Information Systems,” outlines the following responsibilities for the information owner, which can be interpreted the same as the data owner:

- Establishes the rules for appropriate use and protection of the subject data/information (rules of behavior)

- Provides input to information system owners regarding the security requirements and security controls for the information system(s) where the information resides

- Decides who has access to the information system and with what types of privileges or access rights

- Assists in the identification and assessment of the common security controls where the information resides

NIST SP 800-18 frequently uses the phrase “rules of behavior,” which is effectively the same as an acceptable use policy (AUP). Both outline the responsibilities and expected behavior of individuals and state the consequences of not complying with the rules or AUP. Additionally, individuals are required to periodically acknowledge that they have read, understand, and agree to abide by the rules or AUP. Many organizations post these on a website and allow users to acknowledge that they understand and agree to abide by them using an online electronic digital signature.

### Asset Owners

The asset owner (or system owner) is the person who owns the asset or system that processes sensitive data. NIST SP 800-18 outlines the following responsibilities for the system owner:

- Develops a system security plan in coordination with information owners, the system administrator, and functional end users

- Maintains the system security plan and ensures that the system is deployed and operated according to the agreed-upon security requirements

- Ensures that system users and support personnel receive appropriate security training, such as instruction on rules of behavior (or an AUP)

- Updates the system security plan whenever a significant change occurs

- Assists in the identification, implementation, and assessment of the common security controls

The system owner is typically the same person as the data owner, but it can sometimes be someone else, such as a different department head (DH). As an example, consider a web server used for ecommerce that interacts with a back-end database server. A software development department might perform database development and database administration for the database and the database server, but the IT department maintains the web server. In this case, the software development DH is the system owner for the database server, and the IT DH is the system owner for the web server. However, if software developers work within the IT department, the IT DH would be the system owner for both systems.

The system owner is responsible for ensuring that data processed on the system remains secure. This includes identifying the highest level of data that the system processes. The system owner then ensures that the system is labeled accurately and that appropriate security controls are in place to protect the data. System owners interact with data owners to ensure that the data is protected while at rest on the system, in transit between systems, and in use by applications operating on the system.

System and data owners are senior personnel within an organization. As a result, management teams typically include system and data owners. This is especially useful when a system has one owner for the system and another owner for the data.

### Business/Mission Owners

The business/mission owner role is viewed differently in different organizations. NIST SP 800-18 refers to the business/mission owner as a program manager or an information system owner. As such, the responsibilities of the business/mission owner can overlap with the responsibilities of the system owner or be the same role.

Business owners might own processes that use systems managed by other entities. As an example, the sales department could be the business owner, but the IT department and the software development department could be the system owners for systems used in sales processes. Imagine that the sales department focuses on online sales using an ecommerce website, and the website accesses a back-end database server. As in the previous example, the IT department manages the web server as its system owner, and the software development department maintains the database server as its system owner. Even though the sales department doesn't own these systems, it does own the business processes that generate sales using these systems.

In businesses, business owners are responsible for ensuring that systems provide value to the organization. This sounds obvious. However, compare this with IT departments. If there are any successful attacks or data breaches, the fault is likely to fall on them. IT departments often recommend security controls or systems that don't add immediate value to the organization but reduce overall risks. The business owner is responsible for evaluating these recommendations and may decide that the potential loss related to the risks they eliminate is less than the loss of revenue they'll cause.

Another way of looking at this is by comparing the conflict between cost centers and profit centers. The IT department doesn't generate revenue. Instead, it is a cost center generating costs. In contrast, the business side generates revenue as a profit center. Costs generated by the IT department may reduce risks, but they eat up profits generated by the business side. The business side may view the IT department as spending money, reducing profits, and making it more difficult for the business to generate profits. Similarly, the IT department may think that the business side isn't interested in reducing risks, at least until a costly security incident occurs.

Organizations often implement IT governance methods such as Control Objectives for Information and Related Technology (COBIT). These methods help business owners and mission owners balance security control requirements with business or mission needs. The overall goal is to provide a common language that all stakeholders can use to meet security and business needs.

### Data Processors and Data Controllers

Generically, a data processor is any system used to process data. However, in the context of the GDPR, data processor has a more specific meaning. The GDPR defines a data processor as “a natural or legal person, public authority, agency, or other body, which processes personal data solely on behalf of the data controller.”

In this context, the data controller is the person or entity that controls the processing of the data. The data controller decides what data to process, why this data should be processed, and how it is processed.

As an example, a company that collects personal information on employees for payroll is a data controller. If they pass this information to a third-party company to process payroll, the payroll company is the data processor. In this example, the payroll company (the data processor) must not use the data for anything other than processing payroll at the direction of the data controller.

The GDPR restricts data transfers to countries outside the EU. Companies that violate privacy rules in the GDPR may face fines of up to 4 percent of their global revenue. Unfortunately, it is filled with legalese, presenting many challenges for organizations. As an example, clause 107 includes this single sentence statement:

Consequently the transfer of personal data to that third country or international organisation should be prohibited, unless the requirements in this Regulation relating to transfers subject to appropriate safeguards, including binding corporate rules, and derogations for specific situations are fulfilled.

As a result, many organizations have created dedicated roles, such as a data privacy officer, to oversee the control of data and ensure the organization follows all relevant laws and regulations. The GDPR has mandated the role of a data protection officer for any organization that must comply with the GDPR. The person in this role is responsible for ensuring the organization applies the laws to protect individuals' private data.

### Data Custodians

Data owners often delegate day-to-day tasks to a data custodian . A custodian helps protect the integrity and security of data by ensuring that it is properly stored and protected. For example, custodians would ensure that the data is backed up by following guidelines in a backup policy. If administrators have configured auditing on the data, custodians would also maintain these logs.

In practice, personnel within an IT department or system security administrators would typically be the custodians. They might be the same administrators responsible for assigning permissions to data.

### Administrators

You'll often hear the term administrator(s) . However, the term means different things in different contexts. If Sally logs onto the Administrator account in a Windows system, she is an administrator. Similarly, anyone added to an Administrators group in Windows is also an administrator.

However, many organizations view anyone with elevated privileges as administrators, even if they don't have full administrative privileges. For example, help desk employees are granted some elevated privileges to perform their job but aren't granted full administrative privileges. In this context, they are sometimes referred to as administrators. In the context of data roles, a data administrator may be a data custodian or someone in another data role.

### Users and Subjects

A user is any person who accesses data via a computing system to accomplish work tasks. Users should have access only to the data they need to perform their work tasks. You can also think of users as employees or end users.

Users fall into a broader category of subjects, which are discussed further in Chapter 8 , “Principles of Security Models, Design, and Capabilities,” and Chapter 13 . A subject is any entity that accesses an object such as a file or folder. Subjects can be users, programs, processes, services, computers, or anything else that can access a resource.

The GDPR defines a data subject (not just a subject) as a person who can be identified through an identifier, such as a name, identification number, or other means. As an example, if a file includes PII on Sally Smith, Sally Smith is the data subject.
