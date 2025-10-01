---
{
  "id": "chapter-77",
  "title": "Chapter Transport Layer Security (TLS) is the most well-known example of hybrid cryptography, and we discuss that approach later in this chapter. \u2014 Hybrid Cryptography",
  "order": 77,
  "source": {
    "href": "c07.xhtml",
    "anchor": "head-2-132"
  },
  "est_tokens": 276,
  "slug": "chapter-transport-layer-security-tls-is-the-most-well-known-example-of-hybrid-cryptography-and-we-discuss-that-approach-later-in-this-chapter-hybrid-cryptograph",
  "meta": {
    "nav_title": "Hybrid Cryptography",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Hybrid Cryptography

You've now learned about the two major categories of cryptographic systems: symmetric and asymmetric algorithms. You've also learned about the major advantages and disadvantages of each. Chief among these are the facts that symmetric algorithms are fast but introduce key distribution challenges and, though asymmetric algorithms solve the key distribution problem, they are also computationally intensive and slow. If you're choosing between these approaches, you're forced to make a decision between convenience and speed.

Hybrid cryptography combines symmetric and asymmetric cryptography to achieve the key distribution benefits of asymmetric cryptosystems with the speed of symmetric algorithms. These approaches work by setting up an initial connection between two communicating entities using asymmetric cryptography. That connection is used for only one purpose: the exchange of a randomly generated shared secret key, known as an ephemeral key . The two parties then exchange whatever data they wish using the shared secret key with a symmetric algorithm. When the communication session ends, they discard the ephemeral key and then repeat the same process if they wish to communicate again later.

The beauty behind this approach is that it uses asymmetric cryptography for key distribution, a task that requires the encryption of only a small amount of data. Then it switches to the faster symmetric algorithm for the vast majority of data exchanged.

Transport Layer Security (TLS) is the most well-known example of hybrid cryptography, and we discuss that approach later in this chapter.
