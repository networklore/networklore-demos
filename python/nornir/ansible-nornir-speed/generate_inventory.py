import sys

import yaml
from faker import Faker


def main(num_hosts):
    fake = Faker()

    inventory = {}
    location = {}

    for _ in range(num_hosts):
        prefix = fake.state_abbr().lower()
        if prefix not in location:
            location[prefix] = 0
        location[prefix] += 1
        hostname = f"{prefix}-sw-{location[prefix]}"
        host = {}
        host["username"] = "networklore"
        host["password"] = "VeryS3cret!"
        host["mgmt_v4"] = fake.ipv4()
        host["mgmt_v6"] = fake.ipv6()
        if fake.pybool():
            host["subnet_mask"] = "255.255.255.0"
        else:
            host["subnet_mask"] = "255.255.255.128"
        host["mac_address"] = fake.mac_address()
        host["location"] = prefix
        host["building"] = fake.building_number()
        host["serial"] = fake.md5().upper()
        if fake.pybool():
            host["os"] = "ios"
        else:
            host["os"] = "junos"

        inventory[hostname] = host

    ansible = {}
    ansible["all"] = {}
    ansible["all"]["hosts"] = inventory

    with open(f"ansible-inventory-{num_hosts}.yaml", "w") as fobj:
        yaml.dump(ansible, fobj, default_flow_style=False)

    nornir = {}
    for host in inventory:
        nornir[host] = {}
        nornir[host]["hostname"] = host
        nornir[host]["username"] = inventory[host]["username"]
        nornir[host]["password"] = inventory[host]["password"]
        nornir[host]["platform"] = inventory[host]["os"]
        nornir[host]["data"] = {}
        nornir[host]["data"]["mgmt_v4"] = inventory[host]["mgmt_v4"]
        nornir[host]["data"]["mgmt_v6"] = inventory[host]["mgmt_v6"]
        nornir[host]["data"]["subnet_mask"] = inventory[host]["subnet_mask"]
        nornir[host]["data"]["mac_address"] = inventory[host]["mac_address"]
        nornir[host]["data"]["location"] = inventory[host]["location"]
        nornir[host]["data"]["building"] = inventory[host]["building"]
        nornir[host]["data"]["serial"] = inventory[host]["serial"]

    with open(f"nornir-inventory-{num_hosts}.yaml", "w") as fobj:
        yaml.dump(nornir, fobj, default_flow_style=False)


if __name__ == "__main__":
    inventory_size = int(sys.argv[1])
    main(inventory_size)
