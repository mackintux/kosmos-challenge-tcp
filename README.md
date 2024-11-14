# Servidor y Cliente TCP en Python

## Descripción
Este proyecto implementa un servidor y un cliente TCP en Python. El servidor escucha en `localhost` en el puerto `5000` (cambiado por conflictos de puerto a `5001`) y responde a los mensajes en mayúsculas. Si recibe el mensaje "DESCONEXION", cierra la conexión con el cliente.

## Ejecución

### Ejecutar el Servidor
1. Abre una terminal y ejecuta:
   ```bash
   python src/server.py
   ```
   
![Servidor Iniciado](assets/server_started.png)

### Ejecutar el Cliente
1. Abre otra terminal y ejecuta:
   ```bash
   python src/client.py
   ```

![Cliente Iniciado](assets/client_started.png)

2. Ingresa un mensaje y presiona Enter. El servidor responderá con el mensaje en mayúsculas.
3. Para desconectarte, ingresa DESCONEXION.

## Pruebas Manuales

1. Enviar un mensaje de texto normal y verificar que el servidor responda en mayúsculas.

![manual_testing_1.png](assets/manual_testing_1.png)

2. Enviar el mensaje DESCONEXION y confirmar que la conexión se cierra correctamente en ambos lados.

![manual_testing_2.png](assets/manual_testing_2.png)

3. Intentar volver a conectarse con otro cliente, ejecutando nuevamente el paso 1.

![manual_testing_3.png](assets/manual_testing_3.png)

4. Verificando la salida del servidor.

![manual_testing_4.png](assets/manual_testing_4.png)

### Posible problema del puerto
En caso de contar con servicios o programas que se encuentran ejecutando algún proceso por medio del puerto ``5000`` podríamos simplemente cambiarlo dentro del código, o en su caso podríamos cerrar la tarea que se encuentra ejecutando dicho puerto.

Para poder identificar que se encuentra ejecutando dentro del puerto ```5000``` ejecutaríamos el siguiente comando:
   ```bash
   sudo lsof -i :5000 -P -n | grep LISTEN
   ```

![Verificación de puerto](assets/port_check.png)
