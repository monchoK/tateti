#!/bin/bash
dir=$(whereis flutter)
dir2=$(echo $dir | awk -F" " '{print $2}')
flutter=$(echo $dir2 | awk -F"/" '{print "/"$2"/"$3}')
echo "Borrando $flutter/bin/cache/flutter_tools.stamp"
rm -f $flutter/bin/cache/flutter_tools.stamp
if [ -f "$flutter/bin/cache/flutter_tools.stamp" ]; then
echo "Ups, parece que no se puedo ejecutar el script con éxito.
Vuelva a probar con alguno de estos comandos:
    sudo $PWD/fix_flutter_web.sh
    sudo bash $PWD/fix_flutter_web.sh"
exit 1
else
echo "Borrado con éxito"
echo "Editando $flutter/packages/flutter_tools/lib/src/web/chrome.dart"
sed -i "s|      '--disable-extensions',|      '--disable-extensions',\
      '--disable-web-security',|g" $flutter/packages/flutter_tools/lib/src/web/chrome.dart
echo "
Pruebe a ejecutar el proyecto con chrome.
Ahora debería funcionar con una alerta sobre el cambio realizado en este script"
exit 0
fi