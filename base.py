#Juan Pablo Zamarripa Martinez IRE 4.2
#Conexion con un servicio HTTP y  ssh

from netmiko import ConnectHandler
from netmiko.exception import NetmikoTimeOutException, NetmikoAuthentication

#Definimos los parametros para la conexion
device = {
    'device_type':'cisco_ios',
    'host':'devnetsandboxiosec8k.cisco.com',
    'username':'rmacias',
    'password':'&i0&IbteRCH7^7',
    'port':22
}
#El try sirve para generar una excepcion
try:
    #Establecemos la conexion SSH
    net_connect = ConnectHandler(**device)
    #La f aqui nos permite ingresar eso que esta en corchetes 
    #Lo de corchetes es una variable y la f permite leerlo sino todo seria texto
    print(f"Conectado exitosamente a {device['host']}")

    #Ejecucion de comandos de lectura
    output_show = net_connect.send_command("show ip interface brief")
    print("----Esstado de Interfaces---")
    print(output_show)

    #Envio de comandos de configuracion
    config_commands = {
        'interface Loopback100',
        'description Interface creada via Python Netmiko',
        'ip address 10.100.100.1 255.255.255.0',
        'no shutdown'
    }

    output_config=net_connect.send_config_set(config_commands)
    print("---Aplicacndo la configuracion---")
    print(output_config)

    #Cierre de la sesion
