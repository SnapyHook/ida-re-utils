# IDA Reverse Engineering Utilities

This repository contains Python scripts for **IDA Pro** that assist with
static reverse engineering and binary analysis on native binaries
(primarily ARM64).

The scripts are **generic**, target-agnostic, and intended for:
- Reverse engineering research
- Malware and binary analysis
- Function discovery and inspection
- Educational and defensive security work

No exploit, bypass, or circumvention logic is included.

---

## Included Scripts

### 1. Pattern Scanner
Scans binary segments for a given byte pattern with wildcard (`??`) support.
Useful for:
- Locating functions
- Signature-based research
- Binary diffing
- Static analysis workflows

### 2. Function Byte Dumper
Extracts raw bytes of a function by name.
Useful for:
- Offline analysis
- Research documentation
- Signature creation
- Studying compiler output

---

## Environment

- IDA Pro 9.2
- Python (IDA embedded)
- ARM64 binaries

---

## Disclaimer

These scripts are provided **for research and educational purposes only**.
They are not designed or intended to bypass protections or violate
software terms of service.

