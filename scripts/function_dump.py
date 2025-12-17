# IDA 9.1 macOS arm64
# Dump the raw bytecode (hex) of a function by name

import ida_funcs
import ida_bytes
import idc

FUNC_NAME = "sub_6326B3C"  # change this if needed

def get_function_bytes(func_name):
    ea = idc.get_name_ea_simple(func_name)
    if ea == idc.BADADDR:
        print(f"[!] Function {func_name} not found.")
        return None

    func = ida_funcs.get_func(ea)
    if not func:
        print(f"[!] Could not retrieve function info for {func_name}.")
        return None

    start = func.start_ea
    end = func.end_ea
    size = end - start

    data = ida_bytes.get_bytes(start, size)
    if not data:
        print("[!] Failed to read bytes.")
        return None

    return data, start, end

result = get_function_bytes(FUNC_NAME)
if result:
    data, start, end = result
    hex_bytes = " ".join(f"{b:02X}" for b in data)
    print(f"[+] Function {FUNC_NAME} @ 0x{start:X} - 0x{end:X} ({len(data)} bytes)")
    print(hex_bytes)
