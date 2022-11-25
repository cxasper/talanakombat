# Talana Kombat 🛢

## Descripcion
Lado del backend del proyecto cambia con Helix del cliente Enex que sirve las APIs necesarias para el funcionamiento del mismo, que consiste en un manejador de reservas(booking) para cambio de aceite en estaciones Shell.

## Pre-requisitos 📋

-   Docker 19.03^

## Instalación 🔧

1. Clonar el repositorio
```
git clone https://github.com/cxasper/talanakombat
```

2. Una vez dentro del directorio del proyecto posicionarse en la rama _develop_
   (o la rama donde necesites trabajar)
```
git checkout develop
```

3. Levantar y construir el contenedor.
```
docker build --tag talana .

docker run talana
```

4. Usar
```
docker run talana
```
esto ejecutara el script y solicitar un json.

```
{"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}
```

y la respuesta esperada sería:
```
Tonyn se mueve y lanza un(a) patada
Arnaldor conecta un Remuyuken
Tonyn conecta un Taladoken
Arnaldor se mueve
Tonyn se mueve
Arnaldor conecta un Remuyuken
Arnaldor gana la pelea y aun le queda 1
```
