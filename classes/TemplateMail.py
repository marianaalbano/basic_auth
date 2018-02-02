#!/usr/bin/python
#-*- coding: utf8 -*-
from classes.EmailClass import Email



class TemplateEmail():


    def template_senha(self,email, senha):
        msg = Email()
        msg.email = email
        msg.senha = senha
        msg.subject = 'Recuperação de senha'
        msg.mensagem = 'Olá,<br><br> \
                        Você foi cadastrado no sistema, seus dados de acesso:<br><br> \
                        <b>E-mail: {{ email }}\
                        Senha: </b>{{ senha }} <br><br>\
                        Atenciosamente,<br> \
                        Admin <br><br> \
                        <p style="font-size:small;">Esta mensagem foi gerada automaticamente. Por favor, não responda.</p>'
        msg.sendmail_login_senha()