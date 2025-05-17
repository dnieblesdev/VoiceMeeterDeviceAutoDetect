import time
import voicemeeterlib
import os

def obtener_dispositivos_asignados(vm):
    asignados = {}
    for i in range(3):
        try:
            nombre_dispositivo = vm.bus[i].device.name
            if nombre_dispositivo:
                asignados[f'A{i+1}'] = nombre_dispositivo
                print(f"Dispositivo asignado a A{i+1}: {nombre_dispositivo}")
        except Exception as e:
            print(f"Error al obtener el dispositivo asignado a A{i+1}: {e}")
            continue
    return asignados

def main():
    # Obtener los dispositivos asignados a las salidas
    with voicemeeterlib.api('banana') as vm:
        dispositivos_asignados = obtener_dispositivos_asignados(vm)
        print("Dispositivos asignados a la salida.")
        for bus, dispositivo in dispositivos_asignados:
            print(f"{bus}: {dispositivo}")
        

        



if (__name__ == "__main__"):
    main()


