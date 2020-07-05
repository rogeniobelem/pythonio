#!/usr/bin/env python
# -*- coding: utf-8 -*-

arquivo_contatos = open('dados/contatos_escrita.csv', encoding='latin_1', mode='a+')

contato = '11,Carol,carol@carol.com.br\n'

arquivo_contatos.write(contato)