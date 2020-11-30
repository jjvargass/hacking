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

## bandit8
```bash
# conteno de lineas
bandit8@bandit:~$ cat data.txt | wc -l
1001

# filtrar cadenas que poso aparecen una unica vez

# enpezar por ordenar
bandit8@bandit:~$ cat data.txt | sort
07KC3ukwX7kswl8Le9ebb3H3sOoNTsR2
07KC3ukwX7kswl8Le9ebb3H3sOoNTsR2
07KC3ukwX7kswl8Le9ebb3H3sOoNTsR2
07KC3ukwX7kswl8Le9ebb3H3sOoNTsR2
07KC3ukwX7kswl8Le9ebb3H3sOoNTsR2
07KC3ukwX7kswl8Le9ebb3H3sOoNTsR2
07KC3ukwX7kswl8Le9ebb3H3sOoNTsR2
07KC3ukwX7kswl8Le9ebb3H3sOoNTsR2
07KC3ukwX7kswl8Le9ebb3H3sOoNTsR2
07KC3ukwX7kswl8Le9ebb3H3sOoNTsR2
0efnqHY1ZTNRu4LsDX4D73DsxIQq7RuJ
0efnqHY1ZTNRu4LsDX4D73DsxIQq7RuJ
0efnqHY1ZTNRu4LsDX4D73DsxIQq7RuJ
0efnqHY1ZTNRu4LsDX4D73DsxIQq7RuJ

# con  uniq -u  para traer la unica, requiere previamente del sort
bandit8@bandit:~$ cat data.txt | sort | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

# tambien se puede utilizar con unique
```

## bandit9
```bash
bandit9@bandit:~$ cat data.txt
�L�lω;��ßOܛ��ǤX��NdT$��x7��@D@�o��+D��B��M֢�Z/,_��w��#�5���
                                                          Ў�e�&�-��Ϣ�6Q8��J�%fa�
�np�6l
|c���WW"&8��f��
��VJ�$�S~����d�
               �p�k�U�;ֿ�v�Am��H��tɘ�3�ߘ�(ǟ�E'
                                             ���'��:��uP�ע��������g�
!�'�
    t��!P���
            p

# el archivo no es legible
# sting nos permite listar las cadenas de caracteres imprimibles en ficheros

bandit9@bandit:~$ strings data.txt
Z/,_
WW"&8
2Qk)
xWa_
x?Xn
//M$
;yzEt!
WpU~e

#
bandit9@bandit:~$ strings data.txt | grep "====="
========== the*2i"4
========== password
Z)========== is
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk


bandit9@bandit:~$ strings data.txt | grep "=====" | tail -n 1
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```

Ejercicio de bucle
```bash
root@pc:~# touch bucle.sh
root@pc:~# chmod +x !$
chmod +x bucle.sh
root@pc:~#

# El !$ es una forma de referenciar (NO COMANDO)  si no el ultimo argumento del comando previamente ejecutado.

root@pc:~# cat bucle.sh
#!/bin/bash

cat /etc/passwd | while read line; do
	echo "Estamos Aquí: $line"
done

# La forma optimizada del while read line
root@pc:~# cat bucle.sh
#!/bin/bash

while read line; do
	echo "Estamos Aquí: $line"
done < /etc/passwd
root@pc:~#

# las variables en la asignación no deben contenere estacion entre el =.
# Ejemplo var=1

root@pc:~# cat bucle.sh
#!/bin/bash

contador=1

while read line; do
	echo "Línea $contador: $line"
	let contador+=1 # contador = contador +1
done < /etc/passwd
root@pc:~#


# todo lo realizado en un script se puede hacer en un wile liner
bandit9@bandit:~$ strings data.txt | grep "====" | while read line; do echo $line; done
========== the*2i"4
========== password
Z)========== is
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

bandit9@bandit:~$ strings data.txt | grep "====" | while read line; do echo "Hola: $line"; done
Hola: ========== the*2i"4
Hola: ========== password
Hola: Z)========== is
Hola: &========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
bandit9@bandit:~$

bandit9@bandit:~$ contador=1; strings data.txt | grep "====" | while read line; do echo "Linea $contador: $line"; let contador+=1; done
Linea 1: ========== the*2i"4
Linea 2: ========== password
Linea 3: Z)========== is
Linea 4: &========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

bandit9@bandit:~$ contador=1; strings data.txt | grep "====" | while read line; do echo "Linea $contador: $line"; let contador+=1; done | awk 'NR==4'
Linea 4: &========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
bandit9@bandit:~$
```

