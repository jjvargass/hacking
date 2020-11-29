# permisos para GNU/Linux

```bash
rwx rwx rwx
propietarios - grupos - otros
```
```bash
root@pc:~# touch file.txt
root@pc:~# ls -l
total 0
-rw-r--r-- 1 root root 0 Nov 28 15:12 file.txt
root@pc:~#
```

```bash
# otros no puedan leer file.txt
root@pc:~# chmod o-r file.txt
root@pc:~# ls -l
total 0
-rw-r----- 1 root root 0 Nov 28 15:12 file.txt

# otros  puedan leer y escrivir file.txt
root@pc:~# ls -l
total 0
-rw-r--rw- 1 root root 0 Nov 28 15:12 file.txt

# asignar grupo
root@pc:~# chgrp jjvargass file.txt
root@pc:~# ls -l
total 0
-rw-r--rw- 1 root jjvargass 0 Nov 28 15:12 file.txt

# grupos no puedan leer y otros no puedan escrivir

root@pc:~# ls -l
total 0
-rw-r--rw- 1 root jjvargass 0 Nov 28 15:12 file.txt

root@pc:~# chmod g-r,o-w file.txt
root@pc:~# ls -l
total 0
-rw----r-- 1 root jjvargass 0 Nov 28 15:12 file.txt
```

```bash
# privilegios avanzados
root@pc:~# chattr  +i -V file.txt
chattr 1.45.6 (20-Mar-2020)
Flags of file.txt set as ----i---------e-----
root@pc:~# ls -l
total 0
-rw----r-- 1 root jjvargass 0 Nov 28 15:12 file.txt
root@pc:~#

# como rood no puedo escrivir

# si se intenta eliminar el archivo no es permitido
root@pc:~# rm file.txt
rm: cannot remove 'file.txt': Operation not permitted

# Para listar esto permisos especiales es con lsattr
root@pc:~# lsattr
----i---------e----- ./file.txt

# De la misma manera como se asigno con - se elimina este privilegio
root@pc:~# chattr -i -V file.txt
chattr 1.45.6 (20-Mar-2020)
Flags of file.txt set as --------------e-----

root@pc:~# lsattr
--------------e----- ./file.txt
```
