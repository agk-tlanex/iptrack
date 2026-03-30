import os
from utils import printcolor
from utils import banners
from utils import iptracker

def extras():
    pass

def main():
    counter = ""
    while counter != 0:
        try:
            banners.main_banner()
            printcolor.println("[blink bold yellow]Nota:[/blink bold yellow] La IP debe ser una IP pública, de lo contrario\nla información puede no ser correcta", justify="center", style="yellow")
            printcolor.printl("╔═══════════════════════════╗", justify="center", style="green")
            printcolor.printl("║                           ║", justify="center", style="green")
            printcolor.printl("║          [bold green]M E N U[/bold green]          ║", justify="center", style="green")
            printcolor.printl("║                           ║", justify="center", style="green")
            printcolor.printl("║  [ TRACKER ]       » 1 «  ║", justify="center", style="green")
            printcolor.printl("║  [ TRACK ME ]      » 2 «  ║", justify="center", style="green")
            printcolor.printl("║  [ EXTRAS ]        » 3 «  ║", justify="center", style="green")
            printcolor.printl("║  [ EXIT ]          » 0 «  ║", justify="center", style="green")
            printcolor.printl("║                           ║", justify="center", style="green")
            printcolor.printl("╚═══════════════════════════╝", justify="center", style="green")

            try:
                cursor = int(input("TRACK MENU>>> "))
                match(cursor):
                    case 1:
                        try:
                            cursor = str(input("TRACK IP>>> "))
                            iptracker.track(ip=cursor)
                        except Exception as e:
                            print("\n")
                            printcolor.println("ERROR", justify="left", style="bold red")
                            printcolor.printl("Presiona » [blink bold green]Enter[/blink bold green] « para continuar...", justify="left", style="green")
                            input()
                    
                    case 2:
                        try:
                            iptracker.trackme()
                        except Exception as e:
                            print("\n")
                            printcolor.println("ERROR", justify="left", style="bold red")
                            printcolor.printl("Presiona » [blink bold green]Enter[/blink bold green] « para continuar...", justify="left", style="green")
                            input()
                    
                    case 3:
                        try:
                            extras()
                        except Exception as e:
                            print("\n")
                            printcolor.println("ERROR", justify="left", style="bold red")
                            printcolor.printl("Presiona » [blink bold green]Enter[/blink bold green] « para continuar...", justify="left", style="green")
                            input()
                    
                    case 0:
                        print("\n")
                        printcolor.println("B Y E ! ! !", justify="center", style="bold red")
                        printcolor.printl("Presiona » [blink bold green]Enter[/blink bold green] « para salir...", justify="left", style="green")
                        input()
                        break
            except Exception as e:
                print("\n")
                printcolor.printl("[blink bold red]ERROR:[/blink bold red] Ingresa una opción válida", justify="left", style="red")
                printcolor.printl("Presiona » [blink bold green]Enter[/blink bold green] « para continuar...", justify="left", style="green")
                input()


        except KeyboardInterrupt as e:
            print("\n")
            printcolor.println("B Y E ! ! !", justify="center", style="bold red")
            printcolor.printl("Presiona » [blink bold green]Enter[/blink bold green] « para salir...", justify="left", style="green")
            input()
            break

main()