## bandit10
```bash
# la passwor esta encriptada en base64

bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg==
bandit10@bandit:~$

# Ejemplo para codificar el base64
root@pc:~# echo "hola que tal" | base64
aG9sYSBxdWUgdGFsCg==
root@pc:~#

# decodificar   -d
root@pc:~# echo "hola que tal" | base64 | base64 -d
hola que tal

bandit10@bandit:~$ cat data.txt | base64 -d
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
bandit10@bandit:~$

# comando tr
bandit10@bandit:~$ cat data.txt | base64 -d | tr ' ' '\n'
The
password
is
IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
bandit10@bandit:~$

bandit10@bandit:~$ cat data.txt | base64 -d | sed 's/ /\n/g'
The
password
is
IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

root@pc:~# cat /etc/passwd | head -n 1
root:x:0:0:root:/root:/bin/bash
root@pc:~# cat /etc/passwd | head -n 1 | tr 'r' 'o'
ooot:x:0:0:ooot:/ooot:/bin/bash
root@pc:~#

# no es que reemplaza palabras Ejmeplo: tr 'root' 'jjvargas'
# tr reemplazara la r->j  o->j o->v t->a  la o queda con la ultima asignación

root@pc:~# cat /etc/passwd | head -n 1
root:x:0:0:root:/root:/bin/bash
root@pc:~# cat /etc/passwd | head -n 1 | tr 'r' 'o'
ooot:x:0:0:ooot:/ooot:/bin/bash
root@pc:~# cat /etc/passwd | head -n 1 | tr 'root' 'jjvargass'
jvva:x:0:0:jvva:/jvva:/bin/bash
```
## bandit11
```bash
# The password for the next level is stored in the file data.txt,
# where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions


bandit11@bandit:~$ cat data.txt
Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh
bandit11@bandit:~$ cat data.txt  | tr '[G-ZA-Fg-za-f]' '[T-ZA-St-za-s]'
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
bandit11@bandit:~$

# traer el ultimo parametro
bandit11@bandit:~$ cat data.txt  | tr '[G-ZA-Fg-za-f]' '[T-ZA-St-za-s]' | awk 'NF{print $NF}'
5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
bandit11@bandit:~$
```

## bandit12
```bash
bandit12@bandit:~$ cat data.txt
00000000: 1f8b 0808 0650 b45e 0203 6461 7461 322e  .....P.^..data2.
00000010: 6269 6e00 013d 02c2 fd42 5a68 3931 4159  bin..=...BZh91AY
00000020: 2653 598e 4f1c c800 001e 7fff fbf9 7fda  &SY.O...........
00000030: 9e7f 4f76 9fcf fe7d 3fff f67d abde 5e9f  ..Ov...}?..}..^.
00000040: f3fe 9fbf f6f1 feee bfdf a3ff b001 3b1b  ..............;.
00000050: 5481 a1a0 1ea0 1a34 d0d0 001a 68d3 4683  T......4....h.F.
00000060: 4680 0680 0034 1918 4c4d 190c 4000 0001  F....4..LM..@...
00000070: a000 c87a 81a3 464d a8d3 43c5 1068 0346  ...z..FM..C..h.F
00000080: 8343 40d0 3400 0340 66a6 8068 0cd4 f500  .C@.4..@f..h....
00000090: 69ea 6800 0f50 68f2 4d00 680d 06ca 0190  i.h..Ph.M.h.....
000000a0: 0000 69a1 a1a0 1ea0 194d 340d 1ea1 b280  ..i......M4.....
000000b0: f500 3406 2340 034d 3400 0000 3403 d400  ..4.#@.M4...4...
000000c0: 1a07 a832 3400 f51a 0003 43d4 0068 0d34  ...24.....C..h.4
000000d0: 6868 f51a 3d43 2580 3e58 061a 2c89 6bf3  hh..=C%.>X..,.k.
000000e0: 0163 08ab dc31 91cd 1747 599b e401 0b06  .c...1...GY.....
000000f0: a8b1 7255 a3b2 9cf9 75cc f106 941b 347a  ..rU....u.....4z
00000100: d616 55cc 2ef2 9d46 e7d1 3050 b5fb 76eb  ..U....F..0P..v.
00000110: 01f8 60c1 2201 33f0 0de0 4aa6 ec8c 914f  ..`.".3...J....O


