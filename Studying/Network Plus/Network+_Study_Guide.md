# I. Networking Fundamentals

Network Models
TCP/IP Model:
4 layers: Application, Transport, Internet, Network Access (Link)
Focuses on how data is transmitted across the Internet.
OSI Model:
7 layers: Application, Presentation, Session, Transport, Network, Data Link, Physical.
Provides a more granular, theoretical view of networking functions.
Encapsulation: Data is wrapped with headers and trailers as it moves down the layers of a network model (sending host).
Decapsulation: Headers and trailers are removed as data moves up the layers (receiving host).
Network Topologies
Physical Topologies: How devices are physically connected.
Bus: Linear backbone, simple, limited scalability, single point of failure.
Ring: Circular data path, challenging to expand, disruption if cable breaks.
Star: Central hub/switch, easy to expand, single point of failure at the hub/switch.
Mesh: Interconnected nodes, high redundancy, complex and costly (wired mesh), increasingly popular in wireless deployments (wireless mesh).
Hybrid: Combination of topologies.
Logical Topologies: How data flows across the network.
Bus, Ring, Star: Logical implementations often differ from the physical topology.
Network Types
LAN (Local Area Network): Single location, high speed, relatively inexpensive.
WLAN (Wireless LAN): Uses radio frequencies, provides flexibility and mobility.
WAN (Wide Area Network): Spans multiple locations, slower than LAN, often requires leased lines or other WAN technologies.
MAN (Metropolitan Area Network): Covers a larger geographic area than a LAN but smaller than a WAN (e.g., a city).
CAN (Campus Area Network): Interconnects multiple LANs within a limited area (e.g., a university campus or business park).
SAN (Storage Area Network): Networked storage devices, provides block-level access to storage.
PAN (Personal Area Network): Interconnects devices in close proximity (e.g., Bluetooth, NFC).
SDWAN (Software-Defined WAN): Uses software to control WAN connections, increases flexibility and efficiency.
Network Links and Concepts
DSL (Digital Subscriber Line): High-speed Internet over telephone lines.
ADSL (Asymmetric DSL): Faster downloads than uploads.
SDSL (Symmetric DSL): Same speeds for uploads and downloads.
Other DSL Types: IDSL, RADSL, HDSL, VDSL.
Cable Broadband: Always-on Internet access using cable TV infrastructure.
Leased Lines (T-Carrier, E-Carrier): Dedicated lines for high-speed connectivity.
SONET/SDH: Fiber-optic WAN technologies for high bandwidth.
MPLS (Multiprotocol Label Switching): Uses labels for faster routing in WANs.
mGRE (Multipoint Generic Routing Encapsulation): Extension of GRE for multipoint VPN tunnels.
Satellite Internet: Access in remote areas, high latency.
IP Addressing
IPv4 (Internet Protocol version 4):
32-bit addresses, dotted-decimal notation (e.g., 192.168.1.1).
Address Classes (A, B, C, D, E), Subnetting, Subnet Masks.
Private Address Ranges (RFC 1918).
CIDR (Classless Interdomain Routing) Notation (e.g., 192.168.1.0/24).
IPv6 (Internet Protocol version 6):
128-bit addresses, colon-hexadecimal notation (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).
Address Types: Unicast (Global, Link-Local, Unique-Local), Multicast, Anycast.
Neighbor Discovery Protocol (NDP).
Address Assignment
Static Addressing: Manual IP configuration.
Dynamic Addressing (DHCP): Automatic IP assignment, leases, scopes.
BOOTP: Legacy protocol for diskless workstations.
APIPA (Automatic Private IP Addressing): Windows self-configuration (169.254.x.x).
MAC Addressing
MAC (Media Access Control) Address: 48-bit, physically assigned to NICs.
OUI (Organizationally Unique Identifier): First 3 bytes identify the manufacturer.
Finding MAC Address: ipconfig /all (Windows), ifconfig -a (Linux/UNIX), show int interface_name (Cisco routers).
EUI-64: 64-bit MAC address format used in IPv6.
NAT and PAT
NAT (Network Address Translation): Maps private IPs to public IPs.
PAT (Port Address Translation / NAT Overload): Maps multiple private IPs to a single public IP using different ports.
SNAT (Static NAT): Maps a single private IP to a single public IP.
DNAT (Dynamic NAT): Maps a private IP to a public IP from a pool of addresses.

## II. Network Implementations

