# tateti

## Instalar lo necesario desde el docker-compose

```bash
cd database
docker-compose -f docker-compose.yml up
```

o

```bash
cd database
docker-compose up -d
```

## Ejecutar contenedor

```bash
docker exec -it <nombredelcontenedor> bash
```

## Iniciar mysql

```bash
mysql -h db -u root -p
```

> Contraseña: secret

Una vez dentro del mysql, copiar las instrucciones de [db.sql](db.sql)

## Iniciar entorno virtual

```bash
. venv/bin/activate
```

Si no puede iniciar el entorno virtual, cree uno nuevo y ejecute la siguiente instrucción

```bash
pip install -r requirements
```
