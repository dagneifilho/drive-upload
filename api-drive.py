from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import sys


gauth=GoogleAuth()
gauth.LocalWebserverAuth()

from pydrive.drive import GoogleDrive

arquivo_path=str(sys.argv[1])

arquivo =open(arquivo_path,encoding='utf-8')
arq_inv=arquivo_path[::-1]
index_ponto=arq_inv.index('.')
ext_inv=arq_inv[:index_ponto]
extensao=ext_inv[::-1]


if extensao in ['py','txt','cs']:

	drive = GoogleDrive(gauth)
	arquivo_drive=drive.CreateFile({'title':os.path.basename(arquivo.name)})
	arquivo_drive.SetContentString(arquivo.read())
	arquivo_drive.Upload()
	print(f'Upload de {os.path.basename(arquivo.name)} realizado com sucesso!')

else:

	print('Utilize arquivos com o formato .txt, .cs ou .py')

arquivo.close()