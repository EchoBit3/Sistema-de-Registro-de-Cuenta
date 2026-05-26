# Sistema de Registro de Cuenta

Proyecto en Python basado en un Diagrama de Flujo de Datos. Implementa un flujo de registro con validación en cada etapa, donde cada campo se repite hasta cumplir su condición antes de avanzar al siguiente.

## ¿Qué hace?

- Valida nombre y apellidos
- Verifica el RUT/DNI con su dígito verificador
- Exige una contraseña con requisitos mínimos de seguridad
- Lleva un registro de intentos fallidos por sesión

## Cómo funciona por dentro

Cada campo usa un bucle `while` que sigue pidiendo el dato hasta que pase la validación. Cuando pasa, avanza al siguiente. Si no, vuelve a preguntar.

Las validaciones usan operadores lógicos (`and`, `not`) para combinar condiciones, por ejemplo la contraseña tiene que cumplir largo, tener número y tener mayúscula al mismo tiempo.

Los operadores aritméticos aparecen en la validación del RUT, que aplica una serie de multiplicaciones y sumas para calcular si el dígito verificador es correcto, y también para llevar el conteo de intentos y calcular el promedio al final.

Los `if`, `elif` y `else` controlan qué mensaje mostrar o qué camino tomar según el dato ingresado.


## Requisitos

- Python 3.x

## Uso

```bash
python registro_cuenta.py
```