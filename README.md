> [!IMPORTANT]  
> Los archivos json de ventas presentan valores negativos en las cantidades, lo cual no es posible en la vida real. Se asume que estos valores negativos son errores en la captura de datos y se convirtieron a números positivos, además de que algunos productos no cuentan con precio, por lo que son mostrados los nombres de los productos al momento de ejecutar el script.

> [!NOTE]  
> El archivo `SalesResults.txt` cuenta con los resultados de todos los archivos json de ventas, usados como casos de prueba, así como el tiempo que tardó en ejecutarse el script.

# Actividad 5.2. Ejercicio de programación 2 y análisis estático

## 1. [Compute Sales](computeSales.py)

Para ejecutar el script, se debe ejecutar el siguiente comando en la terminal, desde la ruta donde se encuentra el archivo `computeSales.py`:

```
python computeSales.py priceCatalogue.json
salesRecord.json
```

Donde `priceCatalogue.json` es el archivo que contiene el catálogo de precios y `salesRecord.json` es el archivo que contiene el registro de ventas. Es posible agregar más de un archivo de ventas, pudiendo quedar de la siguiente manera:

```
python computeSales.py priceCatalogue.json
salesRecord1.json salesRecord2.json salesRecord3.json
```

Al ejecutarlo se imprime tanto en consola como en el archivo `SalesResults.txt` el registro de ventas con el precio total de cada venta, así como el tiempo que tardó en ejecutarse el script, para acceder a el, se puede dar clic [aquí](SalesResults.txt).

Las capturas de ejecución del script se encuentran en el siguiente archivo [A00822314_A5.2](A00822314_A5.2.pdf).

