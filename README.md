# Que es VoiceMeeter Device Auto Detect?
Es una pequeña aplicación - servicio, que te ayuda a que en el momento en el que se detecta que cualquier de los Hardware outputs (A1, A2, A3) se ha reconectado, automaticamente se reinicia el engine. 

*Por ahora esa es su función principal.*


## Requisitos
* Python 3.10+

## Como usar?

### Instalar un virtual environment de python con el comando

```powershell
py -m venv .env
```

### Activar Entorno Virtual
```powershell
.\.env\Scripts\activate
```

### Instalar dependencia VoiceMeeter API

```powershell
pip install voicemeeter-api o pip install -r requirements.txt

```
### Iniciar

```powershell
py .\run.py
```
