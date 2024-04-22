from flask import make_response, jsonify

def conferir_dados_req_login (username, senha) :
    if not username or username == "" or not senha or senha == "" :
        return False
    
    return True