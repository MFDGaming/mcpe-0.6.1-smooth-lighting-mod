from sdk import Patch, Mod
from os import getcwd, sep

mod = Mod()
patches = [
    Patch(0xffda2, b"\x01\x23"), # movs r3, #1
    Patch(0xd4c0a, b"\x00\xbf\x00\xbf"), # nop nop
    Patch(0xda780, b"\x00\xbf\x00\xbf"), # nop nop
    Patch(0xda948, b"\x00\xbf\x00\xbf"), # nop nop
    Patch(0xf3aa6, b"\x00\xbf\x00\xbf") # nop nop
]

for patch in patches:
    mod.add_patch(patch)

mod.save(getcwd() + sep + "smooth_lighting.mod")
