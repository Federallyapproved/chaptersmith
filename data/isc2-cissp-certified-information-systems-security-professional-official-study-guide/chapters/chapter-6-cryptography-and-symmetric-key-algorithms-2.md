---
{
  "id": "chapter-268",
  "title": "Chapter 6: Cryptography and Symmetric Key Algorithms",
  "order": 268,
  "source": {
    "href": "b02.xhtml",
    "anchor": "head-2-29"
  },
  "est_tokens": 864,
  "slug": "chapter-6-cryptography-and-symmetric-key-algorithms-2",
  "meta": {
    "nav_title": "Chapter 6: Cryptography and Symmetric Key Algorithms",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Chapter 6: Cryptography and Symmetric Key Algorithms

- The major obstacle to the widespread adoption of one-time pad cryptosystems is the difficulty in creating and distributing the very lengthy keys on which the algorithm depends.

- The first step in encrypting this message requires the assignment of numeric column values to the letters of the secret keyword: S E C U R E 5 2 1 6 4 3 Next, the letters of the message are written in order underneath the letters of the keyword: S E C U R E 5 2 1 6 4 3 I W I L L P A S S T H E C I S S P E X A M A N D B E C O M E C E R T I F I E D N E X T M O N T H Finally, the sender enciphers the message by reading down each column; the order in which the columns are read corresponds to the numbers assigned in the first step. This produces the following ciphertext: I S S M C R D O W S I A E E E M P E E D E F X H L H P N M I E T I A C X B C I T L T S A O T N N

```

S E C U R E

5 2 1 6 4 3
```

`S E C U R E`

`5 2 1 6 4 3`

Next, the letters of the message are written in order underneath the letters of the keyword:

```

S E C U R E

5 2 1 6 4 3

I W I L L P

A S S T H E

C I S S P E

X A M A N D

B E C O M E

C E R T I F

I E D N E X

T M O N T H
```

`S E C U R E`

`5 2 1 6 4 3`

`I W I L L P`

`A S S T H E`

`C I S S P E`

`X A M A N D`

`B E C O M E`

`C E R T I F`

`I E D N E X`

`T M O N T H`

Finally, the sender enciphers the message by reading down each column; the order in which the columns are read corresponds to the numbers assigned in the first step. This produces the following ciphertext:

```

I S S M C R D O W S I A E E E M P E E D E F X H L H P N M I E T I A C X B C I T L T S A O T N N
```

`I S S M C R D O W S I A E E E M P E E D E F X H L H P N M I E T I A C X B C I T L T S A O T N N`

- This message is decrypted by using the following function: P = (C - 3) mod 26 C: F R Q J U D W X O D W L R Q V B R X J R W L W P: C O N G R A T U L A T I O N S Y O U G O T I T The hidden message is “Congratulations You Got It.” Congratulations, you got it!

```

P = (C - 3) mod 26

C: F R Q J U D W X O D W L R Q V B R X J R W L W

P: C O N G R A T U L A T I O N S Y O U G O T I T
```

`P = (C - 3) mod 26`

`C: F R Q J U D W X O D W L R Q V B R X J R W L W`

`P: C O N G R A T U L A T I O N S Y O U G O T I T`

The hidden message is “Congratulations You Got It.” Congratulations, you got it!
