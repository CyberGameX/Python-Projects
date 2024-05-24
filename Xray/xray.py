import requests
import os
import subprocess
import nmap
import json
import socket
from tabulate import tabulate
import threading


def who_is_api():
    while True:
        target = input("Enter an IP address or domain name: ")
        try:
            ip_address = socket.gethostbyname(target)
            break
        except socket.error:
            try:
                ip_address = target
                if len(ip_address.split(".")) != 4:
                    raise ValueError
                break
            except ValueError:
                print("Invalid IP format. Please enter a valid IP address (e.g., 8.8.8.8) or domain name.")

    url = f"https://ipinfo.io/{ip_address}/json"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content)
            return data
        else:
            print(f"API request failed: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"  # Use this green color code
YELLOW = "\033[93m"
PURPLE = '\033[0;35m'
CYAN = "\033[36m"
END = "\033[0m"


# Banner
def program_banner_xray():
    """
  Prints a pre-defined banner in green color.
  """
    banner = f"""
  {GREEN}                              
░░███ ░░███                                
 ░░███ ███   ████████   ██████   █████ ████
  ░░█████   ░░███░░███ ░░░░░███ ░░███ ░███ 
   ███░███   ░███ ░░░   ███████  ░███ ░███ 
  ███ ░░███  ░███      ███░░███  ░███ ░███ 
 █████ █████ █████    ░░████████ ░░███████ 
░░░░░ ░░░░░ ░░░░░      ░░░░░░░░   ░░░░░███ 
                                  ███ ░███ 
                                 ░░██████  
                                  ░░░░░░    
"""

    print(f"{GREEN}{banner}{END}")


def about_me():
    print("Name: CyberSec")
    print("Location: Germany")
    print("Interests: Cybersecurity")
    print("\nA bit more about me:")
    print(
        "I am passionate about all things related to cybersecurity. I spend most of my time exploring new "
        "technologies and trends in the cybersecurity field. I believe that continuous learning and staying updated "
        "with the latest security threats is the key to being effective in this field.")
    print("I am always open to connect with like-minded individuals who share the same passion for cybersecurity.")


def arp_tabular():
    try:
        command = os.system(f"powershell.exe arp -a")
        print(command)
    except ValueError as e:
        print(f"An error occurred: {e}")


def getmac():
    try:
        ipaddress = input("Enter IP Address: ")
        command = f"powershell.exe getmac /s {ipaddress}"
        output = subprocess.check_output(command, shell=True).decode()
        print(output)
    except ValueError as e:
        print(f"An error occured while executing netsh {e}")


def grab_banner():
    # Benutzereingabe für die IP-Adresse
    ip_address = input("Please enter the IP address: ")

    # Erstellen Sie ein Nmap-Objekt
    nm = nmap.PortScanner()

    # Führen Sie einen "stealthy" SYN-Scan durch
    nm.scan(ip_address, arguments='-sS')

    # Überprüfen Sie, ob Port 80 offen ist
    if nm[ip_address]['tcp'][80]['state'] == 'open':
        try:
            # Erstellen Sie ein Socket-Objekt
            s = socket.socket()

            # Verbinden Sie das Socket mit der IP-Adresse und dem Port
            s.connect((ip_address, 80))

            # Senden Sie eine HTTP-Anfrage
            request = b"HEAD / HTTP/1.1\r\nHost: " + ip_address.encode() + b"\r\n\r\n"
            s.send(request)

            # Empfangen Sie die Antwort des Servers
            response = s.recv(1024)

            # Teilen Sie die Antwort in Header und Body
            headers, body = response.split(b'\r\n\r\n', 1)

            # Erstellen Sie ein Dictionary für die Header
            headers_dict = {}
            for header in headers.split(b'\r\n'):
                if b': ' in header:
                    key, value = header.split(b': ', 1)
                    headers_dict[key.decode()] = value.decode()

            # Drucken Sie die Header als JSON
            print(json.dumps(headers_dict, indent=2))
        except Exception as e:
            print(f"Fehler beim Abrufen des Headers: {str(e)}")
    else:
        print(f"Port 80 is not open on {ip_address}")


def ipconfig():
    print("Ipconfig is running")
    """
    Displays current ipconfig from windows with the adapters
    :return:
    """
    print("-" * 80)
    os.system("ipconfig")
    print("-" * 80)
    print("Show all Adapters:")
    print()
    os.system("ipconfig /all")
    print("-" * 80)
    print("Routing Tabuallar")
    os.system("netstat -r")
    print("-" * 80)


def nbtstat():
    try:
        ip_address = input("Enter IP Address: ")
        command = f"powershell.exe nbtstat -A {ip_address}"
        output = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(output.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")


def netsh():
    try:
        command = "powershell.exe  netsh interface show interface"
        output = subprocess.check_output(command, shell=True).decode()
        print(output)
    except ValueError as e:
        print(f"An error occured while executing netsh {e}")


def netstat():
    os.system('netstat -an')


def nslookup():
    """
    Nslookup to ip or domain address
    :return:
    """
    target_host = input("Enter Target Host: ")
    command = f"nslookup {target_host}"
    output = os.system(command)
    print(output)


def pathping():
    try:
        ipaddress = input("Enter IP Address: ")
        command = os.system(f"powershell.exe pathping {ipaddress}")
        print(command)
    except ValueError as e:
        print(f"An error occurred: {e}")


def ping():
    target_host = input("Enter Ip address or Domain Name: ")
    command = f"ping {target_host}"
    output = os.system(command)
    print(output)


def scan_port(host, port, description, results):
    try:
        s = socket.socket()
        s.settimeout(1)

        s.connect((host, port))
    except socket.timeout:
        # Wenn die Verbindung fehlschlägt, ist der Port gefiltert
        results.append([port, description, '\033[33mfilterd\033[0m', ''])
    except ConnectionRefusedError:
        # Wenn die Verbindung fehlschlägt, ist der Port geschlossen
        results.append([port, description, '\033[31mclosed\033[0m', ''])
    else:
        # Wenn die Verbindung erfolgreich ist, ist der Port offen
        nm = nmap.PortScanner()
        os_result = nm.scan(host, arguments='-O')
        if host in os_result['scan'] and 'osmatch' in os_result['scan'][host]:
            os_info = os_result['scan'][host]['osmatch'][0]['name']
        else:
            os_info = 'Not recognized'
        results.append([port, description, '\033[32mopen\033[0m', os_info])
    finally:
        s.close()


def port_scanner():
    host_input = input("Input a host to scan: ")

    try:
        host = socket.gethostbyname(host_input)
    except socket.gaierror:
        print(f"Cant resolve {host_input}")
        return

    ports = {
        20: 'FTP Datatransfer',
        21: 'FTP Controller Connection',
        22: 'SSH',
        23: 'Telnet',
        25: 'SMTP',
        53: 'DNS',
        80: 'HTTP',
        110: 'POP3',
        111: 'RPCBIND',
        113: 'AUTH',
        143: 'IMAP',
        443: 'HTTPS',
        445: 'Microsoft-DS (Active Directory, Windows shares, Sasser worm, Agobot worm)',
        631: 'IPP',
        1433: 'Microsoft SQL Server',
        2601: 'ZEBRA',
        3306: 'MySQL',
        3389: 'Remote Desktop Protocol (RDP)',
        5357: 'Wsdapi',
        8080: 'HTTP-Proxy',
        32774: 'RPC11'
    }
    results = []

    print(f"The Portscan has been started on host {host_input} this can take a while...")

    threads = []
    for port, description in ports.items():
        thread = threading.Thread(target=scan_port, args=(host, port, description, results))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"Scan results for host:{host_input}")
    results.sort(key=lambda x: x[0])
    print(tabulate(results, headers=['Port', 'Beschreibung', 'Status', 'OS'], tablefmt='pretty'))


def subnet_lookup():
    # Benutzereingabe für die IP-Adresse und das Subnetz
    ip_subnet = input("Input the Ipaddress and Subnet mask in the CIDR-Notation (example "
                      "192.168.178.1/24): ")

    # Trennen Sie die IP-Adresse und die Subnetzmaske
    ip, subnet = ip_subnet.split('/')
    subnet = int(subnet)

    # Konvertieren Sie die IP-Adresse in eine binäre Darstellung
    ip_binary = ''.join([bin(int(x) + 256)[3:] for x in ip.split('.')])

    # Berechnen Sie die Netzwerkdetails mit Bitoperationen
    network_binary = ip_binary[:subnet] + '0' * (32 - subnet)
    network = '.'.join(str(int(network_binary[i:i + 8], 2)) for i in range(0, 32, 8))

    netmask_binary = '1' * subnet + '0' * (32 - subnet)
    netmask = '.'.join(str(int(netmask_binary[i:i + 8], 2)) for i in range(0, 32, 8))

    broadcast_binary = ip_binary[:subnet] + '1' * (32 - subnet)
    broadcast = '.'.join(str(int(broadcast_binary[i:i + 8], 2)) for i in range(0, 32, 8))

    wildcard_mask_binary = '0' * subnet + '1' * (32 - subnet)
    wildcard_mask = '.'.join(str(int(wildcard_mask_binary[i:i + 8], 2)) for i in range(0, 32, 8))

    hosts_bits = 32 - subnet
    max_hosts = 2 ** hosts_bits - 2

    host_range = f"{network[:-1]}1 - {broadcast[:-1]}{int(broadcast[-1]) - 1}"

    # Ausgabe der Netzwerkdetails
    print(f"Address       = {ip}")
    print(f"Network       = {network} / {subnet}")
    print(f"Netmask       = {netmask}")
    print(f"Broadcast     = {broadcast}")
    print(f"Wildcard Mask = {wildcard_mask}")
    print(f"Hosts Bits    = {hosts_bits}")
    print(f"Max. Hosts    = {max_hosts}   (2^{hosts_bits} - 2)")
    print(f"Host Range    = {{ {host_range} }}")


def terms_of_service():
    print("\n" + "-" * 80)
    print("Terms of Service:")
    print("-" * 80)
    print("\n1. This program is intended for educational purposes only. Do not use it for illegal activities.")
    print("\n2. You should only perform attacks on devices you own or have permission to test.")
    print("\n3. The creator of this program is not responsible for any misuse of information provided by this program.")
    print("\n4. The user assumes all responsibility for any actions taken using this program.")
    print("\n5. By using this program, you agree to these terms.")
    print("\n" + "-" * 80 + "\n")


def traceroute():
    """
    traceroute to ip or domain address
    :return:
    """
    target_host = input("Target IP address or domain name: ")
    command = f"tracert {target_host}"
    output = (os.system(command))
    print(output)


def ip_info():
    """
    Outputs Who is look up from who_is API
    :return:
    """
    target_info = who_is_api()

    if target_info:
        print("-" * 40)
        print("Target Info:")
        print("-" * 40)
        print("Basic Information:")
        print(f"IP-Adress: {target_info['ip']}")
        print(f"Hostname: {target_info['hostname']}")
        print(f"Country: {target_info['country']}")
        print(f"Region: {target_info['region']}")
        print(f"City: {target_info['city']}")
        print(f"Location Long,Alt: {target_info['loc']}")
        print(f"Postal: {target_info['postal']}")
        print(f"Timezone: {target_info['timezone']}")
        print("-" * 40)
        print("Advanced Information:")
        print("-" * 40)
    else:
        print("Invalid IP format or API request failed.")


def menu_net_info():
    while True:
        print("\nNetwork Information Menu")
        print("-" * 100)
        print("[*]1. Port Scanner")
        print("[*]2. Traceroute")
        print("[*]3. HTTP Header")
        print("[*]4. Ping")
        print("[*]5. Whois Lookup")
        print("[*]6. Nslookup")
        print("[*]7. Subnet Calculator")
        print("[*]8. Return to Main Menu")
        print("-" * 100)

        option = input("Enter your option: ")

        try:
            if option == "1":
                port_scanner()
            elif option == "2":
                traceroute()
            elif option == "3":
                grab_banner()
            elif option == "4":
                ping()
            elif option == "5":
                who_is_api()
            elif option == "6":
                nslookup()
            elif option == "7":
                subnet_lookup()
            elif option == "8":
                print("Returning to main menu...")
                break
            else:
                print("Invalid option. Please select a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter the correct format.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


def menu_network_diagnostics_monitoring():
    while True:
        print("\nNetwork Diagnostics and Monitoring")
        print("-" * 100)
        print("[*]1. Netstat")
        print("[*]2. Nbtstat")
        print("[*]3. Netsh")
        print("[*]4. Getmac")
        print("[*]5. Pathping")
        print("[*]6. Ipconfig with Route tabular")
        print("[*]7. Arp Tabular")
        print("[*]8. Return to Main Menu")
        print("-" * 100)
        option = input("Enter your option: ")

        try:
            if option == "1":
                netstat()
            elif option == "2":
                nbtstat()
            elif option == "3":
                netsh()
            elif option == "4":
                getmac()
            elif option == "5":
                pathping()
            elif option == "6":
                ipconfig()
            elif option == "7":
                arp_tabular()
            elif option == "8":
                print("Returning to main menu...")
                break
            else:
                print("Invalid option. Please select a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter the correct format.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


def menu_program_info():
    while True:
        print("\nProgram Information Menu")
        print("Version 1.0")
        print("-" * 100)
        print("[*] 1. About Me")
        print("[*] 2. Terms of Service")
        print("[*] 3. Return to Main Menu")
        print("-" * 100)
        option = input("Enter your option: ")

        try:
            if option == "1":
                about_me()
            elif option == "2":
                terms_of_service()
            elif option == "3":
                print("Returning to main menu...")
                break
            else:
                print("Invalid option. Please select a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter the correct format.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


def main():
    program_banner_xray()

    while True:
        print("\nOptions:")
        print("-" * 200)
        print(" \nCreated by CyberSec Copyright \u00A9 2024")
        print("Main Menu")
        print("[*]1. Network Information")
        print("[*]2. Network Diagnostics and Monitoring")
        print("[*]3. Program Information")
        print("[*]4. EXIT")
        print("-" * 200)
        option = input("Enter your option: ")

        try:
            if option == "1":
                menu_net_info()
            elif option == "2":
                menu_network_diagnostics_monitoring()
            elif option == "3":
                menu_program_info()
            elif option == "4":
                print("Exiting...")
                quit()
            else:
                print("Invalid option. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter the correct format.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
