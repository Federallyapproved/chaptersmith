---
{
  "id": "chapter-269",
  "title": "Chapter 7: PKI and Cryptographic Applications",
  "order": 269,
  "source": {
    "href": "b02.xhtml",
    "anchor": "head-2-30"
  },
  "est_tokens": 156,
  "slug": "chapter-7-pki-and-cryptographic-applications-2",
  "meta": {
    "nav_title": "Chapter 7: PKI and Cryptographic Applications",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Chapter 7: PKI and Cryptographic Applications

- Bob should encrypt the message using Alice's public key and then transmit the encrypted message to Alice.

- Alice would decrypt the message using her private key.

- Bob should generate a message digest from the plaintext message using a hash function. He should then encrypt the message digest using his own private key to create the digital signature. Finally, he should append the digital signature to the message and transmit it to Alice.

- Alice should decrypt the digital signature in Bob's message using Bob's public key. She should then create a message digest from the plaintext message using the same hashing algorithm Bob used to create the digital signature. Finally, she should compare the two message digests. If they are identical, the signature is authentic.
