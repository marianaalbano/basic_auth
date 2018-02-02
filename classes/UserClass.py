from model.Model import Usuarios
import csv
import io
import random
import json
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from classes.TemplateMail import TemplateEmail


class UserClass(object):


    def adicionar_usuario(self,info):
        senha = str(random.randint(1,999999))
        usuario = Usuarios()
        stream = io.StringIO(info.stream.read().decode("UTF8"), newline=None)
        arquivo = csv.reader(stream)
        for info in arquivo:
            #add usuario
            usuario.nome = info[0]
            usuario.sobrenome = info[1]
            usuario.email = info[2]
            usuario.senha = generate_password_hash(senha)
            usuario.data_login = 0
            usuario.save()

            #envia email 
            te = TemplateEmail()
            te.template_senha(info[2], senha)
        print ("usuarios adicionados com sucesso")

    def alterar_senha(self, email, senha):
        
        usuario = Usuarios.objects(email=email)
        usuario.senha = generate_password_hash(str(random.randint(1,999999)))
        usuario.data_login = datetime.now()
        usuario.save()


    def login(self, email, senha):
        print ('aqui')
        print (email)
        print (generate_password_hash(str(senha)))
        usuario = json.loads(Usuarios.objects(email=email).to_json())
        print (usuario[0]["senha"])
        if check_password_hash(usuario[0]["senha"], str(senha)) and usuario[0]["data_login"] == 0:
            return "trocar_senha"
        elif check_password_hash(usuario[0]["senha"], str(senha)) and usuario[0]["email"] == email:
            return "login_ok"
        else:
            return "invalidos"