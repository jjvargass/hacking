# Bash

Se realizara los ejercicio se [overthewire](https://overthewire.org/wargames/) capitulo de Bandit
bandit0
```bash
bandit0@bandit:~$ hostname -I
192.168.101.80

bandit0@bandit:~$ hostname
bandit.otw.local

bandit0@bandit:~$ ls -la /
total 924
drwxr-xr-x   26 root root   4096 May 13  2020 .
drwxr-xr-x   26 root root   4096 May 13  2020 ..
drwxr-xr-x    2 root root   4096 May 13  2020 bin
drwxr-xr-x    4 root root   4096 May  3  2020 boot
dr-xr-xr-x    3 root root      0 Jul 15 21:10 cgroup2
drwxr-xr-x   14 root root  21960 Nov 28 16:02 dev

bandit0@bandit:~$ which docker
/usr/bin/docker
```

bandit1
```bash
bandit1@bandit:~$ whoami
bandit1

bandit1@bandit:~$ ls
-

bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

bandit1@bandit:~$ cat /home/bandit1/-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

bandit1@bandit:~$ cat /home/bandit1/*
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

# $() indicar el output aplicado a nivel de sistemas
bandit1@bandit:~$ cat $(pwd)/-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

bandit2
```bash
bandit2@bandit:~$ ls
spaces in this filename

bandit2@bandit:~$ cat "spaces in this filename"
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

# por tabulacion
bandit2@bandit:~$ cat spaces\ in\ this\ filename
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

bandit2@bandit:~$ cat sp*
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

bandit2@bandit:~$ cat *name
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

bandit2@bandit:~$ cat $(pwd)/*
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

bandit3
```bash
bandit3@bandit:~$ ls -la inhere/
total 12
drwxr-xr-x 2 root    root    4096 May  7  2020 .
drwxr-xr-x 3 root    root    4096 May  7  2020 ..
-rw-r----- 1 bandit4 bandit3   33 May  7  2020 .hidden

# busca cualquier cosa desde el directorio actual de forma recursiva
bandit3@bandit:~$ find .
.
./inhere
./inhere/.hidden
./.bashrc
./.profile
./.bash_logout

# listar archivos
bandit3@bandit:~$ find . -type f
./inhere/.hidden
./.bashrc
./.profile
./.bash_logout

# %f archivos
# %p ruta absoluta
# %u usuario propietario
# %g grupo asignado
# %m el modo (permmiso asignado a nivel numerico)
# \t tabulaciion
bandit3@bandit:~$ find . -type f -printf "%f\t%p\t%u\t%g\t%m\n"
.hidden	./inhere/.hidden	bandit4	bandit3	640
.bashrc	./.bashrc	root	root	644
.profile	./.profile	root	root	644
.bash_logout	./.bash_logout	root	root	644

# para ordenar
bandit3@bandit:~$ find . -type f -printf "%f\t%p\t%u\t%g\t%m\n" | column -t
.hidden       ./inhere/.hidden  bandit4  bandit3  640
.bashrc       ./.bashrc         root     root     644
.profile      ./.profile        root     root     644
.bash_logout  ./.bash_logout    root     root     644


bandit3@bandit:~$ cat inhere/.hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB

# xargs es util para de forma paralela ejecutar comandos sobre el output de un comando ejecutado anteriormente.

# sabemos la salida del primer comando
bandit3@bandit:~$ find . -name .hidden
./inhere/.hidden

# pensariamos en la tuberia "pai" y el cat, pero  no funciona
bandit3@bandit:~$ find . -name .hidden | cat
./inhere/.hidden

# despues de la tuberia
bandit3@bandit:~$ find . -name .hidden | xargs cat
pIwrPrtPN36QITSp3EQaw936yaFoFgAB



```


```bash
```

```bash
```

```bash
```

```bash
```
