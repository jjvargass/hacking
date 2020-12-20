# Bash

Se realizara los ejercicio se [overthewire](https://overthewire.org/wargames/) capitulo de Bandit

## bandit0
The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

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
The password for the next level is stored in a file called - located in the home directory
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
The password for the next level is stored in a file called spaces in this filename located in the home directory
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
The password for the next level is stored in a hidden file in the inhere directory.
```bash
bandit3@bandit:~$ ls -la inhere/
total 12
drwxr-xr-x 2 root    root    4096 May  7  2020 .
drwxr-xr-x 3 root    root    4096 May  7  2020 ..
-rw-r----- 1 bandit4 bandit3   33 May  7  2020 .hidden
```
### find
```bash
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
```
### column 
```bash
# para ordenar
bandit3@bandit:~$ find . -type f -printf "%f\t%p\t%u\t%g\t%m\n" | column -t
.hidden       ./inhere/.hidden  bandit4  bandit3  640
.bashrc       ./.bashrc         root     root     644
.profile      ./.profile        root     root     644
.bash_logout  ./.bash_logout    root     root     644
```
obtenemos la flag
```bash
bandit3@bandit:~$ cat inhere/.hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

### xargs
xargs es util para de forma paralela ejecutar comandos sobre el output de un comando ejecutado anteriormente.
```bash
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
The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.
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
```

### file 
```bash
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

# comando $()
bandit4@bandit:~$ cat $(find . -name -file07)  
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

#### Ejemplo de Magic Number
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
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
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
```

#### find parametros
```bash
# Para buscar archiov: -type f
# Que sea readable entonces: -readable Tambien exitse las opciones (-executable  -writable)
# -size filtar por el tamaño, para especificar bytes agregasr "c"
bandit5@bandit:~$ find . -type f -readable  -size 1033c
./inhere/maybehere07/.file2

# se agrega xargas cat para leer el archivo filtrado
bandit5@bandit:~$ find . -type f -readable  -size 1033c | xargs cat
DXjZPULLxYr17uwoI01bNLQbtFemEgo7

# este archivo contine espacion en blanco y saltos de linea. para limpiar agragamos un xargs solo
bandit5@bandit:~$ find . -type f -readable  -size 1033c | xargs cat  | xargs
DXjZPULLxYr17uwoI01bNLQbtFemEgo7

# de la misma forma como se limpio el archio utilizaremos  tr opcion -d para eliminar
bandit5@bandit:~$ find . -type f -readable  -size 1033c | xargs cat  | tr -d ' '
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```

### sed
sed 's/argumento/aloqueloqueremosconvertir'  
sed 's/root/miusuario/' => cambie root en el archivo por miusuario
```bash
# sed 's/^ *//'
# s/^ *           reemplace todo lo que inicie con espacio en blanco y cualquier cosa
# //              cambielo por nada
bandit5@bandit:~$ find . -type f -readable ! -executable  -size 1033c | xargs cat  | sed 's/^ *//'
DXjZPULLxYr17uwoI01bNLQbtFemEgo7

# ^     todo lo que inicia
# \s    espacions
# /d    vacio
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

### head y tail
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

### sed
```bash
root@pc:~# cat file.txt | head -n 1
root:x:0:0:root:/root:/bin/bash

# Sustitución aplicacio en el primer coincidencia
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

# para especificar con expreciones regulares las que comiencen con r
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
```

Lo que nos interesa el la columna del Name
```bash
root@pc:~# 7z l data.gzip | grep "Name"
   Date      Time    Attr         Size   Compressed  Name
```

Con el parametro -A 2  listeme dos lineas abajo desde el merch que encontrantes
```bash
root@pc:~# 7z l data.gzip | grep "Name" -A 2
   Date      Time    Attr         Size   Compressed  Name
------------------- ----- ------------ ------------  ------------------------
2020-05-07 13:14:30 .....          573          606  data2.bin
```

Con -B lineas por encima
```bash
root@pc:~# 7z l data.gzip | grep "Name" -B 2
Headers Size = 20

   Date      Time    Attr         Size   Compressed  Name
```

Dos por debajo y dos por encima
```bash
root@pc:~# 7z l data.gzip | grep "Name" -C 2
Headers Size = 20

   Date      Time    Attr         Size   Compressed  Name
------------------- ----- ------------ ------------  ------------------------
2020-05-07 13:14:30 .....          573          606  data2.bin
```

Traemos la ultima linea
```bash
root@pc:~# 7z l data.gzip | grep "Name" -C 2 | tail -n 1
2020-05-07 13:14:30 .....          573          606  data2.bin

# ultimo argumento de la salida
root@pc:~# 7z l data.gzip | grep "Name" -C 2 | tail -n 1 | awk 'NF{print $NF}'
data2.bin
```

Cambianos nombre del primer archivo comrpimido
```bash
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
Ultimos retoques en los nombre e imprimiendo el ultimo archivo
```bash
root@pc:~# cat decompresor.sh
#!/bin/bash

name_decompressed=$(7z l content.gzip | grep "Name" -A 2 | tail -n 1 | awk 'NF{print $NF}')
7z x content.gzip > /dev/null 2>&1

while true; do
	7z l $name_decompressed > /dev/null 2>&1
	if [ "$(echo $?)" == "0" ]; then
		decompressed_next=$(7z l $name_decompressed | grep "Name" -A 2 | tail -n 1 | awk 'NF{print $NF}')
		7z x $name_decompressed  > /dev/null 2>&1 && name_decompressed=$decompressed_next
	else
		cat $name_decompressed; rm data* 2>/dev/null
		exit 1
	fi
done

# -- Ejecutando
root@pc:~# ./decompresor.sh
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
root@pc:~#
```

## bandit13
```bash
bandit13@bandit:~$ cat sshkey.private
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAxkkOE83W2cOT7IWhFc9aPaaQmQDdgzuXCv+ppZHa++buSkN+
gg0tcr7Fw8NLGa5+Uzec2rEg0WmeevB13AIoYp0MZyETq46t+jk9puNwZwIt9XgB
ZufGtZEwWbFWw/vVLNwOXBe4UWStGRWzgPpEeSv5Tb1VjLZIBdGphTIK22Amz6Zb
ThMsiMnyJafEwJ/T8PQO3myS91vUHEuoOMAzoUID4kN0MEZ3+XahyK0HJVq68KsV
ObefXG1vvA3GAJ29kxJaqvRfgYnqZryWN7w3CHjNU4c/2Jkp+n8L0SnxaNA+WYA7
jiPyTF0is8uzMlYQ4l1Lzh/8/MpvhCQF8r22dwIDAQABAoIBAQC6dWBjhyEOzjeA
J3j/RWmap9M5zfJ/wb2bfidNpwbB8rsJ4sZIDZQ7XuIh4LfygoAQSS+bBw3RXvzE
pvJt3SmU8hIDuLsCjL1VnBY5pY7Bju8g8aR/3FyjyNAqx/TLfzlLYfOu7i9Jet67
xAh0tONG/u8FB5I3LAI2Vp6OviwvdWeC4nOxCthldpuPKNLA8rmMMVRTKQ+7T2VS
nXmwYckKUcUgzoVSpiNZaS0zUDypdpy2+tRH3MQa5kqN1YKjvF8RC47woOYCktsD
o3FFpGNFec9Taa3Msy+DfQQhHKZFKIL3bJDONtmrVvtYK40/yeU4aZ/HA2DQzwhe
ol1AfiEhAoGBAOnVjosBkm7sblK+n4IEwPxs8sOmhPnTDUy5WGrpSCrXOmsVIBUf
laL3ZGLx3xCIwtCnEucB9DvN2HZkupc/h6hTKUYLqXuyLD8njTrbRhLgbC9QrKrS
M1F2fSTxVqPtZDlDMwjNR04xHA/fKh8bXXyTMqOHNJTHHNhbh3McdURjAoGBANkU
1hqfnw7+aXncJ9bjysr1ZWbqOE5Nd8AFgfwaKuGTTVX2NsUQnCMWdOp+wFak40JH
PKWkJNdBG+ex0H9JNQsTK3X5PBMAS8AfX0GrKeuwKWA6erytVTqjOfLYcdp5+z9s
8DtVCxDuVsM+i4X8UqIGOlvGbtKEVokHPFXP1q/dAoGAcHg5YX7WEehCgCYTzpO+
xysX8ScM2qS6xuZ3MqUWAxUWkh7NGZvhe0sGy9iOdANzwKw7mUUFViaCMR/t54W1
GC83sOs3D7n5Mj8x3NdO8xFit7dT9a245TvaoYQ7KgmqpSg/ScKCw4c3eiLava+J
3btnJeSIU+8ZXq9XjPRpKwUCgYA7z6LiOQKxNeXH3qHXcnHok855maUj5fJNpPbY
iDkyZ8ySF8GlcFsky8Yw6fWCqfG3zDrohJ5l9JmEsBh7SadkwsZhvecQcS9t4vby
9/8X4jS0P8ibfcKS4nBP+dT81kkkg5Z5MohXBORA7VWx+ACohcDEkprsQ+w32xeD
qT1EvQKBgQDKm8ws2ByvSUVs9GjTilCajFqLJ0eVYzRPaY6f++Gv/UVfAPV4c+S0
kAWpXbv5tbkkzbS0eaLPTKgLzavXtQoTtKwrjpolHKIHUz6Wu+n4abfAIRFubOdN
/+aLoRQ0yBDRbdXMsZN/jvY44eM+xRLdRVyMmdPtP8belRi2E2aEzA==
-----END RSA PRIVATE KEY-----
```

```bash
bandit13@bandit:~$ file sshkey.private
sshkey.private: PEM RSA private key
```
### Uso de ssh
Para practicar de forma local
habilitamos #PermitRootLogin prohibit-password
descomentamos y le asignanos yes

```bash
root@pc:~# nano /etc/ssh/sshd_config

#PermitRootLogin prohibit-password
# lo dejamos ahora
PermitRootLogin yes
```
Gestion del servicio ssh
```bash
root@pc:~# service ssh start
root@pc:~# service ssh restart
root@pc:~# service ssh status
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/lib/systemd/system/ssh.service; disabled; vendor preset: disabled)
     Active: active (running) since Wed 2020-12-16 09:49:17 -05; 5s ago
       Docs: man:sshd(8)
             man:sshd_config(5)
    Process: 12452 ExecStartPre=/usr/sbin/sshd -t (code=exited, status=0/SUCCESS)
   Main PID: 12453 (sshd)
      Tasks: 1 (limit: 14165)
     Memory: 1.3M
     CGroup: /system.slice/ssh.service
             └─12453 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups

