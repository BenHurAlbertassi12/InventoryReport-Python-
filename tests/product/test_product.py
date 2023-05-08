from inventory_report.inventory.product import Product


def test_cria_produto():
    test_product = Product(
        1,
        "Cult",
        "Razors",
        "2022-04-04",
        "Indeterminado",
        "321",
        "Use sempre prteção."
    )

    assert test_product.id == 1
    assert test_product.nome_do_produto == "Cult"
    assert test_product.nome_da_empresa == "Razors"
    assert test_product.data_de_fabricacao == "2022-04-04"
    assert test_product.data_de_validade == "Indeterminado"
    assert test_product.numero_de_serie == "321"
    assert test_product.instrucoes_de_armazenamento == "Use sempre prteção."
