#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv, pickle, json
from contato import Contato

def csv_para_contatos(caminho, encoding='latin_1'):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            id, nome, email = linha

            contato = Contato(id, nome, email)
            contatos.append(contato)

    return contatos
