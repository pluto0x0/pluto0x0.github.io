---
title: Communication Networks (5)
date: 2024-01-31 21:56
img_path: /_posts/
math: true
mermaid: true
image:
    path: ../upload/img/2024-01-29-communication-networks-4-image-1.png
---

## Internet transport protocols services

### TCP service

- reliable transport
- flow control
  - sender won’t overwhelm receiver
- congestion control
  - throttle sender when network overloaded
- does not provide
  - timing
  - minimum throughput guarantee
  - security
- connection-oriented

### UDP service

- unreliable data transfer between sending and receiving process
- does not provide
  - reliability
  - flow control
  - congestion control
  - timing
  - throughput guarantee
  - security
  - connection setup

### Applications & transport protocols

| Application            | Application Layer Protocol                            | Underlying Transport Protocol |
|------------------------|-------------------------------------------------------|-------------------------------|
| e-mail                 | SMTP [RFC 2821]                                       | TCP                           |
| remote terminal access | Telnet [RFC 854], SSH                                 | TCP                           |
| Web                    | HTTP [RFC 2616]                                       | TCP                           |
| file transfer          | FTP [RFC 959]                                         | TCP                           |
| streaming multimedia   | HTTP (e.g., YouTube), RTP [RFC 1889]                  | TCP or UDP                    |
| Internet telephony     | SIP, RTP, proprietary (e.g., Skype)                   | TCP or UDP                    |
| naming                 | DNS                                                   | UDP (and TCP)                 |

### Socket programming with UDP

- no handshaking
- sender explicitly attaches IP destination address and port # to each packet
- receiver extracts sender IP address and port# from received packet

### Socket programming with TCP

server must

- first be running
- have created socket (door) that welcomes client’s contact

client contacts server by:

- Creating TCP socket, specifying IP address, port number of server process

server TCP creates new socket

- for server process to communicate with that particular client

### 