Common Networking Devices
Firewall: Controls network access, enforces security policies.
IDS (Intrusion Detection System): Monitors network traffic for suspicious activity, alerts administrators.
IPS (Intrusion Prevention System): Actively blocks malicious traffic.
Router: Forwards traffic between networks.
Switch: Forwards traffic within a network based on MAC addresses.
Multilayer Switch: Combines switching and routing functions.
Hub: Simple, legacy device, forwards traffic to all ports (mostly replaced by switches).
Bridge: Connects network segments, forwards traffic based on MAC addresses.
Modems (DSL/Cable): Provide Internet access.
Access Point (AP): Connects wireless clients to the network.
Media Converter: Connects different cable types (e.g., fiber to copper).
Voice Gateway: Converts between traditional phone lines and VoIP.
Repeater: Amplifies signals to extend network reach.
Load Balancer: Distributes traffic among multiple servers.
Proxy Server: Intermediary between clients and external servers, enhances security and performance.
VPN Concentrator: Manages VPN connections, provides authentication and encryption.
Networked Devices: Printers, IP phones, cameras, IoT devices, etc.
Networking Architectures
Three-Tier Architecture: Core (backbone), Distribution/Aggregation (boundary), Access/Edge (desktop).
Software-Defined Networking (SDN):
Uses software to manage the network.
Layers: Application, Control, Infrastructure.
Management Plane: Monitors and manages the network.
Spine and Leaf Architecture: Two-tier model for data centers, spine switches form the backbone, leaf switches connect to servers.
Top-of-Rack (ToR) Switching: Switches in server racks for high-speed connectivity.
Data Center Concepts
Traffic Flows:
East-West: Traffic between servers within the data center.
North-South: Traffic entering or leaving the data center.
Data Center Location Types:
On-Premises: Owned and managed by the organization.
Colocation: Shared data center space.
Storage Technologies
SAN (Storage Area Network): High-speed network dedicated to storage.
Fibre Channel: High-performance, dedicated network for storage.
FCoE (Fibre Channel over Ethernet): Runs Fibre Channel over Ethernet networks.
NAS (Network Attached Storage): File-level access to storage over the network.
iSCSI (Internet Small Computer System Interface): Uses IP to transport SCSI commands over the network for storage access.

# III. Cabling Solutions & Troubleshooting

Cable Types & Connectors
Twisted Pair:
UTP (Unshielded Twisted Pair): Most common, Cat 5/5e, Cat 6/6a, Cat 7, Cat 8.
STP (Shielded Twisted Pair): Provides additional EMI protection.
Connectors: RJ-45 (networking), RJ-11 (telephone).
Coaxial:
RG-59: Low-power video.
RG-6: Cable TV, cable modems.
Connectors: F-Type.
Twinaxial:
Two inner conductors.
Fiber Optic:
Single-Mode: One light path, long distances, high speed.
Multi-Mode: Multiple light paths, shorter distances, lower cost.
Connectors: ST, SC, LC, MT-RJ, FC.
Plenum Cable: Fire-resistant, low smoke for use in air handling spaces.
Troubleshooting Cable Connectivity Issues
Common Issues:
Attenuation/dB Loss (signal degradation).
Interference (EMI, crosstalk).
Incorrect Pinouts.
Bad Ports/Connectors.
Open/Short Circuits.
Incorrect Transceivers (fiber).
Duplex Mismatches.
Dirty Optical Cables.
Troubleshooting Tools:
Cable Testers (multimeters, TDRs).
Punchdown Tools.
Toner Probes.
Loopback Adapters.
OTDR (Optical Time Domain Reflectometer) for fiber testing.

# IV. Wireless Solutions & Troubleshooting

