---
title: Communication Networks (6)
date: 2024-02-18 02:52:17
img_path: /_posts/
math: true
categories:
- Course Notes
- Communication Networks
---

## Web caches (proxy server)

![alt text](../upload/img/2024-02-18-communication-networks-6-image.png){: w="500" }

1) browser sends all HTTP requests to cache
2) object in cache: cache returns object
3) else cache requests object from origin server, then returns object to client

![alt text](../upload/img/2024-02-18-communication-networks-6-image-1.png){: w="400" }

### Conditional GET

1) send HTTP request with `If-modified-since: <date>`
2) server response `HTTP/1.0 304 Not Modified` if data not modified ever since
3) server response `HTTP/1.0 200 OK <data>` otherwise

---

# Chapter 2

## Electronic mail

major components:

- user agents
- mail servers
- SMTP: Simple Mail Transfer Protocol

### Electronic Mail: SMTP [RFC 2821]

**SMTP: protocol for exchanging email messages**

- use TCP, port 25
- direct transfer
- three phases of transfer
  - handshaking (greeting)
  - transfer of messages
  - closure
- command/response interaction like HTTP
  - commands: ASCII text (7-bit)
  - response: status code and phrase

<details markdown="1">
<summary>Sample SMTP interaction</summary>

```
S: 220 hamburger.edu 
C: HELO crepes.fr 
S: 250  Hello crepes.fr, pleased to meet you 
C: MAIL FROM: <alice@crepes.fr> 
S: 250 alice@crepes.fr... Sender ok 
C: RCPT TO: <bob@hamburger.edu> 
S: 250 bob@hamburger.edu ... Recipient ok 
C: DATA 
S: 354 Enter mail, end with "." on a line by itself 
C: Do you like ketchup? 
C: How about pickles? 
C: . 
S: 250 Message accepted for delivery 
C: QUIT 
S: 221 hamburger.edu closing connection
```

(end with **CRLF.CRLF**)

</details>

### Mail message format

**RFC 822: standard for text message format**

- header lines, e.g.,
To:
From:
Subject:
(different from SMTP MAIL FROM)
- Body: the “message” (ASCII characters only)

### Mail access protocols

![alt text](../upload/img/2024-02-18-communication-networks-6-image-3.png){: w="700" }

**mail access protocol: retrieval from server**

protocol|description
--|---
POP| Post Office Protocol [RFC 1939]: authorization, download
IMAP| Internet Mail Access Protocol [RFC 1730]: more features, including manipulation of stored messages on server
HTTP| gmail, Hotmail, Yahoo! Mail, etc.

## DNS: domain name system

Domain Name System:

- **distributed** database (in hierarchy of **name servers**)
- **application-layer protocol**: hosts, name servers communicate to resolve names (address/name translation)

steps:

- client wants IP for `www.amazon.com`; 1st approximation:
- client queries root server to find com DNS server
- client queries `.com` DNS server to get `amazon.com` DNS server
- client queries `amazon.com` DNS server to get  IP address for `www.amazon.com`

### DNS name servers

Top-level domain (TLD) servers:

- `com`, `org`, `net`, `edu`, ...
- top-level country domains: `uk`, `fr`, ...

Authoritative DNS servers:

- organization’s named hosts
- maintained by organization or service provider

Local DNS name server (cached)

- does not strictly belong to hierarchy
- each ISP has one

### DNS name resolution example

![alt text](../upload/img/2024-02-18-communication-networks-6-image-4.png){: w="500" }
_Diterated query_

![alt text](../upload/img/2024-02-18-communication-networks-6-image-5.png)
_recursive query_

Name server caches mappings untiel expired (time of **TTL**)

### DNS records

Distributed database storing **resource records** (RR).

RR Format: `(name, value, type, ttl)`

type|name|value|
---|---|---
A|hostname|IP address
NS|domain|hostname of authoritative name server for this domain
CNAME|alias name|is canonical(real) name
MX|hostname|mail server

### DNS protocol

![alt text](../upload/img/2024-02-18-communication-networks-6-image-6.png){: w="700" }
