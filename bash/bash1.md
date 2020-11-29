# Bash

Se realizara los ejercicio se [overthewire](https://overthewire.org/wargames/) capitulo de Bandit

## bandit0
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

## bandit1
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

## bandit2
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

## bandit3
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

# el xargs se aplica a cada salida
bandit3@bandit:~$ find . -type f
./inhere/.hidden
./.bashrc
./.profile
./.bash_logout

bandit3@bandit:~$ find . -type f | xargs cat
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac
...

# Incluso para aplicar busquedas en cada archivo
bandit3@bandit:~$ find . -type f | xargs grep "leaving"
./.bash_logout:# when leaving the console clear the screen to increase privacy
```

## bandit4
```bash
bandit4@bandit:~$ ls -l inhere/
total 40
-rw-r----- 1 bandit5 bandit4 33 May  7  2020 -file00
-rw-r----- 1 bandit5 bandit4 33 May  7  2020 -file01
-rw-r----- 1 bandit5 bandit4 33 May  7  2020 -file02
-rw-r----- 1 bandit5 bandit4 33 May  7  2020 -file03
-rw-r----- 1 bandit5 bandit4 33 May  7  2020 -file04
-rw-r----- 1 bandit5 bandit4 33 May  7  2020 -file05
-rw-r----- 1 bandit5 bandit4 33 May  7  2020 -file06
-rw-r----- 1 bandit5 bandit4 33 May  7  2020 -file07
-rw-r----- 1 bandit5 bandit4 33 May  7  2020 -file08
-rw-r----- 1 bandit5 bandit4 33 May  7  2020 -file09

# se debe revisar el archivo humanamente legible, para esto usar los Magic number

bandit4@bandit:~$ find . -name -file* | xargs file
./inhere/-file01: data
./inhere/-file00: data
./inhere/-file06: data
./inhere/-file03: data
./inhere/-file05: data
./inhere/-file08: data
./inhere/-file04: data
./inhere/-file07: ASCII text
./inhere/-file02: data
./inhere/-file09: data

bandit4@bandit:~$ find . -name -file07 | xargs cat
koReBOKuIDDepwhWk7jZC0RTdopnAYKh

bandit4@bandit:~$ cat $(find . -name -file07)  
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

Ejemplo de Magic Number
```bash
root@pc:~# file 1.htb.jpg
1.htb.jpg: JPEG image data, Exif standard: [TIFF image data, big-endian, direntries=7, orientation=upper-left, xresolution=98, yresolution=106, resolutionunit=2, software=Adobe Photoshop CC (Windows), datetime=2019:12:04 07:34:10], progressive, precision 8, 1920x1080, components 3

# editor de binarios
hexeditor 1.htb.jpg
```

```bash
nano file.txt

# y en el editor agregamos lo siguiente
GIF8;

hola que hace esto es un texto

# consultamos
root@pc:~# file file.txt
file.txt: GIF image data 26634 x 27759
root@pc:~#
```

## bandit5
```bash
bandit5@bandit:~$ ls -l inhere/
total 80
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere00
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere01
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere02
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere03
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere04
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere05
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere06
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere07
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere08
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere09
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere10
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere11
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere12
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere13
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere14
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere15
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere16
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere17
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere18
drwxr-x--- 2 root bandit5 4096 May  7  2020 maybehere19

# dentro de cada directorio hay mas archivos
bandit5@bandit:~$ find .
.
./inhere
./inhere/maybehere03
./inhere/maybehere03/.file2
./inhere/maybehere03/spaces file3
./inhere/maybehere03/-file3
./inhere/maybehere03/-file2
./inhere/maybehere03/.file3
./inhere/maybehere03/spaces file1
./inhere/maybehere03/-file1
./inhere/maybehere03/spaces file2
./inhere/maybehere03/.file1
./inhere/maybehere19
./inhere/maybehere19/.file2


# como buscamos archiov -type f
# que sea readable entonces -readable Tambien exitse las opciones (-executable  -writable)
# -size filtar por el tamaño, para especificar bytes agregasr "c"
bandit5@bandit:~$ find . -type f -readable  -size 1033c
./inhere/maybehere07/.file2

bandit5@bandit:~$ find . -type f -readable  -size 1033c | xargs cat
DXjZPULLxYr17uwoI01bNLQbtFemEgo7

# este archivo contine espacion en blanco y saltos de linea. para limpiar agragamos un xargs solo
bandit5@bandit:~$ find . -type f -readable  -size 1033c | xargs cat  | xargs
DXjZPULLxYr17uwoI01bNLQbtFemEgo7

# de la misma forma como se limpio el archio utilizaremos  tr opcion -d para eliminar
bandit5@bandit:~$ find . -type f -readable  -size 1033c | xargs cat  | tr -d ' '
DXjZPULLxYr17uwoI01bNLQbtFemEgo7

# sed 's/argumento/aloqueloqueremosconvertir'
# sed 's/root/miusuario/' => cambie root en el archivo por miusuario

# s/^ *  reemplace todo lo que inicie con espacio en blanco y cualquier cosa  - cambielo por nada

bandit5@bandit:~$ find . -type f -readable ! -executable  -size 1033c | xargs cat  | sed 's/^ *//'
DXjZPULLxYr17uwoI01bNLQbtFemEgo7

# \s espacions
# /d  vacio
bandit5@bandit:~$ find . -type f -readable ! -executable  -size 1033c | xargs cat  | sed '/^\s*$/d'
DXjZPULLxYr17uwoI01bNLQbtFemEgo7


# ^ que inicie
# $ que finalice
root@pc:~# cat /usr/share/wordlists/rockyou.txt | grep "^hola$"
hola

# utilidad de grep -n para ver la linea
root@pc:~# cat /usr/share/wordlists/rockyou.txt | grep "^hola$" -n
19994:hola
```

Comando head y tail
```bash
# nostara la n linesas de un archivo
root@pc:~# cat /etc/passwd | head -n 1
root:x:0:0:root:/root:/bin/bash

root@pc:~# cat /etc/passwd | head -n 2
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin

# las ultimas dos lineas
root@pc:~# cat /etc/passwd | tail -n 2
jjvargass:x:1000:1000:JJVARGASS,,,:/home/jjvargass:/usr/bin/zsh
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin

# la linea 2
root@pc:~# cat /etc/passwd | awk 'NR==2'
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
```

Sed
```bash
root@pc:~# cat file.txt | head -n 6
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin

# sed sustitulle
root@pc:~# cat file.txt | head -n 1
root:x:0:0:root:/root:/bin/bash

# y porque no lo realizo en todos los root
root@pc:~# cat file.txt | head -n 1  | sed 's/root/miusuario/'
miusuario:x:0:0:root:/root:/bin/bash

# para todas las coninciencias se debe colocar g al final
root@pc:~# cat file.txt | head -n 1  | sed 's/root/miusuario/g'
miusuario:x:0:0:miusuario:/miusuario:/bin/bash

# grep
# cuando grepeamos apareceran varias coninciencias
root@pc:~# cat /etc/passwd | grep root
root:x:0:0:root:/root:/bin/bash
nm-openvpn:x:125:130:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin

# para especificar con expreciones regulares  las que comiencen con r
root@pc:~# cat /etc/passwd | grep "^root"
root:x:0:0:root:/root:/bin/bash
```

## bandit6
```bash
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c
find: ‘/root’: Permission denied
find: ‘/home/bandit28-git’: Permission denied
find: ‘/home/bandit30-git’: Permission denied
find: ‘/home/bandit5/inhere’: Permission denied
find: ‘/home/bandit27-git’: Permission denied
find: ‘/home/bandit29-git’: Permission denied
find: ‘/home/bandit31-git’: Permission denied

# no mostrar errores
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
```
Manejo de stderr stdout
```bash
# podemos tambien en script redirigir el error y nostrarlo
root@pc:~# cat llskksk 2>&1
cat: llskksk: No such file or directory

# stderr: se referencia con un 2 = Controla lo errores
# stdout

# muestra el erro
root@pc:~# cat adslkjads
cat: adslkjads: No such file or directory

# si lo redireccionar
root@pc:~# cat adslkjads 2>/dev/null
root@pc:~#

# cuando abrimos firefox, generalmente genera stdout, si no queremos ver eso, podemos dirigir todos al /dev/null y los errores pasarlos al stdout
firefox > /dev/null 2>&1
```
Imdependizar procesos
```bash
root@pc:~# disown -a
```

No Hacer daña el sistema operativo
```bash
mv /* /dev/null
```

```bash
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null | xargs cat
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

## bandit7
```bash
# el archivo es bastante grande
bandit7@bandit:~$ cat data.txt
binning	WnfnFPqkuhl2nwHBohzn2C4L5W0gwcLq
abuts	v8PAwDdkGDdp5NsJ7ZFM5A7TJ5MkYDbm
fathead	wBhCy0fqvbQdexz5kMKBtGoSWgXw7s0H
attacks	3GzwnGiZnBDdVuHivJk1pEfOOYu7uOTa
lopping	H9hzviFp1QO4WF8EzcQNl5MDz5r1bzUC
tyrannosaurus	WxtYXVar4sgInHp7YUpTzOjdUw1Ww0x8

# contar las lineas del archivos
bandit7@bandit:~$ cat data.txt | wc -l
98567

# caracteres totales
bandit7@bandit:~$ cat data.txt | wc -c
4184396

bandit7@bandit:~$ cat data.txt | grep millionth
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV

# la forma adecuada es directamente el grep sobre el archivo
bandit7@bandit:~$ grep "millionth" data.txt
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV

#awk
bandit7@bandit:~$ cat data.txt | awk '/millionth/'
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV

bandit7@bandit:~$ awk '/millionth/' data.txt
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV

# ver velocidades del comando
bandit7@bandit:~$ time awk '/millionth/' data.txt
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV

real	0m0.012s
user	0m0.004s
sys	0m0.008s

bandit7@bandit:~$ time grep '/millionth/' data.txt

real	0m0.004s
user	0m0.000s
sys	0m0.004s

# trabajar con los argumentos del awk
bandit7@bandit:~$ awk '/millionth/' data.txt  | awk '{print $1}'
millionth
bandit7@bandit:~$ awk '/millionth/' data.txt  | awk '{print $2}'
cvX2JJa4CFALtqS87jk27qwqGhBM9plV

bandit7@bandit:~$ awk 'millionth' data.txt  # No Funciona
bandit7@bandit:~$ awk '/millionth/' data.txt
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV

bandit7@bandit:~$ grep '/millionth/' data.txt # No Funciona
bandit7@bandit:~$ grep 'millionth' data.txt
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV

# Argumentos desde la tuberia de un grep y luego de un awk
# desde grep
bandit7@bandit:~$ grep 'millionth' data.txt
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
bandit7@bandit:~$ grep 'millionth' data.txt | awk '{print $1}'
millionth
# desde awk
bandit7@bandit:~$ awk 'millionth' data.txt | awk '{print $1}'
bandit7@bandit:~$ awk '/millionth/' data.txt | awk '{print $1}'
millionth

# traer ultimo argumentos
bandit7@bandit:~$ awk '/millionth/' data.txt
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
bandit7@bandit:~$ awk '/millionth/' data.txt  | awk 'NF{print $NF}'
cvX2JJa4CFALtqS87jk27qwqGhBM9plV

# revertir cadenas
bandit7@bandit:~$ awk '/millionth/' data.txt  | rev
Vlp9MBhGqwq72kj78SqtLAFC4aJJ2Xvc	htnoillim
bandit7@bandit:~$ awk '/millionth/' data.txt  | rev | awk '{print $1}'
Vlp9MBhGqwq72kj78SqtLAFC4aJJ2Xvc
bandit7@bandit:~$ awk '/millionth/' data.txt  | rev | awk '{print $1}' | rev
cvX2JJa4CFALtqS87jk27qwqGhBM9plV

# para recordar
bandit7@bandit:~$ grep 'millionth' data.txt -n
37262:millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
bandit7@bandit:~$ awk 'NR==37262' data.txt
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```
