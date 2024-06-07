
def calcular_subtotais (produto) :
    resultado  = []
    return resultado.append({
        'produto_id': produto.id,
        'subtotal': produto.quantidade_produto * produto.valor
    })