# Sistema de Registro de Cuenta

Proyecto en Python basado en un Diagrama de Flujo de Datos. Implementa un flujo de registro con validación en cada etapa, donde cada campo se repite hasta cumplir su condición antes de avanzar al siguiente.

## ¿Qué hace?

- Valida nombre y apellidos
- Verifica el RUT/DNI con su dígito verificador
- Exige una contraseña con requisitos mínimos de seguridad
- Lleva un registro de intentos fallidos por sesión

## Requisitos

- Python 3.x

## Uso

```bash
python registro_cuenta.py
```