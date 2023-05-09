from .importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> list[dict]:
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path, "r") as file:
            return [row for row in csv.DictReader(file)]
