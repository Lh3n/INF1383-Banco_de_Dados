# Conversor de Dados de Emendas Parlamentares para SQL

## Sobre o Projeto

Este projeto foi desenvolvido durante a disciplina de Banco de Dados da graduação em Ciência da Computação.

Durante o trabalho, foi necessário importar dados públicos de emendas parlamentares para um banco de dados SQL. Os dados foram obtidos a partir do Portal da Transparência, porém o formato exportado não era adequado para inserção direta no banco.

Devido ao grande volume de informações, a correção manual dos registros seria inviável. Para resolver o problema, desenvolvi um script em Python que automatiza o processo de filtragem, limpeza e formatação dos dados.

## Funcionalidades

O script:

* Lê um arquivo TXT contendo os dados exportados;
* Filtra registros de parlamentares específicos;
* Filtra registros a partir do ano de 2023;
* Seleciona apenas as colunas necessárias para o banco de dados;
* Corrige a formatação de valores numéricos;
* Escapa caracteres especiais em campos de texto;
* Gera uma saída pronta para utilização em comandos SQL.

## Tecnologias Utilizadas

* Python
* Manipulação de arquivos
* Processamento de dados
* SQL

## Estrutura

```text
entrada.txt   # Arquivo original exportado
script.py     # Script de processamento
saida.txt     # Arquivo gerado para inserção no banco
```

## Como Executar

1. Coloque o arquivo de entrada na mesma pasta do script.
2. Ajuste os índices das colunas desejadas no código, se necessário.
3. Execute o script.py
4. O arquivo processado será gerado como:

```text
saida.txt
```

## Contexto Acadêmico

O objetivo principal deste projeto foi automatizar uma tarefa repetitiva de preparação de dados para um trabalho acadêmico de Banco de Dados.

Além de reduzir significativamente o trabalho manual, o projeto serviu como prática de manipulação de arquivos, tratamento de dados e integração com bancos de dados relacionais.
