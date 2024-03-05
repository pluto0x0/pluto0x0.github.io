---
title: Communication Networks (9)
date: 2024-03-05 10:56:29
img_path: /_posts/
math: true
categories:
- Course Notes
- Communication Networks
---

## Reliable Data Transfer: Intuition

rdt
: reliable data transfer protocol

udt
: unreliable data transfer protocol

![alt text](../upload/img/2024-02-19-communication-networks-9-image-1.png){: w="500" }

### Reliable Channel

channel is perfectly reliable:

- no bit errors
- no loss of packets

### Channel with Bit Errors

- underlying channel may flip bits in packet

Detect error: checksum

Recover from errors: receiver tells sender with:

- acknowledgements (ACKs)
- negative acknowledgements (NAKs)