Dec 16 09:49:17 pc systemd[1]: Starting OpenBSD Secure Shell server...
Dec 16 09:49:17 pc sshd[12453]: Server listening on 0.0.0.0 port 22.
Dec 16 09:49:17 pc sshd[12453]: Server listening on :: port 22.
Dec 16 09:49:17 pc systemd[1]: Started OpenBSD Secure Shell server.
root@pc:~#
```

```bash
root@pc:~/.ssh# ls
known_hosts

# Crear ssh
root@pc:~/.ssh# ssh-keygen

# listar los archivos que se ha creado
# id_rsa      => Es la clave privada
# id_rsa.pub  => Es la clave publica
root@pc:~/.ssh# ls
id_rsa	id_rsa.pub  known_hosts
```

Hay dos concepto a tener en cuenta a la hora de acceder a una maquina por ssh, utilizando un fichero de identidad autorizado.

Opcion 1:   
Para que los usuarios no deban proporcinar la contraseña cuando se conectan al servidor ssh  
La clave publica de cada uno de estos usuarios se debera alojar en el servidor ssh en el correspondiente directorio `~/.ssh/` de usuario para conectar y guardar como `authorized_keys`

```bash
root@pc:~/.ssh# cp id_rsa.pub authorized_keys
root@pc:~/.ssh# ls
authorized_keys  id_rsa  id_rsa.pub  known_hosts
root@pc:~/.ssh#
```

Comprobar de namera local
```bash
root@pc:~/.ssh# ssh root@localhost
root@pc:~#

