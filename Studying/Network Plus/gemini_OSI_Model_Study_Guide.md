# OSI Model Study Guide

# TCP/IP Model

For networking, two commonly referenced models are the OSI model and the TCP/IP model. While the Network+ exam (Objective 1.1) focuses primarily on the OSI model, it's helpful to understand both. The TCP/IP model is a concise framework with four layers, while the OSI model provides a more detailed breakdown with seven layers. We'll cover both for a comprehensive understanding.

## TCP/IP Model Layers

1. **Network Interface Layer:** Handles the physical transmission of data on the network, including the physical media, data encoding, and signal transmission. It roughly corresponds to the Physical and Data Link Layers of the OSI model.

- **Examples**: Ethernet, Wi-Fi, Token Ring.

2. **Internet Layer:** Responsible for addressing and routing data packets across multiple networks. It's where the Internet Protocol (IP) operates, along with protocols like ICMP and ARP.

- **Examples**: IP addressing, routing, packet fragmentation.

3. **Transport Layer:** Manages the end-to-end communication between applications on different hosts, ensuring reliable data transfer and flow control. This is where TCP and UDP operate.

- **Examples**: TCP three-way handshake, UDP datagram transmission.

4. **Application Layer:** Provides services directly to user applications, enabling communication for various purposes like web browsing, email, and file transfer. It encompasses a wide range of protocols like HTTP, FTP, SMTP, DNS, DHCP, and more.

- **Examples**: Web browsers, email clients, file transfer programs.

# OSI Model

## Memorize

> All People Seem To Need Data Processing

`7.` **Application Layer**
<br>
`6.` **Presentation Layer**
<br>
`5.` **Session Layer**
<br>
`4.` **Transport Layer**
<br>
`3.` **Network Layer**
<br>
`2.` **Data Link Layer**
<br>
`1.` **Physical Layer**

## Layer 1

### Physical Layer

Defines the physical means of data transmission, including cables, Wi-Fi, and connectors.

- **Examples:** Bits, Cables (UTP, STP, Fiber optic, Coaxial), Wi-Fi, RJ-45 connectors, hubs, physical topologies (star, bus, ring, mesh), transmission modes (simplex, half-duplex, full-duplex), encoding schemes (Manchester, NRZI).

## Layer 2

### Data Link Layer

Ensures error-free transfer of data frames between two devices on the same network, using MAC addresses.

- **Examples:** Frames, MAC Addresses, VLAN, Ethernet Protocol, Wi-Fi, switches, bridges, PPP, HDLC, ARP, RARP, Spanning Tree Protocol (STP), MAC address filtering.

## Layer 3

### Network Layer

Routes data between networks, using IP addresses, and handles congestion and routing.

- **Examples:** Packets, Routers, IPv4, IPv6, ARP, NAT, IP Addresses, subnets, routing protocols (RIP, OSPF, EIGRP, BGP), IPsec, ICMP, MPLS.

> **Key Difference:** VLANs operate at Layer 2 of the OSI model and are based on MAC addresses, while subnets operate at Layer 3 and are based on IP addresses.

## Layer 4

### Transport Layer

Provides reliable data transfer between devices, ensuring data is delivered in the correct order. Manages flow control and error correction.

- **Examples:** Segments, TCP, UDP, port numbers, sockets, segmentation, flow control (windowing, buffering), error checking, connection establishment (TCP handshake).

## Layer 5

### Session Layer

Establishes, manages, and terminates connections (or sessions) between applications running on different devices, providing dialog control and synchronization services.

- **Examples:** NetBIOS, SSH, Sockets, RPC, NetBIOS, login sessions, video conferencing, SQL, NFS, authentication services (Kerberos, RADIUS, TACACS+).

## Layer 6

### Presentation Layer

Ensures that data exchanged between applications is properly formatted, encrypted, and compressed for efficient transmission. Handles data translation, encoding, and encryption/decryption.

- **Examples:** SSL, TLS, ASCII, EBCDIC, JPEG, MPEG, Data Compression (e.g., JPEG, GIF, MP3), Encryption (e.g., AES, DES), data conversion and formatting.

## Layer 7

### Application Layer

Provides services to end-user applications, such as email, file transfer, and web browsing. This is where users interact with the network.

- **Examples:** HTTP, FTP, SMTP, DNS, DHCP, Telnet, SSH, web browsers, email clients, file transfer programs, SNMP, TFTP, application-level firewalls, proxy servers.
