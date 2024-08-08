# Security + Notes

## Tools

### `nmap`

```bash
# using nmap to list all devices on current network
# 192.168.1.1/24
nmap -sn 192.168.1.0/24
```

```output
Starting Nmap 7.94 ( https://nmap.org ) at 2024-05-01 19:51 CDT
Nmap scan report for SAC2V1K.lan (192.168.1.1)
Host is up (0.0048s latency).
Nmap scan report for Jesse-s-S20.lan (192.168.1.41)
Host is up (0.0064s latency).
Nmap scan report for debian.lan (192.168.1.54)
Host is up (0.021s latency).
Nmap scan report for Galaxy-A54-5G.lan (192.168.1.169)
Host is up (0.0095s latency).
Nmap scan report for 192.168.1.217
Host is up (0.025s latency).
Nmap scan report for Roku.lan (192.168.1.232)
Host is up (0.15s latency).
Nmap scan report for 192.168.1.233
Host is up (0.015s latency).
Nmap scan report for fedora-40.lan (192.168.1.240)
Host is up (0.00012s latency).
Nmap done: 256 IP addresses (8 hosts up) scanned in 3.30 seconds
```

## Standards

## Technology

### 802.11x

802.11x is a set of IEEE standards that define various methods for securing
wireless networks. These standards include protocols such as WEP (Wired
Equivalent Privacy), WPA (Wi-Fi Protected Access), and WPA2 (Wi-Fi Protected
Access 2). These protocols provide encryption and authentication mechanisms to
protect data transmitted over wireless networks.

## 802.1x (Framework

Standardized framework used for port-based
authentication on wired and wireless networks.

- RADIUS
- TACACS+
- EAP (Framework)
- EAP-TLS
- EAP-MD5
- EAP-TTLS
- EAP-FAST
- EAP-PEAP
- LEAP

> Codeium

802.1x is an industry standard that defines various methods for protecting
wireless networks. These standards include protocols such as WEP (Wired
Equivalent Privacy), WPA (Wi-Fi Protected Access), and WPA2 (Wi-Fi Protected
Access 2). These protocols provide encryption and authentication mechanisms to
protect data transmitted over wireless networks.

> ChatGP

802.1X is an IEEE standard for port-based network access control. It is used to
provide authentication and authorization for devices trying to connect to a
network, such as Wi-Fi networks. 802.1X works by requiring users or devices to
authenticate themselves before they are granted access to the network. This
helps to ensure that only authorized users or devices can connect to the
network, enhancing security and preventing unauthorized access.

## SYSLOG

SYSLOG is a standard protocol used for sending and receiving log and event
messages in a network. It allows devices, such as routers, switches, firewalls,
and servers, to send event notifications to a centralized SYSLOG server for
storage, analysis, and monitoring. SYSLOG messages contain information about
events, errors, warnings, and other activities happening on the network.

### SIEM

A SIEM (Security Information and Event Management) system is a type of security
software that combines security information management (SIM) and security event
management (SEM) functions. SIEM systems collect, analyze, and correlate log
and event data from various sources, including SYSLOG messages, to provide
real-time monitoring, threat detection, incident response, and compliance
reporting. SIEM systems help organizations improve their security posture by
providing visibility into their IT environment and detecting potential security
threats.

#### Difference

SYSLOG and SIEM are related concepts but serve different purposes in the realm
of network security.

### SYSLOG

SYSLOG is a standard protocol used for sending log and event messages in a
network. It allows devices to send event notifications to a centralized SYSLOG
server for storage, analysis, and monitoring. SYSLOG messages contain
information about events, errors, warnings, and other activities happening on
the network.

### SIEM

SIEM (Security Information and Event Management) is a type of security software
that combines security information management (SIM) and security event
management (SEM) functions. SIEM systems collect, analyze, and correlate log
and event data from various sources, including SYSLOG messages, to provide
real-time monitoring, threat detection, incident response, and compliance
reporting. SIEM systems help organizations improve their security posture by
providing visibility into their IT environment and detecting potential security
threats.

