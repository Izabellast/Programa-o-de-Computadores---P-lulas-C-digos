# 🏥 Exercícios de Lógica e Estruturas de Dados em Python

Repositório desenvolvido para registrar exercícios e práticas de **Python**, com foco no desenvolvimento da lógica de programação e na aplicação de estruturas de dados em situações relacionadas à área da saúde.

Os exercícios simulam situações como **fila de atendimento, histórico de pacientes, classificação de prioridade, controle de consultas e análise de especialidades médicas**.

## 🎯 Objetivo

Praticar conceitos fundamentais de programação utilizando problemas práticos, desenvolvendo principalmente:

* Lógica de programação
* Funções e parâmetros
* Estruturas condicionais (`if`, `elif`, `else`)
* Estruturas de repetição (`for`)
* Listas
* Dicionários
* Manipulação de dados
* Contadores e acumuladores
* Ordenação de dados
* Filas de atendimento
* Processamento e classificação de informações

## 📚 Exercícios desenvolvidos

### 1. Ranking de prioridade dos pacientes

O programa calcula uma pontuação para cada paciente com base em critérios como **gravidade do atendimento** e **idade**.

A partir da pontuação, os pacientes são organizados em um ranking de prioridade.

**Conceitos praticados:**

* Listas
* Dicionários
* Condicionais
* Laços de repetição
* Ordenação
* Acumuladores

---

### 2. Especialidade médica mais frequente

O programa analisa uma lista de consultas e identifica qual **especialidade médica possui a maior quantidade de atendimentos**.

Para isso, é utilizado um dicionário como contador de ocorrências.

**Conceitos praticados:**

* Dicionários
* Contadores
* Laços `for`
* Condicionais
* Funções
* `return`

---

### 3. Fila de atendimento

O exercício simula uma **fila de pacientes** aguardando atendimento.

A função `atender_paciente()` foi criada para trabalhar com a fila, permitindo posteriormente implementar a lógica de atendimento e remoção do primeiro paciente.

**Conceitos praticados:**

* Listas
* Funções
* Filas
* Manipulação de elementos
* Passagem de listas como parâmetro

---

### 4. Atualização do histórico de pacientes

O programa mantém um histórico de pacientes e atualiza a posição de um paciente que está retornando.

Caso o paciente já esteja no histórico, ele é removido da posição anterior e adicionado novamente ao final da lista.

**Conceitos praticados:**

* Listas
* `in`
* `remove()`
* `append()`
* Funções
* Manipulação de dados

---

### 5. Processamento de consultas

O programa analisa registros de consultas e calcula, para cada paciente:

* Tempo total de atendimento
* Quantidade de consultas
* Classificação do atendimento

Os pacientes são classificados como:

* **Leve** → tempo total menor que 2
* **Moderado** → tempo total entre 2 e 4
* **Crítico** → tempo total igual ou superior a 5

**Conceitos praticados:**

* Dicionários
* Acumuladores
* Contadores
* Estruturas condicionais
* Processamento de listas
* Agrupamento de informações
* Funções

## 🛠️ Tecnologias utilizadas

* **Python 3**
* Git
* GitHub

## 📂 Estrutura do projeto

```text
exercicios-python/
│
├── ranking_prioridade.py
├── especialidade_top.py
├── atender_paciente.py
├── atualizar_historico.py
├── processar_consultas.py
└── README.md
```

> A estrutura dos arquivos pode ser alterada conforme a organização do projeto.

## 💡 Aprendizados

Com esses exercícios, estou desenvolvendo minha capacidade de transformar problemas do cotidiano em **soluções utilizando programação**.

O projeto faz parte da minha prática de Python e da construção da minha base em **lógica de programação e estruturas de dados**, conhecimentos importantes para minha evolução na área de tecnologia.

## 🚀 Próximos passos

Como evolução dos exercícios, pretendo implementar novas funcionalidades, como:

* Atendimento automático da fila;
* Ordenação dos pacientes por prioridade;
* Inclusão e remoção de pacientes;
* Busca de pacientes;
* Novas métricas de atendimento;
* Organização dos dados de forma mais eficiente;
* Aplicação de estruturas de dados mais avançadas.

---

### 👩‍💻 Projeto de estudos

Este repositório faz parte da minha jornada de aprendizado em **Ciência da Computação e Python**, com foco no desenvolvimento de lógica, análise de dados e resolução de problemas por meio da programação.
