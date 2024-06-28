# Scenario 5

# Illinois

## Routers

### 1. mlsIL033a02a01 (L3 Switch A)

**OSPF**

```cisco
router ospf 1
network 10.2.33.200 0.0.0.3 area 0
network 10.2.33.208 0.0.0.7 area 0
network 10.2.33.216 0.0.0.7 area 0
network 10.2.33.224 0.0.0.31 area 0
```

**IP Helpers**

```cisco
interface vlan 1330
ip helper-address 10.2.33.228
!
interface vlan 2330
ip helper-address 10.2.33.228
!
interface vlan 3330
ip helper-address 10.2.33.228
```

**HSRP**
```cisco
interface vlan 1330
standby version 2
standby 1330 ip 10.2.33.211
standby 1330 priority 110
standby 1330 preempt
!
interface vlan 2330
standby version 2
standby 2330 ip 10.2.33.219
standby 2330 priority 110
standby 2330 preempt
!
interface vlan 3330
standby version 2
standby 3330 ip 10.2.33.227
standby 3330 priority 110
standby 3330 preempt
```

**LACP**

```cisco
interface port-channel 1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 1330,2330,3330
!
interface range g1/0 - 1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 1330,2330,3330
channel-group 1 mode active
```

### 2. mlsIL033a02a02 (new L3 switch)

**OSPF**

```
router ospf 1
network 10.2.33.200 0.0.0.3 area 0
network 10.2.33.208 0.0.0.7 area 0
network 10.2.33.216 0.0.0.7 area 0
network 10.2.33.224 0.0.0.31 area 0
```

**IP Helpers**

```cisco
interface vlan 1330
ip helper-address 10.2.33.228
!
interface vlan 2330
ip helper-address 10.2.33.228
!
interface vlan 3330
ip helper-address 10.2.33.228
```

**HSRP**

> Priority 90

```cisco
interface vlan 1330
standby version 2
standby 1330 ip 10.2.33.211
standby 1330 priority 90
standby 1330 preempt
!
interface vlan 2330
standby version 2
standby 2330 ip 10.2.33.219
standby 2330 priority 90
standby 2330 preempt
!
interface vlan 3330
standby version 2
standby 3330 ip 10.2.33.227
standby 3330 priority 90
standby 3330 preempt
```

**LACP**

```cisco
interface port-channel 1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 1330,2330,3330
!
interface range g1/0 - 1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 1330,2330,3330
channel-group 1 mode active
```

### 3. rtrIL033a02a01 (Illinois Router):

**OSPF**

```cisco
router ospf 1
network 10.2.33.200 0.0.0.3 area 0

**No IP helpers needed on this router**
```

### 4. rtrNY033a02a01 (New York Router):

**IP Helpers**

```cisco
interface g0/3.1332
ip helper-address 10.2.33.228
!
interface g0/3.2332
ip helper-address 10.2.33.228
```

### 5. rtrCA033a02a01 (California Router):

**IP Helpers**

```cisco
interface g0/3.1331
ip helper-address 10.2.33.1
!
interface g0/3.2331
ip helper-address 10.2.33.1
```

# Updates

For mlsIL033a02a01 (L3 Switch A):

```cisco
interface vlan 90
 ip address 10.2.33.194 255.255.255.255
 no shutdown

router ospf 1
 network 10.2.33.194 0.0.0.0 area 0
 no passive-interface vlan 90

interface vlan 1330
 standby version 2
 standby 1330 ip 10.2.33.211
 standby 1330 priority 110
 standby 1330 preempt
 ip helper-address 10.2.33.228

interface vlan 2330
 standby version 2
 standby 2330 ip 10.2.33.219
 standby 1330 priority 110
 standby 2330 preempt
 ip helper-address 10.2.33.228

interface vlan 3330
 standby version 2
 standby 3330 ip 10.2.33.227
 standby 1330 priority 110
 standby 3330 preempt
 ip helper-address 10.2.33.228
```

For mlsIL033a02a02 (L3 Switch B):

```cisco
interface vlan 90
 ip address 10.2.33.198 255.255.255.255
 no shutdown

router ospf 1
 network 10.2.33.198 0.0.0.0 area 0
 no passive-interface vlan 90

interface vlan 1330
 standby version 2
 standby 1330 ip 10.2.33.211
 standby 1330 priority 90
 standby 1330 preempt
 ip helper-address 10.2.33.228

interface vlan 2330
 standby version 2
 standby 2330 ip 10.2.33.219
 standby 1330 priority 90
 standby 2330 preempt
 ip helper-address 10.2.33.228

interface vlan 3330
 standby version 2
 standby 3330 ip 10.2.33.227
 standby 1330 priority 90
 standby 3330 preempt
 ip helper-address 10.2.33.228
```
