
import sys
import ctypes
from ctypes import c_char, c_ushort, c_uint, c_char_p
from ctypes import windll, Structure, POINTER, sizeof

def default_resolution():
    class _DevMode(Structure):
        _fields_ = [
            ("dmDeviceName", c_char * 32),
            ("unused1", c_ushort * 2),
            ("dmSize", c_ushort),
            ("unused2", c_ushort),
            ("unused3", c_uint * 8),
            ("dmFormName", c_char * 32),
            ("dmLogPixels", c_ushort),
            ("dmBitsPerPel", c_ushort),
            ("dmPelsWidth", c_uint),
            ("dmPelsHeight", c_uint),
            ]
    EnumDisplaySettings = windll.user32.EnumDisplaySettingsA
    EnumDisplaySettings.argtypes = c_char_p, c_uint, POINTER(_DevMode)
    ChangeDisplaySettings = windll.user32.ChangeDisplaySettingsA
    ChangeDisplaySettings.argtypes = POINTER(_DevMode), c_uint
    ENUM_CURRENT_SETTINGS = -1
    CDS_UPDATEREGISTRY = 1
    DISP_CHANGE_SUCCESSFUL = 0
    dm = _DevMode()
    r = EnumDisplaySettings(None,0,dm)
    dm.dmPelsWidth = 1920
    dm.dmPelsHeight = 1080
    ret = ChangeDisplaySettings(ctypes.byref(dm), CDS_UPDATEREGISTRY)

    if len(sys.argv) != 3:
        print (sys.argv[0])
        dm = _DevMode()
        dm.dmSize = sizeof(dm)
    if not EnumDisplaySettings(None, ENUM_CURRENT_SETTINGS, dm):
        print ("Error enumerating display settings..")
        dm.dmPelsWidth = int(sys.argv[1])
        dm.dmPelsHeight = int(sys.argv[2])
        ret = ChangeDisplaySettings(dm, CDS_UPDATEREGISTRY)
    if ret != DISP_CHANGE_SUCCESSFUL:
        print ("Error changing display settings..")

if __name__ == "__main__":
    default_resolution()