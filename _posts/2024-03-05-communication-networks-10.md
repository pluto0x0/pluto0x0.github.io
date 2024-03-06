---
title: Communication Networks (10)
date: 2024-03-05 10:56:29
img_path: /_posts/
math: true
categories:
- Course Notes
- Communication Networks
---

# Reliable Data Transfer: Intuition

## Selective Repeat

- receiver individually acknowledges all correctly received pkts
- sender only resends pkts for which ACK not received
- sender window

<!-- ![alt text](../upload/img/2024-03-05-communication-networks-10-image.png){: w="700" } -->

![alt text](../upload/img/2024-03-05-communication-networks-10-image-1.png){: w="800" }

### Selective repeat: dilemma

Receiver can’t see sender side. Assume using Seq. No. 0, 1, 2, 3.

![alt text](../upload/img/2024-03-05-communication-networks-10-image-2.png){: w="400" }

# TCP

point-to-point
: one sender, one receiver

reliable, in-order byte steam
: no “message boundaries”

pipelined
: TCP congestion and flow control set window size

full duplex data
: bi-directional data flow in same connection
: MSS (maximum segment size)

connection-oriented
: handshaking (exchange of control msgs) inits sender, receiver state before data exchange

flow controlled:
: sender will not overwhelm receiver

![alt text](../upload/img/2024-03-05-communication-networks-10-image-3.png){: w="700" }

## Sequence number & ACK number

sequence numbers
: byte stream “number” of first byte in segment’s data

acknowledgements
: seq # of next byte expected from the other side
: cumulative ACK

Sequence numbers acknowledgements are 32-bits unsigned integers.

![alt text](../upload/img/2024-03-05-communication-networks-10-image-4.png){: w="500" }

![alt text](../upload/img/2024-03-05-communication-networks-10-image-5.png)

1. A sends 'C', which is the 42-th byte sent.
2. A has recieved the 78-th byte from B and expecting the 79-th.
3. B sends 'C', which is the 79-th byte sent
4. B has recieved the 42-th byte from B and expecting the 43-th.

## Tcp round Trip Time, Timeout

### RTT

SampleRTT
: measured time from segment transmission until ACK receipt

EstimatedRTT

$$
\text { EstimatedRTT }=(1-\alpha) \times \text { EstimatedRTT }+\alpha \times \text { SampleRTT }
$$

typical value: $\alpha = 0.125$

![alt text](../upload/img/2024-03-05-communication-networks-10-image-6.png){: w="500" }

### Timeout

Timeout Interval
: EstimatedRTT plus “safety margin”
: larger variation $\to$ larger safety margin

Deviation in RTT:

$$
\text { DevRTT }=(1-\beta) \times \text { DevRTT }+\beta \times \vert \text { SampleRTT }=\text { EstimatedRTT } \vert
$$

Typeical $\beta = 0.25$

$$
\text { TimeoutInterval }=\text { EstimatedRTT }+4 \times \text { DevRTT }
$$
