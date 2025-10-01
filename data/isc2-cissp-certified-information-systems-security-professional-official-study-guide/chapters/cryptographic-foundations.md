---
{
  "id": "chapter-64",
  "title": "Cryptographic Foundations",
  "order": 64,
  "source": {
    "href": "c06.xhtml",
    "anchor": "head-2-112"
  },
  "est_tokens": 10452,
  "slug": "cryptographic-foundations",
  "meta": {
    "nav_title": "Cryptographic Foundations",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Cryptographic Foundations

The study of any science must begin with a discussion of the fundamental principles upon which it is built. The following sections lay this foundation with a review of the goals of cryptography, an overview of the basic concepts of cryptographic technology, and a look at the major mathematical principles used by cryptographic systems.

### Goals of Cryptography

Security practitioners use cryptographic systems to meet four fundamental goals: confidentiality, integrity, authentication, and nonrepudiation. Achieving each of these goals requires the satisfaction of a number of design requirements, and not all cryptosystems are intended to achieve all four goals. In the following sections, we'll examine each goal in detail and give a brief description of the technical requirements necessary to achieve it.

#### Confidentiality

Confidentiality ensures that data remains private in three different situations: when it is at rest, when it is in transit, and when it is in use.

Confidentiality is perhaps the most widely cited goal of cryptosystems—the preservation of secrecy for stored information or for communications between individuals and groups. Two main types of cryptosystems enforce confidentiality:

- Symmetric cryptosystems use a shared secret key available to all users of the cryptosystem.

- Asymmetric cryptosystems use individual combinations of public and private keys for each user of the system.

Both of these concepts are explored in the section “Modern Cryptography,” later in this chapter.

When developing a cryptographic system for the purpose of providing confidentiality, you must think about the three different types of data that we discussed in Chapter 5 , “Protecting Security of Assets”:

- Data at rest , or stored data, resides in a permanent location awaiting access. Examples of data at rest include data stored on hard drives, backup tapes, cloud storage services, USB devices, and other storage media.

- Data in motion , or data on the wire, is data being transmitted across a network between two systems. Data in motion might be traveling on a corporate network, a wireless network, or the internet.

- Data in use is data that is stored in the active memory of a computer system, where it may be accessed by a process running on that system.

The concept of protecting data at rest and data in transit is often covered on the CISSP exam. You should also know that data in transit is also commonly called data on the wire , referring to the network cables that carry data communications.

Each of these situations poses different types of confidentiality risks that cryptography can protect against. For example, data in motion may be susceptible to eavesdropping attacks, whereas data at rest is more susceptible to the theft of physical devices. Data in use may be accessed by unauthorized processes if the operating system does not properly implement process isolation.

#### Integrity

Integrity ensures that data is not altered without authorization. If integrity mechanisms are in place, the recipient of a message can be certain that the message received is identical to the message that was sent. Similarly, integrity checks can ensure that stored data was not altered between the time it was created and the time it was accessed. Integrity controls protect against all forms of alteration, including intentional alteration by a third party attempting to insert false information, intentional deletion of portions of the data, and unintentional alteration by faults in the transmission process.

Message integrity is enforced through the use of encrypted message digests, known as digital signatures , created upon transmission of a message. The recipient of the message simply verifies that the message's digital signature is valid, ensuring that the message was not altered in transit. Integrity can be enforced by both public and secret key cryptosystems. This concept is discussed in detail in Chapter 7 , “PKI and Cryptographic Applications.” The use of cryptographic hash functions to protect file integrity is discussed in Chapter 21 , “Malicious Code and Application Attacks.”

#### Authentication

Authentication verifies the claimed identity of system users and is a major function of cryptosystems. For example, suppose that Bob wants to establish a communications session with Alice and they are both participants in a shared secret communications system. Alice might use a challenge-response authentication technique to ensure that Bob is who he claims to be.

Figure 6.1 shows how this challenge-response protocol would work in action. In this example, the shared-secret code used by Alice and Bob is quite straightforward—the letters of each word are simply reversed. Bob first contacts Alice and identifies himself. Alice then sends a challenge message to Bob, asking him to encrypt a short message using the secret code known only to Alice and Bob. Bob replies with the encrypted message. After Alice verifies that the encrypted message is correct, she trusts that Bob himself is truly on the other end of the connection.

FIGURE 6.1 Challenge-response authentication protocol

FIGURE 6.1 Challenge-response authentication protocol

#### Nonrepudiation

Nonrepudiation provides assurance to the recipient that the message was originated by the sender and not someone masquerading as the sender. It also prevents the sender from claiming that they never sent the message in the first place (also known as repudiating the message). Secret key, or symmetric key, cryptosystems (such as simple substitution ciphers) do not provide this guarantee of nonrepudiation. If Jim and Bob participate in a secret key communication system, they can both produce the same encrypted message using their shared secret key. Nonrepudiation is offered only by public key, or asymmetric, cryptosystems, a topic discussed in greater detail in Chapter 7 .

### Cryptography Concepts

As with any science, you must be familiar with certain terminology before studying cryptography. Let's take a look at a few of the key terms used to describe codes and ciphers. Before a message is put into a coded form, it is known as a plaintext message and is represented by the letter P when encryption functions are described. The sender of a message uses a cryptographic algorithm to encrypt the plaintext message and produce a ciphertext message, represented by the letter C . This message is transmitted by some physical or electronic means to the recipient. The recipient then uses a predetermined algorithm to decrypt the ciphertext message and retrieve the plaintext version. (For an illustration of this process, see Figure 6.3 later in this chapter.)

All cryptographic algorithms rely on keys to maintain their security. For the most part, a key is nothing more than a number. It's usually a very large binary number, but it's a number nonetheless. Every algorithm has a specific key space . The key space is the range of values that are valid for use as a key for a specific algorithm. A key space is defined by its bit size . Bit size is nothing more than the number of binary bits (0s and 1s) in the key. The key space is the range between the key that has all 0s and the key that has all 1s. Or to state it another way, the key space is the range of numbers from 0 to 2 n , where n is the bit size of the key. So, a 128-bit key can have a value from 0 to 2 128 (which is roughly 3.40282367 × 10 38 , a very big number!). It is absolutely critical to protect the security of secret keys. In fact, all of the security you gain from cryptography rests on your ability to keep the keys used private.

# Kerckhoffs's Principle

All cryptography relies on algorithms. An algorithm is a set of rules, usually mathematical, that dictates how encryption and decryption processes are to take place. Most cryptographers follow Kerckhoffs's principle, a concept that makes algorithms known and public, allowing anyone to examine and test them. Specifically, Kerckhoffs's principle (also known as Kerckhoffs's assumption) is that a cryptographic system should be secure even if everything about the system, except the key, is public knowledge. The principle can be summed up as “The enemy knows the system.”

A large number of cryptographers adhere to this principle, but not all agree. In fact, some believe that better overall security can be maintained by keeping both the algorithm and the key private. Kerckhoffs's adherents retort that the opposite approach includes the dubious practice of “security through obscurity” and believe that public exposure produces more activity and exposes more weaknesses more readily, leading to the abandonment of insufficiently strong algorithms and quicker adoption of suitable ones.

As you'll learn in this chapter and the next, different types of algorithms require different types of keys. In private key (or secret key) cryptosystems, all participants use a single shared key. In public key cryptosystems, each participant has their own pair of keys. Cryptographic keys are sometimes referred to as cryptovariables , particularly in U.S. government applications.

The art of creating and implementing secret codes and ciphers is known as cryptography . This practice is paralleled by the art of cryptanalysis —the study of methods to defeat codes and ciphers. Together, cryptography and cryptanalysis are commonly referred to as cryptology . Specific implementations of a code or cipher in hardware and software are known as cryptosystems .

Federal Information Processing Standard (FIPS) 140–2, “Security Requirements for Cryptographic Modules,” defines the hardware and software requirements for cryptographic modules that the federal government uses.

### Cryptographic Mathematics

Cryptography is no different from most computer science disciplines in that it finds its foundations in the science of mathematics. To fully understand cryptography, you must first understand the basics of binary mathematics and the logical operations used to manipulate binary values. The following sections present a brief look at some of the most fundamental concepts with which you should be familiar.

It's very unlikely that you'll be asked to directly use cryptographic math on the exam. However, a good grasp of these principles is crucial to understanding how security professionals apply cryptographic concepts to real-world security problems.

#### Boolean Mathematics

Boolean mathematics defines the rules used for the bits and bytes that form the nervous system of any computer. You're most likely familiar with the decimal system. It is a base 10 system in which an integer from 0 to 9 is used in each place and each place value is a multiple of 10. It's likely that our reliance on the decimal system has biological origins—human beings have 10 fingers that can be used to count.

Boolean math can be very confusing at first, but it's worth the investment of time to learn how logical functions work. You need to know these concepts to truly understand the inner workings of cryptographic algorithms.

Similarly, the computer's reliance on the Boolean system has electrical origins. In an electrical circuit, there are only two possible states—on (representing the presence of electrical current) and off (representing the absence of electrical current). All computation performed by an electrical device must be expressed in these terms, giving rise to the use of Boolean computation in modern electronics. In general, computer scientists refer to the on condition as a true value and the off condition as a false value.

#### Logical Operations

The Boolean mathematics of cryptography uses a variety of logical functions to manipulate data. We'll take a brief look at several of these operations.

##### AND

The AND operation (represented by the ∧ symbol) checks to see whether two values are both true. Table 6.1 shows a truth table that illustrates all four possible outputs for the AND function. In this truth table, the first two columns, X and Y, show the input values to the AND function. Remember, the AND function takes only two variables as input. In Boolean math, there are only two possible values for each of these variables (0=FALSE and 1=TRUE), leading to four possible inputs to the AND function. The X ∧ Y column shows the output of the AND function for the input values shown in the two adjacent columns. It's this finite number of possibilities that makes it extremely easy for computers to implement logical functions in hardware. Notice in Table 6.1 that only one combination of inputs (where both inputs are true) produces an output value of true.

TABLE 6.1 AND operation truth table

TABLE 6.1 AND operation truth table

Logical operations are often performed on entire Boolean words rather than single values. Take a look at the following example:

```

X:     0 1 1 0 1 1 0 0

Y:     1 0 1 0 0 1 1 1

___________________________

X ∧ Y: 0 0 1 0 0 1 0 0
```

`X:     0 1 1 0 1 1 0 0`

`Y:     1 0 1 0 0 1 1 1`

`___________________________`

`X ∧ Y: 0 0 1 0 0 1 0 0`

Notice that the AND function is computed by comparing the values of X and Y in each column. The output value is true only in columns where both X and Y are true.

`X`

`Y`

`X`

`Y`

##### OR

The OR operation (represented by the ∨ symbol) checks to see whether at least one of the input values is true. Refer to the truth table in Table 6.2 for all possible values of the OR function. Notice that the only time the OR function returns a false value is when both of the input values are false.

TABLE 6.2 OR operation truth table

TABLE 6.2 OR operation truth table

We'll use the same example we used in the previous section to show you what the output would be if X and Y were fed into the OR function rather than the AND function:

`X`

`Y`

```

X:     0 1 1 0 1 1 0 0

Y:     1 0 1 0 0 1 1 1

___________________________

X ∨ Y: 1 1 1 0 1 1 1 1
```

`X:     0 1 1 0 1 1 0 0`

`Y:     1 0 1 0 0 1 1 1`

`___________________________`

`X ∨ Y: 1 1 1 0 1 1 1 1`

##### NOT

The NOT operation (represented by the ~ symbol) simply reverses the value of an input variable. This function operates on only one variable at a time. Table 6.3 shows the truth table for the NOT function.

TABLE 6.3 NOT operation truth table

TABLE 6.3 NOT operation truth table

In this example, you take the value of X from the previous examples and run the NOT function against it:

`X`

```

X:  0 1 1 0 1 1 0 0

___________________________

~X: 1 0 0 1 0 0 1 1
```

`X:  0 1 1 0 1 1 0 0`

`___________________________`

`~X: 1 0 0 1 0 0 1 1`

##### Exclusive OR

The final logical function you'll examine in this chapter is perhaps the most important and most commonly used in cryptographic applications—the exclusive OR (XOR) function. It's referred to in mathematical literature as the XOR function and is commonly represented by the ⊕ symbol. The XOR function returns a true value when only one of the input values is true. If both values are false or both values are true, the output of the XOR function is false. Table 6.4 provides the truth table for the XOR operation.

TABLE 6.4 Exclusive OR operation truth table

TABLE 6.4 Exclusive OR operation truth table

The following operation shows the X and Y values when they are used as input to the XOR function:

`X`

`Y`

```

X:      0 1 1 0 1 1 0 0

Y:      1 0 1 0 0 1 1 1

___________________________

X ⊕ Y: 1 1 0 0 1 0 1 1
```

`X:      0 1 1 0 1 1 0 0`

`Y:      1 0 1 0 0 1 1 1`

`___________________________`

`X ⊕ Y: 1 1 0 0 1 0 1 1`

#### Modulo Function

The modulo function is extremely important in the field of cryptography. Think back to the early days when you first learned division. At that time, you weren't familiar with decimal numbers and compensated by showing a remainder value each time you performed a division operation. Computers don't naturally understand the decimal system either, and these remainder values play a critical role when computers perform many mathematical functions. The modulo function is, quite simply, the remainder value left over after a division operation is performed.

The modulo function is just as important to cryptography as the logical operations are. Be sure you're familiar with its functionality and can perform simple modular math.

The modulo function is usually represented in equations by the abbreviation mod , although it's also sometimes represented by the % operator. Here are several inputs and outputs for the modulo function:

```

8 mod 6 = 2

6 mod 8 = 6

10 mod 3 = 1

10 mod 2 = 0

32 mod 8 = 0

32 mod 26 = 6
```

`8 mod 6 = 2`

`6 mod 8 = 6`

`10 mod 3 = 1`

`10 mod 2 = 0`

`32 mod 8 = 0`

`32 mod 26 = 6`

We'll revisit this function in Chapter 7 when we explore the RSA public key encryption algorithm (named after Ron Rivest, Adi Shamir, and Leonard Adleman, its inventors).

#### One-Way Functions

A one-way function is a mathematical operation that easily produces output values for each possible combination of inputs but makes it impossible to retrieve the input values. Public key cryptosystems are all based on some sort of one-way function. In practice, however, it's never been proven that any specific known function is truly one way. Cryptographers rely on functions that they believe are one way, but it's always possible that they might be broken by future cryptanalysts.

Here's an example. Imagine you have a function that multiplies three numbers together. If you restrict the input values to single-digit numbers, it's a relatively straightforward matter to reverse-engineer this function and determine the possible input values by looking at the numerical output. For example, the output value 15 was created by using the input values 1, 3, and 5. However, suppose you restrict the input values to five-digit prime numbers. It's still quite simple to obtain an output value by using a computer or a good calculator, but reverse-engineering is not quite so simple. Can you figure out what three prime numbers were used to obtain the output value 10,718,488,075,259? Not so simple, eh? (As it turns out, the number is the product of the prime numbers 17,093; 22,441; and 27,943.) There are actually 8,363 five-digit prime numbers, so this problem might be attacked using a computer and a brute-force algorithm, but there's no easy way to figure it out in your head, that's for sure!

#### Nonce

Cryptography often gains strength by adding randomness to the encryption process. One method by which this is accomplished is through the use of a nonce. A nonce is a random number that acts as a placeholder variable in mathematical functions. When the function is executed, the nonce is replaced with a random number generated at the moment of processing for one-time use. The nonce must be a unique number each time it is used. One of the more recognizable examples of a nonce is an initialization vector (IV), a random bit string that is the same length as the block size (the amount of data to be encrypted in each operation) and is XORed with the message. IVs are used to create unique ciphertext every time the same message is encrypted using the same key.

#### Zero-Knowledge Proof

One of the benefits of cryptography is found in the mechanism to prove your knowledge of a fact to a third party without revealing the fact itself to that third party. This is often done with passwords and other secret authenticators.

The classic example of a zero-knowledge proof involves two individuals: Peggy and Victor. Peggy knows the password to a secret door located inside a circular cave, as shown in Figure 6.2 . Victor would like to buy the password from Peggy, but he wants Peggy to prove that she knows the password before paying her for it. Peggy doesn't want to tell Victor the password for fear that he won't pay later. The zero-knowledge proof can solve their dilemma.

FIGURE 6.2 The magic door

FIGURE 6.2 The magic door

Victor can stand at the entrance to the cave and watch Peggy depart down the path. Peggy then reaches the door and opens it using the password. She then passes through the door and returns via path 2. Victor saw her leave down path 1 and return via path 2, proving that she must know the correct password to open the door.

Zero-knowledge proofs appear in cryptography in cases where one individual wants to demonstrate knowledge of a fact (such as a password or key) without actually disclosing that fact to the other individual. This may be done through complex mathematical operations, such as discrete logarithms and graph theory.

#### Split Knowledge

When the information or privilege required to perform an operation is divided among multiple users, no single person has sufficient privileges to compromise the security of an environment. This separation of duties and two-person control contained in a single solution is called split knowledge . The best example of split knowledge is seen in the concept of key escrow . In a key escrow arrangement, a cryptographic key is stored with a third party for safekeeping. When certain circumstances are met, the third party may use the escrowed key to either restore an authorized user’s access or decrypt the material themselves. This third party is known as the recovery agent . In arrangements that use only a single key escrow recovery agent exists, there is opportunity for fraud and abuse of this privilege, as the single recovery agent could unilaterally decide to decrypt the information. M of N Control requires that a minimum number of agents ( M ) out of the total number of agents ( N ) work together to perform high-security tasks. So, implementing three of eight controls would require three people out of the eight with the assigned work task of key escrow recovery agent to work together to pull a single key out of the key escrow database (thereby also illustrating that M is always less than or equal to N ).

`M`

`N`

`M`

`N`

#### Work Function

You can measure the strength of a cryptography system by measuring the effort in terms of cost and/or time using a work function or work factor. Usually the time and effort required to perform a complete brute-force attack against an encryption system is what the work function represents. The security and protection offered by a cryptosystem is directly proportional to the value of the work function/factor. The size of the work function should be matched against the relative value of the protected asset. The work function need be only slightly greater than the time value of that asset. In other words, all security, including cryptography, should be cost-effective and cost-efficient. Spend no more effort to protect an asset than it warrants, but be sure to provide sufficient protection. Thus, if information loses its value over time, the work function needs to be only large enough to ensure protection until the value of the data is gone.

In addition to understanding the length of time that the data will have value, security professionals selecting cryptographic systems must understand how emerging technologies may impact cipher-cracking efforts. For example, researchers may discover a flaw in a cryptographic algorithm next year that renders information protected with that algorithm insecure. Similarly, technological advancements in cloud-based parallel computing and quantum computing may make brute-force efforts much more feasible down the road.

### Ciphers

Cipher systems have long been used by individuals and governments interested in preserving the confidentiality of their communications. In the following sections, we'll cover the definition of a cipher and explore several common cipher types that form the basis of modern ciphers. It's important to remember that these concepts seem somewhat basic, but when used in combination, they can be formidable opponents and cause cryptanalysts many hours of frustration.

#### Codes vs. Ciphers

People often use the words code and cipher interchangeably, but technically, they aren't interchangeable. There are important distinctions between the two concepts. Codes , which are cryptographic systems of symbols that represent words or phrases, are sometimes secret, but they are not necessarily meant to provide confidentiality. A common example of a code is the “10 system” of communications used by law enforcement agencies. Under this system, the sentence “I received your communication and understand the contents” is represented by the code phrase “10-4.” Semaphores and Morse code are also examples of codes. These codes are commonly known by the public and provide for ease of communication. Some codes are secret. They may convey confidential information using a secret codebook where the meaning of the code is known only to the sender and recipient. For example, a spy might transmit the sentence “The eagle has landed” to report the arrival of an enemy aircraft.

Ciphers , on the other hand, are always meant to hide the true meaning of a message. They use a variety of techniques to alter and/or rearrange the characters or bits of a message to achieve confidentiality. Ciphers convert messages from plaintext to ciphertext on a bit basis (that is, a single digit of a binary code), character basis (that is, a single character of an ASCII message), or block basis (that is, a fixed-length segment of a message, usually expressed in number of bits). The following sections cover several common ciphers in use today.

An easy way to keep the difference between codes and ciphers straight is to remember that codes work on words and phrases, whereas ciphers work on individual characters, bits, and blocks.

#### Transposition Ciphers

Transposition ciphers use an encryption algorithm to rearrange the letters of a plaintext message, forming the ciphertext message. The decryption algorithm simply reverses the encryption transformation to retrieve the original message.

In the challenge-response protocol example in Figure 6.1 earlier in this chapter, a simple transposition cipher was used to reverse the letters of the message so that apple became elppa . Transposition ciphers can be much more complicated than this. For example, you can use a keyword to perform a columnar transposition . In the following example, we're attempting to encrypt the message “The fighters will strike the enemy bases at noon” using the secret key attacker . Our first step is to take the letters of the keyword and number them in alphabetical order. The first appearance of the letter A receives the value 1; the second appearance is numbered 2. The next letter in sequence, C , is numbered 3, and so on. This results in the following sequence:

```

A T T A C K E R

1 7 8 2 3 5 4 6
```

`A T T A C K E R`

`1 7 8 2 3 5 4 6`

Next, the letters of the message are written in order underneath the letters of the keyword:

```

A T T A C K E R

1 7 8 2 3 5 4 6

T H E F I G H T

E R S W I L L S

T R I K E T H E

E N E M Y B A S

E S A T N O O N
```

`A T T A C K E R`

`1 7 8 2 3 5 4 6`

`T H E F I G H T`

`E R S W I L L S`

`T R I K E T H E`

`E N E M Y B A S`

`E S A T N O O N`

Finally, the sender enciphers the message by reading down each column; the order in which the columns are read corresponds to the numbers assigned in the first step. This produces the following ciphertext:

```

T E T E E F W K M T I I E Y N H L H A O G L T B O T S E S N H R R N S E S I E A
```

`T E T E E F W K M T I I E Y N H L H A O G L T B O T S E S N H R R N S E S I E A`

On the other end, the recipient reconstructs the eight-column matrix using the ciphertext and the same keyword and then simply reads the plaintext message across the rows.

#### Substitution Ciphers

Substitution ciphers use the encryption algorithm to replace each character or bit of the plaintext message with a different character. One of the earliest known substitution ciphers was used by Julius Caesar to communicate with Cicero in Rome while he was conquering Europe. Caesar knew that there were several risks when sending messages—one of the messengers might be an enemy spy or might be ambushed while en route to the deployed forces. For that reason, Caesar developed a cryptographic system now known as the Caesar cipher . The system is extremely simple. To encrypt a message, you simply shift each letter of the alphabet three places to the right. For example, A would become D , and B would become E . If you reach the end of the alphabet during this process, you simply wrap around to the beginning so that X becomes A , Y becomes B , and Z becomes C . For this reason, the Caesar cipher also became known as the ROT3 (or Rotate 3) cipher. The Caesar cipher is a substitution cipher that is mono-alphabetic.

Although the Caesar cipher uses a shift of 3, the more general shift cipher uses the same algorithm to shift any number of characters desired by the user. For example, the ROT12 cipher would turn an A into an M , a B into an N , and so on.

Here's an example of the Caesar cipher in action. The first line contains the original sentence, and the second line shows what the sentence looks like when it is encrypted using the Caesar cipher.

```

THE DIE HAS BEEN CAST

WKH GLH KDV EHHQ FDVW
```

`THE DIE HAS BEEN CAST`

`WKH GLH KDV EHHQ FDVW`

To decrypt the message, you simply shift each letter three places to the left.

Although the Caesar cipher is easy to use, it's also easy to crack. It's vulnerable to a type of attack known as frequency analysis . The most common letters in the English language are E , T , A , O , N , R , I , S , and H . An attacker seeking to break a Caesar-style cipher encoding a message that was written in English merely needs to find the most common letters in the encrypted text and experiment with substitutions of these common letters to help determine the pattern.

You can express the ROT3 cipher in mathematical terms by converting each letter to its decimal equivalent (where A is 0 and Z is 25). You can then add three to each plaintext letter to determine the ciphertext. You account for the wrap-around by using the modulo function discussed in the section “Cryptographic Mathematics,” earlier in this chapter. The final encryption function for the Caesar cipher is then this:

```

C = (P + 3) mod 26
```

`C = (P + 3) mod 26`

The corresponding decryption function is as follows:

```

P = (C - 3) mod 26
```

`P = (C - 3) mod 26`

As with transposition ciphers, there are many substitution ciphers that are more sophisticated than the examples provided in this chapter. Polyalphabetic substitution ciphers use multiple alphabets in the same message to hinder decryption efforts. One of the most notable examples of a polyalphabetic substitution cipher system is the Vigenère cipher. The Vigenère cipher uses a single encryption/decryption chart, as shown here:

```

 |A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

A|A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

B|B C D E F G H I J K L M N O P Q R S T U V W X Y Z A

C|C D E F G H I J K L M N O P Q R S T U V W X Y Z A B

D|D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

E|E F G H I J K L M N O P Q R S T U V W X Y Z A B C D

F|F G H I J K L M N O P Q R S T U V W X Y Z A B C D E

G|G H I J K L M N O P Q R S T U V W X Y Z A B C D E F

H|H I J K L M N O P Q R S T U V W X Y Z A B C D E F G

I|I J K L M N O P Q R S T U V W X Y Z A B C D E F G H

J|J K L M N O P Q R S T U V W X Y Z A B C D E F G H I

K|K L M N O P Q R S T U V W X Y Z A B C D E F G H I J

L|L M N O P Q R S T U V W X Y Z A B C D E F G H I J K

M|M N O P Q R S T U V W X Y Z A B C D E F G H I J K L

N|N O P Q R S T U V W X Y Z A B C D E F G H I J K L M

O}O P Q R S T U V W X Y Z A B C D E F G H I J K L M N

P|P Q R S T U V W X Y Z A B C D E F G H I J K L M N O

Q|Q R S T U V W X Y Z A B C D E F G H I J K L M N O P

R|R S T U V W X Y Z A B C D E F G H I J K L M N O P Q

S|S T U V W X Y Z A B C D E F G H I J K L M N O P Q R

T|T U V W X Y Z A B C D E F G H I J K L M N O P Q R S

U|U V W X Y Z A B C D E F G H I J K L M N O P Q R S T

V|V W X Y Z A B C D E F G H I J K L M N O P Q R S T U

W|W X Y Z A B C D E F G H I J K L M N O P Q R S T U V

X|X Y Z A B C D E F G H I J K L M N O P Q R S T U V W

Y|Y Z A B C D E F G H I J K L M N O P Q R S T U V W X

Z|Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
```

`|A B C D E F G H I J K L M N O P Q R S T U V W X Y Z`

`A|A B C D E F G H I J K L M N O P Q R S T U V W X Y Z`

`B|B C D E F G H I J K L M N O P Q R S T U V W X Y Z A`

`C|C D E F G H I J K L M N O P Q R S T U V W X Y Z A B`

`D|D E F G H I J K L M N O P Q R S T U V W X Y Z A B C`

`E|E F G H I J K L M N O P Q R S T U V W X Y Z A B C D`

`F|F G H I J K L M N O P Q R S T U V W X Y Z A B C D E`

`G|G H I J K L M N O P Q R S T U V W X Y Z A B C D E F`

`H|H I J K L M N O P Q R S T U V W X Y Z A B C D E F G`

`I|I J K L M N O P Q R S T U V W X Y Z A B C D E F G H`

`J|J K L M N O P Q R S T U V W X Y Z A B C D E F G H I`

`K|K L M N O P Q R S T U V W X Y Z A B C D E F G H I J`

`L|L M N O P Q R S T U V W X Y Z A B C D E F G H I J K`

`M|M N O P Q R S T U V W X Y Z A B C D E F G H I J K L`

`N|N O P Q R S T U V W X Y Z A B C D E F G H I J K L M`

`O}O P Q R S T U V W X Y Z A B C D E F G H I J K L M N`

`P|P Q R S T U V W X Y Z A B C D E F G H I J K L M N O`

`Q|Q R S T U V W X Y Z A B C D E F G H I J K L M N O P`

`R|R S T U V W X Y Z A B C D E F G H I J K L M N O P Q`

`S|S T U V W X Y Z A B C D E F G H I J K L M N O P Q R`

`T|T U V W X Y Z A B C D E F G H I J K L M N O P Q R S`

`U|U V W X Y Z A B C D E F G H I J K L M N O P Q R S T`

`V|V W X Y Z A B C D E F G H I J K L M N O P Q R S T U`

`W|W X Y Z A B C D E F G H I J K L M N O P Q R S T U V`

`X|X Y Z A B C D E F G H I J K L M N O P Q R S T U V W`

`Y|Y Z A B C D E F G H I J K L M N O P Q R S T U V W X`

`Z|Z A B C D E F G H I J K L M N O P Q R S T U V W X Y`

Notice that the chart is simply the alphabet written repeatedly (26 times) under the master heading, shifting by one letter each time. You need a key to use the Vigenère system. For example, the key could be MILES . Then, you would perform the following encryption process:

- Write out the plaintext.

- Underneath, write out the encryption key, repeating the key as many times as needed to establish a line of text that is the same length as the plaintext.

- Convert each letter position from plaintext to ciphertext. Locate the column headed by the first plaintext character ( A ). Next, locate the row headed by the first character of the key ( S ). Finally, locate where these two items intersect, and write down the letter that appears there ( S ). This is the ciphertext for that letter position.

- Locate the column headed by the first plaintext character ( A ).

- Next, locate the row headed by the first character of the key ( S ).

- Finally, locate where these two items intersect, and write down the letter that appears there ( S ). This is the ciphertext for that letter position.

- Repeat steps 1 through 3 for each letter in the plaintext version. The results are shown in Table 6.5 . TABLE 6.5 Using the Vigenère system Stage of the process Letters Plaintext L A U N C H N O W Key M I L E S M I L E Ciphertext X I F R U T V Z A

TABLE 6.5 Using the Vigenère system

TABLE 6.5 Using the Vigenère system

`L A U N C H N O W`

`M I L E S M I L E`

`X I F R U T V Z A`

Although polyalphabetic substitution protects against direct frequency analysis, it is vulnerable to a second-order form of frequency analysis called period analysis , which is an examination of frequency based on the repeated use of the key.

#### One-Time Pads

A one-time pad is an extremely powerful type of substitution cipher. One-time pads use a different substitution alphabet for each letter of the plaintext message. They can be represented by the following encryption function, where K is the encryption key used to encrypt the plaintext letter P into the ciphertext letter C :

```

C = (P + K) mod 26
```

`C = (P + K) mod 26`

Usually, one-time pads are written as a very long series of numbers to be plugged into the function.

One-time pads are also known as Vernam ciphers , after the name of their inventor, Gilbert Sandford Vernam of AT&T Bell Labs.

The great advantage of one-time pads is that, when used properly, they are an unbreakable encryption scheme. There is no repeating pattern of alphabetic substitution, rendering cryptanalytic efforts useless. However, several requirements must be met to ensure the integrity of the algorithm:

- The one-time pad must be randomly generated. Using a phrase or a passage from a book would introduce the possibility that cryptanalysts could break the code.

- The one-time pad must be physically protected against disclosure. If the enemy has a copy of the pad, they can easily decrypt the enciphered messages.

You may be thinking at this point that the Caesar cipher, Vigenère cipher, and one-time pad sound very similar. They are! The only difference is the key length. The Caesar shift cipher uses a key of length one, the Vigenère cipher uses a longer key (usually a word or sentence), and the one-time pad uses a key that is as long as the message itself.

- Each one-time pad must be used only once. If pads are reused, cryptanalysts can compare similarities in multiple messages encrypted with the same pad and possibly determine the key values used. In fact, a common practice when using paper pads is to destroy the page of keying material after it is used to prevent reuse.

- The key must be at least as long as the message to be encrypted. This is because each character of the key is used to encode only one character of the message.

These one-time pad security requirements are essential knowledge for any network security professional. All too often, people attempt to implement a one-time pad cryptosystem but fail to meet one or more of these fundamental requirements. Read on for an example of how an entire Soviet code system was broken because of carelessness in this area.

If any one of these requirements is not met, the impenetrable nature of the one-time pad instantly breaks down. In fact, one of the major intelligence successes of the United States resulted when cryptanalysts broke a top-secret Soviet cryptosystem that relied on the use of one-time pads. In this project, code-named VENONA, a pattern in the way the Soviets generated the key values used in their pads was discovered. The existence of this pattern violated the first requirement of a one-time pad cryptosystem: the keys must be randomly generated without the use of any recurring pattern. The entire VENONA project was recently declassified and is publicly available on the National Security Agency website at www.nsa.gov/about/cryptologic-heritage/historical-figures-publications/publications/coldwar/assets/files/venona_story.pdf .

One-time pads have been used throughout history to protect extremely sensitive communications. The major obstacle to their widespread use is the difficulty of generating, distributing, and safeguarding the lengthy keys required. One-time pads can realistically be used only for short messages, because of key lengths.

If you're interested in learning more about one-time pads, there is a great description with photos and examples at www.cryptomuseum.com/crypto/otp/index.htm .

#### Running Key Ciphers

Many cryptographic vulnerabilities surround the limited length of the cryptographic key. As you learned in the previous section, one-time pads avoid these vulnerabilities by using a key that is at least as long as the message. However, one-time pads are awkward to implement because they require the physical exchange of pads.

One common solution to this dilemma is the use of a running key cipher (also known as a book cipher ). In this cipher, the encryption key is as long as the message itself and is often chosen from a common book, newspaper, or magazine. For example, the sender and recipient might agree in advance to use the text of a chapter from Moby-Dick , beginning with the third paragraph, as the key. They would both simply use as many consecutive characters as necessary to perform the encryption and decryption operations.

Let's look at an example. Suppose you wanted to encrypt the message “Richard will deliver the secret package to Matthew at the bus station tomorrow” using the key just described. This message is 66 characters in length, so you'd use the first 66 characters of the running key: “With much interest I sat watching him. Savage though he was, and hideously marred.” Any algorithm could then be used to encrypt the plaintext message using this key. Let's look at the example of modulo 26 addition, which converts each letter to a decimal equivalent, adds the plaintext to the key, and then performs a modulo 26 operation to yield the ciphertext. If you assign the letter A the value 0 and the letter Z the value 25, Table 6.6 shows the encryption operation for the first two words of the ciphertext.

TABLE 6.6 The encryption operation

TABLE 6.6 The encryption operation

`R`

`I`

`C`

`H`

`A`

`R`

`D`

`W`

`I`

`L`

`L`

`W`

`I`

`T`

`H`

`M`

`U`

`C`

`H`

`I`

`N`

`T`

`17`

`8`

`2`

`7`

`0`

`17`

`3`

`22`

`8`

`11`

`11`

`22`

`8`

`19`

`7`

`12`

`20`

`2`

`7`

`8`

`13`

`19`

`13`

`16`

`21`

`14`

`12`

`11`

`5`

`3`

`16`

`24`

`4`

`N`

`Q`

`V`

`O`

`M`

`L`

`F`

`D`

`Q`

`Y`

`E`

When the recipient receives the ciphertext, they use the same key and then subtract the key from the ciphertext, perform a modulo 26 operation, and then convert the resulting plaintext back to alphabetic characters.

#### Block Ciphers

Block ciphers operate on “chunks,” or blocks, of a message and apply the encryption algorithm to an entire message block at the same time. The transposition ciphers are examples of block ciphers. The simple algorithm used in the challenge-response algorithm takes an entire word and reverses its letters. The more complicated columnar transposition cipher works on an entire message (or a piece of a message) and encrypts it using the transposition algorithm and a secret keyword. Most modern encryption algorithms implement some type of block cipher.

#### Stream Ciphers

Stream ciphers operate on one character or bit of a message (or data stream) at a time. The Caesar cipher is an example of a stream cipher. The one-time pad is also a stream cipher because the algorithm operates on each letter of the plaintext message independently. Stream ciphers can also function as a type of block cipher. In such operations there is a buffer that fills up to real-time data that is then encrypted as a block and transmitted to the recipient.

#### Confusion and Diffusion

Cryptographic algorithms rely on two basic operations to obscure plaintext messages—confusion and diffusion. Confusion occurs when the relationship between the plaintext and the key is so complicated that an attacker can't merely continue altering the plaintext and analyzing the resulting ciphertext to determine the key. Diffusion occurs when a change in the plaintext results in multiple changes spread throughout the ciphertext. Consider, for example, a cryptographic algorithm that first performs a complex substitution and then uses transposition to rearrange the characters of the substituted ciphertext. In this example, the substitution introduces confusion, and the transposition introduces diffusion.
