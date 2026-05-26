cuentas = []
total_intentos = 0
 
def existe_RUT(rut):
    return "-" in rut and len(rut) >= 9
 
def contrasena_valida(contrasena):
    return len(contrasena) >= 8
 
def RegistrarDatos(nombre, ap_paterno, ap_materno, rut, contrasena):
    cuentas.append({
        "nombre": nombre,
        "ap_paterno": ap_paterno,
        "ap_materno": ap_materno,
        "rut": rut,
        "contrasena": contrasena
    })
 
def main():
    global total_intentos
 
    while True:
        print("\n-- Crear cuenta --")
        intentos = 0
 
        nombre = input("Nombre: ")
        while not nombre:
            intentos += 1
            nombre = input("Nombre inválido. Intente de nuevo: ")
 
        ap_paterno = input("Apellido paterno: ")
        while not ap_paterno:
            intentos += 1
            ap_paterno = input("Apellido paterno inválido. Intente de nuevo: ")
 
        ap_materno = input("Apellido materno: ")
        while not ap_materno:
            intentos += 1
            ap_materno = input("Apellido materno inválido. Intente de nuevo: ")
 
        rut = input("RUT (ej: 12345678-5): ")
        while not existe_RUT(rut):
            intentos += 1
            rut = input("RUT inválido. Intente de nuevo: ")
 
        contrasena = input("Contraseña (mín. 8 caracteres): ")
        while not contrasena_valida(contrasena):
            intentos += 1
            contrasena = input("Contraseña inválida. Intente de nuevo: ")
 
        RegistrarDatos(nombre, ap_paterno, ap_materno, rut, contrasena)
        total_intentos += intentos
 
        print(f"-- Cuenta creada (intentos fallidos: {intentos}) --")
 
        opcion = input("¿Crear otra cuenta? (Si/No): ")
        if opcion != "Si":
            break
 
    print(f"\nCuentas registradas: {len(cuentas)}")
    print(f"Total intentos fallidos: {total_intentos}")
    print(f"Promedio de intentos por cuenta: {total_intentos / len(cuentas):.1f}")
 
main()