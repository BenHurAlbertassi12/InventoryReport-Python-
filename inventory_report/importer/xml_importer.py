from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> list[dict]:
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        return [
            {subitem.tag: subitem.text for subitem in item}
            for item in ET.parse(path).getroot()
        ]
