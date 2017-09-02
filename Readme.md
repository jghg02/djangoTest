# Django


> Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 

## Instalación

#### MAC

> brew install python 
> 
> brew install django 



#### Windows 

- Se necesita installar python. Para esto es necesario descargar el lenguaje en este [link](https://www.python.org/downloads/)
- Agregar las variables de entorno X:\Python27\;X:\Python27\Scripts; al final de la variable PATH, siendo X el disco de instalación




## Init Project

Para crea un proyecto es necesario ejecutar el siguiente comando. 
> django-admin startproject "project_name"

Este script crea los archivos y directorios necesarios para la App que creaste. 

**manage.py**: Es un script que ayuda con la administración del sitio. Con ello podremos iniciar un servidor web en nuestro ordenador sin necesidad de instalar nada más, entre otras cosas.

**settings.py**: Contiene la configuración de tu sitio web.

**urls.py**: Contiene una lista de los patrones utilizados (URL's)


## Config Data Base

En el archivo **settings.py** contiene una sección para configurar la base de datos que se utilizara en el proyecto. Se pueden usar muchos motores de Base de Datos. 

Esta configuración aplica para **sqlite**

	DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

Para crear una base de datos para nuestro blog, ejecutemos lo siguiente en la consola: **python manage.py migrate**

## Run

Para probar que tu código este correcto es necesario ejecutar el siguiente comando. 
> 	python manage.py runserver 



## Creando una aplicación 

Basicamente sirve para poder organizar tu código. Para crear una app dentro del proyecto que se ha creado es necesario ejecutar el siguiente comando: 
> python manage.py startapp blog

Luego de crear una app es necesario decirle a Django que debe utilizarla. Para esto lo agregamos en el archivo de **settings.py**. Tenemos que encontrar `INSTALLED_APPS` y añadir una línea que contenga 'blog'.

	INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog',
    )


## Modelos en Django

Básicamente se trata de describir cosas reales en el código con propiedades `propiedades del objeto`y las acciones `metodos`

Un modelo en Django es un tipo especial de objeto que se guarda en la base de datos.

Ejemplo de un modelo. 

	class Post(models.Model):
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title
            

El último paso es añadir nuestro nuevo modelo a nuestra base de datos. Primero tenemos que hacer que Django sepa que tenemos algunos cambios en nuestro modelo (acabamos de crearlo), escribe `python manage.py makemigrations blog`

`python manage.py migrate`


## Coneccion con MySql

Esta es la configuración que se necesita agregar en el archivo **settings.py**

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql',
	        'NAME': 'django',
	        'USER': 'admin',
	        'PASSWORD': '1234'
	    }
	}

Se necesita installar el siguiente driver para que funcione [driver](https://dev.mysql.com/downloads/connector/python/) o ejecutar el siguiente comando por consola. 
> sudo pip install mysql-python


## URL's

	^ denota el principio del texto
	$ denota el final del texto
	\d representa un dígito
	+ indica que el ítem anterior debería ser repetido por lo menos una vez
	() para encerrar una parte del patrón
