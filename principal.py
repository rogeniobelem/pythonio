#!/usr/bin/env python
# -*- coding: utf-8 -*-

arquivo_contatos = open('dados/contatos.csv', encoding='latin_1')

# conteudo = arquivo_contatos.readlines()

for linha in arquivo_contatos:
    print(linha, end='')
