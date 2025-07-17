
# Test Django UBUNTU

## Descripción:
=== Test de despliegue para Django en UBUNTU con una aplicación sencilla utilizando NGINX y Gunicorn ===

# Pasos para probar el proyecto:
1. Crear un entorno virtual y activarlo
    `python3 -m venv venvDeploy`
    `source venvDeploy/bin/activate`
2. Instalar los paquetes necesarios desde "requirements.txt"
    `pip install -r requirements.txt`
3. Crear la base de datos y aplicar migraciones de Django:
    `python manage.py migrate`
3. (Opcional) Crear un super usuario para entrar al admin de Django
    `python manage.py createsuperuser`
4. Ejecutar el servidor de desarrollo de Django para pruebas
    `python manage.py runserver`
    `ctrl + C` -> Para cerrar el servidor de prueba
5. Recolectar los archivos estáticos del proyecto
    `python manage.py collectstatic`
6. Ejecutar Gunicorn para probar el proyecto
    `gunicorn testdeploy.wsgi:application`
7. Entrar a la ruta de la página local en el puerto 8000 a la dirección del proyecto especificada
Ejemplo: http://127.0.0.1:8000/app


## Autor:

 - Angel Díaz (HefestoPrimal)

## Licencia:

 - Libre