# verificar
root@pc:~# whoami
root
root@pc:~# lsof -i:22
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
sshd    12453 root    3u  IPv4 123857      0t0  TCP *:ssh (LISTEN)
sshd    12453 root    4u  IPv6 123859      0t0  TCP *:ssh (LISTEN)
ssh     57807 root    3u  IPv6 200682      0t0  TCP localhost:54444->localhost:ssh (ESTABLISHED)
sshd    57808 root    4u  IPv6 202075      0t0  TCP localhost:ssh->localhost:54444 (ESTABLISHED)
root@pc:~# exit
logout
Connection to localhost closed.
```

Si se elimina el archivo `authorized_keys` ahora solicitará contraseña
```bash
root@pc:~/.ssh# rm authorized_keys
root@pc:~/.ssh# ssh root@localhost
root@localhost's password:
```
Opcion 2:   
La forma que se implementara para el bandit13   
Con el comando `ssh-copy-id` convertirlo el  fichero `id_rsa` en un fichero de identidad autorizado.
pasandole al comando el usuario@ip_servidor_ssh
```bash
root@pc:~/.ssh# ls
id_rsa	id_rsa.pub  known_hosts

# usuario: root
# maquina: localhost
root@pc:~/.ssh# ssh-copy-id -i id_rsa root@localhost
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
/usr/bin/ssh-copy-id: 260: EOF: not found

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'root@localhost'"
and check to make sure that only the key(s) you wanted were added.

# listamos archivos
root@pc:~/.ssh# ls
authorized_keys  id_rsa  id_rsa.pub  known_hosts
```

Es el archivo id_rsa el que se les comparte a los usuario para que se conecte.  
Para conectarse un usuario serial de la siguietne manera
```bash
authorized_keys  id_rsa  id_rsa.pub  known_hosts
root@pc:~/.ssh# ssh -i id_rsa root@localhost
root@pc:~#
```
Solución del bandit13

```bash
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost
bandit14@bandit:~$ whoami
bandit14
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

bandit14@bandit:~$ exit
logout
Connection to localhost closed.
bandit13@bandit:~$ exit
```
### lsof y pwdx

lsof => te permite listar los procesos que estan corriendo en tu sistema por un puerto especifico
```bash
root@pc:~# service apache2 start

root@pc:~# lsof -i:80
COMMAND   PID      USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
chrome   2153 jjvargass   65u  IPv6 259403      0t0  TCP localhost:43936->localhost:http (ESTABLISHED)
apache2 59106      root    4u  IPv6 251490      0t0  TCP *:http (LISTEN)
apache2 59113  www-data    4u  IPv6 251490      0t0  TCP *:http (LISTEN)
apache2 59114  www-data    4u  IPv6 251490      0t0  TCP *:http (LISTEN)
apache2 59115  www-data    4u  IPv6 251490      0t0  TCP *:http (LISTEN)
apache2 59116  www-data    4u  IPv6 251490      0t0  TCP *:http (LISTEN)
apache2 59117  www-data    4u  IPv6 251490      0t0  TCP *:http (LISTEN)
apache2 59118  www-data    4u  IPv6 251490      0t0  TCP *:http (LISTEN)
apache2 59398  www-data    4u  IPv6 251490      0t0  TCP *:http (LISTEN)
```
revisar proceso del navegador
```bash
root@pc:~# netstat -nat | grep "443"
tcp        0      0 192.168.31.114:56018    142.250.78.165:443      ESTABLISHED
tcp      130      0 192.168.31.114:47094    142.250.78.170:443      CLOSE_WAIT
tcp        0      0 192.168.31.114:53606    172.217.172.10:443      ESTABLISHED
tcp        0      0 192.168.31.114:54716    142.250.78.67:443       ESTABLISHED
tcp        0      0 192.168.31.114:59058    173.194.216.188:443     ESTABLISHED
tcp        0      0 192.168.31.114:51096    157.240.6.53:443        ESTABLISHED
tcp        0      0 192.168.31.114:50714    172.217.28.110:443      ESTABLISHED
tcp        0      0 192.168.31.114:57288    142.250.78.78:443       ESTABLISHED

