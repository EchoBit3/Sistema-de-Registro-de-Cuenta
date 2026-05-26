cuentas = []
 
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
    while True:
        print("\n-- Crear cuenta --")
 
        nombre = input("Nombre: ")
        while not nombre:
            nombre = input("Nombre inválido. Ingrese nombre: ")
 
        ap_paterno = input("Apellido paterno: ")
        while not ap_paterno:
            ap_paterno = input("Apellido paterno inválido. Intente de nuevo: ")
 
        ap_materno = input("Apellido materno: ")
        while not ap_materno:
            ap_materno = input("Apellido materno inválido. Intente de nuevo: ")
 
        rut = input("RUT (ej: 12345678-5): ")
        while not existe_RUT(rut):
            rut = input("RUT inválido. Intente de nuevo: ")
 
        contrasena = input("Contraseña (mín. 8 caracteres): ")
        while not contrasena_valida(contrasena):
            contrasena = input("Contraseña inválida. Intente de nuevo: ")
 
        RegistrarDatos(nombre, ap_paterno, ap_materno, rut, contrasena)
        print("-- Cuenta creada --")
 
        opcion = input("¿Crear otra cuenta? (Si/No): ")
        if opcion != "Si":
            break
 
main()