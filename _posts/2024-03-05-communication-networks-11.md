---
title: Communication Networks (11)
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

