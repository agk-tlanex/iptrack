import os
import requests
from utils import banners
from utils import printcolor

URL = "https://api.ipquery.io/"

def track(ip=None, me=None):
    if ip:
        os.system('cls' if os.name == 'nt' else 'clear')
        banners.random_banner()
        str(ip)

        IPURL = URL + ip
        response = requests.get(url=IPURL)

        status = str(response.status_code)
        if response.status_code == 200 or response.status_code == 201:
            data = response.json()
            printcolor.printl(f"IP: {data['ip']}", justify="left", style="green")

            printcolor.printl(f"╔═════════════════════════╗", justify="center", style="green")
            printcolor.printl(f"║    P R O V E E D O R    ║", justify="center", style="green")
            printcolor.printl(f"╚═════════════════════════╝", justify="center", style="green")
            printcolor.printl(f"ASN: {data['isp']['asn']}", justify="left", style="green")
            printcolor.printl(f"ORG: {data['isp']['org']}", justify="left", style="green")
            printcolor.printl(f"ISP: {data['isp']['isp']}", justify="left", style="green")

            printcolor.printl(f"╔═════════════════════════╗", justify="center", style="green")
            printcolor.printl(f"║    U B I C A C I Ó N    ║", justify="center", style="green")
            printcolor.printl(f"╚═════════════════════════╝", justify="center", style="green")
            printcolor.printl(f"País: {data['location']['country']}", justify="left", style="green")
            printcolor.printl(f"Código: {data['location']['country_code']}", justify="left", style="green")
            printcolor.printl(f"Ciudad: {data['location']['city']}", justify="left", style="green")
            printcolor.printl(f"Estado: {data['location']['state']}", justify="left", style="green")
            printcolor.printl(f"Latitud: {data['location']['latitude']}", justify="left", style="green")
            printcolor.printl(f"Longitud: {data['location']['longitude']}", justify="left", style="green")
            printcolor.printl(f"Zona Horaria: {data['location']['timezone']}", justify="left", style="green")
            printcolor.printl(f"Hora local: {data['location']['localtime']}", justify="left", style="green")

            if me == 1:
                printcolor.printl(f"╔═════════════════════════╗", justify="center", style="green")
                printcolor.printl(f"║           M E           ║", justify="center", style="green")
                printcolor.printl(f"╚═════════════════════════╝", justify="center", style="green")
                printcolor.printl(f"Movil: {data['risk']['is_mobile']}", justify="left", style="green")
                printcolor.printl(f"VPN: {data['risk']['is_vpn']}", justify="left", style="green")
                printcolor.printl(f"Tor: {data['risk']['is_tor']}", justify="left", style="green")
                printcolor.printl(f"Proxy: {data['risk']['is_proxy']}", justify="left", style="green")
            else:
                pass
            printcolor.printl("Presiona » [blink bold green]Enter[/blink bold green] « para continuar...", justify="left", style="green")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')


        elif response.status_code == 400:
            banners.banner_error()
            printcolor.printl(f"Error: Solicitud incorrecta.", justify="left", style="red")
            printcolor.printl(f"Error descripción: IP o formato no válido.", justify="left", style="red")
            printcolor.printl(f"Code: {status}", justify="left", style="red")
            printcolor.printl("Presiona » [blink bold green]Enter[/blink bold green] « para continuar...", justify="left", style="green")
            input()


        elif response.status_code == 404:
            banners.banner_error()
            printcolor.printl(f"Error: No encontrado.", justify="left", style="red")
            printcolor.printl(f"Error descripción: Recurso no encontrado.", justify="left", style="red")
            printcolor.printl(f"Code: {status}", justify="left", style="red")
            printcolor.printl("Presiona » [blink bold green]Enter[/blink bold green] « para continuar...", justify="left", style="green")
            input()
        
        elif response.status_code == 429:
            banners.banner_error()
            printcolor.printl(f"Error: Demasiadas solicitudes.", justify="left", style="red")
            printcolor.printl(f"Error descripción: Se ha excedido el límite de solicitudes.", justify="left", style="red")
            printcolor.printl(f"Code: {status}", justify="left", style="red")
            printcolor.printl("Presiona » [blink bold green]Enter[/blink bold green] « para continuar...", justify="left", style="green")
            input()
        
        elif response.status_code == 500:
            banners.banner_error()
            printcolor.printl(f"Error: Error interno.", justify="left", style="red")
            printcolor.printl(f"Error descripción: Error interno del servidor.", justify="left", style="red")
            printcolor.printl(f"Code: {status}", justify="left", style="red")
            printcolor.printl("Presiona » [blink bold green]Enter[/blink bold green] « para continuar...", justify="left", style="green")
            input()
    
    else:
        banners.banner_error()
        printcolor.printl(f"Error: Faltan datos.", justify="left", style="red")
        printcolor.printl(f"Error descripción: Ingrese una dirección IP valida.", justify="left", style="red")
        printcolor.printl(f"Code: 000", justify="left", style="red")
        printcolor.printl("Presiona » [blink bold green]Enter[/blink bold green] « para continuar...", justify="left", style="green")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        pass

def trackme():
    os.system('cls' if os.name == 'nt' else 'clear')
    response = requests.get('https://api.ipquery.io/')
    ip = response.text
    track(ip=ip, me=1)
