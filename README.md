# 🌐 IP Tracker CLI

Herramienta en línea de comandos para rastrear información pública de direcciones IP utilizando la API de **ipquery.io**. Permite consultar datos de ubicación, proveedor de red y riesgos asociados (VPN, proxy, etc.).

---

## 📦 Características

- 🔍 Búsqueda de información de cualquier IP pública  
- 📍 Obtiene ubicación geográfica (país, ciudad, estado, coordenadas)  
- 🌐 Información del ISP (ASN, organización, proveedor)  
- 🛡️ Detección de:
  - VPN
  - Proxy
  - Tor
  - Dispositivos móviles  
- 🖥️ Interfaz CLI interactiva con menú  
- 🎨 Salida estilizada usando `rich`

---

## ⚙️ Instalación

1. Clona el repositorio:

```bash```
git clone https://github.com/tu-usuario/ip-tracker-cli.git
cd ip-tracker-cli
Instala las dependencias:
pip install -r requirements.txt
🚀 Uso

Ejecuta el programa:

python iptrack.py

Menú principal
[ TRACKER ]  » 1 «  → Rastrear una IP
[ TRACK ME ] » 2 «  → Obtener tu propia IP e información
[ EXTRAS ]   » 3 «  → Funciones adicionales (no implementadas)
[ EXIT ]     » 0 «  → Salir
🔎 Ejemplo de uso
Rastrear una IP
Selecciona opción 1
Ingresa una IP pública:
TRACK IP>>> 8.8.8.8

📊 Obtendrás:

IP
ISP (ASN, organización)
País, ciudad, estado
Latitud y longitud
Zona horaria
Hora local
📡 Rastrear tu propia IP

Selecciona opción 2

Incluye información adicional:

Uso de VPN
Proxy
Red Tor
Si es móvil
⚠️ Notas importantes
Solo funciona correctamente con IPs públicas
Las IPs privadas (ej. 192.168.x.x) no devolverán información válida
La precisión de la ubicación depende del proveedor de la API
🧰 Dependencias
requests
rich
Pygments
markdown-it-py

(Ver requirements.txt para versiones específicas)

🔌 API utilizada
https://api.ipquery.io/
🛠️ Pendiente / Mejoras
Implementar opción EXTRAS
Manejo más detallado de errores
Exportar resultados a JSON o archivo
Historial de consultas
📄 Licencia

Este proyecto es de uso libre para fines educativos y personales.
