# TCP/IP Model

For networking, two commonly referenced models are the OSI model and the TCP/IP model, with Objective 1.1 of the Network+ exam focusing solely on the OSI model, providing a detailed discussion with a brief mention of the TCP/IP model for additional context.

# OSI Model

## Memorize

> PDN TSPA

1. Physical Layer
2. Data Link Layer
3. Network Layer
4. Transport Layer
5. Session Layer
6. Presentation Layer
7. Application Layer

## Layer 1

### Physical Layer

Defines the physical means of data transmission, including cables, Wi-Fi, and connectors.

- Examples: Cables, Wi-Fi, RJ-45 connectors, hubs

## Layer 2

### Data Link Layer

Ensures error-free transfer of data frames between two devices on the same network, using MAC addresses.

- Examples: Frames, MAC Addresses, VLAN, Frames, Ethernet Protocol, Wi-Fi, switches, bridges

## Layer 3

### Network Layer

Routes data between networks, using IP addresses, and handles congestion and routing.

- Examples: Routers, ARP, NAT, IP Addresses, subnets

> VLANs operate at Layer 2 of the OSI model and are based on MAC addresses, while subnets operate at Layer 3 and are based on IP addresses.

## Layer 4

### Transport Layer

Provides reliable data transfer between devices, ensuring data is delivered in the correct order. Error Correction.

- Examples: TCP, UDP, port numbers, sockets

## Layer 5

### Session Layer

Establishes, manages, and terminates connections (or sessions) between applications running on different devices, providing dialog control and synchronization services.

- Examples: NetBIOS, SSH, login sessions, video conferencing

## Layer 6

### Presentation Layer

Ensures that data exchanged between applications is properly formatted, encrypted, and compressed for efficient transmission, as well as handling data translation and encoding.

- Examples: SSL, TLS, Data Compression (e.g., JPEG), Encryption (e.g., AES)

## Layer 7

### Application Layer

Provides services to end-user applications, such as email, file transfer, and web browsing.

- Examples: HTTP, FTP, SMTP, DNS, web browsers, email clients
