from ftplib import FTP

print('[!] Pasa el [USUARIO] y [CONTRASEÑA] separados por una coma [!]')
ftplogin= input("login@login#>> ")

#Separa el login por la coma para pasarlo como variable por "ftpconnect"
separandoElLogin=ftplogin.split(",")

#Conexion con el servidor FTP por defecto
ftpConnect = FTP('furyos.obiterdicta.net')
print('Connected')
#incia sesion con usuario y contraseña
ftpConnect.login(user=separandoElLogin[0],passwd=separandoElLogin[1])
print('loged')
#Lista el directorio del FTP
ftpConnect.retrlines('LIST')

#Recoge el nombre del archivo
print('[!] Nombre del archivo o directorio [!]')
ftpupload= input("login@login#>> ")

#Guardar archivos
ftpConnect.storbinary("STOR "+ ftpupload , open(ftpupload, 'rb'))

#lista el directorio despues de subir el archivo
ftpConnect.retrlines('LIST')
