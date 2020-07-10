#!/usr/bin/env python
# -*- coding: utf-8 -*-

arquivo = open('dados/contatos-escrita.csv', encoding='latin_1', mode='a+'')

print(type(arquivo))

print(type(arquivo.buffer))

conteudo = arquivo.buffer.read()
print(conteudo)


arquivo.close()