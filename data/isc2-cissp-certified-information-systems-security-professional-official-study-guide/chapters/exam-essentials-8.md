---
{
  "id": "chapter-90",
  "title": "Exam Essentials",
  "order": 90,
  "source": {
    "href": "c08.xhtml",
    "anchor": "head-2-154"
  },
  "est_tokens": 1143,
  "slug": "exam-essentials-8",
  "meta": {
    "nav_title": "Exam Essentials",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Exam Essentials

Be able to define object and subject in terms of access. The subject is the user or process that makes a request to access a resource. The object is the resource a user or process wants to access.

Be able to describe open and closed systems. Open systems are designed using industry standards and are usually easy to integrate with other open systems. Closed systems are generally proprietary hardware and/or software. Their specifications are not normally published, and they are usually harder to integrate with other systems.

Understand open and closed source. An open source solution is one where the source code, and other internal logic, is exposed to the public. A closed source solution is one where the source code and other internal logic is hidden from the public.

Know about secure defaults. Never assume the default settings of any product are secure. It is always up to the system's administrator and/or company security staff to alter a product's settings to comply with the organization's security policies.

Understand the concept of fail securely. Failure management includes programmatic error handling (aka exception handling) and input sanitization; secure failure is integrated into the system (fail-safe vs. fail-secure).

Know about the principle of “keep it simple.” “Keep it simple” is the encouragement to avoid overcomplicating the environment, organization, or product design. The more complex a system, the more difficult it is to secure.

Understand zero trust. Zero trust is a security concept where nothing inside the organization is automatically trusted. Each request for activity or access is assumed to be from an unknown and untrusted location until otherwise verified. The concept is “never trust, always verify.” The zero trust model is based around “assume breach” and microsegmentation.

Know about Privacy by Design. Privacy by Design (PbD) is a guideline to integrate privacy protections into products during the early design phase rather than attempting to tack them on at the end of development. The PbD framework is based on seven foundational principles.

Understand “trust but verify.” “Trust but verify” is a traditional security approach of trusting subjects and devices within the company's security perimeter automatically. This type of security approach leaves an organization vulnerable to insider attacks and grants intruders the ability to easily perform lateral movement among internal systems.

Know what confinement, bounds, and isolation are. Confinement restricts a process to reading from and writing to certain memory locations. Bounds are the limits of memory a process cannot exceed when reading or writing. Isolation is the mode a process runs in when it is confined through the use of memory bounds.

Know how security controls work and what they do. Security controls use access rules to limit the access by a subject to an object.

Understand trust and assurance. A trusted system is one in which all protection mechanisms work together to process sensitive data for many types of users while maintaining a stable and secure computing environment. In other words, trust is the presence of a security mechanism or capability. Assurance is the degree of confidence in satisfaction of security needs. In other words, assurance is how reliable the security mechanisms are at providing security.

Define a trusted computing base (TCB). A TCB is the combination of hardware, software, and controls that form a trusted base that enforces the security policy.

Be able to explain what a security perimeter is. A security perimeter is the imaginary boundary that separates the TCB from the rest of the system. TCB components communicate with non-TCB components using trusted paths.

Know what the reference monitor and the security kernel are. The reference monitor is the logical part of the TCB that confirms whether a subject has the right to use a resource prior to granting access. The security kernel is the collection of the TCB components that implement the functionality of the reference monitor.

Know details about each of the security models. Know the security models and their functions:

- The state machine model ensures that all instances of subjects accessing objects are secure.

- The information flow model is designed to prevent unauthorized, insecure, or restricted information flow.

- The noninterference model prevents the actions of one subject from affecting the system state or actions of another subject.

- The take-grant model dictates how rights can be passed from one subject to another or from a subject to an object.

- An access control matrix is a table of subjects and objects that indicates the actions or functions that each subject can perform on each object.

- Bell–LaPadula subjects have a clearance level that allows them to access only those objects with the corresponding classification levels, which protects confidentiality.

- Biba prevents subjects with lower security levels from writing to objects at higher security levels.

- Clark–Wilson is an integrity model that relies on the access control triplet (i.e., subject/program/object).

- Goguen–Meseguer and Sutherland models focus on integrity.

- Graham–Denning focuses on the secure creation and deletion of both subjects and objects.

- The Harrison–Ruzzo–Ullman (HRU) model focuses on the assignment of object access rights to subjects as well as the integrity (or resilience) of those assigned rights.

- The Common Criteria (ISO/IEC 15408) is a subjective security function evaluation tool that uses protection profiles (PPs) and security targets (STs) and assigns an Evaluation Assurance Level (EAL).

- Authorization to Operate (ATO) (from the RMF) is a formal approval to operate IT/IS based on an acceptable risk level based on the implementation of an agreed-on set of security and privacy controls.

Understand the security capabilities of information systems. Common security capabilities include memory protection, virtualization, Trusted Platform Module (TPM), encryption/decryption, interfaces, and fault tolerance.
