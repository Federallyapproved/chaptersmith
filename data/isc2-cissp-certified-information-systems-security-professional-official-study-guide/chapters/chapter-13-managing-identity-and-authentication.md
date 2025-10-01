---
{
  "id": "chapter-254",
  "title": "Chapter 13: Managing Identity and Authentication",
  "order": 254,
  "source": {
    "href": "b01.xhtml",
    "anchor": "head-2-15"
  },
  "est_tokens": 1528,
  "slug": "chapter-13-managing-identity-and-authentication",
  "meta": {
    "nav_title": "Chapter 13: Managing Identity and Authentication",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Chapter 13: Managing Identity and Authentication

- A. An on-premises identity management system will provide the organization with the most control and is the best choice. A cloud-based solution is controlled by a third party. Either an on-premises or a cloud-based solution is needed. There's no need to have both in a hybrid solution. Identity management solutions provide single sign-on (SSO), but SSO is a benefit of identity management, not a type of identity management.

- A. A primary goal when controlling access to assets is to protect against losses, including any loss of confidentiality, loss of availability, or loss of integrity. Subjects authenticate on a system, but objects do not authenticate. Subjects access objects, but objects do not access subjects. Identification and authentication are important as the first step in access control, but much more is needed to protect assets.

- C. The subject is active and is always the entity that receives information about, or data from, the object. A subject can be a user, a program, a process, a file, a computer, a database, and so on. The object is always the entity that provides or hosts information or data. The roles of subject and object can switch while two entities communicate to accomplish a task.

- D. NIST SP 800-63B recommends users only be required to change their password if their current password is compromised. They do not recommend that users be required to change their password regularly at any interval.

- B. Password history can prevent users from rotating between two passwords. It remembers previously used passwords. Password complexity and password length help ensure that users create strong passwords. Password age ensures that users change their password regularly.

- B. A passphrase is a long string of characters that is easy to remember, such as IP@$$edTheCISSPEx@m. It is not short and typically includes at least three sets of character types. It is strong and complex, making it difficult to crack.

- A. A synchronous token generates and displays onetime passwords that are synchronized with an authentication server. An asynchronous token uses a challenge-response process to generate the onetime password. Smartcards do not generate onetime passwords, and common access cards are a version of a smartcard that includes a picture of the user.

- C. The point at which the biometric false rejection rate and the false acceptance rate are equal is the crossover error rate (CER). It does not indicate that sensitivity is too high or too low. A lower CER indicates a higher-quality biometric device, and a higher CER indicates a less accurate device.

- A. A false rejection, sometimes called a false negative authentication or a Type I error, occurs when an authentication doesn't recognize a valid subject (Sally in this example). A false acceptance, sometimes called a false positive authentication or a Type II error, occurs when an authentication system incorrectly recognizes an invalid subject. Crossover errors and equal errors aren't valid terms related to biometrics. However, the crossover error rate (also called equal error rate) compares the false rejection rate to the false acceptance rate and provides an accuracy measurement for a biometric system.

- C. An authenticator app on a smartphone or tablet device is the best solution. SMS has vulnerabilities, and NIST has deprecated its use for two-factor authentication. Biometric authentication methods, such as fingerprint scans, provide strong authentication. However, purchasing biometric readers for each employee's home would be expensive. A PIN is in the something you know factor of authentication, so it doesn't provide two-factor authentication when used with a password.

- B. Physical biometric methods such as fingerprints and iris scans provide authentication for subjects. An account ID provides identification. A token is something you have, and it creates onetime passwords, but it is not related to physical characteristics. A personal identification number (PIN) is something you know.

- B, C, D. Ridges, bifurcations, and whorls are fingerprint minutiae. Ridges are the lines in a fingerprint. Some ridges abruptly end, and some ridges bifurcate or fork into branch ridges. Whorls are a series of circles. Palm scans measure vein patterns in a palm.

- A. Fingerprints can be counterfeited or duplicated. It is not possible to change fingerprints. Users will always have a finger available (except for major medical events), so they will always have a fingerprint available. It usually takes less than a minute for registration of a fingerprint.

- A, D. Accurate identification and authentication are required to support accountability. Logs record events, including who took an action, but without accurate identification and authentication, the logs can't be relied on. Authorization grants access to resources after proper authentication. Auditing occurs after logs are created, but identification and authentication must occur first.

- C. Authentication is necessary to ensure a network supports accountability. Note that authentication indicates that a user claimed an identity such as with a username and proved the identity such as with a password. In other words, valid authentication includes identification. However, identification doesn't include authentication. If users could just claim an identity without proving it's their identity, the system doesn't support accountability. Audit trails (not available as a possible answer) help provide accountability as long as users have authenticated. Integrity provides assurances that unauthorized entities have not modified data or system settings. Confidentiality ensures that unauthorized entities can't access sensitive data and is unrelated to this question.

- C. The most likely reason (of the provided options) is to prevent sabotage. If the user's account remains enabled, the user may log on later and cause damage. Disabling the account doesn't remove the account or remove assigned privileges. Disabling an account doesn't encrypt any data, but it does retain encryption keys that supervisors can use to decrypt any data encrypted by the user.

- C. The most likely reason to delete the account (of the provided options) is if an employee left the organization and will start a new job tomorrow. It would not be appropriate to delete the account for any other answer options. If an administrator used their account to run services, deleting their account would prevent the services from running. It would be appropriate to disable the account of a disgruntled employee. If this employee encrypted data with their account, deleting the account would prevent access to the encrypted data. It would be appropriate to change the password of a shared account used by temporary employees.

- D. It's appropriate to disable an account when an employee takes a leave of absence of 30 days or more. The account should not be deleted because the employee will return after the leave of absence. If the password is reset, someone could still log on. If nothing is done to the account, someone else may access it and impersonate the employee.

- C. Account access reviews can detect security issues for service accounts such as the sa (short for system administrator) account in Microsoft SQL Server systems. Reviews can ensure that service account passwords are strong and changed often. The other options suggest removing, disabling, or deleting the sa account, but doing so is likely to affect the database server's performance. Account deprovisioning ensures accounts are removed when they are no longer needed. Disabling an account ensures it isn't used, and account revocation deletes the account.

- D. A periodic account access review can discover when users have more privileges than they need and could have been used to discover that this employee had permissions from several positions. Strong authentication methods (including multifactor authentication methods) would not have prevented the problems in this scenario. Logging records what happened, but it doesn't prevent events.
