# Instalación
```bash
cd /opt   
git clone https://github.com/Proxmark/proxmark3
```
gogleamos 'parrot os proxmark installation'
Ingresamos al repo de [Chrissy-Morgan](https://github.com/Chrissy-Morgan/Proxmark3-RDV4-ParrotOS)   
[Buscamos el link de instalación](https://github.com/Chrissy-Morgan/proxmark3/tree/master/Installation_Instructions)

Seguimos la instalación de la paquina, algunos paquete no se intalan y se han eliminado del comando "libqt4-dev libreadline5"
```bash
sudo apt remove modemmanager

sudo apt-get update

sudo apt-get install p7zip git build-essential libreadline-dev \
libusb-0.1-4 libusb-dev perl pkg-config wget libncurses5-dev gcc-arm-none-eabi libpcsclite-dev

# ingresamos a la carpeta proxmark3 del repo clomnado

cd proxmark3

make clean && make all
```
No realizaremos un make install.   
Utilizaremos el binario en la ruta donde esta instalado.

## Flash the BOOTROM & FULLIMAGE
comprobamos que exista el archivo flasher
```bash
file client/flasher                             
client/flasher: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=c883c292b278edc89aa9cbe2e6d2f5b84b5f83aa, for GNU/Linux 3.2.0, with debug_info, not stripped                                                                  
```
**Esta parte es importante**   
El siguiente comando debe ser ejecudado, apretando los siguientes botones de la proxmark3.

Cogemos la proxmark3 y mantenemos pulsado el boton lateral, antes de meter el cable
imagen

teniendo pulsado el boton lateral, metemos el cable
imagen

Al ingresar el cable observamos que el boton naranja debe estar alumbrando. del siguiente modo. aun debes tener pulsado el boton lateral.
imagen

y ahora ejecutamos el comando.
```bash
client/flasher /dev/ttyACM0 -b bootrom/obj/bootrom.elf armsrc/obj/fullimage.elf
```
imagen

Luego de este mensaje desconectamos el cable de la proxmark3

## Revisando la conexion de usb
```bash
watch -n 1 lsusb

Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 005: ID 5986:0708 Acer, Inc Integrated Camera
Bus 001 Device 004: ID 8087:0a2b Intel Corp. Bluetooth wireless interface
Bus 001 Device 003: ID 0c45:5004 Microdia Redragon Mitra RGB Keyboard
Bus 001 Device 002: ID 1017:900a Speedy Industrial Supplies, Pte., Ltd USB Gaming Mouse
Bus 001 Device 008: ID 9ac4:4b8f J. Westhues ProxMark-3 RFID Instrument
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

Para evitar problemitas, debemos buscar y editar el siguiente archivo.
```bash
cd client
find \-name formatMifare*
./scripts/formatMifare.lua

pwd                      
/opt/proxmark3/proxmark3/client/scripts

nano formatMifare.lua

# al final del archivo, encontraremos esto:
# quitar las lineas "--" de esta espreció --core.console(cmd)
# para que quede solo:  core.console(cmd)
if block ~= 0 then
        print(cmd)
        --core.console(cmd)
end
```

# laboratorio

```bash
# ingresamos al directorio client
pwd
/opt/proxmark3/proxmark3/client

# ejecutando al binario proxmark3 le pasamos la ruta donde se encuentra el dispositivo alojado

./proxmark3 /dev/ttyACM0


Prox/RFID mark3 RFID instrument          
bootrom: master/v3.1.0-209-g6116334-suspect 2021-08-28 01:13:29
os: master/v3.1.0-209-g6116334-suspect 2021-08-28 01:13:30
fpga_lf.bit built for 2s30vq100 on 2019/11/21 at 09:02:37
fpga_hf.bit built for 2s30vq100 on 2020/03/05 at 19:09:39
SmartCard Slot: not available

uC: AT91SAM7S512 Rev B          
Embedded Processor: ARM7TDMI          
Nonvolatile Program Memory Size: 512K bytes. Used: 207291 bytes (40%). Free: 316997 bytes (60%).          
Second Nonvolatile Program Memory Size: None          
Internal SRAM Size: 64K bytes          
Architecture Identifier: AT91SAM7Sxx Series          
Nonvolatile Program Memory Type: Embedded Flash Memory          
proxmark3>

# aqui ya estamos dentro de dispositivo
```

## validar frecuencia
La frecuencia alta se valida en la parte plana
La frecuencia vaja se valida en la rueda

```bash
# validar frecuencia alta (High Frequency)
proxmark3> hf search

 UID : 01 02 03 04          
ATQA : 00 04          
 SAK : 08 [2]          
TYPE : NXP MIFARE CLASSIC 1k | Plus 2k SL1          
proprietary non iso14443-4 card found, RATS not supported          
Chinese magic backdoor commands (GEN 1a) detected          
Prng detection: WEAK          

Valid ISO14443A Tag Found - Quiting Search
```

## Copiar UID
```bash
# Tarjeta origen
proxmark3> hf search

 UID : 90 e8 49 fa          
ATQA : 00 04          
 SAK : 08 [2]          
TYPE : NXP MIFARE CLASSIC 1k | Plus 2k SL1          
proprietary non iso14443-4 card found, RATS not supported          
No chinese magic backdoor command detected          
Prng detection: WEAK          

Valid ISO14443A Tag Found - Quiting Search


# Tarjeta China
proxmark3> hf search

 UID : 01 02 03 04          
ATQA : 00 04          
 SAK : 08 [2]          
TYPE : NXP MIFARE CLASSIC 1k | Plus 2k SL1          
proprietary non iso14443-4 card found, RATS not supported          
Chinese magic backdoor commands (GEN 1a) detected          
Prng detection: WEAK          

Valid ISO14443A Tag Found - Quiting Search

# Copiar datos
# es el comando inicial y damos enter y se nos despliega las opciones, esta info es la de ejemplo
proxmark3> hf mf csetuid

Usage:  hf mf csetuid <UID 8 hex symbols> [ATQA 4 hex symbols SAK 2 hex symbols]          
sample:  hf mf csetuid 01020304          
sample:  hf mf csetuid 01020304 0004 08          
Set UID, ATQA, and SAK for magic Chinese card (only works with such cards)  

# Copiando datos
proxmark3> hf mf csetuid 90e849fa 0004 08
uid:90 e8 49 fa          
--atqa:00 04 sak:08          
Chinese magic backdoor commands (GEN 1a) detected          
old block 0:  01 02 03 04 04 08 04 00 00 00 00 00 00 00 be af          
new block 0:  90 e8 49 fa cb 08 04 00 00 00 00 00 00 00 be af          
old UID:01 02 03 04          
new UID:90 e8 49 fa          
proxmark3>
```

## Copiar toda la Data de la tarjeta
```bash
# ver los sectores de la tarjeta
proxmark3> hf mf chk
Usage:  hf mf chk <block number>|<*card memory> <key type (A/B/?)> [t|d|s|ss] [<key (12 hex symbols)>] [<dic (*.dic)>]          
          * - all sectors          
card memory - 0 - MINI(320 bytes), 1 - 1K, 2 - 2K, 4 - 4K, <other> - 1K          
d  - write keys to binary file (not used when <block number> supplied)          
t  - write keys to emulator memory          
s  - slow execute. timeout 1ms          
ss - very slow execute. timeout 5ms          
      sample: hf mf chk 0 A 1234567890ab keys.dic          
              hf mf chk *1 ? t          
              hf mf chk *1 ? d          
              hf mf chk *1 ? s          
              hf mf chk *1 ? dss     

# ejecutamos con la tarjeta original puesta
proxmark3> hf mf chk *1 ?
--chk keys. sectors:16, block no:  0, key type:?, eml:n, dmp=n checktimeout=471 us          
No key specified, trying default keys          
chk default key[ 0] ffffffffffff          
chk default key[ 1] 000000000000          
chk default key[ 2] a0a1a2a3a4a5          
chk default key[ 3] b0b1b2b3b4b5          
chk default key[ 4] aabbccddeeff          
chk default key[ 5] 1a2b3c4d5e6f          
chk default key[ 6] 123456789abc          
chk default key[ 7] 010203040506          
chk default key[ 8] 123456abcdef          
chk default key[ 9] abcdef123456          
chk default key[10] 4d3a99c351dd          
chk default key[11] 1a982c7e459a          
chk default key[12] d3f7d3f7d3f7          
chk default key[13] 714c5c886e97          
chk default key[14] 587ee5f9350f          
chk default key[15] a0478cc39091          
chk default key[16] 533cb6c723f6          
chk default key[17] 8fd0a4f256e9          

To cancel this operation press the button on the proxmark...          
--o          
|---|----------------|----------------|          
|sec|key A           |key B           |          
|---|----------------|----------------|          
|000|  ffffffffffff  |  ffffffffffff  |          
|001|  ffffffffffff  |  ffffffffffff  |          
|002|  ffffffffffff  |  ffffffffffff  |          
|003|  ffffffffffff  |  ffffffffffff  |          
|004|  ffffffffffff  |  ffffffffffff  |          
|005|  ffffffffffff  |  ffffffffffff  |          
|006|  ffffffffffff  |  ffffffffffff  |          
|007|  ffffffffffff  |  ffffffffffff  |          
|008|  ffffffffffff  |  ffffffffffff  |          
|009|  ffffffffffff  |  ffffffffffff  |          
|010|  ffffffffffff  |  ffffffffffff  |          
|011|  ffffffffffff  |  ffffffffffff  |          
|012|  ffffffffffff  |  ffffffffffff  |          
|013|  ffffffffffff  |  ffffffffffff  |          
|014|  ffffffffffff  |  ffffffffffff  |          
|015|  ffffffffffff  |  ffffffffffff  |          
|---|----------------|----------------|    

# para leer el sector especifico tenemos dos opciones
proxmark3> hf mf
help             This help          
dbg              Set default debug mode          
rdbl             Read MIFARE classic block          
rdsc             Read MIFARE classic sector          
dump             Dump MIFARE classic tag to binary file       

# Es mas facil por sectores
# ejemplos del comando
proxmark3> hf mf rdsc
Usage:  hf mf rdsc    <sector number> <key A/B> <key (12 hex symbols)>          
        sample: hf mf rdsc 0 A FFFFFFFFFFFF          

# ejecutamos sector 10 de la key A  contraseña
proxmark3> hf mf rdsc 10 A ffffffffffff
--sector no:10 key type:A key:ff ff ff ff ff ff           

#db# READ SECTOR FINISHED          
isOk:01          
data   : 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00          
data   : 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00          
data   : 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00          
trailer: 00 00 00 00 00 00 ff 07 80 69 ff ff ff ff ff ff          
Trailer decoded:          
Access block 40: read AB; write AB; increment AB; decrement transfer restore AB          
Access block 41: read AB; write AB; increment AB; decrement transfer restore AB          
Access block 42: read AB; write AB; increment AB; decrement transfer restore AB          
Access block 43: write A by A; read ACCESS by A write ACCESS by A; read B by A; write B by A          
UserData: 69         

# sector 0
proxmark3> hf mf rdsc 0 A ffffffffffff
--sector no:0 key type:A key:ff ff ff ff ff ff           

#db# READ SECTOR FINISHED          
isOk:01          
data   : 90 e8 49 fa cb 08 04 00 02 ae ab 56 4b 0e b0 1d          
data   : 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00          
data   : 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00          
trailer: 00 00 00 00 00 00 ff 07 80 69 ff ff ff ff ff ff          
Trailer decoded:          
Access block 0: read AB; write AB; increment AB; decrement transfer restore AB          
Access block 1: read AB; write AB; increment AB; decrement transfer restore AB          
Access block 2: read AB; write AB; increment AB; decrement transfer restore AB          
Access block 3: write A by A; read ACCESS by A write ACCESS by A; read B by A; write B by A          
UserData: 69     

# de exadecimal pasamos a formato legible
└─# echo "0 e8 49 fa cb 08 04 00 02 ae ab 56 4b 0e b0 1d"  | xxd -ps -r; echo   
�����@*�d��
```

## Dump de la tarjeta
```bash
# este es el comando, pero no funciona, requiere que previo a esto se realice la obtención de claves pero con la opcion (d) para crear el archivo necesario

proxmark3> hf mf dump 1
Could not find file dumpkeys.bin   

# proceso dump

# (1) con al opción d - las contraseñas encontradas las guarda en el fichero dumpkeys.bin
proxmark3> hf mf chk *1 ? d
--chk keys. sectors:16, block no:  0, key type:?, eml:n, dmp=y checktimeout=471 us          
No key specified, trying default keys          
chk default key[ 0] ffffffffffff          
chk default key[ 1] 000000000000          
chk default key[ 2] a0a1a2a3a4a5          
chk default key[ 3] b0b1b2b3b4b5          
chk default key[ 4] aabbccddeeff          
chk default key[ 5] 1a2b3c4d5e6f          
chk default key[ 6] 123456789abc          
chk default key[ 7] 010203040506          
chk default key[ 8] 123456abcdef          
chk default key[ 9] abcdef123456          
chk default key[10] 4d3a99c351dd          
chk default key[11] 1a982c7e459a          
chk default key[12] d3f7d3f7d3f7          
chk default key[13] 714c5c886e97          
chk default key[14] 587ee5f9350f          
chk default key[15] a0478cc39091          
chk default key[16] 533cb6c723f6          
chk default key[17] 8fd0a4f256e9          

To cancel this operation press the button on the proxmark...          
--o          
|---|----------------|----------------|          
|sec|key A           |key B           |          
|---|----------------|----------------|          
|000|  ffffffffffff  |  ffffffffffff  |          
|001|  ffffffffffff  |  ffffffffffff  |          
|002|  ffffffffffff  |  ffffffffffff  |          
|003|  ffffffffffff  |  ffffffffffff  |          
|004|  ffffffffffff  |  ffffffffffff  |          
|005|  ffffffffffff  |  ffffffffffff  |          
|006|  ffffffffffff  |  ffffffffffff  |          
|007|  ffffffffffff  |  ffffffffffff  |          
|008|  ffffffffffff  |  ffffffffffff  |          
|009|  ffffffffffff  |  ffffffffffff  |          
|010|  ffffffffffff  |  ffffffffffff  |          
|011|  ffffffffffff  |  ffffffffffff  |          
|012|  ffffffffffff  |  ffffffffffff  |          
|013|  ffffffffffff  |  ffffffffffff  |          
|014|  ffffffffffff  |  ffffffffffff  |          
|015|  ffffffffffff  |  ffffffffffff  |          
|---|----------------|----------------|          
Found keys have been dumped to file dumpkeys.bin. 0xffffffffffff has been inserted for unknown keys.  

# (2) Ejecutar dump

proxmark3> hf mf dump 1
|-----------------------------------------|          
|------ Reading sector access bits...-----|          
|-----------------------------------------|          
#db# READ BLOCK FINISHED          
#db# READ BLOCK FINISHED          
#db# READ BLOCK FINISHED          
#db# READ BLOCK FINISHED          
#db# READ BLOCK FINISHED          
#db# READ BLOCK FINISHED          
#db# READ BLOCK FINISHED          
#db# READ BLOCK FINISHED          
#db# READ BLOCK FINISHED          
#db# READ BLOCK FINISHED          
#db# READ BLOCK FINISHED          
#db# READ BLOCK FINISHED          
#db# READ BLOCK FINISHED          
#db# READ BLOCK FINISHED          
#db# READ BLOCK FINISHED          
#db# READ BLOCK FINISHED          
|-----------------------------------------|          
|----- Dumping all blocks to file... -----|          
|-----------------------------------------|          
#db# READ BLOCK FINISHED          
Successfully read block  0 of sector  0.          
#db# READ BLOCK FINISHED          
Successfully read block  1 of sector  0.          
#db# READ BLOCK FINISHED          
Successfully read block  3 of sector 15.          
Dumped 64 blocks (1024 bytes) to file dumpdata.bin    

# pdemos ferificar la información del dump
# en otra terminal
root@pc:/opt/proxmark3/proxmark3/client# pwd
/opt/proxmark3/proxmark3/client

root@pc:/opt/proxmark3/proxmark3/client# ls -l | grep dumpdata.bin
-rw-r--r--  1 root root    1024 Aug 27 23:21 dumpdata.bin

root@pc:/opt/proxmark3/proxmark3/client# hexeditor dumpdata.bin
```
### Formatear tarjeta china
```bash
proxmark3> hf mf cwipe 1 f
Chinese magic backdoor commands (GEN 1a) detected          
--blocks count:64 wipe:n fill:y          
OK          

# script disponibles
proxmark3> script list

# dar formato
proxmark3> script run  formatMifare
--- Executing: formatMifare.lua, args ''
----------------------------------------
----------------------------------------

No response from card
No response from card
Estimating number of blocks: 64
Old key:    FFFFFFFFFFFF
New key:    FFFFFFFFFFFF
New Access: FF0780

```

## Copiar el dump en la tarjeta formateada
```bash

# ahora colocamos la tarjeta formateada "la china" y ejecutamos lo siguiete

proxmark3> hf mf restore 1
Restoring dumpdata.bin to card          
Writing to block   0: 01 02 03 04 04 08 04 00 00 00 00 00 00 00 be af          
#db# Cmd Error: 04          
#db# Write block error          
#db# WRITE BLOCK FINISHED          
isOk:00          
Writing to block   1: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00          
#db# WRITE BLOCK FINISHED          
isOk:01          
Writing to block   2: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00          
#db# WRITE BLOCK FINISHED          
isOk:01          
Writing to block   3: ff ff ff ff ff ff ff 07 80 00 ff ff ff ff ff ff          
#db# WRITE BLOCK FINISHED          
isOk:01          
Writing to block   4: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00          
#db# WRITE BLOCK FINISHED      
```
