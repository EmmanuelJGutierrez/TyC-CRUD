# "TyC - Sistema de Tickets y Consultas

## Descripcion:

"  " es un Sistema de **Tickets** y **Consultas** que busca no solo solucionar errores y consultas por parte de los usuarios consumidores, sino que tambien *comunicar*, *delegar* y *anunciar* esto a otros empleados. Por un lado tanto como los *Tickets* como las *Consultas* van a contar con sus respectivos estados, *prioridades* y deberan tener detallados en una breve descripcion de que tratara cada solicitud o consulta.

## Tipos de Usuario:

Como se menciono antes existen dos tipos:

- Usuarios registrados.
- Empleados afines al sistema.

## Estados de un Ticket:

Los tickets se van a mostrar con los siguientes estados:

- Enviado: El ticket fue enviado y esta a la espera de revision.
- Abierto: EL ticket fue leido y esta siendo definido si procesarlo o descartarlo.
- En progreso: El ticket fue aceptado y se esta buscando solucionarlo.
- Cerrado/Solucionado: El problema fue resuelto y se notificara o se explicara el porque este no puede ser solucionado.

## Prioridades:

Basado en las practicas ITIL, las prioridades se dividen en:

- P1: Nivel de **urgencia Critica**, resolucion inmediata.
- P2: Alta, resolucion en pocas horas.
- P3: Media, existe solucion temporal.
- P4: Baja, Problemas menores que no impiden el trabajo.
- P5: Minima, Cambios esteticos.

## Funcionalidades Principales:

El sistema esta orientado a recibir, gestionar y solucionar las diferentes solicitudes que se ingresen al sistema.
Un ejemplo de un posible recorrido es, un *usuario consumidor* ingresa a su cuenta con un usuario y contraseña, selecciona la opcion de realizar un ticket, en este mismo debera rellenar la opcion de: **Titulo** en el que debera resaltar el problema o consulta principal, **Descripcion** en la que detallara el origen de la consulta o el error que lo aflije a profundida, debera elegir el nivel de **Prioridad** a conciencia viendo que esta refleje la importancia de su problema y al enviar esta mostrara lo detallado por el usuario mas una **fecha de envio** y el **Estado** de la consulta, este Estado se actualizara al igual que la fecha en el transcurso de que sea analizado por un profesional, este decidira si el ticket tiene que ser descartado o emitira la respuesta de que la solucion esta en proceso, para la posterior confirmacion de solucion del problema, el usuario podra ver las actualizaciones al estado de su consulta asi como las notas sobre esta que deje el profesional. 
Un empleado podra realizar las mismas operaciones solo que tambien podra asignar esta tarea a otro empleado con su recordatorio de ser necesario. 

## Tecnologias:

- FastAPI
- PostgreSQL
- React