# Cetacoin Backend

_Cetacoin Backend manage user accounts and their wallets through bitcoin core and provides the apis to Cetacoin Frontend_

## Construido con 🛠️

* [Django REST](https://www.django-rest-framework.org/) - El framework web usado
* [Pipenv](https://pipenv.pypa.io/en/latest/) - Manejador de dependencias
* [Docker](https://www.docker.com/) - Para desarrollo


## Entorno de desarrollo 🔧

### Pre-requisitos 📋

* [Docker] (https://www.docker.com/)
* [Docker-compose] (https://docs.docker.com/compose/)
* [Algorand Sandbox](https://github.com/algorand/sandbox) - Algorand development enviroment

### Instalación 

_Iniciar red de algorand_

_Entrar a carpeta donde se descargo "Algorand Sandbox" e iniciar los nodos con red Testnet_

```
./sandbox up testnet -s
```

_Correr el archivo de docker-compose que levanta un contenedor para la aplicación y un contenedor con postgresql para almacenar los datos_

_Entrar a la carpeta donde se clono es repositorio y correr el siguiente comando:_

```
docker-compose up
```

_Abrir el navegador con la url: localhost:8080_


## Entorno de producción 📦

### Pre-requisitos 📋

* [Docker] (https://www.docker.com/)
* [Docker-compose] (https://docs.docker.com/compose/)

### Instalación 
_Correr el archivo de docker-compose para producción que levanta un contenedor para la aplicación y un contenedor con postgresql para almacenar los datos_

_Entrar a la carpeta donde se clono es repositorio y correr el siguiente comando:_

```
docker-compose -f "docker-compose-deploy.yml" up -d --build 
```