# hexadecimal
root@pc:~# echo "hola que tal" | xxd
00000000: 686f 6c61 2071 7565 2074 616c 0a         hola que tal.

root@pc:~# echo "hola que tal" | xxd | xxd -r
hola que tal
root@pc:~#
```

Trabajar el fichero data de forma local copiando la salida del cat en un archivo local
```bash
root@pc:~# nano data.hex

# primer saber que es
root@pc:~# xxd -r data.hex
P�^data2.bin=��BZh91AY&SY�O����ڞOv���}?��}��^���������ߣ��;�����4���h�F�F��4LM
                                                                             @��z��FM��C�hF�C@�4@f��h
4hh��=C%�>X�,�k���1��GY��                                                                            ��i�hPh�Mh
�J�쌑Oϊ��{RBp�Qix�Y�Z!d��j�(�搿ݳ��/��A�#�A�F��0P��v��`�"3�

                                          ��d�bX?��z��2��<��A �n}
5(3A��
      wO�R����6�XS{�
��9?L�P�yB��=z�m?�L�Nt*�7{qP��̜�%"�w9�qm4�� N3�6���K��H䋑[��}!

# redireccionamos a un arhcivo
root@pc:~# xxd -r data.hex > data

# saber el numero magico
root@pc:~# file data
data: gzip compressed data, was "data2.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix, original size modulo 2^32 573
root@pc:~#

# renombramos acorde a su tipo
root@pc:~# mv data data.gzip
```

Trabajar con 7z

Listar
```bash
# recomendación - no es necesario utilizar gunzip, tar -xf, bzip2 = hay un monton de tipos de comprimidos
# Pero 7z ES UNIVERSAL, permite listar el contenido de un comprimido
root@pc:~# 7z l data.gzip

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,4 CPUs Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz (406E3),ASM,AES-NI)

Scanning the drive for archives:
1 file, 606 bytes (1 KiB)

Listing archive: data.gzip

--
Path = data.gzip
Type = gzip
Headers Size = 20

   Date      Time    Attr         Size   Compressed  Name
------------------- ----- ------------ ------------  ------------------------
2020-05-07 13:14:30 .....          573          606  data2.bin
------------------- ----- ------------ ------------  ------------------------
2020-05-07 13:14:30                573          606  1 files
root@pc:~#
```

Extraer
```bash
# para extraer con el parametro x
root@pc:~# 7z x data.gzip

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,4 CPUs Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz (406E3),ASM,AES-NI)

Scanning the drive for archives:
1 file, 606 bytes (1 KiB)

Extracting archive: data.gzip
--
Path = data.gzip
Type = gzip
Headers Size = 20

Everything is Ok

Size:       573
Compressed: 606
root@pc:~# ls
data2.bin  data.gzip  data.hex
```

La Salida de la Descompresión, da nuevamente un data2.bin que es un bzip2
```bash
# revisamos data.bin con file
root@pc:~# file data2.bin
data2.bin: bzip2 compressed data, block size = 900k
root@pc:~#

root@pc:~# 7z l data2.bin

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,4 CPUs Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz (406E3),ASM,AES-NI)

Scanning the drive for archives:
1 file, 573 bytes (1 KiB)

Listing archive: data2.bin

--
Path = data2.bin
Type = bzip2

   Date      Time    Attr         Size   Compressed  Name
------------------- ----- ------------ ------------  ------------------------
                    .....                            data2
------------------- ----- ------------ ------------  ------------------------
                                                573  1 files
root@pc:~#
```

Como vemos esto ha sido comrpimido multiple veces
```bash
# vamos a crear un script para realizar esta operción multiples veces
root@pc:~# touch decompresor.sh
root@pc:~# chmod +x !$
chmod +x decompresor.sh
root@pc:~#
```

Obtener el nombre del siguietne comprimido
```bash
root@pc:~# 7z l data.gzip

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,4 CPUs Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz (406E3),ASM,AES-NI)

