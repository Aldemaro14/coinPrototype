# Cetacoin Backend

_Cetacoin Backend manage user accounts and their wallets through bitcoin core and provides the apis to Cetacoin Frontend

## Construido con 🛠️

* [Django REST](https://www.django-rest-framework.org/) - El framework web usado
* [Pipenv](https://pipenv.pypa.io/en/latest/) - Manejador de dependencias
* [Docker](https://www.docker.com/) - Para desarrollo


## Entorno de desarrollo 🔧

### Pre-requisitos 📋

* Docker
* Docker-compose
* [Algorand Sandbox](https://github.com/algorand/sandbox) - Algorand development enviroment

### Instalación 

_Iniciar red de algorand_

_Entrar a carpeta donde se descargo "Algorand Sandbox" e iniciar los nodos con red Testnet"_

```
./sandbox up testnet -s
```

_Correr el archivo de docker-compose que levanta un contenedor para la aplicación y un contenedor con postgresql para almacenar los datos_

```
docker-compose up
```

_Abrir el navegador con la url: localhost:8080_


## Entorno de producción 📦

### Pre-requisitos 📋

* Docker
* Docker-compose

_Agrega notas adicionales sobre como hacer deploy_

## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```
