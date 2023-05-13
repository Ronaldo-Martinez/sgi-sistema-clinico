# SGI - SISTEMA - CLINICO

Proyecto Gerencial para el sistema clinico medico de Cojutepeque


# Configuración.
* Solicitar archivo con las varibales de entorno y colocarlo en la raíz del proyecto
* Si no se utiliza DevContainer ejecutar los siguientes comandos
```
pip install -r requirements.txt
```

## Migraciones
````
python manage.py migrate
```` 

## Subir Datos base (Ejecutar solo si es necesario)

````
python manage.py loaddata db.json
````

## Servidor de desarrollo
```
python manage.py runserver
```

