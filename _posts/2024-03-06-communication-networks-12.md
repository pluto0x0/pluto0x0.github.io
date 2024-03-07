---
title: Communication Networks (12)
date: 2024-03-6 04:33:30
img_path: /_posts/
math: true
categories:
- Course Notes
- Communication Networks
---

## TCP reliable data transfer

### TCP ACK generation

![alt text](../upload/img/2024-03-05-communication-networks-11-image.png){: w="400" }

![alt text](../upload/img/2024-03-05-communication-networks-11-image-1.png){: w="400" }

![alt text](../upload/img/2024-03-05-communication-networks-11-image-2.png){: w="400" }

Arrival of in-order segment with expected seq #. One other segment has ACK pending | Immediately send single **cumulative** ACK, ACKing both in-order segments
Arrival of out-of-order segment higher-than-expect seq. #. Gap detected. | Immediately send **duplicate** ACK, indicating seq. # of next expected byte
Arrival of segment that partially or completely fills gap.|Immediate send ACK, provided that segment starts at lower end of gap
  
### TCP fast retransmit

TCP fast retransmit
: if sender receives 3 ACKs for same data (“triple duplicate ACKs”), resend unacked segment with smallest seq #
: likely that unacked segment lost, so don’t wait for timeout

![alt text](../upload/img/2024-03-05-communication-networks-11-image-3.png){: w="300" }

## TCP flow control

flow control
: receiver controls sender, so sender won’t overflow receiver’s buffer by transmitting too much, too fast

- receiver “advertises” free buffer space by including rwnd value in TCP header of receiver-to-sender segments
- sender limits amount of unacked (“in-flight”) data to receiver’s rwnd value
- guarantees receive buffer will not overflow

![alt text](../upload/img/2024-03-05-communication-networks-11-image-4.png){: w="300" }

## Connection Management

before exchanging data, sender/receiver “handshake”:

- agree to establish connection (each knowing the other willing to establish connection)
- agree on connection parameters

### TCP 3-way handshake

![alt text](../upload/img/2024-03-05-communication-networks-11-image-5.png){: w="700" }

### TCP closing a connection

![alt text](../upload/img/2024-03-05-communication-networks-11-image-6.png){: w="700" }

## Congestion Control

### Principles of congestion control

congestion
: “too many sources sending too much data too fast for network to handle”
: lost packets (buffer overflow at routers)

- congestion control: for network
- flow control: for reciever

#### one router, **infinite** buffers

![alt text](../upload/img/2024-03-06-communication-networks-12-image.png){: w="600" }

$$
T=\frac{1}{\mu-\lambda}
$$

#### one router, **finite** buffers

> TODO

### TCP Congestion Control: CWND

cwnd
: congestion window
: dynamic, function of perceived network congestion

LastByteSent - LastByteAcked $\le$ cwnd

$$
\text { rate } \approx \frac{\text { cwnd }}{\mathrm{RTT}} \text { bytes/sec }
$$


### TCP Slow Start 

