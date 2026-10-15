# this the python code for vlan configuration

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.10.10",
    "username": "admin",
    "password": "password123",
}

connection = ConnectHandler(**device)

commands = [
    "vlan 100",
    "name USERS",
    "vlan 200",
    "name SERVERS"
]

connection.send_config_set(commands)

connection.disconnect()