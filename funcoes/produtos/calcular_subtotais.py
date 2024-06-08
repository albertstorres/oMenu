from bancodedados.modelos.Produtos import Produtos

def calcular_subtotais (array_de_produtos, array_vazio_resultados) :
    try :
        for produto in array_de_produtos :
                    produto_encontrado = Produtos.get_by_id(produto['produto_id'])
                    array_vazio_resultados.append(
                        {
                            "produto_id": produto['produto_id'],
                            "subtotal": produto['quantidade_produto'] * produto_encontrado.valor
                            }
                        )

    except AttributeError :
           return NameError       