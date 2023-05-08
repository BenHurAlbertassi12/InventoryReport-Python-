import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    __report_types = {
        "simples": SimpleReport,
        "completo": CompleteReport
    }

    def import_data(arq: str, rep_type: str):
        with open(arq, "r") as file:
            data = []

            if arq.endswith(".json"):
                content = file.read()
                data = json.loads(content)

            elif arq.endswith(".csv"):
                content = csv.DictReader(file, delimiter=",", quotechar='"')
                data = [row for row in content]

            elif arq.endswith(".xml"):
                content = file.read()
                parse = xmltodict.parse(content)
                data = parse["dataset"]["record"]

        class_type = Inventory.__report_types[rep_type]
        report = class_type.generate(data)
        return report
