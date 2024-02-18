---
title: Communication Networks (6)
date: 2024-02-18 02:52:17
img_path: /_posts/
math: true
categories:
- CourseNotes
- Commd d d fsdf fffff
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



