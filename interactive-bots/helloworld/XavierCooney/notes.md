I used the Windows 10 feature bash Windows Subsystem for Linux (WSL).
It lets users use a linux environment parallel to the win32 kernel
without the overhead of virtual machines.

The process was relatively easy, and the only problem I encountered was during
provisioning I encountered an error message that looked like
```
creating build/temp.linux-x86_64-2.7/backports/lzma
  x86_64-linux-gnu-gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/mnt/c/blah/gci/bots/python-zulip-api/zulip-api-py2-venv/include -I/home/Xavier/include -I/opt/local/include -I/usr/local/include -I/usr/include/python2.7 -c backports/lzma/_lzmamodule.c -o build/temp.linux-x86_64-2.7/backports/lzma/_lzmamodule.o
  backports/lzma/_lzmamodule.c:12:20: fatal error: Python.h: No such file or directory
   #include "Python.h"
                      ^
  compilation terminated.
  error: command 'x86_64-linux-gnu-gcc' failed with exit status 1

  ----------------------------------------
  Failed building wheel for backports.lzma
```

This was because `python` was version `2.7.6`, and running
`python3 tools/provision` resolved this issue. I then ran the activation
script without a problem, and after that had no problem runnning the actual
bot.