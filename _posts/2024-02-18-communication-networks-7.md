---
title: Communication Networks (7)
date: 2024-02-18 08:20:19
img_path: /_posts/
math: true
categories:
- Course Notes
- Communication Networks
image:
  path: ../upload/img/2024-02-18-communication-networks-7-image-1.png
---

## Pure P2P architecture

- no always-on server
- arbitrary end systems directly communicate
- peers are intermittently connected and change IP addresses

### File distribution: client-server vs P2P

![alt text](../upload/img/2024-02-18-communication-networks-7-image.png){: w="600" }
_client-server model_

Time to distribute $F$ to $N$ clients using client-server approach

$$
D_{c-s} \geq \max \left\{N F / u_s, F / d_{\min }\right\}
$$

Time to  distribute $F$ to $N$ clients using P2P approach

$$
D_{P 2 P} \geq \max \left\{F / u_s, F / d_{\min }, N F /\left(u_s+\sum u_i\right)\right\}
$$

### P2P file distribution: BitTorrent

- File divided into 256Kb chunks
- Peers in torrent send/receive file chunks

![alt text](../upload/img/2024-02-18-communication-networks-7-image-1.png){: w="600" }

peer joining torrent:

- has no chunks, accumulate them over time from other peers.
- registers with tracker to get list of peers, connects to **subset of peers** (“neighbors”)

requesting chunks:

- different peers have different subsets of file chunks
- periodically, asks each peer for list of chunks that they have
- requests missing chunks from peers, rarest first

sending chunks: tit-for-tat

- sends chunks to those four peers currently sending her chunks at highest rate
  - re-evaluate top 4 every 10 secs
  - other peers are choked by Alice (do not receive chunks from her)
- every 30 secs: randomly select another peer, starts sending chunks
  - newly chosen peer may join top 4 (and unchoke them)

## Distributed Hash Table (DHT)

Compared to simple Database, use Hash Table: `key` = hash(`original key`)

Original|Key|Key Value
--|--|--
John Washington|8962458|132-54-3570
Diana Louise Jones|7800356|761-55-3791
...|...|...

- Evenly distribute `(key, value)` over pairs
- Any peer can query database with a key
- Each peer only knows about a small number of other peers
- small number of messages exchanged among peers

### Assign key-value pairs to peers

rule: assign key-value pair to the peer that has the closest ID (**the immediate successor**).

> e.g., ID space $\{0,1,2,3,…,63\}$
> suppose 8 peers: $1, 12, 13, 25, 32, 40, 48, 60$
>
> - If key = 51, then assigned to peer 60
> - If key = 60, then assigned to peer 60
> - If key = 61, then assigned to peer 1
{: .prompt-tip }

### Silly Strawman Circular DHT

each peer only aware of immediate successor and predecessor.

![alt text](../upload/img/2024-02-18-communication-networks-7-image-2.png){: w="400" }

![alt text](../upload/img/2024-02-18-communication-networks-7-image-3.png){: w="500" }
_$O(N)$_

### Circular DHT with shortcuts (Chord)

![alt text](../upload/img/2024-02-18-communication-networks-7-image-5.png){: w="500" }
_$O(\log N)$_

### Peer churn

- peers may come and go (churn)
- each peer knows address of its two successors
- each peer periodically pings its two successors to check aliveness
- if immediate uccessor leaves, choose next successor as new immediate successor
- and ask for the successors of its new immediate successor

## Video Streaming and CDNs

- CBR: (constant bit rate): video encoding rate fixed
- VBR:  (variable bit rate): video encoding rate changes as amount of spatial, temporal coding changes
- examples:
  - MPEG 1 (CD-ROM) 1.5 Mbps
  - MPEG2 (DVD) 3-6 Mbps
  - MPEG4 (often used in Internet, < 1 Mbps)

### Streaming multimedia: DASH

DASH: Dynamic, Adaptive Streaming over HTTP

- divides video file into multiple chunks
- each chunk stored, encoded at different rates
- manifest file: provides URLs for different chunks
- client requests chunks according to server-to-client bandwidth.

### Content distribution networks (CDN)

- To stream content to hundreds of thousands of simultaneous users.
- Store/serve multiple copies of videos at multiple geographically distributed sites (CDN)

![alt text](../upload/img/2024-02-18-communication-networks-7-image-6.png){: w="600" }
