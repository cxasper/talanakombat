# Talana Kombat 🛢

## Descripcion
Lado del backend del proyecto cambia con Helix del cliente Enex que sirve las APIs necesarias para el funcionamiento del mismo, que consiste en un manejador de reservas(booking) para cambio de aceite en estaciones Shell.

## Pre-requisitos 📋

-   Docker 19.03^

## Instalación 🔧

1. Clonar el repositorio
```
git clone https://gitlab.com/e-commerce/enex-backend.git
```

2. Una vez dentro del directorio del proyecto posicionarse en la rama _develop_
   (o la rama donde necesites trabajar)
```
git checkout develop
```

3. Levantar y construir el contenedor en segundo plano.
```
docker build --tag talana .

docker run talana
```

4. Verifica la instalacion navegando a la siguiente url

    [http://localhost:8000/admin/](http://localhost:8000/admin/)
