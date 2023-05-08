from datetime import datetime
from collections import Counter


class SimpleReport:
    def generate(prod):
        antiga = SimpleReport._find_antiga(prod)
        validade = SimpleReport._find_validade(prod)
        mais_produtos = SimpleReport._find_common(prod, "nome_da_empresa")

        return f"""Data de fabricação mais antiga: {antiga}
Data de validade mais próxima: {validade}
Empresa com mais produtos: {mais_produtos}"""

    def _find_common(lista, filtered):
        comp = [item[filtered] for item in lista]
        mais_comum = Counter(comp).most_common(1)[0]
        return mais_comum[0]

    def _find_validade(prod):
        valid = []
        for item in prod:
            val = datetime.strptime(item.get("data_de_validade"), "%Y-%m-%d")
            if val > datetime.now():
                valid.append(item["data_de_validade"])
        return min(valid)

    def _find_antiga(prod):
        date_fab = [item["data_de_fabricacao"] for item in prod]
        return min(date_fab)