Scanning the drive for archives:
1 file, 606 bytes (1 KiB)

Listing archive: data.gzip

--
Path = data.gzip
Type = gzip
Headers Size = 20

   Date      Time    Attr         Size   Compressed  Name
------------------- ----- ------------ ------------  ------------------------
2020-05-07 13:14:30 .....          573          606  data2.bin
------------------- ----- ------------ ------------  ------------------------
2020-05-07 13:14:30                573          606  1 files

# lo que nos interesa el la columna del Name

root@pc:~# 7z l data.gzip | grep "Name"
   Date      Time    Attr         Size   Compressed  Name

# con el parametro -A 2  listeme dos lineas abajo desde el merch que encontrantes
root@pc:~# 7z l data.gzip | grep "Name" -A 2
   Date      Time    Attr         Size   Compressed  Name
------------------- ----- ------------ ------------  ------------------------
2020-05-07 13:14:30 .....          573          606  data2.bin

# con -B lineas por encima
root@pc:~# 7z l data.gzip | grep "Name" -B 2
Headers Size = 20

   Date      Time    Attr         Size   Compressed  Name

# dos por debajo y dos por encima
root@pc:~# 7z l data.gzip | grep "Name" -C 2
Headers Size = 20

   Date      Time    Attr         Size   Compressed  Name
------------------- ----- ------------ ------------  ------------------------
2020-05-07 13:14:30 .....          573          606  data2.bin

# traemos la ultima linea
root@pc:~# 7z l data.gzip | grep "Name" -C 2 | tail -n 1
2020-05-07 13:14:30 .....          573          606  data2.bin

# ultimo argumento de la salida
root@pc:~# 7z l data.gzip | grep "Name" -C 2 | tail -n 1 | awk 'NF{print $NF}'
data2.bin

# cambianos nombre del primer archivo comrpimido
root@pc:~# mv data.gzip content.gzip
```

Iniciamos con el scritp   
(Paso 1)
```bash
# crear script
root@pc:~# cat decompresor.sh
#!/bin/bash

name_compressed=$(7z l content.gzip | grep "Name" -A 2 | tail -n 1 | awk 'NF{print $NF}')

echo $name_compressed
```

(Paso 2) Descomprimimos el archivo y
```bash
# ahora descomprimimos el archivo y controlamos la salida
root@pc:~# cat decompresor.sh
#!/bin/bash

name_compressed=$(7z l content.gzip | grep "Name" -A 2 | tail -n 1 | awk 'NF{print $NF}')

7z x content.gzip


root@pc:~#


# ejecutamos
root@pc:~# ./decompresor.sh

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,4 CPUs Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz (406E3),ASM,AES-NI)

Scanning the drive for archives:
1 file, 606 bytes (1 KiB)

Extracting archive: content.gzip
--
Path = content.gzip
Type = gzip
Headers Size = 20

Everything is Ok

Size:       573
Compressed: 606
root@pc:~#
```

(Paso 3) Controlar el stderr stdout
```bash
# pero el stderr stdout no nos intereza mostar en el script
root@pc:~# cat decompresor.sh
#!/bin/bash

name_compressed=$(7z l content.gzip | grep "Name" -A 2 | tail -n 1 | awk 'NF{print $NF}')

7z x content.gzip > /dev/null 2>&1

# ejecutamos

root@pc:~# ./decompresor.sh
root@pc:~#
```

Bucle
```bash
# se crea bucle infinito y se controla el exit con el codigo de estado $?
# cuando es correcto da 0
# cuando es erroneo da 1

root@pc:~# cat decompresor.sh
#!/bin/bash

name_compressed=$(7z l content.gzip | grep "Name" -A 2 | tail -n 1 | awk 'NF{print $NF}')
7z x content.gzip > /dev/null 2>&1

while true; do
	7z l $name_compressed > /dev/null 2>&1
	if[ "$(echo $?)" == "0" ]; then
		decompressed_next=$(7z l $name_compressed | grep "Name" -A 2 | tail -n 1 | awk 'NF{print $NF}')
		7z x $name_compressed  > /dev/null 2>&1 && name_compressed=$decompressed_next
	else
		exit 0
	fi
done
root@pc:~#
```





```bash

```

```bash

```


```bash

```

```bash

```
