# 📊 ANTA Report <a id="anta-report"></a>

**Table of Contents:**

- [ANTA Report](#anta-report)
  - [Run Overview](#run-overview)
  - [Test Results Summary](#test-results-summary)
    - [Summary Totals](#summary-totals)
    - [Summary Totals Device Under Test](#summary-totals-device-under-test)
    - [Summary Totals Per Category](#summary-totals-per-category)
  - [Test Results](#test-results)

## 📋 Run Overview <a id="run-overview"></a>

| ⚙️ Run Metric | 📝 Details |
| :- | :- |
| **ANTA Version** | v1.8.0 |
| **Test Execution Start Time** | 2026-06-19 15:31:50.621+00:00 |
| **Test Execution End Time** | 2026-06-19 15:31:52.813+00:00 |
| **Total Duration** | 2 seconds |
| **Total Devices In Inventory** | 6 |
| **Devices Unreachable At Setup** | None |
| **Devices Filtered At Setup** | None |
| **Filters Applied** | None |

## 📉 Test Results Summary <a id="test-results-summary"></a>

### 🔢 Summary Totals <a id="summary-totals"></a>

| Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- |
| 13 | 11 | 2 | 0 | 0 |

### 🔌 Summary Totals Device Under Test <a id="summary-totals-device-under-test"></a>

| Device | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error | Categories Skipped | Categories Failed |
| :- | :- | :- | :- | :- | :- | :- | :- |
| **xdc1-leaf-01** | 2 | 2 | 0 | 0 | 0 | - | - |
| **xdc1-leaf-02** | 2 | 2 | 0 | 0 | 0 | - | - |
| **xdc1-leaf-03** | 3 | 3 | 0 | 0 | 0 | - | - |
| **xdc1-leaf-04** | 2 | 2 | 0 | 0 | 0 | - | - |
| **xdc1-spine-01** | 2 | 1 | 1 | 0 | 0 | VXLAN | - |
| **xdc1-spine-02** | 2 | 1 | 1 | 0 | 0 | VXLAN | - |

### 🗂️ Summary Totals Per Category <a id="summary-totals-per-category"></a>

| Test Category | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- | :- |
| **Connectivity** | 1 | 1 | 0 | 0 | 0 |
| **Interfaces** | 6 | 6 | 0 | 0 | 0 |
| **VXLAN** | 6 | 4 | 2 | 0 | 0 |

## 🧪 Test Results <a id="test-results"></a>

| Device | Categories | Test | Description | Custom Field | Result | Messages |
| :- | :- | :- | :- | :- | :- | :- |
| xdc1-leaf-01 | Interfaces | VerifySVI | Verifies the status of all SVIs. | - | ✅&nbsp;Success | - |
| xdc1-leaf-01 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | ✅&nbsp;Success | - |
| xdc1-leaf-02 | Interfaces | VerifySVI | Verifies the status of all SVIs. | - | ✅&nbsp;Success | - |
| xdc1-leaf-02 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | ✅&nbsp;Success | - |
| xdc1-leaf-03 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | - | ✅&nbsp;Success | - |
| xdc1-leaf-03 | Interfaces | VerifySVI | Verifies the status of all SVIs. | - | ✅&nbsp;Success | - |
| xdc1-leaf-03 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | ✅&nbsp;Success | - |
| xdc1-leaf-04 | Interfaces | VerifySVI | Verifies the status of all SVIs. | - | ✅&nbsp;Success | - |
| xdc1-leaf-04 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | ✅&nbsp;Success | - |
| xdc1-spine-01 | Interfaces | VerifySVI | Verifies the status of all SVIs. | - | ✅&nbsp;Success | - |
| xdc1-spine-01 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | ⏭️&nbsp;Skipped | VXLAN is not configured |
| xdc1-spine-02 | Interfaces | VerifySVI | Verifies the status of all SVIs. | - | ✅&nbsp;Success | - |
| xdc1-spine-02 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | ⏭️&nbsp;Skipped | VXLAN is not configured |
