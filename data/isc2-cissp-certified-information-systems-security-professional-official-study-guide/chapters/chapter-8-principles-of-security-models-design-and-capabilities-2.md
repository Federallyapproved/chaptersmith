---
{
  "id": "chapter-270",
  "title": "Chapter 8: Principles of Security Models, Design, and Capabilities",
  "order": 270,
  "source": {
    "href": "b02.xhtml",
    "anchor": "head-2-31"
  },
  "est_tokens": 434,
  "slug": "chapter-8-principles-of-security-models-design-and-capabilities-2",
  "meta": {
    "nav_title": "Chapter 8: Principles of Security Models, Design, and Capabilities",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Chapter 8: Principles of Security Models, Design, and Capabilities

- Security models include state machine (establishes the concept of a perfectly secure system), information flow (controls movement of data), noninterference (actions of subjects at one level do not affect the system state or actions of subjects at other levels), take-grant (control passage of rights to subjects), access control matrix (provides a perspective on access of multiple subjects across multiple objects), Bell–LaPadula (protects confidentiality), Biba (protects integrity), Clark–Wilson (protects integrity), Brewer and Nash (avoids conflicts of interest), Goguen–Meseguer (protects integrity), Sutherland (protects integrity), Graham–Denning (provides for secure creation and deletion of both subjects and objects), and the Harrison–Ruzzo–Ullman (HRU) model (manages assignment of rights to subjects).

- The primary components of the trusted computing base (TCB) are the hardware and software elements used to enforce the security policy (these elements are called the TCB), the security perimeter distinguishing and separating TCB components from non-TCB components, and the reference monitor that serves as an access control device across the security perimeter.

- The two primary rules of Bell–LaPadula are the simple rule of no read-up and the star rule of no write-down. The two rules of Biba are the simple rule of no read-down and the star rule of no write-up.

- An open system is one with published APIs that allows third parties to develop products to interact with it. A closed system is one that is proprietary with no third-party product support. Open source is a coding stance that allows others to view the source code of a program. Closed source is an opposing coding stance that keeps source code confidential.

- There are at least eight design principles listed in this chapter: objects and subjects, open and closed systems, secure defaults, fail securely, keep it simple, zero trust, privacy by design, and trust by verify. Please compare your descriptions to the text in each section under the heading “Secure Design Principles.”
