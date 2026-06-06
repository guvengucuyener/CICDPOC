# 📊 ANTA Report <a id="anta-report"></a>

**Table of Contents:**

- [ANTA Report](#anta-report)
  - [Test Results Summary](#test-results-summary)
    - [Summary Totals](#summary-totals)
    - [Summary Totals Device Under Test](#summary-totals-device-under-test)
    - [Summary Totals Per Category](#summary-totals-per-category)
  - [Test Results](#test-results)

## 📉 Test Results Summary <a id="test-results-summary"></a>

### 🔢 Summary Totals <a id="summary-totals"></a>

| Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- |
| 124 | 111 | 0 | 13 | 0 |

### 🔌 Summary Totals Device Under Test <a id="summary-totals-device-under-test"></a>

| Device | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error | Categories Skipped | Categories Failed |
| :- | :- | :- | :- | :- | :- | :- | :- |
| **xdc2-leaf-01** | 21 | 18 | 0 | 3 | 0 | - | Interfaces, Logging |
| **xdc2-leaf-02** | 21 | 19 | 0 | 2 | 0 | - | Interfaces, Logging |
| **xdc2-leaf-03** | 21 | 19 | 0 | 2 | 0 | - | Interfaces, Logging |
| **xdc2-leaf-04** | 21 | 19 | 0 | 2 | 0 | - | Interfaces, Logging |
| **xdc2-spine-01** | 20 | 18 | 0 | 2 | 0 | - | Interfaces, Logging |
| **xdc2-spine-02** | 20 | 18 | 0 | 2 | 0 | - | Interfaces, Logging |

### 🗂️ Summary Totals Per Category <a id="summary-totals-per-category"></a>

| Test Category | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- | :- |
| **BGP** | 6 | 6 | 0 | 0 | 0 |
| **Configuration** | 12 | 12 | 0 | 0 | 0 |
| **Connectivity** | 12 | 12 | 0 | 0 | 0 |
| **Interfaces** | 30 | 23 | 0 | 7 | 0 |
| **Logging** | 6 | 0 | 0 | 6 | 0 |
| **Routing** | 6 | 6 | 0 | 0 | 0 |
| **STP** | 6 | 6 | 0 | 0 | 0 |
| **System** | 42 | 42 | 0 | 0 | 0 |
| **VXLAN** | 4 | 4 | 0 | 0 | 0 |

## 🧪 Test Results <a id="test-results"></a>

| Device | Categories | Test | Description | Result | Messages |
| :- | :- | :- | :- | :- | :- |
| xdc2-leaf-01 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ❌&nbsp;Failure | Interface: Management0 - Non-zero discard counter(s): inDiscards: 351 |
| xdc2-leaf-01 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ❌&nbsp;Failure | Interface: Ethernet3 - Not configured |
| xdc2-leaf-01 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Jun  6 09:17:05 xdc2-leaf-01 LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> Jun  6 09:43:49 xdc2-leaf-01 ConfigAgent: %SYS-3-CONFIG_SESSION_COMMIT_TIMER_TIMEDOUT: The commit timer on session cvp-provisioning-27b24134-0222-4d0c-b130-b0282fa17699 has expired.The system configuration will be rolled back.<br> Jun  6 10:33:32 xdc2-leaf-01 ConfigAgent: %SYS-3-CONFIG_SESSION_COMMIT_TIMER_TIMEDOUT: The commit timer on session cvp-provisioning-c59325a4-cca1-45f2-a78e-bef26bf2c92c has expired.The system configuration will be rolled back.<br> <br> |
| xdc2-leaf-02 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ❌&nbsp;Failure | Interface: Management0 - Non-zero discard counter(s): inDiscards: 477 |
| xdc2-leaf-02 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Jun  6 09:17:42 xdc2-leaf-02 LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> Jun  6 10:33:33 xdc2-leaf-02 ConfigAgent: %SYS-3-CONFIG_SESSION_COMMIT_TIMER_TIMEDOUT: The commit timer on session cvp-provisioning-1f07ddf1-c122-4336-a7e0-d5e49d243202 has expired.The system configuration will be rolled back.<br> <br> |
| xdc2-leaf-03 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ❌&nbsp;Failure | Interface: Management0 - Non-zero discard counter(s): inDiscards: 340 |
| xdc2-leaf-03 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Jun  6 10:33:33 xdc2-leaf-03 ConfigAgent: %SYS-3-CONFIG_SESSION_COMMIT_TIMER_TIMEDOUT: The commit timer on session cvp-provisioning-ce7d5866-9004-400d-8eba-be5c892a3701 has expired.The system configuration will be rolled back.<br> <br> |
| xdc2-leaf-04 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ❌&nbsp;Failure | Interface: Management0 - Non-zero discard counter(s): inDiscards: 338 |
| xdc2-leaf-04 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Jun  6 09:16:56 xdc2-leaf-04 NorCalInit: %HARDWARE-0-SYSTEM_IDENTIFICATION_FAILED: Failed to identify this system<br> Jun  6 09:17:05 xdc2-leaf-04 LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> Jun  6 10:33:33 xdc2-leaf-04 ConfigAgent: %SYS-3-CONFIG_SESSION_COMMIT_TIMER_TIMEDOUT: The commit timer on session cvp-provisioning-a708ffc9-1ebd-4049-bfbf-795e819fc03c has expired.The system configuration will be rolled back.<br> <br> |
| xdc2-spine-01 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ❌&nbsp;Failure | Interface: Management0 - Non-zero discard counter(s): inDiscards: 330 |
| xdc2-spine-01 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Jun  6 10:33:33 xdc2-spine-01 ConfigAgent: %SYS-3-CONFIG_SESSION_COMMIT_TIMER_TIMEDOUT: The commit timer on session cvp-provisioning-c0ab593a-2497-492d-9cf1-eb108658f14d has expired.The system configuration will be rolled back.<br> <br> |
| xdc2-spine-02 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ❌&nbsp;Failure | Interface: Management0 - Non-zero discard counter(s): inDiscards: 321 |
| xdc2-spine-02 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Jun  6 09:43:49 xdc2-spine-02 ConfigAgent: %SYS-3-CONFIG_SESSION_COMMIT_TIMER_TIMEDOUT: The commit timer on session cvp-provisioning-87fe0120-3526-45de-9e20-c04b3489c4cf has expired.The system configuration will be rolled back.<br> <br> |
| xdc2-leaf-01 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | System | VerifyNTP | Verifies if NTP is synchronised. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| xdc2-leaf-01 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | System | VerifyNTP | Verifies if NTP is synchronised. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| xdc2-leaf-02 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | System | VerifyNTP | Verifies if NTP is synchronised. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| xdc2-leaf-03 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | System | VerifyNTP | Verifies if NTP is synchronised. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| xdc2-leaf-04 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| xdc2-spine-01 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| xdc2-spine-01 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| xdc2-spine-01 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| xdc2-spine-01 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| xdc2-spine-01 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| xdc2-spine-01 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| xdc2-spine-01 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| xdc2-spine-01 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| xdc2-spine-01 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| xdc2-spine-01 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| xdc2-spine-01 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| xdc2-spine-01 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| xdc2-spine-01 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| xdc2-spine-01 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| xdc2-spine-01 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| xdc2-spine-01 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| xdc2-spine-01 | System | VerifyNTP | Verifies if NTP is synchronised. | ✅&nbsp;Success | - |
| xdc2-spine-01 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| xdc2-spine-02 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| xdc2-spine-02 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| xdc2-spine-02 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| xdc2-spine-02 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| xdc2-spine-02 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| xdc2-spine-02 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| xdc2-spine-02 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| xdc2-spine-02 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| xdc2-spine-02 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| xdc2-spine-02 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| xdc2-spine-02 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| xdc2-spine-02 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| xdc2-spine-02 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| xdc2-spine-02 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| xdc2-spine-02 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| xdc2-spine-02 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| xdc2-spine-02 | System | VerifyNTP | Verifies if NTP is synchronised. | ✅&nbsp;Success | - |
| xdc2-spine-02 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
