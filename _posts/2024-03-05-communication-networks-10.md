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

receiver can’t see sender side.

![alt text](../upload/img/2024-03-05-communication-networks-10-image-2.png){: w="500" }

# TCP

point-to-point
: one sender, one receiver 

reliable, in-order byte steam
: no “message boundaries”

pipelined
: TCP congestion and flow control set window size
