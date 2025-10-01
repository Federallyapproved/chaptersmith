---
{
  "id": "chapter-247",
  "title": "Chapter 6: Cryptography and Symmetric Key Algorithms",
  "order": 247,
  "source": {
    "href": "b01.xhtml",
    "anchor": "head-2-8"
  },
  "est_tokens": 1154,
  "slug": "chapter-6-cryptography-and-symmetric-key-algorithms",
  "meta": {
    "nav_title": "Chapter 6: Cryptography and Symmetric Key Algorithms",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Chapter 6: Cryptography and Symmetric Key Algorithms

- A, D. Keys must be long enough to withstand attack for as long as the data is expected to remain sensitive. They should not be generated in a predictable way but, rather, should be randomly generated. Keys should be securely destroyed when they are no longer needed and not indefinitely retained. Longer keys do indeed provide greater security against brute-force attacks.

- A. Nonrepudiation prevents the sender of a message from later denying that they sent it. Confidentiality protects the contents of encrypted data from unauthorized disclosure. Integrity protects data from unauthorized modification. Availability is not a goal of cryptography.

- B. The strongest keys supported by the Advanced Encryption Standard are 256 bits. The valid AES key lengths are 128, 192, and 256 bits.

- D. The Diffie–Hellman algorithm allows the exchange of symmetric encryption keys between two parties over an insecure channel.

- A, D. Confusion and diffusion are two principles underlying most cryptosystems. Confusion occurs when the relationship between the plaintext and the key is so complicated that an attacker can't merely continue altering the plaintext and analyzing the resulting ciphertext to determine the key. Diffusion occurs when a change in the plaintext results in multiple changes spread throughout the ciphertext.

- B, C, D. AES provides confidentiality, integrity, and authentication when implemented properly. Nonrepudiation requires the use of a public key cryptosystem to prevent users from falsely denying that they originated a message and cannot be achieved with a symmetric cryptosystem, such as AES.

- D. Assuming that it is used properly, the one-time pad is the only known cryptosystem that is not vulnerable to attacks. All other cryptosystems, including transposition ciphers, substitution ciphers, and even AES, are vulnerable to attack, even if no attack has yet been discovered.

- B, C, D. The encryption key must be at least as long as the message to be encrypted. This is because each key element is used to encode only one character of the message. The three other facts listed are all characteristics of one-time pad systems.

- C. In a symmetric cryptosystem, a unique key exists for each pair of users. In this case, every key involving the compromised user must be changed, meaning that the key that the user shared with each of the other 19 users must be changed.

- C. Block ciphers operate on message “chunks” rather than on individual characters or bits. The other ciphers mentioned are all types of stream ciphers that operate on individual bits or characters of a message.

- A. Symmetric key cryptography uses a shared secret key. All communicating parties utilize the same key for communication in any direction. Therefore, James only needs to create a single symmetric key to facilitate this communication.

- B. M of N Control requires that a minimum number of agents (M) out of the total number of agents (N) work together to perform high-security tasks. M of N Control is an example of a split knowledge technique, but not all split knowledge techniques are used for key escrow.

- A. An initialization vector (IV) is a random bit string (a nonce) that is the same length as the block size that is XORed with the message. IVs are used to create a unique ciphertext every time the same message is encrypted with the same key. Vigenère ciphers are an example of a substitution cipher technique. Steganography is a technique used to embed hidden messages within a binary file. Stream ciphers are used to encrypt continuous streams of data.

- B. Galois/Counter Mode (GCM) and Counter with Cipher Block Chaining Message Authentication Code mode (CCM) are the only two modes that provide both confidentiality and data authenticity. Other modes, including Electronic Code Book (ECB), Output Feedback (OFB), and Counter (CTR) modes, only provide confidentiality.

- D. Data that is stored in memory is being actively used by a system and is considered data in use. Data at rest is data that is stored on nonvolatile media, such as a disk. Data in motion is being actively transferred over a network.

- B, C. The Advanced Encryption Standard (AES) and Rivest Cipher 6 (RC6) are modern, secure algorithms. The Data Encryption Standard (DES) and Triple DES (3DES) are outdated and no longer considered secure.

- B. One important consideration when using CBC mode is that errors propagate—if one block is corrupted during transmission, it becomes impossible to decrypt that block and the next block as well. The other modes listed here do not suffer from this flaw.

- C. Offline key distribution requires a side channel of trusted communication, such as in-person contact. This can be difficult to arrange when users are geographically separated. Alternatively, the individuals could use the Diffie–Hellman algorithm or other asymmetric/public key encryption technique to exchange a secret key. Key escrow is a method for managing the recovery of lost keys and is not used for key distribution.

- A. The AES-256 algorithm is a modern, secure cryptographic algorithm. 3DES, RC4, and Skipjack are all outdated algorithms that suffer from significant security issues.

- C. A separate key is required for each pair of users who want to communicate privately. In a group of six users, this would require a total of 15 secret keys. You can calculate this value by using the formula (n * (n – 1) / 2). In this case, n = 6, resulting in (6 * 5) / 2 = 15 keys.