# El reemplazo de netstat es ahora ss
root@pc:~# ss | grep https
udp   ESTAB  0      0                                  192.168.31.114:49834       142.250.78.67:https        
udp   ESTAB  0      0                                  192.168.31.114:46082     172.217.193.189:https        
udp   ESTAB  0      0                                  192.168.31.114:38198       142.250.78.78:https        
tcp   ESTAB  0      0                                  192.168.31.114:43764     172.217.173.197:https        
tcp   ESTAB  0      0                                  192.168.31.114:54748       142.250.78.67:https        
tcp   ESTAB  0      0                                  192.168.31.114:54716       142.250.78.67:https        
tcp   ESTAB  0      0                                  192.168.31.114:59058     173.194.216.188:https        
tcp   ESTAB  0      0                                  192.168.31.114:56724       142.250.78.46:https        
tcp   ESTAB  0      0                                  192.168.31.114:51096        157.240.6.53:https        
tcp   ESTAB  0      0                                  192.168.31.114:56726       142.250.78.46:https        
mptcp ESTAB  0      0                                  192.168.31.114:43764     172.217.173.197:https        
mptcp ESTAB  0      0                                  192.168.31.114:54748       142.250.78.67:https        
mptcp ESTAB  0      0                                  192.168.31.114:54716       142.250.78.67:https        
mptcp ESTAB  0      0                                  192.168.31.114:59058     173.194.216.188:https        
mptcp ESTAB  0      0                                  192.168.31.114:56724       142.250.78.46:https        
mptcp ESTAB  0      0                                  192.168.31.114:51096        157.240.6.53:https        
mptcp ESTAB  0      0                                  192.168.31.114:56726       142.250.78.46:https
```
Podemos ver los servicios corriedno con lsof pero con el PID y con el comando `pwdx` podemos obtener la ruta donde se ejecuta el servicio
```bash
root@pc:~# lsof -i:22
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
sshd    58666 root    3u  IPv4 238912      0t0  TCP *:ssh (LISTEN)
sshd    58666 root    4u  IPv6 238914      0t0  TCP *:ssh (LISTEN)
root@pc:~# pwdx 58666
58666: /

# segundo ejemplo

root@pc:/home/jjvargass# nc -nlvp 4646
listening on [any] 4646 ...

root@pc:~# lsof -i:4646
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
nc      59764 root    3u  IPv4 273775      0t0  TCP *:4646 (LISTEN)
root@pc:~# pwdx 59764
59764: /home/jjvargass
```

## bandit14
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.
```bash
# se verifica que el puerto este abierto
bandit14@bandit:~$ echo '' > /dev/tcp/127.0.0.1/30000
# debuelve codigo de estado exitoso
bandit14@bandit:~$ echo $?
0
# con un puerto cerrado
bandit14@bandit:~$ echo '' > /dev/tcp/127.0.0.1/30123
-bash: connect: Connection refused
-bash: /dev/tcp/127.0.0.1/30123: Connection refused
bandit14@bandit:~$ echo $?
1
```
```bash
bandit14@bandit:~$ echo '' > /dev/tcp/127.0.0.1/30000 && echo "[*] Puerto abierto" || echo "[*] Puerto cerrado"
[*] Puerto abierto


bandit14@bandit:~$ echo '' > /dev/tcp/127.0.0.1/30123 && echo "[*] Puerto abierto" || echo "[*] Puerto cerrado"
-bash: connect: Connection refused
-bash: /dev/tcp/127.0.0.1/30123: Connection refused
[*] Puerto cerrado

# eviamos los errores al /dev/null
bandit14@bandit:~$ echo '' > /dev/tcp/127.0.0.1/30123 2>/dev/null && echo "[*] Puerto abierto" || echo "[*] Puerto cerrado"
-bash: connect: Connection refused
-bash: /dev/tcp/127.0.0.1/30123: Connection refused
[*] Puerto cerrado

# no funciona entonces bamos a intentar englovar todo el comando
bandit14@bandit:~$ bash -c "echo '' > /dev/tcp/127.0.0.1/30123" 2>/dev/null && echo "[*] Puerto abierto" || echo "[*] Puerto cerrado"
[*] Puerto cerrado

# enviamos la passwor al puerto
bandit14@bandit:~$ echo "4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e" | nc localhost 30000
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr

# otra forma
bandit14@bandit:~$ telnet localhost 30000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr

