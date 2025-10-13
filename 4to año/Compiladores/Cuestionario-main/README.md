## Para ejecutar el copilador:

1. Hay que agregar el compilador de C# `csc.exe` a las variables de entorno, esto se logra modificando la variable de entorno PATH y agregandole la entrada `C:\Windows\Microsoft.NET\Framework\v4.0.30319` (probablemente no tengan esa version exacta asi que pueden colocar otra, preferiblemente `v4.x.x`, solo hay que asegurarse que dentro este el archivo `csc.exe`)
2. Abrir una terminal (cmd o powershell) y posicionarla en la carpeta con el proyecto
3. Utilizar el comando: `cmd /c ".\compilar.bat"` (si se esta utilizando un cmd se puede simplemente escribir `compilar`)

##### El archivo `compilar.bat` tiene una sucecion de comandos que:

1. Borran los resultados de compilaciones anteriores (si es que los hay)
2. Ejecuta `Coco.exe` con la gramatica `Cuestionario.ATG` de entrada y deja los archivos generados `Parser.cs` y `Scanner.cs` en la carpeta `out`
3. Luego en la carpeta `out` se utiliza el comando `csc` para compilar los 5 archivos `.cs` que se encuentran ahi y el ejecutable `Cuestionario.exe` generado se guarda en la carpeta `compilado`
4. Despues en la carpeta `compilado` se ejecuta el compilador generado `Cuestionario.exe` con el archivo `cuestionario.txt` de entrada, y esto genera el archivo `cuestionario.ps1`
5. Por ultimo ejecuta el archivo `.ps1` generado
