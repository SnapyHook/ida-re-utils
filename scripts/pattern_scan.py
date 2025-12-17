import idaapi
import ida_bytes
import idc

def find_pattern(hex_string):
    # Convert hex string into raw bytes
    pattern = bytes(int(b, 16) if b != "??" else 0 for b in hex_string.split())
    mask = "".join("x" if b != "??" else "?" for b in hex_string.split())

    start_ea = idaapi.get_first_seg().start_ea
    end_ea = idaapi.get_last_seg().end_ea

    ea = start_ea
    while ea < end_ea:
        data = ida_bytes.get_bytes(ea, len(pattern))
        if not data:
            ea += 1
            continue
        match = True
        for i in range(len(pattern)):
            if mask[i] == "x" and data[i] != pattern[i]:
                match = False
                break
        if match:
            print(f"[+] Match at 0x{ea:X}")
            func = idaapi.get_func(ea)
            if func:
                print(f"    Function: {idc.get_func_name(func.start_ea)} (0x{func.start_ea:X} - 0x{func.end_ea:X})")
            return ea
        ea += 1

    print("[!] Pattern not found")
    return None

# Example: first 16 bytes of your block (no relocations, so no wildcards yet)
pattern = "FD 7B B9 A9 FD 03 00 91 A0 1F 00 F9 A1 37 00 B9"

find_pattern(pattern)
