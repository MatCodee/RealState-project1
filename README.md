
![Imagen de proyecto](/doc/images/project.png)

## Comenzando 🚀
Este es un proyecto de real state, es decir una plataforma de bienes raices.

Mira **Deployment** para conocer como desplegar el proyecto.

### Pre-requisitos 📋
- Cuenta de AWS, Crear un entorno S3
- Keys AWS
- Instalado PostgreSQL
- python
- Entorno virtual
- Google Key para envios de Email

#### Nota:
Sino tiene instalado PostgreSql o Google Keys, solo dejara de funcionar el email, y en configuracion del archivo .env puede modificar
la propiedad 'DEV_ENVIRONT' en True para Utilizar la DB sqlite3 por defecto y desa forma los archivos se guardaran en la carpeta local de 
media.

### Instalación 🔧
_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

Windows:
Suponer que tienes instalado lo anterior
estamos en la carpeta raiz del proyecto
```
virtualenv env
env\Scripts\activate
pip install -r requirements.txt
```

Correr el proyecto
```
python manage.py migrate
python manage.py runserver
```


