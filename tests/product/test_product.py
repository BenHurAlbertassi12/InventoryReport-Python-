from inventory_report.inventory.product import Product


def test_cria_produto():
    test_product = Product(
        1,
        "CADEIRA",
        "Forces of Nature",
        "2022-04-04",
        "2023-02-09",
        "FR48",
        "Sentar com cuidado."
    )

    assert test_product.id == 1
    assert test_product.nome_do_produto == "CADEIRA"
    assert test_product.nome_da_empresa == "Forces of Nature"
    assert test_product.data_de_fabricacao == "2022-04-04"
    assert test_product.data_de_validade == "2023-02-09"
    assert test_product.numero_de_serie == "FR48"
    assert test_product.instrucoes_de_armazenamento == "Sentar com cuidado."
