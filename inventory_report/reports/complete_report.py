from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(prod):
        antiga = CompleteReport._find_antiga(prod)
        validade = CompleteReport._find_validade(prod)
        mais_prod = CompleteReport._find_common(prod, "nome_da_empresa")
        prod_comp = CompleteReport._quant_prod(prod, "nome_da_empresa")

        return f"""Data de fabricação mais antiga: {antiga}
Data de validade mais próxima: {validade}
Empresa com mais produtos: {mais_prod}
Produtos estocados por empresa:
{prod_comp}"""

    def _quant_prod(lista, filter):
        texto = ""
        company = [item[filter] for item in lista]
        contagem = Counter(company).items()

        for comp in contagem:
            name, quant = comp
            texto += f"- {name}: {quant}\n"

        return texto
