---
{
  "id": "chapter-78",
  "title": "Applied Cryptography",
  "order": 78,
  "source": {
    "href": "c07.xhtml",
    "anchor": "head-2-133"
  },
  "est_tokens": 7997,
  "slug": "applied-cryptography",
  "meta": {
    "nav_title": "Applied Cryptography",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Applied Cryptography

Up to this point, you've learned a great deal about the foundations of cryptography, the inner workings of various cryptographic algorithms, and the use of the public key infrastructure to distribute identity credentials using digital certificates. You should now feel comfortable with the basics of cryptography and be prepared to move on to higher-level applications of this technology to solve everyday communications problems.

In the following sections, we'll examine the use of cryptography to secure data at rest, such as that stored on portable devices, as well as data in transit, using techniques that include secure email, encrypted web communications, and networking.

### Portable Devices

The now ubiquitous nature of laptop computers, smartphones, and tablets brings new risks to the world of computing. Those devices often contain highly sensitive information that, if lost or stolen, could cause serious harm to an organization and its customers, employees, and affiliates. For this reason, many organizations turn to encryption to protect the data on these devices in the event they are misplaced.

Current versions of popular operating systems now include disk encryption capabilities that make it easy to apply and manage encryption on portable devices. For example, Microsoft Windows includes the BitLocker and Encrypting File System (EFS) technologies, macOS includes FileVault encryption, and the VeraCrypt open source package allows the encryption of disks on Linux, Windows, and Mac systems.

# Trusted Platform Module

Modern computers often include a specialized cryptographic component known as a Trusted Platform Module (TPM). The TPM is a chip that resides on the motherboard of the device. The TPM serves a number of purposes, including the storage and management of keys used for full-disk encryption (FDE) solutions. The TPM provides the operating system with access to the keys only if the user successfully authenticates. This prevents someone from removing the drive from one device and inserting it into another device to access the drive's data.

A wide variety of commercial tools are available that provide added features and management capability. The major differentiators between these tools are how they protect keys stored in memory, whether they provide full-disk or volume-only encryption, and whether they integrate with hardware-based Trusted Platform Modules (TPMs) to provide added security. Any effort to select encryption software should include an analysis of how well the alternatives compete on these characteristics.

Don't forget about smartphones when developing your portable device encryption policy. Most major smartphone and tablet platforms include enterprise-level functionality that supports encryption of data stored on the phone.

### Email

We have mentioned several times that security should be cost-effective. When it comes to email, simplicity is the most cost-effective option, but sometimes cryptography functions provide specific security services that you can't avoid using. Since ensuring security is also cost-effective, here are some simple rules about encrypting email:

- If you need confidentiality when sending an email message, encrypt the message.

- If your message must maintain integrity, you must hash the message.

- If your message needs authentication, integrity, and/or nonrepudiation, you should digitally sign the message.

- If your message requires confidentiality, integrity, origin authentication, and nonrepudiation, you should encrypt and digitally sign the message.

It is always the responsibility of the sender to put proper mechanisms in place to ensure that the security (that is, confidentiality, integrity, authenticity, and nonrepudiation) of a message or transmission is maintained.

The coverage of email in this chapter focuses on the use of cryptography to provide secure communications between two parties. You'll find more coverage of email security topics in Chapter 12 , “Secure Communications and Network Attacks.”

One of the most in-demand applications of cryptography is encrypting and signing email messages. Until recently, encrypted email required the use of complex, awkward software that in turn required manual intervention and complicated key exchange procedures. An increased emphasis on security in recent years resulted in the implementation of strong encryption technology in mainstream email packages. Next, we'll look at some of the secure email standards in widespread use today.

#### Pretty Good Privacy

Phil Zimmerman's Pretty Good Privacy (PGP) secure email system appeared on the computer security scene in 1991. It combines the CA hierarchy described earlier in this chapter with the “web of trust” concept—that is, you must become trusted by one or more PGP users to begin using the system. You then accept their judgment regarding the validity of additional users and, by extension, trust a multilevel “web” of users descending from your initial trust judgments.

PGP initially encountered a number of hurdles to widespread use. The most difficult obstruction was the U.S. government export regulations, which treated encryption technology as munitions and prohibited the distribution of strong encryption technology outside the United States. Fortunately, this restriction has since been repealed, and PGP may be freely distributed to most countries.

PGP is available in two versions: the commercial product that is now sold by Symantec and an open source variant called OpenPGP. These products allow for the use of modern encryption algorithms, hash functions, and signature standards within the PGP framework.

PGP messages are often sent in text-encoded format to facilitate compatibility with other email systems. Here is an example of how an encrypted message appears when sent using PGP:

```

-----BEGIN PGP MESSAGE-----

hQGMAyHB9q9kWbl7AQwAmgyZoaXC2Xvo3jrVIWains3/UvUImp3YEbcEmlLK+26o

TNGBSNi5jLi2A62e8TLGbPkJv5vN3JZH4F27ZvYIhqANwk2nTI1sE0bA2Rzlw6Pc

XCUooGhNY/rmmWTLvWNVRdSXZj2i28fk2gi2QJlrEwYLkKJdUxzKldSLht+Bc+V2

NbvQrTzJ0LmRq9FKvZ4lz5v7Qj/f1GdKF/5HCTthUWxJMxxuSzCp46rFR6sKAQXG

tHdi2IzrroyQLR23HO6KuleisGf1X2wzfWENlXMUNGNLxPi2YNvo3MaFMMw3o1dF

Zj28ptpCH8eGOVIAa05ZNnCk2a6alqTf9aKH8932uCS/AcYG3xqVcRCz7qyaLqD5

NFg4GXq10KD8Jo1VP/HncOx7/39MGRDuzJqFieQzsVo0uCwVB2zJYC0SeJyMHkyD

TaAxz4HMQxzm8FubreTfisXKuUfPbYAuT855kc2iBKTGo9Cz1WjhQo6mveI6hvu0

qYUaX5sGgfbD4bzCMFJj0nUBUdMni0jqHJ2XuZerEd8m0DioUOBRJybLlohtRkik

Gzra/+WGE1ckQmzch5LDPdIEZphvV+5/DbhHdhxN7QMWe6ZkaADAZRgu77tkQK6c

QvrBPZdk22uS0vzdwzJzzvybspzq1HkjD+aWR9CpSZ9mukZPXew=

=7NWG

-----END PGP MESSAGE-----
```

`-----BEGIN PGP MESSAGE-----`

`hQGMAyHB9q9kWbl7AQwAmgyZoaXC2Xvo3jrVIWains3/UvUImp3YEbcEmlLK+26o`

`TNGBSNi5jLi2A62e8TLGbPkJv5vN3JZH4F27ZvYIhqANwk2nTI1sE0bA2Rzlw6Pc`

`XCUooGhNY/rmmWTLvWNVRdSXZj2i28fk2gi2QJlrEwYLkKJdUxzKldSLht+Bc+V2`

`NbvQrTzJ0LmRq9FKvZ4lz5v7Qj/f1GdKF/5HCTthUWxJMxxuSzCp46rFR6sKAQXG`

`tHdi2IzrroyQLR23HO6KuleisGf1X2wzfWENlXMUNGNLxPi2YNvo3MaFMMw3o1dF`

`Zj28ptpCH8eGOVIAa05ZNnCk2a6alqTf9aKH8932uCS/AcYG3xqVcRCz7qyaLqD5`

`NFg4GXq10KD8Jo1VP/HncOx7/39MGRDuzJqFieQzsVo0uCwVB2zJYC0SeJyMHkyD`

`TaAxz4HMQxzm8FubreTfisXKuUfPbYAuT855kc2iBKTGo9Cz1WjhQo6mveI6hvu0`

`qYUaX5sGgfbD4bzCMFJj0nUBUdMni0jqHJ2XuZerEd8m0DioUOBRJybLlohtRkik`

`Gzra/+WGE1ckQmzch5LDPdIEZphvV+5/DbhHdhxN7QMWe6ZkaADAZRgu77tkQK6c`

`QvrBPZdk22uS0vzdwzJzzvybspzq1HkjD+aWR9CpSZ9mukZPXew=`

`=7NWG`

`-----END PGP MESSAGE-----`

Similarly, digitally signed messages contain the text of the message followed by a PGP signature. Here is an example:

```

-----BEGIN PGP SIGNED MESSAGE-----

Hash: SHA256

I am enjoying my preparation for the CISSP exam.

-----BEGIN PGP SIGNATURE-----

iQGzBAEBCAAdFiEE75kumjjPhsn37slI+Cb2Pddh6OYFAmAF4FMACgkQ+Cb2Pddh

6Oba4gv8D4ybEtYidHdlfDYfbF+wYAz8JZ0Mw//f41iwkBG6BO6RtKtNPV202Ngb

3Uxqjody48ndmDM4q60x3EMy+97ZXNoZL7fY5vv2viDa1so4BqevtRKYe6sfjxMg

XImhPVxUknWhJUlUopQvsetBe51nqiqhpVONx/GRDXR9gdmGO89gD7XSCy0vHhEW

AuoBVNBjbXqmxWdBPdrGcA9zFhdvxzmc6iI4zYe2mQxk1Nt1K6PRXNGjJLIxqchL

sD7rLVYG1I7+CLGYreJH0siW0Xltbr96qT++1u4tMo1ng1UraoB21zTPVcHA0pJu

DLrlXB0GFxVbDHpttOhYDPFZPk4NpzztDuAeNCA5/Oi3JJMjzBRrRuoIH7abmePX

qc0Bl1/DAbbiYd5uX01i8ejIveLoeb4OZfLZH/j+bJZT5762Wx0DwkVtm8smk6nl

+whpAZb5MV6SaS1xEcsRpU+w/O61OPteZ6eIHkU9pDu0yXM6IdtfRpqEw3LKVN/M

zblGsAq4

=GXp+

-----END PGP SIGNATURE-----
```

`-----BEGIN PGP SIGNED MESSAGE-----`

`Hash: SHA256`

`I am enjoying my preparation for the CISSP exam.`

`-----BEGIN PGP SIGNATURE-----`

`iQGzBAEBCAAdFiEE75kumjjPhsn37slI+Cb2Pddh6OYFAmAF4FMACgkQ+Cb2Pddh`

`6Oba4gv8D4ybEtYidHdlfDYfbF+wYAz8JZ0Mw//f41iwkBG6BO6RtKtNPV202Ngb`

`3Uxqjody48ndmDM4q60x3EMy+97ZXNoZL7fY5vv2viDa1so4BqevtRKYe6sfjxMg`

`XImhPVxUknWhJUlUopQvsetBe51nqiqhpVONx/GRDXR9gdmGO89gD7XSCy0vHhEW`

`AuoBVNBjbXqmxWdBPdrGcA9zFhdvxzmc6iI4zYe2mQxk1Nt1K6PRXNGjJLIxqchL`

`sD7rLVYG1I7+CLGYreJH0siW0Xltbr96qT++1u4tMo1ng1UraoB21zTPVcHA0pJu`

`DLrlXB0GFxVbDHpttOhYDPFZPk4NpzztDuAeNCA5/Oi3JJMjzBRrRuoIH7abmePX`

`qc0Bl1/DAbbiYd5uX01i8ejIveLoeb4OZfLZH/j+bJZT5762Wx0DwkVtm8smk6nl`

`+whpAZb5MV6SaS1xEcsRpU+w/O61OPteZ6eIHkU9pDu0yXM6IdtfRpqEw3LKVN/M`

`zblGsAq4`

`=GXp+`

`-----END PGP SIGNATURE-----`

The preceding example sends the message in plaintext with a PGP signature appended to the bottom. If you add encryption to protect the confidentiality of the message, the encryption is applied after the message is digitally signed, producing output that appears similar to any other encrypted message. For example, here is that same digitally signed message with encryption added:

```

-----BEGIN PGP MESSAGE-----

owEBBwL4/ZANAwAIAfgm9j3XYejmAaxAYgh0ZXN0LnR4dGAF4N1JIGFtIGVuam95

aW5nIG15IHByZXBhcmF0aW9uIGZvciB0aGUgQ0lTU1AgZXhhbS4KCokBswQAAQgA

HRYhBO+ZLpo4z4bJ9+7JSPgm9j3XYejmBQJgBeDdAAoJEPgm9j3XYejmLfoL/RRW

oDUl+AeZGffqwnYiJH2gB+Tn+pLjnXAhdf/YV4OsWEsjqKBvItctgcQuSOFJzuO+

jNgoCAFryi6RrwJ6dTh3F50QJYyJYlgIXCbkyVlaV6hXCZWPT40Bk/pI+HX9A6l4

J272xabjFf63/HiIEUJDHg/9u8FXKVvBImV3NuMMjJEqx9RcivwvpPn6YLJJ1MWy

zlUhu3sUIGDWNlArJ4SdskfY32hWAvHkgOAY8JSYmG6L6SVhvbRgv3d+rOOlutqK

4bVIO+fKMvxycnluPuwmVH99I1Ge8p1ciOMYCVg0dBEP/DeoFlQ4tvKMCPJG0w0E

ZgLgKyKQpjmNU9BheGvIfzRt1dKYeMx7lGZPlu7rr1Fk0oX/yMiaePWy5NYE2O5I

D6op9EcJImcMn8wmPM9YTZbmcfcumSpaG1i0EzzAT5eMXn3BoDij12JJrkCCbhYy

34u2CFR4WycGIIoFHV4RgKqu5TTuV+SCc//vgBaN20Qh9p7gRaNfOxHspto6fA==

=oTCB

-----END PGP MESSAGE-----
```

`-----BEGIN PGP MESSAGE-----`

`owEBBwL4/ZANAwAIAfgm9j3XYejmAaxAYgh0ZXN0LnR4dGAF4N1JIGFtIGVuam95`

`aW5nIG15IHByZXBhcmF0aW9uIGZvciB0aGUgQ0lTU1AgZXhhbS4KCokBswQAAQgA`

`HRYhBO+ZLpo4z4bJ9+7JSPgm9j3XYejmBQJgBeDdAAoJEPgm9j3XYejmLfoL/RRW`

`oDUl+AeZGffqwnYiJH2gB+Tn+pLjnXAhdf/YV4OsWEsjqKBvItctgcQuSOFJzuO+`

`jNgoCAFryi6RrwJ6dTh3F50QJYyJYlgIXCbkyVlaV6hXCZWPT40Bk/pI+HX9A6l4`

`J272xabjFf63/HiIEUJDHg/9u8FXKVvBImV3NuMMjJEqx9RcivwvpPn6YLJJ1MWy`

`zlUhu3sUIGDWNlArJ4SdskfY32hWAvHkgOAY8JSYmG6L6SVhvbRgv3d+rOOlutqK`

`4bVIO+fKMvxycnluPuwmVH99I1Ge8p1ciOMYCVg0dBEP/DeoFlQ4tvKMCPJG0w0E`

`ZgLgKyKQpjmNU9BheGvIfzRt1dKYeMx7lGZPlu7rr1Fk0oX/yMiaePWy5NYE2O5I`

`D6op9EcJImcMn8wmPM9YTZbmcfcumSpaG1i0EzzAT5eMXn3BoDij12JJrkCCbhYy`

`34u2CFR4WycGIIoFHV4RgKqu5TTuV+SCc//vgBaN20Qh9p7gRaNfOxHspto6fA==`

`=oTCB`

`-----END PGP MESSAGE-----`

As you can see, it is not possible to tell that this message is digitally signed until after it is decrypted.

Many commercial providers also offer PGP-based email services as web-based cloud email offerings, mobile device applications, or webmail plug-ins. These services appeal to administrators and end users because they remove the complexity of configuring and maintaining encryption certificates and provide users with a managed secure email service. Some products in this category include ProtonMail, StartMail, Mailvelope, SafeGmail, and Hushmail.

#### S/MIME

The Secure/Multipurpose Internet Mail Extensions (S/MIME) protocol has emerged as a de facto standard for encrypted email. S/MIME uses the RSA encryption algorithm and has received the backing of major industry players, including RSA Security. S/MIME has already been incorporated in a large number of commercial products, including these:

- Microsoft Outlook and Office 365

- Apple Mail

- Google G Suite Enterprise edition

S/MIME relies on the use of X.509 certificates for exchanging cryptographic keys. The public keys contained in these certificates are used for digital signatures and for the exchange of symmetric keys used for longer communications sessions. Users who receive a message signed with S/MIME will be able to verify that message by using the sender's digital certificate. Users who wish to use S/MIME for confidentiality or wish to create their own digitally signed messages must obtain their own certificates.

Despite strong industry support for the S/MIME standard, technical limitations have prevented its widespread adoption. Although major desktop mail applications support S/MIME email, mainstream web-based email systems do not support it out of the box (the use of browser extensions is required).

### Web Applications

Encryption is widely used to protect web transactions. This is mainly because of the strong movement toward ecommerce and the desire of both ecommerce vendors and consumers to securely exchange financial information (such as credit card information) over the web. We'll look at the two technologies that are responsible for the small lock icon within web browsers—Secure Sockets Layer (SSL) and Transport Layer Security (TLS).

#### Secure Sockets Layer (SSL)

SSL was originally developed by Netscape to provide client/server encryption for web traffic sent using the Hypertext Transfer Protocol Secure (HTTPS). Over the years, security researchers discovered a number of critical flaws in the SSL protocol that render it insecure for use today. However, SSL serves as the technical foundation for its successor, Transport Layer Security (TLS), which remains widely used today.

Even though TLS has been in existence for more than a decade, many people still mistakenly call it SSL. When you hear people use the term SSL , that's a red flag that you should further investigate to ensure that they're really using the modern, secure TLS and not the outdated SSL.

#### Transport Layer Security (TLS)

TLS relies on the exchange of server digital certificates to negotiate encryption/decryption parameters between the browser and the web server. TLS's goal is to create secure communications channels that remain open for an entire web browsing session. It depends on a combination of symmetric and asymmetric cryptography. The following steps are involved:

- When a user accesses a website, the browser retrieves the web server's certificate and extracts the server's public key from it.

- The browser creates a random symmetric key (known as the ephemeral key), uses the server's public key to encrypt it, and sends the encrypted symmetric key to the server.

- The server decrypts the symmetric key using its own private key, and the two systems exchange all future messages using the symmetric encryption key.

This approach allows TLS to leverage the advanced functionality of asymmetric cryptography while encrypting and decrypting the vast majority of the data exchanged using the faster symmetric algorithm.

When TLS was first proposed as a replacement for SSL, not all browsers supported the more modern approach. To ease the transition, early versions of TLS supported downgrading communications to SSL v3.0 when both parties did not support TLS. However, in 2011, TLS v1.2 dropped this backward compatibility.

In 2014, an attack known as the Padding Oracle On Downgraded Legacy Encryption (POODLE) demonstrated a significant flaw in the SSL 3.0 fallback mechanism of TLS. In an effort to remediate this vulnerability, many organizations completely dropped SSL support and now rely solely on TLS security.

The original version of TLS, TLS 1.0, was simply an enhancement to the SSL 3.0 standard. TLS 1.1, developed in 2006 as an upgrade to TLS 1.0, also contains known security vulnerabilities. TLS 1.2, released in 2008, is now considered the minimum secure option. TLS 1.3, released in 2018, is also secure and adds performance improvements.

It's important to understand that TLS is not an encryption algorithm itself. It is a framework within which other encryption algorithms may function. Therefore, it isn't sufficient to verify that a system is using a secure version of TLS. Security professionals must also ensure that the algorithms being used with TLS are secure as well.

Each system supporting TLS provides a listing of the cipher suites that it supports. These are combinations of encryption algorithms that it is willing to use together, and these lists are used by two systems to identify a secure option that both systems support. The cipher suite consists of four components:

- The key exchange algorithm that will be used to exchange the ephemeral key. For example, a server might support RSA, Diffie–Hellman (abbreviated DH) and Elliptic Curve Diffie Hellman (abbreviated ECDH).

- The authentication algorithm that will be used to prove the identity of the server and/or client. For example, a server might support RSA, DSA, and ECDSA.

- The bulk encryption algorithm that will be used for symmetric encryption. For example, a server might support multiple versions of AES and 3DES.

- The hash algorithm that will be used to create message digests. For example, a server might support different versions of the SHA algorithm.

Cipher suites are usually expressed in long strings that combine each of these four elements. For example, the cipher suite:

```

TLS_DH_RSA_WITH_AES_256_CBC_SHA384
```

`TLS_DH_RSA_WITH_AES_256_CBC_SHA384`

means that the server supports TLS using Diffie–Hellman key exchange (DH). In this cipher suite, it will perform authentication using the RSA protocol and will perform bulk encryption using AES CBC mode with a 256-bit key. Hashing will take place using the SHA-384 algorithm.

You may also see cipher suites that use DHE or ECDHE key exchange algorithms. The “E” indicates that the Diffie–Hellman (or Elliptic Curve Diffie–Hellman) algorithm uses different, ephemeral keys for each communication to provide forward secrecy and reduce the likelihood of key compromise. The “E” versions of these algorithms provide added security, but this comes at the cost of added computational complexity.

#### Tor and the Dark Web

Tor , formerly known as The Onion Router, provides a mechanism for anonymously routing traffic across the internet using encryption and a set of relay nodes. It relies on a technology known as perfect forward secrecy , where layers of encryption prevent nodes in the relay chain from reading anything other than the specific information they need to accept and forward the traffic. By using perfect forward secrecy in combination with a set of three or more relay nodes, Tor allows for both anonymous browsing of the standard internet, as well as the hosting of completely anonymous sites on the dark web.

### Steganography and Watermarking

Steganography is the art of using cryptographic techniques to embed secret messages within another message. Steganographic algorithms work by making alterations to the least significant bits of the many bits that make up image files. The changes are so minor that there is no appreciable effect on the viewed image. This technique allows communicating parties to conceal messages in plain sight—for example, they might embed a secret message within an illustration on an otherwise innocent web page.

It is also possible to embed messages inside larger excerpts of text. This approach is known as a concealment cipher.

Steganographers often embed their secret messages within images or WAV files because these files are often so large that the secret message would easily be missed by even the most observant inspector. Steganography techniques are often used for illegal activities, such as espionage and child pornography.

Steganography can also be used for legitimate purposes, however. Adding digital watermarks to documents to protect intellectual property is accomplished by means of steganography. The hidden information is known only to the file's creator. If someone later creates an unauthorized copy of the content, the watermark can be used to detect the copy and (if uniquely watermarked files are provided to each original recipient) trace the offending copy back to the source.

Steganography commonly works by modifying the least significant bit (LSB) of a pixel value. For example, each pixel might be described by using three decimal numbers ranging from 0 to 255. One represents the degree of red color in the image, the second represents blue, and the third represents green. If a pixel has a blue value of 64, changing that value to 65 would result in an imperceptible change but does allow the encoding of a bit of steganographic data.

Steganography is an extremely simple technology to use, with free tools openly available on the internet. Figure 7.2 shows the entire interface of one such tool, iSteg. It simply requires that you specify a text file containing your secret message and an image file that you wish to use to hide the message. Figure 7.3 shows an example of a picture with an embedded secret message; the message is impossible to detect with the human eye because the text file was added into the message by modifying only the least significant bits of the file. Those do not survive the printing process, and in fact, even if you examined the original full-color, high-resolution digital images, you would not be able to detect the difference.

FIGURE 7.2 Steganography tool

FIGURE 7.2 Steganography tool

FIGURE 7.3 Image with embedded message

FIGURE 7.3 Image with embedded message

### Networking

The final application of cryptography we'll explore in this chapter is the use of cryptographic algorithms to provide secure networking services. In the following sections, we'll take a brief look at methods used to secure communications circuits.

#### Circuit Encryption

Security administrators use two types of encryption techniques to protect data traveling over networks:

- Link encryption protects entire communications circuits by creating a secure tunnel between two points using either a hardware solution or a software solution that encrypts all traffic entering one end of the tunnel and decrypts all traffic entering the other end of the tunnel. For example, a company with two offices connected via a data circuit might use link encryption to protect against attackers monitoring at a point in between the two offices.

- End-to-end encryption protects communications between two parties (for example, a client and a server) and is performed independently of link encryption. An example of end-to-end encryption would be the use of TLS to protect communications between a user and a web server. This protects against an intruder who might be monitoring traffic on the secure side of an encrypted link or traffic sent over an unencrypted link.

The critical difference between link and end-to-end encryption is that in link encryption, all the data, including the header, trailer, address, and routing data, is also encrypted. Therefore, each packet has to be decrypted at each hop so that it can be properly routed to the next hop and then reencrypted before it can be sent along its way, which slows the routing. End-to-end encryption does not encrypt the header, trailer, address, and routing data, so it moves faster from point to point but is more susceptible to sniffers and eavesdroppers.

When encryption happens at the higher OSI layers, it is usually end-to-end encryption, and if encryption is done at the lower layers of the OSI model, it is usually link encryption.

Secure Shell (SSH) is a good example of an end-to-end encryption technique. This suite of programs provides encrypted alternatives to common internet applications such as the File Transfer Protocol (FTP), Telnet, and rlogin. There are actually two versions of SSH. SSH1 (which is now considered insecure) supports the Data Encryption Standard (DES), Triple DES (3DES), International Data Encryption Algorithm (IDEA), and Blowfish algorithms. SSH2 drops support for DES and IDEA but adds several security enhancements, including support for the Diffie–Hellman key exchange protocol and the ability to run multiple sessions over a single SSH connection. SSH2 provides added protection against man-in-the-middle (on-path) attacks, eavesdropping, and IP/DNS spoofing.

#### IPsec

Various security architectures are in use today, each one designed to address security issues in different environments. One such architecture that supports secure communications is the Internet Protocol security (IPsec) standard. IPsec is a standard architecture set forth by the Internet Engineering Task Force (IETF) for setting up a secure channel to exchange information between two entities.

The IP security (IPsec) protocol provides a complete infrastructure for secured network communications. IPsec has gained widespread acceptance and is now offered in a number of commercial operating systems out of the box. IPsec relies on security associations, and there are two main components:

- The Authentication Header (AH) provides assurances of message integrity and nonrepudiation. AH also provides authentication and access control and prevents replay attacks.

- The Encapsulating Security Payload (ESP) provides confidentiality and integrity of packet contents. It provides encryption and limited authentication and prevents replay attacks.

ESP also provides some limited authentication, but not to the degree of the AH. Though ESP is sometimes used without AH, it's rare to see AH used without ESP.

IPsec provides for two discrete modes of operation. When IPsec is used in transport mode for end-to-end encryption, only the packet payload is encrypted. This mode is designed for peer-to-peer communication. When it's used in tunnel mode , the entire packet, including the header, is encrypted. This mode is designed for link encryption.

At runtime, you set up an IPsec session by creating a security association (SA) . The SA represents the communication session and records any configuration and status information about the connection. The SA represents a simplex connection. If you want a two-way channel, you need two SAs, one for each direction. Also, if you want to support a bidirectional channel using both AH and ESP, you will need to set up four SAs.

Some of IPsec's greatest strengths come from being able to filter or manage communications on a per-SA basis so that clients or gateways between which security associations exist can be rigorously managed in terms of what kinds of protocols or services can use an IPsec connection. Also, without a valid security association defined, pairs of users or gateways cannot establish IPsec links.

Further details of the IPsec algorithm are provided in Chapter 11 , “Secure Network Architecture and Components.”

### Emerging Applications

Cryptography plays a central role in many emerging areas of cybersecurity and technology. Let's take a look at a few of these concepts: the blockchain, lightweight cryptography, and homomorphic encryption.

#### Blockchain

The blockchain is, in its simplest description, a distributed and immutable public ledger. This means that it can store records in a way that distributes those records among many different systems located around the world and do so in manner that prevents anyone from tampering with those records. The blockchain creates a data store that nobody can tamper with or destroy.

The first major application of the blockchain is cryptocurrency . The blockchain was originally invented as a foundational technology for Bitcoin, allowing the tracking of Bitcoin transactions without the use of a centralized authority. In this manner, the blockchain allows the existence of a currency that has no central regulator. Authority for Bitcoin transactions is distributed among all participants in the Bitcoin blockchain.

Although cryptocurrency is the blockchain application that has received the most attention, there are many other uses for a distributed immutable ledger—so much so that new applications of blockchain technology seem to be appearing every day. For example, property ownership records could benefit tremendously from a blockchain application. This approach would place those records in a transparent, public repository that is protected against intentional or accidental damage. Blockchain technology might also be used to track supply chains, providing consumers with confidence that their produce came from reputable sources and allowing regulators to easily track down the origin of recalled produce.

#### Lightweight Cryptography

There are many specialized use cases for cryptography that you may encounter during your career where computing power and energy might be limited.

Some devices operate at extremely low power levels and put a premium on conserving energy. For example, imagine sending a satellite into space with a limited power source. Thousands of hours of engineering go into getting as much life as possible out of that power source. Similar cases happen here on Earth, where remote sensors must transmit information using solar power, a small battery, or other equipment.

Smartcards are another example of a low-power environment. They must be able to securely communicate with smartcard readers but only using the energy either stored on the card or transferred to it by a magnetic field.

In these cases, cryptographers often design specialized hardware that is purpose-built to implement lightweight cryptographic algorithms with as little power expenditure as possible. You won't need to know the details of how these algorithms work, but you should be familiar with the concept that specialized hardware can minimize power consumption.

Another specialized use for cryptography is in cases where you need very low latency. That simply means that the encryption and decryption should not take a long time. Encrypting network links is a common example of low-latency cryptography. The data is moving quickly across a network and the encryption should be done as quickly as possible to avoid becoming a bottleneck.

Specialized encryption hardware also solves many low-latency requirements. For example, a dedicated VPN hardware device may contain cryptographic hardware that implements encryption and decryption operations in highly efficient form to maximize speed.

High resiliency requirements exist when it is extremely important that data be preserved and not accidentally destroyed during an encryption operation. In cases where resiliency is extremely important, the easiest way to address the issue is for the sender of data to retain a copy until the recipient confirms the successful receipt and decryption of the data.

#### Homomorphic Encryption

Privacy concerns also introduce some specialized use cases for encryption. In particular, we sometimes have applications where we want to protect the privacy of individuals but still want to perform calculations on their data. Homomorphic encryption technology allows this, encrypting data in a way that preserves the ability to perform computation on that data. When you encrypt data with a homomorphic algorithm and then perform computation on that data, you get a result that, when decrypted, matches the result you would have received if you had performed the computation on the plaintext data in the first place.
