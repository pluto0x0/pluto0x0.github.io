---
title: Communication Networks (8)
date: 2024-02-18 22:53:26
img_path: /_posts/
math: true
categories:
- Course Notes
- Communication Networks
---

# Chapter 3: Transport Layer

## Transport services and protocols

- transport protocols run in end systems
- send side: breaks app messages into segments, passes to  network layer
- rcv side: reassembles segments into messages, passes to app layer
- TCP / UDP

TCP and UDP:

- TCP: reliable, in-order delivery
- UDP: unreliable, unordered delivery

**Transport** vs. **Network Layer**

- network layer: logical communication between hosts
- transport layer: logical communication between processes

## Multiplexing/Demultiplexing

- multiplexing at sender
- demultiplexing at receiver

host uses **IP addresses & port** numbers to direct segment to appropriate socket

![alt text](../upload/img/2024-02-18-communication-networks-7-image-7.png){: w="400" }
_TCP/UDP segment format_

### In Connectionless Demultiplexing (UDP)

In **UDP**, IP datagrams with same dest. port #, but **different** source IP addresses and/or source port numbers will be directed to **same socket** at dest.

### In Connection-Oriented Demux (TCP)

TCP socket identified by 4-tuple:

- source IP address
- source port number
- dest IP address
- dest port number

demux: receiver uses **all four values** to direct segment to appropriate socket

- server have different sockets for each connecting client
- non-persistent HTTP will have different socket for each request

## UDP: User Datagram Protocol [RFC 768]

- UDP segments may be: lost or delivered out-of-order to app
- connectionless
  - no handshaking between UDP sender, receiver
  - each UDP segment handled independently of others
- used in
  - streaming multimedia apps (loss tolerant, rate sensitive)
  - DNS
  - SNMP
  
![alt text](../upload/img/2024-02-18-communication-networks-7-image-8.png){: w="400" }
_UDP segment format_

checksum is used to detect errors.
