## Instrucciones de uso

1. Descargar o clonar proyecto y descomprimir
2. Descargar [Node.js](https://nodejs.org/en/)
3. Actualizar variables de entorno en caso de ser necesario
4. Abrir una terminal en la ruta del proyecto
5. Ejecutar el comando `npm i` para instalar las dependencias
6. Para ejecutar el proyecto usar el comando `npm start`

Observaciones

Debido al tamaño de la cabecera es muy ineficiente para archivos pequeños, y debido al que es muy dificil trabajar a nivel de bit en javascript del modo requerido el trabajo sobre los datos se realizo sobre una cadena en binario, lo cual es muy ineficiente en terminos de memoria y conlleva a que sea muy lento para archivos muy grandes

Tambien por simplicidad no se pregunta como quiere llamar al archivo comprimido/descomprimido, simplemente se agrega una extension

## Muestra

#### Compresion

```powershell
PS F:\Programacion> ts-node "f:\Programacion\Compresor\src\index.ts"
Que desea hacer?
1. Comprimir
2. Descomprimir
3. Test

1
Ingrese la ruta al archivo a comprimir: F:\Programacion\Compresor\test\Cuestionario memoria cache.txt
Cantidad de codificaciones de shannon: 538
Tamaño original (en bits): 148792
Tamaño comprimido (en bits): 88933 (% 59.8 del tamaño original)
Tamaño de la cabecera (en bits): 42711
Tamaño del texto comprimido (en bits): 46222 (% 31.1 del tamaño original)
Archivo comprimido: F:\Programacion\Compresor\test\Cuestionario memoria cache.txt.shannon
```

Resultado:

```
Cuestionario memoria cache.txt                   19 KB
Cuestionario memoria cache.txt.shannon           11 KB 
```

#### Descompresion

```powershell
PS F:\Programacion> ts-node "f:\Programacion\Compresor\src\index.ts"
Que desea hacer?
1. Comprimir
2. Descomprimir
3. Test

2
Ingrese la ruta al archivo descomprimir: F:\Programacion\Compresor\test\Cuestionario memoria cache.txt.shannon
Archivo descomprimido: F:\Programacion\Compresor\test\Cuestionario memoria cache.txt.decompressed
```

#### Test

Hace la compresion y descompresion de una sola vez y compara los resultados

```powershell
PS F:\Programacion> ts-node "f:\Programacion\Compresor\src\index.ts"
Que desea hacer?
1. Comprimir
2. Descomprimir
3. Test

3
Ingrese la ruta al archivo a comprimir: F:\Programacion\Compresor\test\Cuestionario memoria cache.txt
Cantidad de codificaciones de shannon: 545
Tamaño original (en bits): 145344
Tamaño comprimido (en bits): 88062 (% 60.6 del tamaño original)
Tamaño de la cabecera (en bits): 42608
Tamaño del texto comprimido (en bits): 45454 (% 31.3 del tamaño original)

Archivo comprimido: F:\Programacion\Compresor\test\Cuestionario memoria cache.txt.shannon

Es igual al original: true
Archivo descomprimido: F:\Programacion\Compresor\test\Cuestionario memoria cache.txt.decompressed  

PS F:\Programacion> 
```

Resultado:

```
Cuestionario memoria cache.txt                   19 KB
Cuestionario memoria cache.txt.shannon           11 KB 
Cuestionario memoria cache.txt.decompressed      19 KB
```

## Otras muestras

Comprimiendo un PDF

```powershell
PS F:\Programacion> ts-node "f:\Programacion\Compresor\src\index.ts"
Que desea hacer?
1. Comprimir
2. Descomprimir
3. Test

1
Ingrese la ruta al archivo a comprimir: F:\Programacion\Compresor\test\CALENDARIO23-24.pdf
Cantidad de codificaciones de shannon: 65534
Tamaño original (en bits): 6861128
Tamaño comprimido (en bits): 20361660 (% 296.8 del tamaño original)
Tamaño de la cabecera (en bits): 17012915
Tamaño del texto comprimido (en bits): 3348745 (% 48.8 del tamaño original)
Archivo comprimido: F:\Programacion\Compresor\test\CALENDARIO23-24.pdf.shannon
```

Aqui se puede apreciar como el tamaño de la cabecera es extremadamente grande, tambien se puede observar que en total hay 65534 codificaciones de shannon (el maximo es 65535) esto se debe a que aparecen casi todas las combinaciones de 2 simbolos ASCII (256 * 256 = 65536) debido a que los archivos PDF la entropia es muy alta
