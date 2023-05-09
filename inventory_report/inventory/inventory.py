import os.path
import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    def import_data(file: str, type: str) -> list[dict]:
        arquivo = os.path.splitext(file)[1].lower()
        if arquivo == ".csv":
            content = Inventory.import_csv_req_04(file)
        elif arquivo == ".json":
            content = Inventory.import_json_req_05(file)
        elif arquivo == ".xml":
            content = Inventory.import_xml_req_06(file)
        else:
            raise ValueError("Invalid")
        return Inventory.reports_generation(content, type)

    def import_csv_req_04(path: str) -> list[dict]:
        with open(path, "r") as file:
            return [row for row in csv.DictReader(file)]

    def import_json_req_05(path: str) -> list[dict]:
        with open(path, "r") as file:
            return json.load(file)

    def import_xml_req_06(path: str) -> list[dict]:
        return [
            {subitem.tag: subitem.text for subitem in item}
            for item in ET.parse(path).getroot()
        ]
    # https://docs.python.org/pt-br/3/library/xml.etree.elementtree.html

    def reports_generation(inventory: list[dict], type: str) -> list[dict]:
        if type == "simples":
            return SimpleReport.generate(inventory)
        elif type == "completo":
            return CompleteReport.generate(inventory)
        else:
            raise ValueError("Invalid")
