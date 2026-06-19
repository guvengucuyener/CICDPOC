# FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| FABRIC | l3leaf | xdc1-leaf-01 | 192.168.154.13/24 | cEOSLab | Provisioned | - |
| FABRIC | l3leaf | xdc1-leaf-02 | 192.168.154.10/24 | cEOSLab | Provisioned | - |
| FABRIC | l3leaf | xdc1-leaf-03 | 192.168.154.11/24 | cEOSLab | Provisioned | - |
| FABRIC | l3leaf | xdc1-leaf-04 | 192.168.154.14/24 | cEOSLab | Provisioned | - |
| FABRIC | spine | xdc1-spine-01 | 192.168.154.15/24 | cEOSLab | Provisioned | - |
| FABRIC | spine | xdc1-spine-02 | 192.168.154.16/24 | cEOSLab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | --------- | -------------- |
| l3leaf | xdc1-leaf-01 | Ethernet1 | spine | xdc1-spine-01 | Ethernet1 |
| l3leaf | xdc1-leaf-01 | Ethernet2 | spine | xdc1-spine-02 | Ethernet1 |
| l3leaf | xdc1-leaf-02 | Ethernet1 | spine | xdc1-spine-01 | Ethernet2 |
| l3leaf | xdc1-leaf-02 | Ethernet2 | spine | xdc1-spine-02 | Ethernet2 |
| l3leaf | xdc1-leaf-03 | Ethernet1 | spine | xdc1-spine-01 | Ethernet3 |
| l3leaf | xdc1-leaf-03 | Ethernet2 | spine | xdc1-spine-02 | Ethernet3 |
| l3leaf | xdc1-leaf-04 | Ethernet1 | spine | xdc1-spine-01 | Ethernet4 |
| l3leaf | xdc1-leaf-04 | Ethernet2 | spine | xdc1-spine-02 | Ethernet4 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.255.255.0/26 | 64 | 16 | 25.0 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| xdc1-leaf-01 | Ethernet1 | 10.255.255.1/31 | xdc1-spine-01 | Ethernet1 | 10.255.255.0/31 |
| xdc1-leaf-01 | Ethernet2 | 10.255.255.3/31 | xdc1-spine-02 | Ethernet1 | 10.255.255.2/31 |
| xdc1-leaf-02 | Ethernet1 | 10.255.255.5/31 | xdc1-spine-01 | Ethernet2 | 10.255.255.4/31 |
| xdc1-leaf-02 | Ethernet2 | 10.255.255.7/31 | xdc1-spine-02 | Ethernet2 | 10.255.255.6/31 |
| xdc1-leaf-03 | Ethernet1 | 10.255.255.9/31 | xdc1-spine-01 | Ethernet3 | 10.255.255.8/31 |
| xdc1-leaf-03 | Ethernet2 | 10.255.255.11/31 | xdc1-spine-02 | Ethernet3 | 10.255.255.10/31 |
| xdc1-leaf-04 | Ethernet1 | 10.255.255.13/31 | xdc1-spine-01 | Ethernet4 | 10.255.255.12/31 |
| xdc1-leaf-04 | Ethernet2 | 10.255.255.15/31 | xdc1-spine-02 | Ethernet4 | 10.255.255.14/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.255.0.0/27 | 32 | 6 | 18.75 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | xdc1-leaf-01 | 10.255.0.3/32 |
| FABRIC | xdc1-leaf-02 | 10.255.0.4/32 |
| FABRIC | xdc1-leaf-03 | 10.255.0.5/32 |
| FABRIC | xdc1-leaf-04 | 10.255.0.6/32 |
| FABRIC | xdc1-spine-01 | 10.255.0.1/32 |
| FABRIC | xdc1-spine-02 | 10.255.0.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 10.255.1.0/27 | 32 | 4 | 12.5 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| FABRIC | xdc1-leaf-01 | 10.255.1.3/32 |
| FABRIC | xdc1-leaf-02 | 10.255.1.4/32 |
| FABRIC | xdc1-leaf-03 | 10.255.1.5/32 |
| FABRIC | xdc1-leaf-04 | 10.255.1.6/32 |
