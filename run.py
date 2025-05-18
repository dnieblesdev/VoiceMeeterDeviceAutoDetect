import time
import voicemeeterlib
import os

# Opcional
PROFILE_PATH = ""


def obtener_dispositivos_asignados(vm):
    dispositivos_asinados = {}
    for i in range(3):
        try:
            nombre_dispositivo = vm.bus[i].device.name
            if nombre_dispositivo:
                dispositivos_asinados[f"A{i+1}"] = nombre_dispositivo
                print(f"[A{i+1}] Dispositivo asignado: {dispositivos_asinados[f'A{i+1}']}")
        except Exception as e:
            print(f"[A{i+1}] Error al obtener el dispositivo asignado: {e}")
            continue
    return dispositivos_asinados


def obtener_dispositivos_out_disponibles(vm):
    dispositivos_disponibles = []
    for dispositivo_out in range(vm.device.outs):
        try:
            informacion_dispositivo = vm.device.output(dispositivo_out)
            if 'name' in informacion_dispositivo:
                dispositivos_disponibles.append(informacion_dispositivo["name"])
        except Exception as e:
            continue
    return dispositivos_disponibles


def main():
    KIND_ID = "banana"
    # Obtener los dispositivos asignados a las salidas
    with voicemeeterlib.api(KIND_ID) as vm:
        try:
            
            dispositivos_asignados = obtener_dispositivos_asignados(vm)
            print("Dispositivos asignados a la salida.")
            for bus, dispositivo in dispositivos_asignados.items():
                print(f"{bus}: {dispositivo}")
            
            disconnected = set()

            while True:
                dispositivos_disponibles = obtener_dispositivos_out_disponibles(vm)

                for bus, dispositivo in dispositivos_asignados.items():
                    # Verificar si el dispositivo asignado está disponible
                    if dispositivo not in dispositivos_disponibles:
                        if bus not in disconnected:
                            print(
                                f"[{bus}] El dispositivo {dispositivo} está desconectado."
                            )
                            disconnected.add(bus)
                    else:
                        # Si el dispositivo está disponible y estaba desconectado, lo reconectamos
                        if bus in disconnected:
                            print(
                                f"[{bus}] El dispositivo {dispositivo} ha sido reconectado."
                            )
                            disconnected.remove(bus)

                            # Reiniciar el motor de audio para que se active el dispositivo
                            print(
                                f"Reiniciando el motor de audio VoiceMeeter para {bus}..."
                            )
                            vm.command.restart()

                        # IDEA (Cargar un perfil en el momento en el que se conecta un dispositivo)
                        # PROFILE_PATH esta vació para que no cargue nada
                        if PROFILE_PATH and os.path.isfile(PROFILE_PATH):
                            print(f"Cargando perfil {PROFILE_PATH}...")
                            vm.command.load_profile(PROFILE_PATH)

                time.sleep(5)  # Esperar 5 segundos antes de volver a comprobar
        except Exception as e:
            print(f"Error {e}")
        finally:
            print("Deslogeando de VoiceMeeter...")
            vm.logout()


if __name__ == "__main__":
    main()
