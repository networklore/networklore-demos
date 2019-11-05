import sys

from nornir import InitNornir
from nornir.plugins.tasks import files, text
from nornir.plugins.functions.text import print_result




def generate(task):
    template = task.run(
        task=text.template_file,
        name="Render",
        template="nornir-base.j2",
        path="templates",
    )
    task.run(
        task=files.write_file,
        name="Write",
        filename=f"output/nornir/{task.host}.cfg",
        content=template.result,
    )


def main(inventory_size):
    nornir = InitNornir(
        inventory={"options": {"host_file": f"nornir-inventory-{inventory_size}.yaml"}}, dry_run=False
    )
    result = nornir.run(task=generate)
    print_result(result)


if __name__ == "__main__":
    inventory_size = int(sys.argv[1])
    main(inventory_size)
