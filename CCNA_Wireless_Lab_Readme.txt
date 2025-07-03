
# CCNA 3-Tier IPv4/IPv6 with Wireless Packet Tracer Lab

**Lab Author:** Anthony Mazyck II  
**Credit:** Based on East Charmer's video walkthrough: https://youtu.be/4hisEIlSv0g?si=wiz2X4k6lTKK_j_K  
**Channel:** https://www.youtube.com/@EastCharmer

## Objective
Design and configure a scalable enterprise-style 3-tier hierarchical network using IPv4 and IPv6 addressing, implement wireless connectivity, and verify end-to-end connectivity with static addressing and secure wireless encryption.

## Devices Used
- 1 x ISR4331 Router (Router0)
- 2 x 3650 Multilayer Switches (Core)
- 2 x 3650 Multilayer Switches (Distribution)
- 3 x 2960 Access Layer Switches
- 3 x PCs (PC0, PC1, PC2)
- 1 x Server (Server0)
- 1 x Access Point (Access Point1)
- 1 x Laptop (Laptop0 with WPC300N wireless NIC)

## Final IP Scheme (IPv4)
| Device       | IP Address         | Subnet Mask       | Default Gateway     |
|--------------|--------------------|--------------------|----------------------|
| PC0          | 192.168.100.5      | 255.255.255.192    | 192.168.100.1        |
| PC1          | 192.168.100.10     | 255.255.255.192    | 192.168.100.1        |
| PC2          | 192.168.100.65     | 255.255.255.192    | 192.168.100.64       |
| Server0      | 192.168.100.20     | 255.255.255.192    | 192.168.100.1        |
| Router0 G0/0 | 192.168.100.1      | 255.255.255.192    | -                    |
| Router0 G0/1 | 192.168.100.66     | 255.255.255.192    | -                    |

## IPv6 Configuration
- Link-local: FE80::/10 (auto-assigned)
- Optional Global Unicast: 2001:DB8:ACAD:X::/64
- Enabled via SLAAC

### Router IPv6 Commands
```bash
ipv6 unicast-routing
interface g0/0
 ipv6 address FE80::1 link-local
 no shutdown
interface g0/1
 ipv6 address FE80::2 link-local
 no shutdown
```

## Wireless Configuration
- SSID: HQ-WiFi
- Security: WPA2-PSK
- Password: eastside

### Setup Steps
1. AP Config > Port 1 > Set SSID, WPA2-PSK, password
2. Laptop > Physical > Add WPC300N > Desktop > PC Wireless > Connect

## Mistakes & Fixes
- Used network address `192.168.100.64` as a host – fixed with `.66`
- Server originally placed in wrong subnet – moved to 192.168.100.20 / GW .1
- Forgot wireless NIC and PSK config – corrected in AP & Laptop
- Server unreachable – fixed subnet, gateway, and verified link

## Useful Cisco Commands
```bash
interface GigabitEthernet0/0
 ip address 192.168.100.1 255.255.255.192
 no shutdown

interface GigabitEthernet0/1
 ip address 192.168.100.66 255.255.255.192
 no shutdown

show ip interface brief
ping 192.168.100.20
ping 192.168.100.1
ping FE80::1
```

## Summary
This lab reinforces core CCNA topics: subnetting, IPv6, Layer 2/3 switching, wireless security, and CLI troubleshooting.

🎓 Tutorial: https://youtu.be/4hisEIlSv0g?si=wiz2X4k6lTKK_j_K  
📺 East Charmer Channel: https://www.youtube.com/@EastCharmer
