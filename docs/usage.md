# Usage

## Pattern Scanner

1. Open a binary in IDA Pro
2. Load the script inside IDA's Python console or via File → Script file
3. Provide a hex pattern string (supports ?? wildcards)
4. The script scans loaded segments and reports matches

---

## Function Byte Dumper

1. Ensure functions are identified in IDA
2. Set the target function name inside the script
3. Run the script
4. Raw bytes are printed in hexadecimal format

---

## Notes

- Script output depends on IDA’s analysis state
- Better results are achieved after auto-analysis completes
