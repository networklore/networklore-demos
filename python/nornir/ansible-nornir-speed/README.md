Sample files for the article [Ansible vs. Nornir: Speed Challenge](https://networklore.com/ansible-nornir-speed/).

### Install requirements

```bash
pip install -r requirements.txt
```

### Test Ansible

```bash
time ansible-playbook -i ansible-inventory-100.yaml ansible-run.yaml
time ansible-playbook -i ansible-inventory-1000.yaml ansible-run.yaml
time ansible-playbook -i ansible-inventory-5000.yaml ansible-run.yaml
time ansible-playbook -i ansible-inventory-10000.yaml ansible-run.yaml
```

### Test Nornir
```bash
time python3 nornir-run.py 100
time python3 nornir-run.py 1000
time python3 nornir-run.py 5000
time python3 nornir-run.py 10000
```

### Generate inventory file

Generate a new inventory with 500 hosts:

```bash
python generate_inventory.py 500
```

