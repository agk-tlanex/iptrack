# 🌐 IP Tracker CLI

> Herramienta de línea de comandos para rastrear información pública de direcciones IP, incluyendo ubicación geográfica, proveedor de red y detección de riesgos como VPN, proxy y Tor.

---

## ✨ Características

| Funcionalidad | Descripción |
|---|---|
| 🔍 Rastreo de IP | Consulta cualquier dirección IP pública |
| 📍 Geolocalización | País, ciudad, estado, coordenadas, zona horaria y hora local |
| 🌐 Info de red | ASN, organización e ISP |
| 🛡️ Detección de riesgos | VPN, proxy, Tor y redes móviles |
| 🖥️ Interfaz interactiva | Menú CLI con navegación por teclado |
| 🎨 Salida estilizada | Renderizado con `rich` |

---

## 📁 Estructura del proyecto

```
ip-tracker-cli/
├── main.py          # Punto de entrada, menú principal
├── requirements.txt    # Dependencias del proyecto
└── utils/
    ├── iptracker.py    # Lógica de consulta a la API
    ├── banners.py      # Banners ASCII decorativos
    └── printcolor.py   # Utilidades de impresión con rich
```

---

## ⚙️ Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/ip-tracker.git
cd ip-tracker
```

### 2. Instala las dependencias

```bash
pip install -r requirements.txt
```

> **Requisitos:** Python 3.10 o superior (se usa `match/case`).

---

## 🚀 Uso

Ejecuta el programa:

```bash
python main.py
```

### Menú principal

```
[ TRACKER  ]  » 1 «  → Rastrear una IP específica
[ TRACK ME ]  » 2 «  → Obtener información de tu propia IP
[ EXTRAS   ]  » 3 «  → Redes sociales del autor
[ EXIT     ]  » 0 «  → Salir
```

> Puedes interrumpir el programa en cualquier momento con `Ctrl+C`.

---

## 🔎 Ejemplos de uso

### Opción 1 — Rastrear una IP

```
TRACK IP>>> 8.8.8.8
```

**Datos obtenidos:**

- Dirección IP
- ISP: ASN, organización y proveedor
- Ubicación: país, código de país, ciudad y estado
- Coordenadas: latitud y longitud
- Zona horaria y hora local

### Opción 2 — Rastrear tu propia IP

Detecta automáticamente tu IP pública y muestra, además de los datos anteriores:

- 📱 Si estás en una red móvil
- 🔒 Si usas VPN
- 🧅 Si estás en la red Tor
- 🕵️ Si tu tráfico pasa por un proxy

---

## 🛡️ Manejo de errores

El programa detecta y muestra mensajes descriptivos para los siguientes códigos HTTP:

| Código | Descripción |
|---|---|
| `400` | IP o formato no válido |
| `404` | Recurso no encontrado |
| `429` | Límite de solicitudes excedido |
| `500` | Error interno del servidor |
| `000` | No se ingresó ninguna IP |

---

## 🧰 Dependencias

```
requests==2.33.1
rich==14.3.3
```

> Ver [`requirements.txt`](./requirements.txt) para la lista completa con versiones fijadas.

---

## 🔌 API utilizada

Este proyecto utiliza la API pública de **ipquery.io**:

```
https://api.ipquery.io/
```

No se requiere API key para uso básico. Consulta su [documentación oficial](https://ipquery.io) para información sobre límites de uso y *rate limiting*.

---

## ⚠️ Consideraciones importantes

- Solo funciona correctamente con **IPs públicas**.
- Las IPs privadas (ej. `192.168.x.x`, `10.x.x.x`) no retornan información válida.
- La precisión geográfica depende de los datos del proveedor de la API.
- El uso excesivo puede estar sujeto a límites de tasa (*rate limiting*, código `429`).

---

## 👤 Autor

Creado por **agk-tlanex**

[![GitHub](https://img.shields.io/badge/GitHub-agk--tlanex-181717?logo=github)](https://github.com/agk-tlanex)
[![TikTok](https://img.shields.io/badge/TikTok-@agk.tlanex-000000?logo=tiktok)](https://www.tiktok.com/@agk.tlanex)
[![Instagram](https://img.shields.io/badge/Instagram-@agk.tlanex-E4405F?logo=instagram)](https://www.instagram.com/agk.tlanex)
[![YouTube](https://img.shields.io/badge/YouTube-agk.tlanex-FF0000?logo=youtube)](https://www.youtube.com/channel/UCtp5Yi8hXZmvECXEPMiufRw)

