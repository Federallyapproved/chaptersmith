---
{
  "id": "chapter-67",
  "title": "Cryptographic Lifecycle",
  "order": 67,
  "source": {
    "href": "c06.xhtml",
    "anchor": "head-2-118"
  },
  "est_tokens": 310,
  "slug": "cryptographic-lifecycle",
  "meta": {
    "nav_title": "Cryptographic Lifecycle",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Cryptographic Lifecycle

With the exception of the one-time pad, all cryptographic systems have a limited life span. Moore's law, a commonly cited trend in the advancement of computing power, states that the processing capabilities of a state-of-the-art microprocessor will double approximately every two years. This means that, eventually, processors will reach the amount of strength required to simply guess the encryption keys used for a communication.

Security professionals must keep this cryptographic lifecycle in mind when selecting an encryption algorithm and have appropriate governance controls in place to ensure that the algorithms, protocols, and key lengths selected are sufficient to preserve the integrity of a cryptosystem for however long it is necessary to keep the information it is protecting secret. Security professionals can use the following algorithm and protocol governance controls:

- Specifying the cryptographic algorithms (such as AES, 3DES, and RSA) acceptable for use in an organization

- Identifying the acceptable key lengths for use with each algorithm based on the sensitivity of information transmitted

- Enumerating the secure transaction protocols (such as TLS) that may be used

For example, if you're designing a cryptographic system to protect the security of business plans that you expect to execute next week, you don't need to worry about the theoretical risk that a processor capable of decrypting them might be developed a decade from now. On the other hand, if you're protecting the confidentiality of information that could be used to construct a nuclear bomb, it's virtually certain that you'll still want that information to remain secret 10 years in the future!
