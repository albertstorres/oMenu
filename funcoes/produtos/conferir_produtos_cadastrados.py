from bancodedados.modelos.Produtos import Produtos

def conferir_produtos_cadastrados (produto_id) :
    try :
        Produtos.get_by_id(produto_id)
        return True
    
    except Produtos.DoesNotExist :
        return False
    