Wireless Standards & Technologies
802.11 Standards:
802.11a: 5 GHz, up to 54 Mbps.
802.11b: 2.4 GHz, up to 11 Mbps.
802.11g: 2.4 GHz, up to 54 Mbps, backward compatible with 802.11b.
802.11n (Wi-Fi 4): 2.4 GHz or 5 GHz, up to 600 Mbps, uses MIMO.
802.11ac (Wi-Fi 5): 5 GHz, up to 1.3 Gbps, uses MU-MIMO.
802.11ax (Wi-Fi 6): 2.4 GHz and 5 GHz, up to 10 Gbps, uses MU-MIMO, OFDMA.
802.11ay (Wi-Fi 7): 60Ghz, 20-40 Gbps, uses CMU-MIMO, enhanced OFDMA
Frequencies & Channels:
2.4 GHz (more congested, longer range).
5 GHz (less congested, shorter range).
6 GHz (used by Wi-Fi 6E, very high bandwidth).
Channel Bonding: Combining channels for increased bandwidth.
MIMO (Multiple Input, Multiple Output): Uses multiple antennas for improved speed and range.
MU-MIMO (Multi-User MIMO): Allows APs to communicate with multiple clients simultaneously.
OFDMA (Orthogonal Frequency-Division Multiple Access): Divides channels into smaller subcarriers for efficient data transmission (802.11ax).
Cellular Technology Access: 3G, 4G (LTE), 5G.
Troubleshooting Wireless Issues
Signal Strength and Interference: Distance from AP, obstacles, competing signals.
Configuration Issues: Incorrect SSID, channel mismatches, security settings, driver problems.
Security Issues: Weak security protocols, rogue APs, evil twin attacks.
Environmental Factors: Weather, physical obstructions.
Troubleshooting Tools:
Wi-Fi Analyzers.
Signal Strength Meters.
V. Network Security
Security Concepts
CIA Triad: Confidentiality, Integrity, Availability.
Defense in Depth: Layered security approach.
AAA (Authentication, Authorization, Accounting):
Authentication: Verifying user identity (passwords, biometrics, multi-factor authentication).
Authorization: Granting access to resources based on identity.
Accounting: Tracking user activity.
Network Segmentation: Dividing the network into smaller, more secure segments (VLANs, firewalls).
Screened Subnet (DMZ): Isolate public-facing servers from the internal network.
Separation of Duties: Prevent fraud and errors.
Honeypots: Decoy systems to attract and analyze attackers.
Common Attacks
DoS (Denial of Service): Overwhelm a system with requests, making it unavailable.
DDoS (Distributed Denial of Service): DoS from multiple sources, often using botnets.
Man-in-the-Middle: Attacker intercepts traffic between two parties.
Social Engineering: Tricking users into revealing sensitive information.
Phishing: Fraudulent emails or websites to steal information.
Ransomware: Malware that encrypts data and demands payment for decryption.
Malware (Viruses, Worms, Trojans): Malicious software.
SQL Injection: Attack on databases.
Cross-Site Scripting (XSS): Attack on websites.
Network Hardening
Disable Unneeded Services and Ports.
Change Default Passwords.
Use Strong Passwords and Password Policies.
Keep Systems and Software Updated (Patches, Firmware).
Implement Access Control Lists (ACLs).
Use Firewalls and Intrusion Detection/Prevention Systems (IDS/IPS).
Encrypt Sensitive Data (in transit and at rest).
Use Secure Protocols (SSH, HTTPS, etc.).
Implement Physical Security Measures.
Wireless Security
Use Strong Encryption (WPA2/WPA3).
Disable SSID Broadcast.
Enable MAC Address Filtering.
Implement 802.1X Authentication.
Use a VPN for Public Wi-Fi.
Remote Access Methods and Security
VPN (Virtual Private Network): Creates a secure tunnel over a public network.
VPN Protocols: IPsec, SSL/TLS.
VPN Types: Site-to-Site, Client-to-Site.
Remote Desktop:
RDP (Remote Desktop Protocol): Windows remote access protocol.
VNC (Virtual Network Computing): Platform-independent remote access protocol.
SSH (Secure Shell): Secure remote access and command execution.

# VI. Network Management & Operations

Monitoring Network Performance
Performance Metrics: Bandwidth utilization, latency, packet loss, error rates, CPU/memory usage.
Monitoring Tools:
Network Performance Monitors (SNMP, WMI, IPMI).
Protocol Analyzers.
Bandwidth Testers.
Performance/Load/Stress Testing: Assess network capacity and identify bottlenecks.
Log Management:
Security Logs: Logon attempts, access violations.
System Logs: Hardware and software events.
Application Logs: Events related to applications.
Maintaining Network Documentation
Network Diagrams (Physical and Logical).
Wiring Schematics.
Baseline Configurations.
Policies and Procedures.
Inventory of Hardware and Software.
High Availability and Disaster Recovery
Fault Tolerance: RAID, redundant hardware, NIC teaming.
Load Balancing: Distribute traffic among servers to increase availability.
Multipathing: Using multiple paths to access data.
Backups:
Full Backup: Complete copy of data.
Incremental Backup: Only backs up changes since last backup.
Differential Backup: Backs up changes since last full backup.
Disaster Recovery Sites:
Cold Site: Basic infrastructure, needs time to set up equipment.
Warm Site: Partially equipped site with some systems pre-installed.
Hot Site: Fully operational duplicate of the primary site.
Recovery Time Objective (RTO): Maximum acceptable downtime.
Recovery Point Objective (RPO): Maximum acceptable data loss.

# VII. Troubleshooting Methodology & Tools

## Troubleshooting Steps:

1. Identify the Problem: Gather information, interview users, observe symptoms.
2. Establish a Theory: Consider probable causes, question the obvious.
3. Test the Theory: Try to duplicate the problem.
4. Establish a Plan of Action: Develop steps to resolve the issue.
5. Implement the Solution: Apply the fix, test the results.
6. Verify Full System Functionality: Ensure the fix resolved the issue and didn't cause new problems.
7. Document Findings, Actions, and Outcomes: Record the process and lessons learned.

## Troubleshooting Tools

- Command-Line Utilities:
  - ping: Test network connectivity.
  - tracert/traceroute: Trace the path of packets through the network.
  - ipconfig/ifconfig: View IP configuration.
  - nslookup/dig: Test DNS resolution.
  - netstat: View network connections and statistics.
  - arp: View and manage the ARP cache.
  - route: View and manage routing tables.
  - tcpdump: Capture and analyze network packets (Linux/UNIX).

## GUI Tools:

- Protocol Analyzers: Wireshark, tcpdump (with GUI).
- Bandwidth Testers: iperf, speed test websites.
- Port Scanners: Nmap, online port scanners.
