# 🌐 IP Tracker CLI

> Herramienta de línea de comandos para rastrear información pública de direcciones IP, incluyendo ubicación geográfica, proveedor de red y detección de riesgos como VPN, proxy y Tor.

---

## ✨ Características

| Funcionalidad | Descripción |
|---|---|
| 🔍 Rastreo de IP | Consulta cualquier dirección IP pública |
| 📍 Geolocalización | País, ciudad, estado, coordenadas, zona horaria |
| 🌐 Info de red | ASN, organización e ISP |
| 🛡️ Detección de riesgos | VPN, proxy, Tor y redes móviles |
| 🖥️ Interfaz interactiva | Menú CLI amigable |
| 🎨 Salida estilizada | Renderizado con `rich` |

---

## ⚙️ Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/ip-tracker-cli.git
cd ip-tracker-cli
```

### 2. Instala las dependencias

```bash
pip install -r requirements.txt
```

> **Requisitos:** Python 3.8 o superior.

---

## 🚀 Uso

Ejecuta el programa:

```bash
python iptrack.py
```

### Menú principal

```
[ TRACKER  ]  » 1 «  → Rastrear una IP específica
[ TRACK ME ]  » 2 «  → Obtener información de tu propia IP
[ EXTRAS   ]  » 3 «  → Funciones adicionales (próximamente)
[ EXIT     ]  » 0 «  → Salir
```

---

## 🔎 Ejemplos de uso

### Opción 1 — Rastrear una IP

```
TRACK IP>>> 8.8.8.8
```

**Datos obtenidos:**

- Dirección IP
- ISP (ASN y organización)
- País, ciudad y estado
- Latitud y longitud
- Zona horaria y hora local

### Opción 2 — Rastrear tu propia IP

Además de la información anterior, incluye detección de:

- ✅ / ❌ VPN activa
- ✅ / ❌ Proxy detectado
- ✅ / ❌ Red Tor
- ✅ / ❌ Conexión móvil

---

## 🧰 Dependencias

```
requests
rich
Pygments
markdown-it-py
```

> Ver [`requirements.txt`](./requirements.txt) para versiones específicas.

---

## 🔌 API utilizada

Este proyecto utiliza la API pública de **ipquery.io**:

```
https://api.ipquery.io/
```

No se requiere API key para uso básico. Consulta su [documentación oficial](https://ipquery.io) para límites de uso.

---

## ⚠️ Consideraciones importantes

- Solo funciona correctamente con **IPs públicas**.
- Las IPs privadas (ej. `192.168.x.x`, `10.x.x.x`) no retornan información válida.
- La precisión geográfica depende de los datos del proveedor de la API.
- El uso excesivo puede estar sujeto a límites de tasa (*rate limiting*).

---

## 🛠️ Roadmap

- [ ] Implementar funciones de la opción **EXTRAS**
- [ ] Manejo de errores más detallado (timeouts, IPs inválidas, etc.)
- [ ] Exportar resultados a JSON o CSV
- [ ] Historial de consultas con búsqueda
- [ ] Soporte para consultas en lote (múltiples IPs a la vez)
- [ ] Modo silencioso (`--quiet`) para integración con scripts

---

## 📄 Licencia

Este proyecto es de uso libre para fines **educativos y personales**.  
Si lo usas en un proyecto propio, ¡una mención siempre es bienvenida! 🙌