### Difference

> GPTo
> The main difference between a SIEM (Security Information and Event Management) and SYSLOG is their functionality and purpose. SYSLOG is a standard protocol used for logging system messages and events from various devices and applications, providing a centralized way to collect and store log data. In contrast, a SIEM is a comprehensive security solution that not only collects and stores log data (often using SYSLOG) but also analyzes and correlates this data to identify and respond to potential security threats in real-time. Essentially, SYSLOG is about logging, while SIEM is about both logging and actively managing security.
> GPT3.5
> A SIEM (Security Information and Event Management) is a comprehensive security solution that collects, analyzes, and correlates data from various sources to provide real-time threat detection and response capabilities. It includes features such as log management, event correlation, and incident response. On the other hand, SYSLOG is a protocol used for sending log messages and event data from network devices to a centralized logging server. While both SIEM and SYSLOG are used for collecting and analyzing log data, the main difference is that SIEM is a more advanced and comprehensive security solution that includes additional features for threat detection and response, whereas SYSLOG is primarily focused on collecting and forwarding log data.

## Hashing

Hashing is the process of converting data into a fixed-length string of
characters or numbers.

### Algorithms

SHA-1 creates a 160-bit fixed output. SHA-2 creates a 256-bit fixed output.
NTLM creates a 128-bit fixed output. MD-5 creates a 128-bit fixed output.j

- NTLM

NTLM is an authentication protocol used in Windows. It is used to provide
authentication and authorization for devices trying to connect to a network,
such as Wi-Fi networks. NTLM works by requiring users or devices to
authenticate themselves before they are granted access to the network. This
helps to ensure that only authorized users or devices can connect to the
network, enhancing security and preventing unauthorized access. Uses MD4 hash
algorithm, which has a fixed output length of 128 bits.

- SHA-3

## Non-Repudiation

Non-repudiation occurs when a sender cannot claim they didn’t send an email
when they did. A digital signature should be attached to each email sent to
achieve non-repudiation. This digital signature is comprised of a digital hash
of the email’s contents, and then encrypting that digital hash using the
sender’s private key. The receiver can then unencrypt the digital hash using
the sender’s public key to verify the integrity of the message.

## CSR

Certificate Signing Request. What is submitted to the CA (certificate
authority) to request a digital certificate.

## Key Escrow

Key escrow stores keys

## CRL

CRL is a list of revoked certificate
A Certificate Revocation List (CRL) is a list of digital certificates that have been revoked by the issuing Certificate Authority (CA) before their expiration date. CRLs are used to verify the validity of a certificate by checking if it has been revoked due to compromise or other reasons. This helps ensure the security and integrity of the certificate-based authentication system. CRLs are an essential component of a Public Key Infrastructure (PKI) and are used by clients to determine if a certificate should be trusted for secure communication.

> Certificate of the Certificate?
> A Certificate Revocation List (CRL) acts as a list of revoked certificates, providing a way to verify the validity of a digital certificate. It serves as a mechanism to ensure that certificates that have been compromised or are no longer trusted are not used for secure communication. Just as a certificate is used to verify the identity of an entity in a PKI system, a CRL is used to verify the validity of that certificate.

## OCSP

Status of certificates that provides validity such as good, revoked, or unknown.

## IPSec

Internet Protocol Security. Protocol that encrypts data over the internet.
Most secure protocol that works with VPNs. The use of PPTP and SSL
is discouraged for VPN security. Due to this, the use of PPTP and SSL for a VPN
will likely alert during a vulnerability scan as an issue to be remediated.

## Common Ports

- Port 443 is used for HTTPS traffic. This is secure web browsing over SSL or TLS.
- Port 21 is used for the File Transfer Protocol (FTP).
- Port 80 is used for unsecured web browsing (HTTP).
- Port 143 is used for Internet Mail Application Protocol (IMAP).