Connection closed by foreign host.
```

## bandit15
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.  
Si realizamos los mismos metodos del ejercicio anterior no dan resultado, por lo que la información viaja encriptada
```bash
bandit15@bandit:~$ echo "BfMYroe26WYalil77FoDi9qh59eK5xNr" | nc localhost  30001
bandit15@bandit:~$ telnet localhost 30001
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
BfMYroe26WYalil77FoDi9qh59eK5xNr
Connection closed by foreign host.
bandit15@bandit:~$
```
Con `openssl` podemos actuar como cliente `s_client`
```bash
bandit15@bandit:~$ openssl s_client -connect 127.0.0.1:30001
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIEDU18oTANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjAwNTA3MTgxNTQzWhcNMjEwNTA3MTgxNTQzWjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAK3CPNFR
FEypcqUa8NslmIMWl9xq53Cwhs/fvYHAvauyfE3uDVyyX79Z34Tkot6YflAoufnS
+puh2Kgq7aDaF+xhE+FPcz1JE0C2bflGfEtx4l3qy79SRpLiZ7eio8NPasvduG5e
pkuHefwI4c7GS6Y7OTz/6IpxqXBzv3c+x93TAgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBAC9uy1rF2U/OSBXbQJYuPuzT5mYwcjEEV0XwyiX1MFZbKUlyFZUw
rq+P1HfFp+BSODtk6tHM9bTz+p2OJRXuELG0ly8+Nf/hO/mYS1i5Ekzv4PL9hO8q
PfmDXTHs23Tc7ctLqPRj4/4qxw6RF4SM+uxkAuHgT/NDW1LphxkJlKGn
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: A9BCDB0DE60EC2777D06069A5BFCC506654347F2D5A733FC9C28753BF34E76DF
    Session-ID-ctx:
    Master-Key: E27DD4F50B6580CF4DE824F2FED9B41918FEB9C355F1C7E1E925314357A7564960317A8467604344CFE2B55EC369C98F
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - aa 02 e6 3a 2e 0b c8 5d-6f 54 4a 1b 5a e0 2c 0e   ...:...]oTJ.Z.,.
    0010 - 30 6b b7 42 d3 32 9d a6-6d dd 0b 7b c5 7f 27 62   0k.B.2..m..{..'b
    0020 - 73 98 b5 dc a6 92 17 22-a6 3b ee 09 25 63 0e 4d   s......".;..%c.M
    0030 - e4 f5 78 9d c6 33 c9 eb-40 54 67 fe bb 60 8b 35   ..x..3..@Tg..`.5
    0040 - f9 21 d4 66 4b 50 d8 ee-ac 39 a1 6c f5 03 d2 50   .!.fKP...9.l...P
    0050 - 2d b0 53 99 b0 88 d1 00-a7 3f 4a 95 f2 9e 0e 4f   -.S......?J....O
    0060 - 82 6b 47 59 db a6 7e 50-65 ab a5 99 08 5f 8c 23   .kGY..~Pe...._.#
    0070 - cb 2c 91 51 f8 ea 20 ec-e7 57 51 f0 c0 f0 8a 31   .,.Q.. ..WQ....1
    0080 - 4a e8 c8 de 6a cd d1 2c-01 13 6b ba 8b 14 58 4f   J...j..,..k...XO
    0090 - a6 68 11 7a 47 74 75 51-8c b4 e5 66 bf 44 0e 8c   .h.zGtuQ...f.D..

    Start Time: 1608147387
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
BfMYroe26WYalil77FoDi9qh59eK5xNr
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd

closed
```

## bandit16
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

```bash
bandit16@bandit:~$ nmap --open -T5 -v -n -p31000-32000 127.0.0.1

Starting Nmap 7.40 ( https://nmap.org ) at 2020-12-16 20:47 CET
Initiating Ping Scan at 20:47
Scanning 127.0.0.1 [2 ports]
Completed Ping Scan at 20:47, 0.00s elapsed (1 total hosts)
Initiating Connect Scan at 20:47
Scanning 127.0.0.1 [1001 ports]
Discovered open port 31691/tcp on 127.0.0.1
Discovered open port 31960/tcp on 127.0.0.1
Discovered open port 31518/tcp on 127.0.0.1
Discovered open port 31046/tcp on 127.0.0.1
Discovered open port 31790/tcp on 127.0.0.1
Completed Connect Scan at 20:47, 0.04s elapsed (1001 total ports)
Nmap scan report for 127.0.0.1
Host is up (0.00028s latency).
Not shown: 996 closed ports
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 0.10 seconds
```
Ahora de estos 5 puertos revisar cual esta hablando por ssh
```bash
bandit16@bandit:~$ openssl s_client -connect 127.0.0.1:31790
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIERpugdDANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjAxMjAzMTIyNTAyWhcNMjExMjAzMTIyNTAyWjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMeJ7q8+
/5v/Q0OcS1qrtLv1GSYrXx8tddEmigEkXjxt96mbA62A7XPH6QZe5vVv6yOuS2JO
AvtwxWXeb5lAkcR88pkvITjPa1QX+Q4LqNDpGs4evJDmBcX7NG8Sx9zFXChq5eRN
Mis7GMk/RtwGbniNei1heI96rg2t0mRbR1kRAgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBADYJu67M8KiVPJo1HZsO+TW4bRr8rtrEKdirbH3CUEsZo3Wx6/PP
C8w/rWjx7CnnjF4qrpZLFlZ2TY+/pNOIBhixCKS9MHZXVix4GAHP3BkUCExc1jE9
mp1AQwblNeka4fPVkIrHfrRZQRJr96wT+YejVQqenVX6cFF2xpkpD+Me
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 05C045E5583B3BE5D8F2DD0FEFF69DC2124FE40CAB5815DF77EF0C66D4363C17
    Session-ID-ctx:
    Master-Key: 87B37AF8579C7F7D2D3B2F5F91B7D6E59E01E71BF384D2F1F787C039BDAC64088B54D8DFF22E2E9CBEF5DFE1D9184841
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 71 44 15 26 06 51 98 56-4a 2f 37 3a 47 04 b9 e3   qD.&.Q.VJ/7:G...
    0010 - e7 66 02 25 ba c8 ca 47-e1 b4 db c9 d1 34 07 2e   .f.%...G.....4..
    0020 - ee a5 32 ee 70 4f 1a b2-94 1c 01 12 a1 25 7e 18   ..2.pO.......%~.
    0030 - 3b a5 c4 7f 80 06 ec ae-f5 fe c0 9f 85 fa 2d 83   ;.............-.
    0040 - b3 75 09 19 22 d2 ec eb-fd 12 36 5f ad 32 68 1f   .u..".....6_.2h.
    0050 - ca 34 83 ac 1d 47 aa f3-b4 57 65 5f ca 29 f9 c3   .4...G...We_.)..
    0060 - fa 4d 04 5f 24 18 f5 49-40 46 1f 6a be 86 e6 a4   .M._$..I@F.j....
    0070 - 80 3a 1a 13 09 52 46 3a-b5 4c 9b 60 08 a9 ff 54   .:...RF:.L.`...T
    0080 - 8d 6d d3 7b 32 64 66 db-09 5f 42 ed db e7 69 a6   .m.{2df.._B...i.
    0090 - f5 28 53 ee d6 60 eb d3-ec f6 c5 26 3a 97 37 4f   .(S..`.....&:.7O

    Start Time: 1608148240
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
cluFn7wTiGryunymYOu4RcffSxQluehd
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

closed
```
Ha proporcionado llave privada
```bash
# creadmos directorio temporal
bandit16@bandit:~$ mktemp -d
/tmp/tmp.T3nRBubidN
bandit16@bandit:~$ cd /tmp/tmp.T3nRBubidN
bandit16@bandit:/tmp/tmp.T3nRBubidN$

# copiammos la llave que se nos porporcionó
bandit16@bandit:/tmp/tmp.T3nRBubidN$ nano id_rsa

# Asignamos correctos permisos
bandit16@bandit:/tmp/tmp.T3nRBubidN$ chmod 600 id_rsa

# ahora nos conectamos por ssh con bandit17
bandit16@bandit:/tmp/tmp.T3nRBubidN$ ssh -i id_rsa bandit17@localhost

# obtenemos la contraseña de bandit17
bandit17@bandit:~$ cat /etc/bandit_pass/bandit17
xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn
```

## bandit17
There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

```bash
bandit17@bandit:~$ ls
passwords.new  passwords.old

bandit17@bandit:~$ cat passwords.new | wc -l
100
bandit17@bandit:~$ cat passwords.old | wc -l
100
```
listar las diferencias entre los archivos
```bash
bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< w0Yfolrc5bwjS4qw5mq1nnQi6mF03bii
---
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
```
### scripting de bash implementación
```bash
root@pc:~# cd /dev/shm
root@pc:/dev/shm#

# crear script
root@pc:/dev/shm# touch procmon.sh
root@pc:/dev/shm# chmod +x procmon.sh
```
Script para monitorizar los procesos del sistema
```bash
#!/bin/bash
old_process=$(ps -eo command)
while true; do
        new_process=$(ps -eo command)
        diff <(echo "$old_process") <(echo "$new_process") | grep -v -E "procmon|command"
        old_process=$new_process
done
```
Ejecutamos
```bash
root@pc:/dev/shm# ./procmon.sh
27c27
< [kworker/3:1-events_freezable]
---
> [kworker/3:1-events]
84c84
< [kworker/u9:2+i915_flip]
---
> [kworker/u9:2-i915_flip]
47c47
< [kworker/u9:0+i915_flip]
---
```

# bandit18
The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220
Byebye !
Connection to bandit.labs.overthewire.org closed.
```
Lo malo de la bashrc es que cualquier comando o acción que tenga definido se ba a ejecutar despues que te conectes pero hay un margen de tiempo.  
A continuacion alcanzamos a ejecutar whoami
```bash
jjvargass@pc  ~  ssh bandit18@bandit.labs.overthewire.org -p 2220 whoami
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password:
bandit18
```
Nos podemos aprobechar de esto para definir una bash
```bash
jjvargass@pc  ~  ssh bandit18@bandit.labs.overthewire.org -p 2220 bash  
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password:
whoami
bandit18
pwd
/home/bandit18
```
Existe una utilidad para decier al ssh que no lea el bashrc
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 "bash --norc"
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password:
ls
readme
cat readme
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```

## bandit19
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.
```bash
bandit19@bandit:~$ ls
bandit20-do

# tiene permisos setuid, quiere decir que lo puedo ejecutar de forma temporal como el usuario propietario "como bandit20"
bandit19@bandit:~$ ls -l
total 8
-rwsr-x--- 1 bandit20 bandit19 7296 May  7  2020 bandit20-do
```
Ejecutar
```bash
bandit19@bandit:~$ ./bandit20-do
Run a command as another user.
  Example: ./bandit20-do id

# solicita argumento o comando
bandit19@bandit:~$ ./bandit20-do  whoami
bandit20
bandit19@bandit:~$ ./bandit20-do  id
uid=11019(bandit19) gid=11019(bandit19) euid=11020(bandit20) groups=11019(bandit19)

# abrir fichero
bandit19@bandit:~$ ./bandit20-do "cat /etc/bandit_pass/bandit20"
env: ‘cat /etc/bandit_pass/bandit20’: No such file or directory

# con sh atiende a suid
bandit19@bandit:~$ ./bandit20-do sh
$ whoami
bandit20

# con bash no atiende el suid
bandit19@bandit:~$ ./bandit20-do bash
bash-4.4$ whoami
bandit19

# para evitar el problema, desde la bash para que atienda el suid por medidas de proteccion se le asigan el parametro -p
bandit19@bandit:~$ ./bandit20-do bash -p
bash-4.4$ whoami
bandit20
bandit19@bandit:~$ ./bandit20-do bash -p
bash-4.4$ whoami
bandit20
bash-4.4$ cat /etc/bandit_pass/bandit20
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```

## bandit20
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

```bash
bandit20@bandit:~$ ls -l
total 12
-rwsr-x--- 1 bandit21 bandit20 12088 May  7  2020 suconnect
```
Se debe realizar dos conexiones
bash 1
```bash
bandit20@bandit:~$ nc -nlvp 5757
listening on [any] 5757 ...
```

bash 2
```bash
bandit20@bandit:~$ ./suconnect
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.

# ejecutamos con el puerto que esta escuchando con nc 5757
# luego suministramos la contraseña del bandit20
bandit20@bandit:~$ nc -nlvp 5757
listening on [any] 5757 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 39790
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
```

## bandit21
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.
```bash
bandit21@bandit:~$ ls -l /etc/cron.d/
total 24
-rw-r--r-- 1 root root  62 May 14  2020 cronjob_bandit15_root
-rw-r--r-- 1 root root  62 Jul 11 15:56 cronjob_bandit17_root
-rw-r--r-- 1 root root 120 May  7  2020 cronjob_bandit22
-rw-r--r-- 1 root root 122 May  7  2020 cronjob_bandit23
-rw-r--r-- 1 root root 120 May 14  2020 cronjob_bandit24
-rw-r--r-- 1 root root  62 May 14  2020 cronjob_bandit25_root

bandit21@bandit:~$ cat /etc/cron.d/cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null

# se esta ejecutando a intervalo de un minuto este archivo /usr/bin/cronjob_bandit22.sh, se revisará
bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

# entonces consultamos el directorio donde se esta guardando la contraseña
bandit21@bandit:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```

## bandit22
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

```bash
bandit22@bandit:~$ ls  -l /etc/cron.d/
total 24
-rw-r--r-- 1 root root  62 May 14  2020 cronjob_bandit15_root
-rw-r--r-- 1 root root  62 Jul 11 15:56 cronjob_bandit17_root
-rw-r--r-- 1 root root 120 May  7  2020 cronjob_bandit22
-rw-r--r-- 1 root root 122 May  7  2020 cronjob_bandit23
-rw-r--r-- 1 root root 120 May 14  2020 cronjob_bandit24
-rw-r--r-- 1 root root  62 May 14  2020 cronjob_bandit25_root


bandit22@bandit:~$ cat /etc/cron.d/cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null

bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget

# entendiendo un poco el script

bandit22@bandit:~$ echo I am user bandit23 | md5sum | cut -d ' ' -f 1
8ca319486bfbbc3663ea0fbe81326349


bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
```

## bandit23
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

```bash
bandit23@bandit:~$ ls -l /etc/cron.d
total 24
-rw-r--r-- 1 root root  62 May 14  2020 cronjob_bandit15_root
-rw-r--r-- 1 root root  62 Jul 11 15:56 cronjob_bandit17_root
-rw-r--r-- 1 root root 120 May  7  2020 cronjob_bandit22
-rw-r--r-- 1 root root 122 May  7  2020 cronjob_bandit23
-rw-r--r-- 1 root root 120 May 14  2020 cronjob_bandit24
-rw-r--r-- 1 root root  62 May 14  2020 cronjob_bandit25_root
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
```

```bash
bandit23@bandit:~$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done


bandit23@bandit:~$ ls -l /var/spool/
total 12
drwxrwx-wx 31 root bandit24 4096 Dec 17 19:47 bandit24
drwxr-xr-x  3 root root     4096 May  3  2020 cron
lrwxrwxrwx  1 root root        7 May  3  2020 mail -> ../mail
drwx------  2 root root     4096 Jan 14  2018 rsyslog



bandit23@bandit:~$ ls -l /var/spool/bandit24/
ls: cannot open directory '/var/spool/bandit24/': Permission denied
bandit23@bandit:~$

bandit23@bandit:~$ cat /etc/bandit_pass/bandit24
cat: /etc/bandit_pass/bandit24: Permission denied
```
Crearemos un script y lo copiaremos en el directorio donde esta ejecutandonse gracias al cron
```bash
bandit23@bandit:~$  mktemp -d
/tmp/tmp.Z21GOahHr4
bandit23@bandit:/tmp/tmp.Z21GOahHr4$ cd /tmp/tmp.Z21GOahHr4
bandit23@bandit:/tmp/tmp.Z21GOahHr4$ chmod o+rx ../tmp.Z21GOahHr4
```
script
```bash
bandit23@bandit:/tmp/tmp.kgvqXM1q3h$ ls
jotascript.sh
bandit23@bandit:/tmp/tmp.kgvqXM1q3h$ cat jotascript.sh
#!/bin/bash

cat /etc/bandit_pass/bandit24 > /tmp/tmp.kgvqXM1q3h/jotapwned.txt


# permisos al script
bandit23@bandit:/tmp/tmp.Z21GOahHr4$ chmod +x jotascript.sh

# se copia en el directorio spool
bandit23@bandit:/tmp/tmp.kgvqXM1q3h$ cp jotascript.sh /var/spool/bandit24/script.sh

```
se podria utilizar el wat
```bash
# cada segundo hacer ls -l
bandit23@bandit:/tmp/tmp.kgvqXM1q3h$ watch -n 1 ls -l

# falta un permiso para que el escript pueda escrivir en la carpeta
bandit23@bandit:/tmp/tmp.Z21GOahHr4$ chmod o+w /tmp/tmp.Z21GOahHr4


bandit23@bandit:/tmp/tmp.Z21GOahHr4$ watch -n 1 ls -l
bandit23@bandit:/tmp/tmp.Z21GOahHr4$ ls
jotapwned.txt  jotascript.sh
bandit23@bandit:/tmp/tmp.Z21GOahHr4$ cat jotapwned.txt
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```

## bandit24
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
```bash
bandit24@bandit:~$ mktemp -d
/tmp/tmp.7xDJrnCeaw
bandit24@bandit:~$ cd /tmp/tmp.7xDJrnCeaw
bandit24@bandit:/tmp/tmp.7xDJrnCeaw$

# script
bandit24@bandit:/tmp/tmp.7xDJrnCeaw$ touch script.sh
bandit24@bandit:/tmp/tmp.7xDJrnCeaw$ chmod +x !$
chmod +x script.sh


bandit24@bandit:/tmp/tmp.7xDJrnCeaw$ cat script.sh
#!/bin/bash

for i in {0000..9999}; do
	echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i"
done

bandit24@bandit:/tmp/tmp.7xDJrnCeaw$
```
Es diferente trabajar con la secuenta
```bash
#Es diferente trabajar con la secuenta
$ for i in $(seq 0 100); do echo $i; done
0
1
2
3
4
5

# y requerinos generar ping code 0000, para solucionar
jjvargass@pc  ~  for i in {001..100}; do echo $i; done
001
002
003
004
005
006
007
008
009
```

Ejecutamos scritp
```bash

bandit24@bandit:/tmp/tmp.7xDJrnCeaw$ ./script.sh
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0000
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0001
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0002
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0003
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0004
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0005
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0006
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0007
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0008
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0009
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0010

# escrivimos ahora un diccionario
bandit24@bandit:/tmp/tmp.7xDJrnCeaw$ ./script.sh  > dictionary.txt

# ejecutamos por el puerto
bandit24@bandit:/tmp/tmp.7xDJrnCeaw$ cat dictionary.txt | nc localhost 30002
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
```

para limpiar un ppoco la salida
```bash
bandit24@bandit:/tmp/tmp.7xDJrnCeaw$ cat dictionary.txt | nc localhost 30002 | grep -v "Wrong"
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

Exiting.


# tambien por please
bandit24@bandit:/tmp/tmp.7xDJrnCeaw$ cat dictionary.txt | nc localhost 30002 | grep -v -E "Wrong|Please"
Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

Exiting.
bandit24@bandit:/tmp/tmp.7xDJrnCeaw$
```

## bandit25
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.
```bash
bandit25@bandit:~$ ls
bandit26.sshkey
bandit25@bandit:~$

bandit25@bandit:~$ ssh -i bandit26.sshkey bandit26@localhost
Connection to localhost closed.
bandit25@bandit:~$

# podriamos intentar con bash, pero no funciona
bandit25@bandit:~$ ssh -i bandit26.sshkey bandit26@localhost bash
Could not create directory '/home/bandit25/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit25/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

whoami      
```

revisammos la terminal del usaurio
```bash
bandit25@bandit:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext


bandit25@bandit:~$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
```


# para aprobecharnos del more, debemos reducir el tamaño de la terminal
#  v  => entras en modo   luego
# :e  => para editar el archivo que queremos ver

3  | |__   __ _ _ __   __| |_| |_   ) / /_
~/text.txt[RO] [dec= 95] [hex=5F] [pos=0001:0003][16% of 6]                                                                                                               
:e /etc/bandit_pass/bandit26

5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z   


## bandit26
```bash
ssh bandit26@bandit.labs.overthewire.org -p 2220
Connection to bandit.labs.overthewire.org closed.

# nuevamente debemos reducir el tamaño de la terminal y expaunear una shell
# v                     => entras en modo   luego
# :set shell=/bin/bash  => para definir una shell
# :shell

# obtenemos uns shell, escapando del contexto de more
bandit26@bandit:~$ ls
bandit27-do  text.txt
bandit26@bandit:~$

# permisos suid
bandit26@bandit:~$ ls -l
total 12
-rwsr-x--- 1 bandit27 bandit26 7296 May  7  2020 bandit27-do
-rw-r----- 1 bandit26 bandit26  258 May  7  2020 text.txt


bandit26@bandit:~$ ./bandit27-do
Run a command as another user.
  Example: ./bandit27-do id
bandit26@bandit:~$


bandit26@bandit:~$ ./bandit27-do whoami
bandit27
bandit26@bandit:~$ ./bandit27-do bash -p
bash-4.4$ whoami
bandit27
bash-4.4$

bash-4.4$ cat /etc/bandit_pass/bandit27
3ba3118a22e93127a4ed485be72ef5ea
```

## bandit28
