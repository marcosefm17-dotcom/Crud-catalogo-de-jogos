# 📓 LOGBOOK AFP — Algoritmos e Programação (2026.2)

> **Como usar este arquivo:** copie-o para a raiz do **seu** repositório (ou para `logbook/LOGBOOK.md`) e preencha **direto no GitHub** (botão ✏️ *Edit this file*) ou no VS Code. Ele reúne todos os instrumentos do Protocolo AFP 2026.2 (Logbook Individual — Campos 01 a 04, 06 e 07; Registro de Revisão por Pares — Campo 05; Checkpoint Conceitual; Rubrica de Defesa Técnica).
>
> **Organização:** o Logbook está dividido em **3 grupos de entrega**, cada um com seu prazo. Dentro de cada grupo, os **ciclos de entrega (01 a 12)** continuam os mesmos, com as orientações de preenchimento. Siga a ordem: **Grupo 1 → Grupo 2 → Grupo 3 → Defesa Técnica**.
>
> O `Diario.md` do checklist passa a ser **este arquivo**: o registro de cada ciclo está na seção do ciclo correspondente.

## 📍 Navegação rápida

| Seção | Prazo |
|---|---|
| [👨‍🎓 Identificação](#-identificação) | Hoje |
| [🟢 Grupo 1](#-grupo-1--prazo-segunda-1611-às-23h59) · Registros 01–04, Campos 01 e 02 | **Segunda 16/11, 23h59** |
| [🟠 Grupo 2](#-grupo-2--prazo-sábado-2111-às-23h59) · Registros 05–08, Checkpoint, Campos 03 e 04 | **Sábado 21/11, 23h59** |
| [🔵 Grupo 3](#-grupo-3--prazo-quinta-2611-às-23h59) · Registros 09–12, Campos 05, 06 e 07 | **Quinta 26/11, 23h59** |
| [🏁 Defesa Técnica](#-defesa-técnica--quarta-1811) | **Quarta 18/11** |
| [🆘 Estou atrasado](#-estou-atrasado-no-logbook-e-agora) | — |

---

## 👨‍🎓 Identificação

| Campo | Preencha |
|---|---|
| **Nome do estudante** | Marcos Eduardo |
| **Curso / Módulo** | Engenharia de Software · 2º período  |
| **Unidade curricular** | Algoritmos e Programação — UnDB 2026.2 |
| **Professor** | Rondineli Seba Salomão |
| **App-base do meu CRUD** | Catálogo de Jogos|
| **Link do meu repositório** | [_https://github.com/…](https://github.com/marcosefm17-dotcom/Crud-catalogo-de-jogos)_ |
| **Dupla de revisão (Campo 05)** | Maria Luiza
| **Função neste ciclo** | _Autor do meu CRUD · Revisor do CRUD de um colega_ |

---

## 🧭 Regras de ouro (leia antes de preencher)

1. **Processo, não resultado.** O Logbook mostra *como você pensou*, não só o que funcionou. Registre erros, desvios e dúvidas reais.
2. **Vocabulário técnico.** Use os termos da área (ex.: "laço de repetição", "validação de entrada", "estrutura de dados"). Respostas genéricas ("aprendi Python") não são aceitas.
3. **Todo registro relevante tem 3 âncoras:** o **objeto de conhecimento** mobilizado + a **justificativa técnica** + a **referência/fonte**. *Decisão sem objeto de conhecimento e sem referência é considerada não rastreável e não conta para a avaliação formativa.*
4. **Coerência entre campos.** O Campo 02 deve ser coerente com o Campo 01. *Incoerência é evidência de autoria externa.* O Campo 07 retoma o Campo 01.
5. **IA é permitida e avaliada (Campo 04).** *Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.* Você precisa mostrar o que aceitou **e** o que questionou/descartou, com argumento técnico.
6. **O histórico do Git é a sua evidência.** Faça commits pequenos e frequentes. Nunca reescreva o histórico (`force push`) do arquivo do Logbook.
7. **Campo 01 e Checkpoint são "sem consulta".** Preencha em um bloco contínuo, sem internet, sem material e sem colegas, no tempo indicado (Campo 01: durante o laboratório; Checkpoint: 20 min). Depois **não edite** esses campos — se perceber um erro, corrija em um campo posterior (Campo 03 ou 07), explicando.
8. **Os prazos dos grupos (16/11, 21/11 e 26/11, às 23h59)** valem para o commit no GitHub. O horário do commit é o registro oficial.

### ✅ Padrão de commit do Logbook

```text
docs(logbook): campo 01 — ciclo 02
docs(logbook): registro do ciclo 05
docs(logbook): campo 05 — revisão do CRUD de <colega>
```

---

## 🗓️ Calendário de entregas e Defesa

Os grupos têm **5 dias entre um prazo e outro**. O horário do commit no GitHub é o registro oficial.

| Grupo | Janela de preenchimento | **Prazo** | O que entregar |
|:--:|---|---|---|
| **1** | Qua 11/11 → seg 16/11 | **Segunda 16/11, 23h59** | Identificação · Registros dos Ciclos 01 a 04 · Campo 01 · Campo 02 |
| **2** | Seg 16/11 → sáb 21/11 | **Sábado 21/11, 23h59** | Registros dos Ciclos 05 a 08 · Checkpoint Conceitual · Campo 03 · Campo 04 |
| **3** | Sáb 21/11 → qui 26/11 | **Quinta 26/11, 23h59** | Registros dos Ciclos 09 a 12 · Campo 05 (2 revisões) · Campo 06 · Campo 07 |
| 🏁 | — | **Quarta 18/11** | **Defesa Técnica individual** (Rubrica) |

### Linha do tempo

| Data | Evento |
|---|---|
| Qua 11/11 | **Hoje:** começa o Grupo 1 |
| Seg 16/11 | ✅ Prazo do **Grupo 1** |
| **Qua 18/11** | 🏁 **Defesa Técnica** |
| Sáb 21/11 | ✅ Prazo do **Grupo 2** |
| Qua 25/11 | Avaliação P2 |
| Qui 26/11 | ✅ Prazo do **Grupo 3** |
| Qua 02/12 | Avaliação Substitutiva |
| Qua 09/12 | Avaliação Final |

> ⚠️ **Atenção:** a Defesa Técnica (18/11) acontece **antes** dos prazos dos Grupos 2 e 3. Na defesa você será arguido sobre **o que já estiver registrado e commitado**. Veja a seção [Defesa Técnica](#-defesa-técnica--quarta-1811) para saber o que priorizar até 18/11.

### Ciclos de entrega por grupo

| Ciclo | Data da aula | Tema do ciclo | Grupo | O que preencher |
|:--:|:--:|---|:--:|---|
| 01 | 12/08 | Preparação do laboratório e escolha do projeto | **1** | Registro do Ciclo |
| 02 | 19/08 | Variáveis, tipos de dados, entrada/saída | **1** | Registro + **Campo 01** + **Campo 02** |
| 03 | 26/08 | Operadores, fluxogramas, paradigmas | **1** (registro) · **2** (campos) | Registro (G1) · **Checkpoint**, **Campo 03**, **Campo 04** (G2) |
| 04 | 02/09 | Condicionais: `if`, `elif`, `else` | **1** | Registro do Ciclo |
| 05 | 09/09 | Condicionais aninhadas e operadores lógicos | **2** | Registro do Ciclo |
| 06 | 30/09 | Repetição: `for`, `while`, `break`, `continue` | **2** | Registro do Ciclo (inclui devolutiva da P1) |
| 07 | 07/10 | Listas: armazenamento e iteração | **2** | Registro do Ciclo |
| 08 | 14/10 | Busca e introdução a dicionários/matrizes | **2** | Registro do Ciclo |
| 09 | 21/10 | Atualização e exclusão: CRUD completo | **3** | Registro + **Campo 05** (revisão nº 1) |
| 10 | 28/10 | Modularização: funções | **3** | Registro do Ciclo |
| 11 | 04/11 | Recursividade | **3** | Registro + **Campo 06** |
| 12 | 11/11 | Refatoração e qualidade de código | **3** | Registro + **Campo 05** (revisão nº 2) + **Campo 07** |

---

## 📊 Painel de acompanhamento

Atualize a cada commit (troque ⬜ por ✅).

| Grupo | Item | Prazo | Preenchido | Commit |
|:--:|---|---|:--:|:--:|
| 1 | Identificação | 16/11 | ⬜ | ⬜ |
| 1 | Registros dos Ciclos 01, 02, 03 e 04 | 16/11 | ⬜ | ⬜ |
| 1 | Campo 01 — Instrumento de entrada | 16/11 | ⬜ | ⬜ |
| 1 | Campo 02 — Aprofundamento | 16/11 | ⬜ | ⬜ |
| 2 | Registros dos Ciclos 05, 06, 07 e 08 | 21/11 | ⬜ | ⬜ |
| 2 | Checkpoint Conceitual | 21/11 | ⬜ | ⬜ |
| 2 | Campo 03 — Execução e desvios | 21/11 | ⬜ | ⬜ |
| 2 | Campo 04 — Interação com IA | 21/11 | ⬜ | ⬜ |
| 3 | Registros dos Ciclos 09, 10, 11 e 12 | 26/11 | ⬜ | ⬜ |
| 3 | Campo 05 — Revisão por pares nº 1 e nº 2 | 26/11 | ⬜ | ⬜ |
| 3 | Campo 06 — Próximos passos | 26/11 | ⬜ | ⬜ |
| 3 | Campo 07 — Evolução conceitual | 26/11 | ⬜ | ⬜ |
| 🏁 | Defesa Técnica | 18/11 | ⬜ | — |

---

## ❓ A questão-problema da AFP

**Título:** *O sistema em produção: diagnosticando as falhas do CRUD que você mesmo construiu.*

> **Enunciado completo (Apêndice A):** _professor(a): cole aqui o enunciado e os anexos liberados conforme o cronograma._

A questão-problema é **a mesma durante todo o semestre**: ela se aplica ao **seu** CRUD, que cresce a cada ciclo. Os **dados com defeito** do seu app chegam em um **lote cumulativo único** e vão expondo problemas diferentes conforme sua estrutura evolui. Seu trabalho é diagnosticar, ajustar o CRUD para tratar cada falha e **registrar o raciocínio** neste Logbook.

---

# 🔁 REGISTRO DO CICLO — modelo (copie em cada ciclo)

Cada ciclo tem sua própria seção abaixo, já com o modelo. Se precisar de espaço extra, acrescente linhas.

```markdown
### Registro do Ciclo NN — DD/MM
1. **Desafio do ciclo (em 1 frase):**
2. **O que implementei (commits / arquivos / links):**
3. **Objeto(s) de conhecimento mobilizado(s) (vocabulário técnico):**
4. **Desvio ou erro encontrado + causa técnica:**
5. **Decisão de ajuste + fonte (livro, doc, vídeo, colega, IA):**
6. **Feedback recebido (professor/colega) e o que mudei por causa dele:**
7. **Próximo passo:**
```

**Como preencher bem:** escreva como se explicasse a um colega que não esteve na aula. O item 3 e o item 5 são os mais importantes: eles ligam o que você fez ao **conteúdo** e à **fonte**.

| ❌ Fraco | ✅ Forte |
|---|---|
| "Aprendi a usar `if`." | "Usei estrutura condicional aninhada para validar a idade antes de cadastrar. Meu erro foi comparar `str` com `int` (resultado de `input()`); corrigi com `int()` (Pense em Python, cap. 2)." |
| "Deu erro e consertei." | "O programa quebrou com `ZeroDivisionError` ao calcular a média de um item sem avaliações. Causa: divisão por `len(lista)` com lista vazia. Ajuste: testar `if len(lista) > 0`." |

---

# 🟢 GRUPO 1 — prazo segunda 16/11 às 23h59

> **Janela:** quarta 11/11 → segunda 16/11. **O que entregar:** Identificação · Registros dos Ciclos 01, 02, 03 e 04 · Campo 01 · Campo 02.
>
> **Sugestão de ordem:** (1) Identificação → (2) **Campo 01 primeiro, sem consulta** → (3) Registros dos Ciclos 01 a 04 → (4) Campo 02, com pesquisa.

**Checklist do Grupo 1**
- [x] Identificação preenchida (app-base, link do repositório, dupla de revisão)
- [x ] Campo 01: 3 objetos de conhecimento, 3 lacunas, hipótese de até 5 linhas
- [x ] Registros dos Ciclos 01, 02, 03 e 04 com os 7 itens
- [x ] Campo 02: 2 referências com contribuição, hipótese revisada, 3 recursos
- [x ] Commits no GitHub e painel atualizado

## 🟢 CICLO 01 — 12/08 — Preparação do laboratório e escolha do projeto

<details>
<summary>📘 Orientações do Ciclo 01</summary>

- **Hoje não há Campo do Protocolo.** O foco é preparar o ambiente: criar o repositório, configurar o VS Code e escolher o **app-base** do seu CRUD (e, portanto, o *schema* dos seus dados).
- Preencha a **Identificação** (no início deste arquivo) e o **Registro do Ciclo 01**.
- No item 3, registre **o que você já sabia** e o que era novo (Git, GitHub, VS Code). Isso será útil para o Campo 07.
- No item 4, registre qualquer problema de instalação ou configuração e como o resolveu — isso conta como desvio.
- Faça o primeiro commit: `docs(logbook): registro do ciclo 01`.
</details>

#### Registro do Ciclo 01 — 12/08
1. **Desafio do ciclo (em 1 frase):** _Configurar o ambiente de desenvolvimento (interpretador Python, IDE VS Code e repositório Git/GitHub)…_
2. **O que implementei (commits / arquivos / links):** _Criação do repositório remoto no GitHub, estruturação inicial do arquivo `LOGBOOK.md` na raiz do projeto, configuração do diretório local (`Catálogo de jogos`) e criação do arquivo base `main.py`_
3. **Objeto(s) de conhecimento mobilizado(s):** _…Configuração de ambiente de execução (interpretador Python e variável de ambiente `PATH`), controle de versão distribuído (repositório Git, commits e sincronização com GitHub), navegação em interface de linha de comando (CLI / PowerShell) e definição de esquema de dados (*schema* com tipos `str`, `int` e `float` para título, ano e nota)._
4. **Desvio ou erro encontrado + causa técnica:** _…O VS Code não exibia a opção de execução do script (`Select Python Interpreter`) e o terminal PowerShell não reconhecia o comando do interpretador. Causa técnica: ausência da instalação local do interpretador Python adicionada ao `PATH` do sistema e abertura do terminal no diretório raiz do usuário.
5. **Decisão de ajuste + fonte:** _Instalação oficial do Python marcando a opção *Add python.exe to PATH*, seleção do interpretador na barra de status do VS Code, navegação até a pasta correta via comando `cd` no PowerShell e execução direta com `py main.py`. Fonte: Documentação oficial do Python (`docs.python.org`), documentação do VS Code (*Python in VS Code*) e apoio de IA para diagnóstico do terminal._
6. **Feedback recebido e o que mudei:** _Orientação do protocolo da disciplina para manter o arquivo de registro padronizado como `LOGBOOK.md` na raiz do repositório e registrar problemas reais de configuração de ambiente como evidência de processo._
7. **Próximo passo:** _Resolver problemas na alteração dos nomes e notas dos jogos_

## 🟢 CICLO 02 — 19/08 — Variáveis, tipos de dados e entrada/saída

<details>
<summary>📘 Orientações do Ciclo 02 — Campo 01 (sem consulta) e Campo 02 (pesquisa)</summary>

**Campo 01 — Instrumento de entrada** · *sem consulta · faça primeiro*
- Preencha **antes de tudo**, em um bloco contínuo de cerca de 15 minutos, sem internet, sem material, sem IA e sem colegas, depois de conhecer a questão-problema e a primeira amostra de dados do seu app. Depois do Campo 01 você pode consultar o que quiser.
- **1a.** Liste pelo menos **3 objetos de conhecimento** que você acha que precisa dominar para resolver o problema. Use o vocabulário técnico da área. *Não precisa acertar tudo — o Campo 07 vai mostrar o quanto você evoluiu.*
- **1b.** Liste pelo menos **3 lacunas**: o que você **não sabe** e precisa descobrir, com precisão (ruim: "não sei programar"; bom: "não sei como validar a entrada para impedir que o usuário digite texto onde espero número").
- **1c.** Escreva sua **hipótese inicial** em até 5 linhas: o que você acha que está causando as falhas do CRUD e por quê.
- Faça o commit **logo ao terminar**. Depois, **não edite** o Campo 01.

**Campo 02 — Aprofundamento** · *AV Qualis · segunda 16/11, 23h59*
- Preencha **depois do Campo 01, com pesquisa real**, e seja coerente com ele.
- **2a.** Pelo menos **2 referências** (livro, documentação, vídeo, artigo), cada uma com a **contribuição** concreta para a sua solução. Não basta listar o título.
- **2b.** **Hipótese revisada:** o que mudou em relação ao Campo 01 e **por quê**. Se não mudou nada, explique por que a pesquisa confirmou a hipótese.
- **2c.** **Dimensionamento inicial de recursos** (mínimo 3 itens), com quantidade estimada e justificativa técnica. Exemplos de recursos no seu contexto: horas de estudo, número de casos de teste, módulos/arquivos do projeto, dados de teste, bibliotecas.
</details>

### 🧩 CAMPO 01 — Instrumento de entrada
*Grupo 1 | Prazo segunda 16/11, 23h59 | SEM CONSULTA*

**1a. Objetos de conhecimento identificados (mínimo 3, com vocabulário técnico):**
1. _…_Variáveis e tipos primitivos de dados (`str` para título do jogo, `int` para ano de lançamento e `float` para nota de avaliação
2. _…_Instruções de entrada e saída padrão (`input()` e `print()`) e conversão explícita de tipos (*type casting* com `int()` e `float()`).
3. _…_Estruturas de controle de fluxo: condicionais (`if`, `elif`, `else`) para validação de regras e laços de repetição (`while`) para manter o menu ativo.
4. _…_ *(opcional)*

**1b. Lacunas — o que não sei e preciso descobrir (mínimo 3, com precisão técnica):**
1. _…_Não sei como impedir que o programa encerre abruptamente (quebre com erro de execução) quando o usuário digitar texto ou deixar o campo vazio onde o sistema espera um número inteiro (`ano`) ou decimal (`nota`)
2. _…_Não sei como estruturar e percorrer uma lista de dicionários para localizar, atualizar ou remover um jogo específico sem gerar erro de índice inexistente.
3. _…_Não sei como modularizar as operações do CRUD em funções isoladas (passagem de parâmetros e retorno) nem como aplicar recursividade dentro da lógica do catálogo.

**1c. Hipótese inicial em até 5 linhas — com lógica da área de formação:**

> _…_Acredito que as falhas no CRUD ocorrem principalmente porque a função `input()` sempre retorna dados no formato texto (`str`), e a falta de validação ou conversão adequada antes de processar operações numéricas e buscas na lista provoca erros de tipo (`ValueError`/`TypeError`) e acesso a índices inválidos. Além disso, sem estruturas condicionais rigorosas para filtrar entradas vazias ou fora da faixa permitida (como anos e notas inválidas), dados inconsistentes acabam sendo armazenados na memória.

### 🧩 CAMPO 02 — Aprofundamento pós-aula
*AV Qualis — Grupo 1 | Segunda 16/11, 23h59*

> **Preenchido depois do Campo 01, com pesquisa real. Deve ser coerente com o Campo 01. Incoerência = evidência de autoria externa.**

**2a. Aprofundamento dos objetos de conhecimento (mínimo 2 referências com síntese da contribuição para a solução):**

- **Referência 1:** _DOWNEY, Allen B. *Pense em Python: Pense como um cientista da computação* (Capítulos 2 e 8 — Variáveis, expressões, instruções e strings). — **Contribuição:** Esclareceu a tipagem dinâmica do Python, o comportamento da função nativa `input()` (que sempre retorna `str`), a necessidade de conversão explícita (*type casting*) com `int()` e `float()` antes de validações numéricas, e o uso de métodos de string como `.strip()` para higienizar espaços em branco na entrada de títulos._ — **Contribuição:** _…_
- **Referência 2:** _…_ — **Contribuição:** _Documentação Oficial do Python (`docs.python.org/pt-br/3/tutorial/errors.html` — Erros e Exceções). — **Contribuição:** Demonstrou como o tratamento de exceções com blocos `try` e `except ValueError` intercepta falhas de conversão de tipos em tempo de execução, impedindo que o programa aborte quando o usuário digita caracteres não numéricos nos campos `ano` ou `nota`.

**2b. Hipótese revisada — o que mudou em relação ao Campo 01 e por quê:**A pesquisa confirmou a hipótese inicial de que a falta de conversão explícita da saída de `input()` causa `ValueError` e `TypeError`, mas aprofundou a compreensão técnica ao evidenciar que apenas estruturas condicionais (`if/else`) não bastam para evitar a quebra do programa durante a conversão de texto para número. Para garantir resiliência na entrada de dados, é necessário combinar sanitização de strings (`.strip()`), blocos de tratamento de exceções (`try/except`) para capturar falhas de tipo e validações condicionais de domínio (faixas válidas de ano entre 1970 e 2026 e nota entre 0 e 10).

**2b. Hipótese revisada — o que mudou em relação ao Campo 01 e por quê:**

> _…_

**2c. Dimensionamento inicial de recursos (recurso, quantidade estimada, justificativa técnica — mínimo 3 itens):** RECURSO / MATERIAL / INSUMO | QUANTIDADE ESTIMADA | JUSTIFICATIVA TÉCNICA |
|---|---|---|
| Casos de teste de entrada (válidos, vazios, fora de faixa e tipos incorretos) | 12 casos de teste (4 por atributo: título, ano e nota) | Validar isoladamente o comportamento de conversão de tipos (`str` → `int`/`float`), tratamento de `ValueError` e limites de domínio antes de persistir o registro na memória. |
| Estrutura de dados em memória (lista principal + dicionários por registro) | 1 lista (`catalogo`) contendo até 20 dicionários de teste | Permitir o armazenamento estruturado dos 3 atributos (`titulo`, `ano`, `nota`) com acesso rápido por chave e iteração indexada nas operações do CRUD. |
| Horas de estudo, codificação e depuração incremental no VS Code | 8 horas distribuídas ao longo dos ciclos | Cobrir leitura da documentação/livro, implementação incremental das 4 operações do CRUD, testes de borda no terminal e refatoração modular. |

| RECURSO / MATERIAL / INSUMO | QUANTIDADE ESTIMADA | JUSTIFICATIVA TÉCNICA |
|---|---|---|
| _Aulas sobre variáveis_ | _2 aulas_ | _aprender sobre variáveis_ |
| _praticar programação_ | _2 dias_ | _praticar os conteúdos_ |
| _pasta main.py_ | _organizar pasta _ | _melhorar o cóigo_ |
| _repositório no git hub_ | _1 repositório_ | _salvar projeto e atualizar continuamente_ |

#### Registro do Ciclo 02 — 19/08
1. **Desafio do ciclo (em 1 frase):** _Implementar a leitura segura dos dados de entrada (`titulo`, `ano` e `nota`) no Catálogo de Jogos, garantindo a conversão correta dos tipos primitivos e evitando que entradas inválidas encerrem a execução do programa._
2. **O que implementei (commits / arquivos / links):** _Implementação do fluxo inicial de entrada e saída (`input`/`print`), sanitização de texto com `.strip()`, conversão de tipos com `int()` e `float()`, e validação inicial de exceções com `try/except ValueError` no arquivo `main.py` (commit: `docs(logbook): campo 02 e registro do ciclo 02`)._
3. **Objeto(s) de conhecimento mobilizado(s):** _Variáveis e tipos primitivos (`str`, `int`, `float`), entrada e saída padrão (`input()`, `print()`), conversão explícita de tipos (*type casting*), manipulação de strings (`.strip()`) e tratamento básico de exceções (`try/except ValueError`)._
4. **Desvio ou erro encontrado + causa técnica:** _Ao testar o cadastro digitando letras ou deixando o campo em branco no ano de lançamento ou na nota, o programa interrompia com `ValueError: invalid literal for int() with base 10`. Causa técnica: a função `input()` retorna uma `str`, e a conversão direta via `int()` ou `float()` sem tratamento de exceção não consegue converter cadeias não numéricas ou vazias_
5. **Decisão de ajuste + fonte:** _Ao testar o cadastro digitando letras ou deixando o campo em branco no ano de lançamento ou na nota, o programa interrompia com `ValueError: invalid literal for int() with base 10`. Causa técnica: a função `input()` retorna uma `str`, e a conversão direta via `int()` ou `float()` sem tratamento de exceção não consegue converter cadeias não numéricas ou vazias_
6. **Feedback recebido e o que mudei:** _Orientação para não confiar apenas na entrada ideal do usuário e sempre testar casos de borda (entradas vazias e tipos trocados), motivando a inclusão imediata de verificações de string vazia e tratamento de `ValueError`._
7. **Próximo passo:** _Resolver problema de ao salvar informações dos jogos._

## 🟢 CICLO 03 — 26/08 — Operadores, fluxogramas e paradigmas

<details>
<summary>📘 Orientações do Ciclo 03 — Registro (Grupo 1)</summary>

- Neste grupo você preenche **apenas o Registro do Ciclo 03**. O **Checkpoint Conceitual** e os **Campos 03 e 04** deste ciclo estão no **Grupo 2**.
- Item 3: nomeie os **operadores** (aritméticos, relacionais, lógicos) e os **tipos** que usou. Se montou fluxogramas, cite o que o fluxograma ajudou a perceber.
- Item 4: registre erros de precedência de operadores, divisão por zero ou confusão entre `=` e `==`, com a causa técnica.
</details>

#### Registro do Ciclo 03 — 26/08
1. **Desafio do ciclo (em 1 frase):** _Modelar o fluxo lógico de decisão do Catálogo de Jogos por meio de fluxograma e aplicar operadores relacionais, lógicos e aritméticos para validar as regras de domínio dos dados._
2. **O que implementei (commits / arquivos / links):** _Elaboração do fluxograma do menu e das validações de entrada, e implementação das expressões relacionais (`==`, `<`, `>`, `>=`), lógicas (`or`) e aritméticas (`+`, `-`) no arquivo `main.py` (commit: `docs(logbook): registro do ciclo 03`)._
3. **Objeto(s) de conhecimento mobilizado(s):** _Paradigma imperativo/estruturado, representação algorítmica via fluxograma (que evidenciou a necessidade de desviar o fluxo de volta ao início do menu em caso de entrada inválida), operadores relacionais (`==` para verificar opção do menu e string vazia `""`; `<` e `>` para limites de ano e nota; `>=` para limite superior de índice), operadores lógicos (`or` para validar intervalos inválidos em uma única expressão booleana), operadores aritméticos (`+` na exibição do índice amigável `i + 1` e `-` na conversão do índice digitado `indice - 1`) e tipos de dados (`str`, `int`, `float` e `bool`)._
4. **Desvio ou erro encontrado + causa técnica:** _Durante a escrita das condições do menu e da validação do título, ocorreu erro de sintaxe (`SyntaxError: invalid syntax`) ao escrever `if opcao = "1":` em vez de `if opcao == "1":`, além de inversão lógica inicial ao tentar validar o ano com `and` (`ano < 1970 and ano > 2026`), condição que nunca era satisfeita. Causa técnica: confusão entre o operador de atribuição (`=`) e o operador relacional de igualdade (`==`), e uso incorreto da conjunção lógica (`and`) para intervalos mutuamente exclusivos onde o correto é a disjunção (`or`)._
5. **Decisão de ajuste + fonte:** _Substituir `=` por `==` nas comparações e corrigir as expressões de faixa inválida para `ano < 1970 or ano > 2026` e `nota < 0 or nota > 10`. Fonte: DOWNEY, Allen B. *Pense em Python* (Capítulo 5 — Condicionais e recursividade) e Documentação Oficial do Python (*Expressões e operadores*)._
6. **Feedback recebido e o que mudei:** _Orientação das diretrizes do Ciclo 03 para mapear o fluxo de decisão antes de codificar e revisar a precedência e o sentido booleano dos operadores relacionais e lógicos antes de encadear múltiplas condições._
7. **Próximo passo:** _Estruturar a árvore completa de decisão do menu e das validações utilizando as estruturas condicionais `if`, `elif` e `else` no Registro do Ciclo 04._

## 🟢 CICLO 04 — 02/09 — Estruturas condicionais: `if`, `elif`, `else`

<details>
<summary>📘 Orientações do Ciclo 04</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 04.
- Conecte **cada condicional** do seu CRUD a uma **regra de negócio** (ex.: "preço não pode ser negativo").
- Se já recebeu o lote de dados com defeito, procure **qual registro quebra qual condição** e registre o item 4 com a **causa técnica** (ex.: valor `None`, texto vazio, número negativo, divisão por zero).
- No item 5, cite a fonte da decisão: livro (*Pense em Python*), documentação ou exercício que você resolveu.
- Compare com o **Campo 02**: o desvio de hoje já estava previsto no seu dimensionamento?
</details>

#### Registro do Ciclo 04 — 02/09
1. **Desafio do ciclo (em 1 frase):*Estruturar o roteamento de opções do menu principal e as regras de negócio de validação de dados utilizando desvios condicionais encadeados (`if`, `elif`, `else`).* _…_
2. **O que implementei (commits / arquivos / links):** _Implementação da cadeia condicional do menu (`if opcao == "1":` até `elif opcao == "0":` e `else:` para opções inválidas) e das validações de domínio de título, ano, nota e existência de registros no arquivo `main.py` (commit: `docs(logbook): registro do ciclo 04`)._
3. **Objeto(s) de conhecimento mobilizado(s):** _Estruturas de seleção/decisão (`if`, `elif`, `else`), controle de fluxo em laços (`continue` e `break`), verificação de comprimento de coleção (`len(catalogo) == 0`) e alinhamento por indentação obrigatória em Python._
4. **Desvio ou erro encontrado + causa técnica:** _Ao testar entradas com defeito, registros com título composto apenas por espaços (`"   "`), anos anteriores a 1970 (ex.: `1950`), notas acima de 10 (ex.: `12`) ou opções inexistentes no menu (ex.: `"9"`) quebravam as regras de negócio ou causavam comportamento inesperado. Além disso, houve erro de indentação (`IndentationError` / bloco ignorado) nos ramos `elif opcao == "3":` e `elif opcao == "4":`. Causa técnica: ausência de cláusula `else` final para capturar opções fora do intervalo `"0"` a `"4"`, falta de verificação prévia de lista vazia (`len(catalogo) == 0`) antes de listar/editar/excluir, e desalinhamento de espaços à esquerda nos blocos `elif`. Esse cenário já havia sido parcialmente previsto no dimensionamento de 12 casos de teste de borda do Campo 02._
5. **Decisão de ajuste + fonte:** _Conectar cada condicional a uma regra de negócio explícita (`titulo == ""` após `.strip()`, `ano < 1970 or ano > 2026`, `nota < 0 or nota > 10` e `len(catalogo) == 0`), padronizar a indentação em 4 espaços e incluir o bloco `else:` final no menu. Fonte: DOWNEY, Allen B. *Pense em Python* (Capítulo 5 — Condicionais e recursividade) e Documentação Oficial do Python (*Mais ferramentas de controle de fluxo*)._
6. **Feedback recebido e o que mudei:** _Orientação do protocolo do Ciclo 04 para vincular cada estrutura condicional a uma regra de negócio clara do domínio e comparar os desvios encontrados com os testes planejados no Campo 02._
7. **Próximo passo:** _Atualizar os checkboxes do Grupo 1 no Painel de Acompanhamento_

---

# 🟠 GRUPO 2 — prazo sábado 21/11 às 23h59

> **Janela:** segunda 16/11 → sábado 21/11. **O que entregar:** Registros dos Ciclos 05, 06, 07 e 08 · Checkpoint Conceitual · Campo 03 · Campo 04.
>
> ⚠️ O prazo cai num **sábado**: planeje terminar na sexta. Os campos do Ciclo 03 (Checkpoint, 03 e 04) aparecem **primeiro**, porque são a base da investigação.

**Checklist do Grupo 2**
- [ x] Checkpoint Conceitual feito conforme orientação do professor (20 min, sem consulta)
- [ x] Campo 03: 2 achados com objeto, 1 desvio com causa técnica, 1 decisão com fonte
- [x ] Campo 04: ferramenta, pergunta íntegra, resumo, o que aceitei e o que questionei
- [ x] Registros dos Ciclos 05, 06, 07 e 08 com os 7 itens (devolutiva da P1 no ciclo 06)
- [x ] Commits no GitHub e painel atualizado

## 🟠 CICLO 03 (campos) — 26/08 — Checkpoint, Campo 03 e Campo 04

<details>
<summary>📘 Orientações — Checkpoint, Campo 03 e Campo 04 (referentes ao Ciclo 03)</summary>

**Checkpoint Conceitual** · *20 min · sem consulta · conforme orientação do professor*
- Verifica o **seu domínio individual** do conteúdo — não avalia a sua solução. São **3 questões dissertativas**. Quem investiu por conta própria responde com segurança.
- Respostas **genéricas, sem ancoragem técnica, não são aceitas**. Defina o objeto **e** relacione-o ao problema do seu CRUD, explicitando as implicações.
- Critérios: *precisão conceitual*, *relação conteúdo-problema*, *qualidade do raciocínio*.
- Se for insatisfatório, você recebe **feedback escrito em até 48h** e deve ajustar a investigação antes da avaliação somativa.
- Se o professor aplicar o Checkpoint via GitHub, use o arquivo abaixo **só durante os 20 minutos**, com um único commit ao final.

**Campo 03 — Execução e desvios** · *sábado 21/11, 23h59*
- **3a.** Pelo menos **2 achados** que mudaram sua compreensão do problema, cada um com o **objeto de conhecimento** associado.
- **3b.** Pelo menos **1 desvio** em relação ao Campo 02 (o que você planejou e não aconteceu) e a **causa técnica** — não vale "falta de tempo".
- **3c.** Pelo menos **1 decisão de ajuste**, com justificativa e **fonte**, e o objeto de conhecimento mobilizado.

**Campo 04 — Interação com IA** · *sábado 21/11, 23h59 · obrigatório e avaliado*
- Registre **pelo menos uma** interação real com uma IA sobre o seu CRUD.
- **4b.** Transcreva a pergunta **na íntegra** (copie e cole).
- **4c.** Resuma a resposta em **um parágrafo** com as suas palavras.
- **4d.** O que você **aceitou**, ligando ao objeto de conhecimento.
- **4e.** O que você **questionou ou descartou**, com **argumento técnico ou fonte** (teste, documentação, livro). Dica: **rode o código** que a IA sugeriu antes de decidir.
- **Print sem análise crítica = devolução imediata.** Se você aceitou tudo, volte e procure o que verificar.
</details>

### 🧩 CHECKPOINT CONCEITUAL INDIVIDUAL
*20 minutos · sem consulta a qualquer fonte, material ou colega · conforme orientação do professor.*

| | |
|---|---|
| **Nome do estudante** | _Marcos Eduardo_ |
| **Data de realização** | _21/11/2026_ |
| **Unidade curricular** | Algoritmos e Programação |
| **Professor(a)** | Rondineli Seba Salomão |

> **INSTRUÇÕES:** Responda individualmente, sem consulta. Você tem 20 minutos. As questões avaliam seu domínio dos objetos de conhecimento do componente — não sua solução para o problema. Respostas genéricas sem ancoragem técnica não são aceitas.

**QUESTÃO 1** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _> Operadores relacionais (`==`, `<`, `>`) comparam valores retornando `bool`, os lógicos (`and`, `or`) combinam condições e os aritméticos (`+`, `-`) fazem cálculos numéricos. No Catálogo de Jogos, após converter `input()` de `str` para `int`/`float`, uso relacionais com `or` (`ano < 1970 or ano > 2026`) para bloquear dados fora da faixa e operadores aritméticos (`i + 1` e `indice - 1`) para alinhar a lista exibida ao índice base zero do Python, evitando `TypeError` e `IndexError`._

**QUESTÃO 2** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…> O fluxograma mapeia visualmente o fluxo de execução e as decisões antes do código. No Catálogo de Jogos, ele mostrou a necessidade de criar desvios para entradas inválidas (título vazio, letras no lugar de números ou índice inexistente). Isso orientou o uso do laço `while True` com condicionais `if/elif/else` e `continue`, fazendo o programa voltar ao menu sem quebrar com `ValueError` ou `IndexError`._

**QUESTÃO 3** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _O paradigma imperativo estruturado organiza o programa em sequência, seleção (`if/elif/else`) e repetição (`while/for`), alterando o estado da memória passo a passo. No Catálogo de Jogos, cada operação do CRUD modifica ou consulta a lista de dicionários (`catalogo`) em uma ordem rigorosa — higienizando e convertendo entradas antes de salvar e checando `len(catalogo) == 0` antes de editar ou excluir — o que garante previsibilidade e facilidade de manutenção._

<details>
<summary>🔒 Uso do professor — critérios de avaliação do Checkpoint</summary>

| CRITÉRIO | SATISFATÓRIO | INSATISFATÓRIO |
|---|---|---|
| **Precisão conceitual** | Domínio do objeto de conhecimento, com vocabulário técnico adequado e sem erros conceituais relevantes. | Resposta vaga, com erros conceituais ou sem ancoragem nos objetos de conhecimento do componente. |
| **Relação conteúdo-problema** | Conecta o objeto de conhecimento ao problema trabalhado na AFP. | Responde o objeto de forma isolada, sem relação com o problema do ciclo. |
| **Qualidade do raciocínio** | Raciocínio técnico articulado: relaciona o objeto ao problema e explicita implicações para a investigação. | Apenas define o objeto, sem articular raciocínio ou relação com o problema investigado. |

**RESULTADO:** ☐ Satisfatório ☐ Insatisfatório
**AÇÃO DO PROFESSOR:** Checkpoint insatisfatório gera feedback escrito individualizado até 48h — o aluno ajusta a investigação antes da avaliação somativa.
</details>

### 🧩 CAMPO 03 — Execução e desvios
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59*

**3a. O que descobri que mudou minha compreensão do problema (mínimo 2 achados, com objeto de conhecimento associado):**
1. _…_ — *Objeto de conhecimento:* _Validar apenas o tipo de dado (`int` ou `float`) não impede a entrada de dados semanticamente inválidos no catálogo (como anos fora de faixa ou notas negativas), exigindo a combinação de tratamento de exceções com operadores relacionais e lógicos de domínio. — *Objeto de conhecimento:* Tratamento de exceções (`try/except ValueError`) combinado com operadores relacionais (`<`, `>`) e lógicos (`or`)._
2. _…_ — *Objeto de conhecimento:* _A exibição dos jogos ao usuário começa em `1`, enquanto as listas em Python são indexadas a partir de `0`, exigindo conversão aritmética (`indice - 1`) e checagem prévia dos limites da lista antes de atualizar ou excluir. — *Objeto de conhecimento:* Indexação baseada em zero em listas, operadores aritméticos (`+`, `-`) e prevenção de `IndexError`._
3. _…_ *(opcional)*

**3b. Desvio em relação ao Campo 02 (ao menos 1 — causa técnica):**
- **Desvio:** _O planejamento inicial previa testar os casos de borda diretamente nas operações do CRUD, mas durante os testes no VS Code as alterações nas opções de atualizar (`3`) e excluir (`4`) não surtiam efeito e falhavam no fluxo._
- **Causa técnica:** _O arquivo `main.py` não estava sendo salvo (`Ctrl + S`) antes de rodar novamente no terminal PowerShell (que mantinha a versão antiga em execução), somado a desalinhamento de indentação (4 espaços) nos blocos `elif` dentro do laço `while True`._

**3c. Decisão de ajuste (ao menos 1) com justificativa e fonte:**
- **Decisão:** _Padronizar a indentação de todos os blocos condicionais (`if`, `elif`, `else`) em 4 espaços, salvar o arquivo antes de cada execução (`py main.py`) e validar `if indice < 0 or indice >= len(catalogo):` antes de acessar qualquer posição da lista._
- **Fonte:** _Documentação Oficial do Python (`docs.python.org/pt-br/3/tutorial/controlflow.html` — Estruturas de controle de fluxo) e DOWNEY, Allen B. *Pense em Python* (Capítulos 5 e 10 — Condicionais e Listas)._

**Objeto de conhecimento mobilizado nesta decisão:** _Estruturas condicionais encadeadas (`if/elif/else`), indentação em blocos Python e validação de limites de índice em listas (`len()`)._

### 🧩 CAMPO 04 — Interação com IA
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59 | OBRIGATÓRIO*

> **Obrigatório e avaliado. Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.**

**4a. Ferramenta:** _GEMINI_  **Data:** _21/11/2026

**4b. Pergunta formulada (transcrita integralmente):**

> _…Não consigo excluir, nem alterar os jogos, o que fazer ?_

**4c. Resposta da IA (resumida em parágrafo):**

> _A IA apontou que a falha ocorria por possível erro de indentação nos blocos `elif opcao == "3":` e `elif opcao == "4":` dentro do laço `while True:` e pelo fato de o terminal ainda estar executando a versão anterior do arquivo `main.py` não salva. Como solução, apresentou a implementação completa das rotinas de atualização e exclusão utilizando `enumerate(catalogo)` para exibir a lista numerada, subtração de `1` para ajustar a entrada do usuário ao índice da lista, validação de faixa com `if indice < 0 or indice >= len(catalogo):` e remoção por meio do método `catalogo.pop(indice)`._

**4d. O que aceitei — com referência ao objeto de conhecimento do componente:**

>  Aceitei o alinhamento de indentação em 4 espaços nos blocos condicionais (`elif`), o uso de `enumerate(catalogo)` para exibir índices amigáveis (`i + 1`), a validação de limites (`indice < 0 or indice >= len(catalogo)`) para evitar `IndexError` e o uso do método nativo `catalogo.pop(indice)` para remover o dicionário escolhido da lista (objetos de conhecimento: estruturas condicionais `if/elif/else`, laços de repetição `for`/`while`, listas, dicionários e tratamento de exceções `ValueError`)._

**4e. O que questionei ou descartei — com argumento técnico ou fonte:**

> _Questionei o fluxo da rotina de atualização sugerida porque ela obriga o usuário a redigitar todos os atributos (`titulo`, `ano` e `nota`) e rejeita strings vazias (`if novo_titulo == "":`), impedindo a edição parcial de apenas um campo (como corrigir só a nota). Além disso, após rodar o código no terminal, constatei que a solução mantinha toda a lógica concentrada em um único laço monolítico sem modularização em funções (`def`), o que dificulta a manutenção e será refatorado conforme a Documentação Oficial do Python (*Definindo Funções*, `docs.python.org`)._

## 🟠 CICLO 05 — 09/09 — Condicionais aninhadas e operadores lógicos

<details>
<summary>📘 Orientações do Ciclo 05</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 05.
- Registre **qual combinação de condições** (`and`, `or`, `not`) você precisou e **por que** uma condicional aninhada ou um operador lógico foi a melhor escolha.
- Descreva **pelo menos um caso de teste** que você usou para provar a lógica (entrada → resultado esperado → resultado obtido).
- **Atenção à P1 (23/09):** reveja o Logbook até aqui. Complete itens em branco e confirme se os commits estão em dia.
- Na semana de 16/09 (Nivelamento / Peer Instruction), reserve 10 minutos para atualizar este arquivo.
</details>

#### Registro do Ciclo 05 — 09/09
1. **Desafio do ciclo (em 1 frase):** _Combinar condicionais aninhadas e operadores lógicos (`or`, `and`) para validar regras de domínio e evitar operações em catálogo vazio._
2. **O que implementei (commits / arquivos / links):** _Condicionais aninhadas (`if len(catalogo) == 0:` seguido de `else:` e validação de faixa com `or`) nos ramos de cadastro, atualização e exclusão do `main.py` (commit: `docs(logbook)_
3. **Objeto(s) de conhecimento mobilizado(s):** _Estruturas condicionais aninhadas (`if` dentro de `else`), operadores lógicos (`or`, `and`) e operadores relacionais (`<`, `>`, `<=`, `>=`, `==`).
_
4. **Desvio ou erro encontrado + causa técnica:**Ao tentar atualizar ou excluir com a lista vazia, o programa solicitava o índice antes de verificar se havia jogos cadastrados. Causa técnica: ausência de condicional externa testando `len(catalogo) == 0` antes da leitura de entrada.
 __
5. **Decisão de ajuste + fonte:** _Criar condicional aninhada externa verificando `if len(catalogo) == 0:` e validar faixas inválidas com `or` (`ano < 1970 or ano > 2026`). Caso de teste comprovado: entrada `ano = 1965` → esperado: erro de faixa → obtido: `"Erro: Digite um ano válido entre 1970 e 2026!"`. Fonte: DOWNEY, Allen B. *Pense em Python* 
6. **Feedback recebido e o que mudei:** _Orientação do Ciclo 05 para registrar casos de teste (entrada → esperado → obtido) e justificar o aninhamento de condições.

7. **Próximo passo:** _Implementar os laços de repetição (`while` e `for`) e controle de fluxo (`break`, `continue`)_

## 🟠 CICLO 06 — 30/09 — Devolutiva da P1 + repetição: `for`, `while`, `break`, `continue`

<details>
<summary>📘 Orientações do Ciclo 06</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 06.
- Use o item 6 para registrar a **devolutiva da P1**: o que errou e **qual conceito** estava faltando. Esses erros alimentam o **Campo 07c** (conceitos corrigidos). *Anote já, para não esquecer.*
- Registre **por que escolheu `for` ou `while`** em cada laço do seu CRUD (cadastro em lote, listagem, menu).
- Item 4: se um laço ficou infinito ou pulou itens, descreva a **causa técnica** (condição de parada, incremento, `break` fora de lugar).
</details>

#### Registro do Ciclo 06 — 30/09
1. **Desafio do ciclo (em 1 frase):** _Controlar a repetição contínua do menu e a iteração sobre os jogos cadastrados usando `while`, `for`, `break` e `continue`.
_
2. **O que implementei (commits / arquivos / links):** Laço `while True:` no menu principal com `break` na opção `"0"`, `continue` nos erros de validação e laço `for i, jogo in enumerate(catalogo):` na listagem do `main.py` (commit: `docs(logbook): registro do ciclo 06`)
3. **Objeto(s) de conhecimento mobilizado(s):** _Laços de repetição indefinida (`while`), laços definidos (`for` com `enumerate()`), instruções de controle de laço (`break` e `continue`).

4. **Desvio ou erro encontrado + causa técnica:** _O programa encerrava por completo ao errar a digitação de uma nota ou ano, em vez de voltar ao menu. Causa técnica: uso incorreto de `break` (que interrompe o laço `while`) no lugar de `continue` (que salta para a próxima iteração)._
5. **Decisão de ajuste + fonte:** _Manter `while True` com `break` apenas na opção `"0"`, usar `continue` em todos os tratamentos de erro e `for` para percorrer a lista de tamanho conhecido. Fonte: DOWNEY, Allen B. *Pense em Python* (Capítulo 7) e Documentação Oficial do Python (*break e continue*)._
6. **Feedback recebido (inclui devolutiva da P1) e o que mudei:** __
7. **Próximo passo:** _Estruturar o armazenamento dinâmico e as operações sobre a lista_

## 🟠 CICLO 07 — 07/10 — Listas: armazenamento e iteração

<details>
<summary>📘 Orientações do Ciclo 07</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 07.
- Justifique **por que seus dados cabem em uma lista** e como você os percorre (iteração).
- Item 4: erros típicos — índice fora do intervalo, alterar a lista enquanto percorre, confundir cópia com referência. Registre qual deles aconteceu e a causa técnica.
- Item 3: nomeie as **operações de lista** que usou (adicionar, remover, ordenar, fatiar…).
</details>

#### Registro do Ciclo 07 — 07/10
1. **Desafio do ciclo (em 1 frase):** _Armazenar e manipular dinamicamente os registros do Catálogo de Jogos em memória utilizando listas e seus métodos nativos._
2. **O que implementei (commits / arquivos / links):** _Lista principal `catalogo = []`, inserção com `.append()`, consulta de tamanho com `len(catalogo)`, iteração com `enumerate()` e remoção por índice com `.pop(indice)` no `main.py` (commit: `docs(logbook)_
3. **Objeto(s) de conhecimento mobilizado(s):** _Estrutura de dados mutável (`list`), indexação base zero e métodos/funções de lista (`.append()`, `.pop()`, `len()`, `enumerate()`).
_
4. **Desvio ou erro encontrado + causa técnica:** _Falha com `IndexError: list index out of range` ao tentar excluir ou alterar um jogo digitando o número exibido na tela. Causa técnica: a exibição ao usuário inicia em `1`, enquanto a lista em Python inicia no índice `0` e vai até `len(catalogo) - 1`._
5. **Decisão de ajuste + fonte:** _Usar lista pela necessidade de coleção dinâmica e ordenada, subtrair `1` do índice digitado (`int(input(...)) - 1`) e validar `if indice < 0 or indice >= len(catalogo)_
6. **Feedback recebido e o que mudei:** _Orientação para nunca remover itens de uma lista dentro de um laço `for` que a percorre, realizando a remoção pontual pelo índice validado fora da iteração.
_
7. **Próximo passo:** _Estruturar cada jogo como um dicionário (`chave: valor`) para organizar os atributos no Ciclo 08.
_

## 🟠 CICLO 08 — 14/10 — Busca/consulta e introdução a dicionários e matrizes

<details>
<summary>📘 Orientações do Ciclo 08</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 08.
- Explique **por que cada item do seu catálogo virou um dicionário** (chave → valor) em vez de uma lista de valores soltos.
- Item 4: registre **qual busca falhou** (item inexistente, tipo diferente — `"2"` ≠ `2`, chave com maiúscula errada) e a causa técnica.
- Se usou o lote de dados defeituoso, registre **qual registro** quebrou a busca.
- Item 5: cite a fonte (*Pense em Python*, cap. 11, ou outra).
</details>

#### Registro do Ciclo 08 — 14/10
1. **Desafio do ciclo (em 1 frase):** _ Modelar cada jogo do catálogo como um dicionário (`titulo`, `ano`, `nota`) dentro da lista principal para acesso e edição estruturada por chave.
_
2. **O que implementei (commits / arquivos / links):** _Criação do dicionário `novo_jogo = {"titulo": titulo, "ano": ano, "nota": nota}`, leitura por chave na listagem (`jogo['titulo']`) e atualização direta (`catalogo[indice]["nota"] = nova_nota`) no `main.py` (commit: `docs(logbook)_
3. **Objeto(s) de conhecimento mobilizado(s):** _Estrutura de dados associativa (`dict` — mapeamento chave-valor), composição de lista de dicionários, acesso e mutação por chave.
_
4. **Desvio ou erro encontrado + causa técnica:** _Erro `KeyError` ao buscar `jogo['Titulo']` e `TypeError` ao tentar acessar `catalogo["titulo"]` diretamente. Causa técnica: sensibilidade a maiúsculas/minúsculas nas chaves do dicionário e tentativa de indexar a lista externa (`list`) com string antes de selecionar o índice numérico do item.
_
5. **Decisão de ajuste + fonte:** _Adotar dicionários em vez de listas soltas para dar significado semântico a cada campo, padronizando todas as chaves em minúsculo (`"titulo"`, `"ano"`, `"nota"`) e indexando primeiro a lista (`catalogo[indice]`) e depois a chave (`["titulo"]`)._
6. **Feedback recebido e o que mudei:** _Orientação do Ciclo 08 para padronizar rigorosamente o esquema de chaves dos dicionários e validar entradas antes de indexar a estrutura.
_
7. **Próximo passo:** _Atualizar o Painel de Acompanhamento, realizar o commit final do Grupo 2 hoje_

---

# 🔵 GRUPO 3 — prazo quinta 26/11 às 23h59

> **Janela:** sábado 21/11 → quinta 26/11. **O que entregar:** Registros dos Ciclos 09, 10, 11 e 12 · Campo 05 (duas revisões por pares) · Campo 06 · Campo 07.
>
> ⚠️ O prazo vem **um dia depois da P2 (25/11)**. Os Campos 06 e 07 dependem de todo o Logbook: deixe-os para o final, mas **adiante o rascunho do 6c e do 7a/7b antes da Defesa (18/11)**.

**Checklist do Grupo 3**
- [ x] Registros dos Ciclos 09, 10, 11 e 12 com os 7 itens
- [ x] Campo 05: duas revisões (Ciclos 09 e 12), blocos 5a a 5e
- [x ] Campo 06: decisão autônoma, lacuna com plano, pergunta da banca com 5 linhas ou mais
- [ x] Campo 07: 7a a 7e, com 3 objetos, 2 equívocos corrigidos e transferência
- [ x] Coerência entre Campo 01 e Campo 07
- [x ] Painel de acompanhamento completo

## 🔵 CICLO 09 — 21/10 — Atualização e exclusão: CRUD completo

<details>
<summary>📘 Orientações do Ciclo 09 — Registro + Campo 05 (revisão por pares nº 1)</summary>

- Neste ciclo seu CRUD ficou **completo** (Create, Read, Update, Delete). Preencha o Registro do Ciclo 09.
- **Item 4:** *atualizar* ou *excluir* item inexistente, e excluir durante um laço (a lista muda de tamanho e itens são pulados) são erros comuns.
- **Campo 05 — Registro de Revisão por Pares.** Você passa a ser **revisor** do CRUD de um colega.
  - Cada revisão tem **um registro** (copie a seção do Campo 05) com o nome e o link do repositório revisado.
  - **Revise o processo, não só o código:** o que foi decidido, em que objeto de conhecimento se apoia, com que fonte.
  - **5a:** liste as etapas da revisão (ex.: rodar o CRUD, testar com o lote de dados com defeito, ler o código, registrar achados, devolver feedback).
  - **5b:** liste os insumos que usou (lote de dados, casos de teste, `requisitos.md`) com quantidade planejada, utilizada e variação.
  - **5c:** diga se a solução do colega atende ao critério (Sim/Parcialmente/Não) e **qual critério** usou (ex.: requisito do `requisitos.md`).
  - **5d:** riscos da revisão (ex.: não conseguir rodar o código do colega) e como mitigou.
  - **5e:** registre **cada decisão técnica** da revisão com **data, responsável, objeto de conhecimento e fundamentação/referência**. *Sem objeto e sem referência, não é rastreável.*
  - Feedback ao colega: **específico e respeitoso** (o que está bom, o que quebrou, como reproduzir, sugestão).
</details>

#### Registro do Ciclo 09 — 21/10
1. **Desafio do ciclo (em 1 frase):** _…_
2. **O que implementei (commits / arquivos / links):** _…_
3. **Objeto(s) de conhecimento mobilizado(s):** _…_
4. **Desvio ou erro encontrado + causa técnica:** _…_
5. **Decisão de ajuste + fonte:** _…_
6. **Feedback recebido e o que mudei:** _…_
7. **Próximo passo:** _…_

### 🧩 CAMPO 05 — Registro de Revisão por Pares
*Adaptação do **Logbook do Time** (Apêndice C) para o CRUD individual. Documento atualizado pelo **revisor**. Cada decisão técnica relevante deve ter associado o objeto de conhecimento correspondente.*

> ⚠️ **Nota de adaptação:** o Apêndice C original prevê Gestor, Responsável Técnico, Analista de Qualidade e Comunicador. Como o CRUD é **individual** e os alunos atuam como **revisores**, mantive os blocos 5a a 5e e troquei os papéis por **Autor** (dono do CRUD) e **Revisor** (você). *Pendente de validação do professor/NDE.*

> **O Logbook de revisão é um registro de conhecimento em ação.** Cada decisão técnica relevante deve estar associada ao objeto de conhecimento que a fundamenta, à justificativa técnica e à referência utilizada. Registros sem esse vínculo não são aceitos.

#### Revisão nº 1

| | |
|---|---|
| **Autor do CRUD revisado** | _nome_ |
| **Repositório revisado** | _link_ |
| **Revisor** | _seu nome_ |
| **Unidade curricular / Semestre** | Algoritmos e Programação · 2026.2 |
| **Ciclo / data** | _Ciclo 09 · 21/10_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO — análise técnica de cada etapa:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 1. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 2. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 3. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 4. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 5. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:** _…_
- **A solução atende?** ☐ Sim ☐ Parcialmente ☐ Não

**5d. GESTÃO DE RISCOS:**
- **Risco:** _…_
- **Estratégia de mitigação:** _…_

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |

> **IMPORTANTE:** Decisão registrada sem objeto de conhecimento associado e sem referência é considerada **não rastreável** e não conta para a avaliação formativa. O vínculo entre processo e conteúdo é obrigatório em todas as decisões relevantes.

## 🔵 CICLO 10 — 28/10 — Modularização: funções

<details>
<summary>📘 Orientações do Ciclo 10</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 10.
- Explique **como dividiu** o CRUD em funções (`cadastrar()`, `buscar()`, `alterar()`, `excluir()`, `listar()`, `menu()`) e **por que** cada função tem aquela responsabilidade.
- Item 4: erros típicos — variável fora de escopo, função sem `return`, parâmetro na ordem errada.
- Compare o código **antes e depois** da refatoração: o que ficou mais claro? Registre no item 6 o feedback do colega que fez a *peer review*.
</details>

#### Registro do Ciclo 10 — 28/10
1. **Desafio do ciclo (em 1 frase):** _…_
2. **O que implementei (commits / arquivos / links):** _…_
3. **Objeto(s) de conhecimento mobilizado(s):** _…_
4. **Desvio ou erro encontrado + causa técnica:** _…_
5. **Decisão de ajuste + fonte:** _…_
6. **Feedback recebido e o que mudei:** _…_
7. **Próximo passo:** _…_

## 🔵 CICLO 11 — 04/11 — Recursividade

<details>
<summary>📘 Orientações do Ciclo 11 — Registro + Campo 06 (Grupo 3)</summary>

- Preencha o Registro do Ciclo 11 (caso base, chamada recursiva, pilha de execução).
- **Campo 06 — Próximos passos para a defesa** · *individual · quinta 26/11, 23h59*. Prepare-se para a **Defesa Técnica de quarta 18/11**: como o prazo é posterior à defesa, **adiante pelo menos o 6c** (pergunta da banca e resposta) e leve-o para a arguição.
  - **6a.** Uma **decisão técnica que você defende com plena autonomia**: algo que aprendeu e **é exclusivamente seu**, que nenhum colega consegue explicar por você.
  - **6b.** Uma **lacuna técnica real** e um **plano de ação** com passos e datas para saná-la antes da defesa.
  - **6c.** Uma **pergunta que a banca pode fazer** (nível de Avaliação ou Criação) e a sua **resposta fundamentada em, no mínimo, 5 linhas**, com o objeto de conhecimento e a fonte.
  - Dica: leia a **Rubrica de Defesa Técnica** (no Encerramento) e escolha uma pergunta que teste *aplicação*, *evolução* ou *transferência*.
</details>

#### Registro do Ciclo 11 — 04/11
1. **Desafio do ciclo (em 1 frase):** _…_
2. **O que implementei (commits / arquivos / links):** _…_
3. **Objeto(s) de conhecimento mobilizado(s):** _…_
4. **Desvio ou erro encontrado + causa técnica:** _…_
5. **Decisão de ajuste + fonte:** _…_
6. **Feedback recebido e o que mudei:** _…_
7. **Próximo passo:** _…_

### 🧩 CAMPO 06 — Próximos passos para a defesa
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

**6a. Decisão técnica que defendo com plena autonomia — o que aprendi que é exclusivamente meu e não consigo transferir para nenhum colega:**

> _…_

**6b. Lacuna técnica e plano de ação para saná-la:**

- **Lacuna:** _…_
- **Plano de ação (passos e datas):** _…_

**6c. Pergunta que a banca pode fazer — com resposta fundamentada (mínimo 5 linhas):**

- **Pergunta:** _…_
- **Resposta:**

> _…_

**Objeto de conhecimento mobilizado:** _…_
**Fonte:** _…_

## 🔵 CICLO 12 — 11/11 — Refatoração e qualidade de código

<details>
<summary>📘 Orientações do Ciclo 12 — Registro + Campo 05 (revisão nº 2) + início do Campo 07</summary>

- Preencha o Registro do Ciclo 12. Registre o que revisou: código duplicado, nomes ruins, funções grandes, comentários desnecessários, lógica confusa.
- **Campo 05 — Revisão por pares nº 2.** Foque em **qualidade**: o CRUD do colega resiste aos casos de teste (mínimos, máximos, inválidos, entradas vazias) e ao **lote de dados com defeito**? Use a seção abaixo (copie o bloco *Revisão nº 1* do Ciclo 09 e preencha novamente).
- **Campo 07 — Evolução conceitual** · *individual · quinta 26/11, 23h59.* Comece agora, enquanto a memória do semestre está fresca; leve o rascunho de 7a e 7b para a Defesa de 18/11. Dicas por item:
  - **7a.** Releia o **Campo 01** e resuma o que você *pensava* e *achava que sabia*. Seja honesto, mesmo se o Campo 01 estiver "errado".
  - **7b.** Pelo menos **3 objetos de conhecimento** na tabela: o que você *não dominava*, o que *aprendeu e consegue demonstrar* e a **evidência** (em qual Campo ou ciclo do Logbook aparece).
  - **7c.** Pelo menos **2 equívocos corrigidos**, dizendo **o que os corrigiu** (Fechamento Teórico, pesquisa, *Peer Review*, arguição, devolutiva da P1).
  - **7d.** **Transferência:** um exemplo concreto de aplicar o que aprendeu em um **contexto diferente** do CRUD (outra área do seu curso ou outro tipo de sistema).
  - **7e.** Avaliação honesta do que **ainda não domina** e vai aprofundar.
</details>

#### Registro do Ciclo 12 — 11/11
1. **Desafio do ciclo (em 1 frase):** _…_
2. **O que implementei (commits / arquivos / links):** _…_
3. **Objeto(s) de conhecimento mobilizado(s):** _…_
4. **Desvio ou erro encontrado + causa técnica:** _…_
5. **Decisão de ajuste + fonte:** _…_
6. **Feedback recebido e o que mudei:** _…_
7. **Próximo passo:** _…_

### 🧩 CAMPO 05 — Registro de Revisão por Pares (revisão nº 2)

| | |
|---|---|
| **Autor do CRUD revisado** | _nome_ |
| **Repositório revisado** | _link_ |
| **Revisor** | _seu nome_ |
| **Ciclo / data** | _Ciclo 12 · 11/11_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 1. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 2. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 3. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 4. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 5. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:** _…_
- **A solução atende?** ☐ Sim ☐ Parcialmente ☐ Não

**5d. GESTÃO DE RISCOS:**
- **Risco:** _…_
- **Estratégia de mitigação:** _…_

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |

### 🧩 CAMPO 07 — Evolução conceitual
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

*Evidência rastreável de aprendizagem entre o início e o encerramento do ciclo AFP.*

**7a. O que eu pensava no início do ciclo (com base no Campo 01 — registrar a hipótese inicial e os objetos de conhecimento que achava conhecer):**

> _…_

**7b. O que aprendi — conceitos, princípios ou relações técnicas que não dominava no início e que agora consigo explicar com precisão (mínimo 3 objetos de conhecimento):**

| OBJETO DE CONHECIMENTO | O QUE EU NÃO DOMINAVA | O QUE APRENDI E CONSIGO DEMONSTRAR | EVIDÊNCIA (campo do Logbook onde aparece) |
|---|---|---|---|
| _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ |

**7c. Conceitos que precisei corrigir ao longo do ciclo — onde eu estava equivocado e o que o corrigiu (Fechamento Teórico, pesquisa, Peer Review, arguição):**

1. **Equívoco:** _…_ — **Correção:** _…_
   **O que corrigiu:** _…_
2. **Equívoco:** _…_ — **Correção:** _…_
   **O que corrigiu:** _…_

**7d. Transferência — como este aprendizado se aplica a um contexto diferente do problema trabalhado (ao menos 1 exemplo concreto da área de formação):**

> _…_

**7e. Avaliação honesta do próprio percurso — o que ainda não domino e preciso aprofundar após este ciclo:**

> _…_

---

# 🏁 DEFESA TÉCNICA — quarta 18/11

<details>
<summary>📘 Orientações para a Defesa Técnica e preparação</summary>

**A Defesa é antes dos prazos dos Grupos 2 e 3.** Você será arguido sobre o que já estiver registrado e commitado. Priorize, até **terça 17/11**:
- [ ] **Grupo 1 entregue** (prazo 16/11): Identificação, Registros 01 a 04, Campos 01 e 02.
- [ ] **Campo 04 (IA)** e **Campo 03** ao menos em rascunho, para sustentar as perguntas sobre decisões (critérios 2 e 5).
- [ ] **Campo 06c** (pergunta da banca e resposta) e **rascunho de 7a e 7b**, para sustentar a evolução conceitual (critério 3).
- [ ] Registros dos Ciclos já feitos, mesmo que ainda não "entregues" no prazo do grupo.
- [ ] `README.md`, `docs/` e CRUD rodando.
- [ ] Você consegue explicar **cada linha** do seu código e **cada decisão** registrada.
- Os demais itens seguem com os prazos dos grupos (21/11 e 26/11). A banca pode consultar o histórico do Git.

**A Defesa Técnica é individual.** Você será arguido sobre o que registrou. Cada aluno recebe pelo menos **1 questão** nos níveis de **Avaliação** ou **Criação** (taxonomia de Bloom).

**Como a Rubrica se liga ao seu Logbook:**

| Critério da Rubrica | Onde você prepara a evidência |
|---|---|
| 1. Domínio dos objetos de conhecimento | Campos 01, 02 e 07b |
| 2. Aplicação do conteúdo à solução ⚠️ *inegociável* | Registros dos ciclos (itens 3 e 5), Campo 03c e Campo 05e |
| 3. Evolução conceitual ⚠️ *inegociável* | Campo 01 → Campo 07 (7a, 7b e 7c; leve o rascunho) |
| 4. Capacidade de transferência | Campo 07d |
| 5. Argumentação sob pressão | Campo 06c e Campo 04e |
| 6. Autonomia intelectual e coerência com o Logbook | Todo o Logbook (principalmente Campos 04 e 06a) |

**Treino:** peça a um colega que faça 3 perguntas "imprevistas" sobre o seu CRUD e responda **sem consultar** o Logbook. Se não conseguir, volte ao Campo 06b.
</details>

## 🧩 RUBRICA DE DEFESA TÉCNICA (revisada)
*Avaliação individual de cada membro na Semana 16. Cada membro recebe ao menos 1 questão nos níveis de Avaliação ou Criação da Taxonomia de Bloom. Critérios revisados para medir aprendizagem, aplicação, evolução e transferência do conteúdo.*

| | |
|---|---|
| **Nome** | _…_ |
| **Curso / Time / Função** | _…_ |

<details>
<summary>🔒 Uso do professor — rubrica completa</summary>

| CRITÉRIO | EXCELENTE (4,0) | SATISFATÓRIO (3,0) | INSATISFATÓRIO (2,0) | AUSENTE (0) |
|---|---|---|---|---|
| **1. DOMÍNIO DOS OBJETOS DE CONHECIMENTO** — Responde com precisão técnica, sem apoio dos colegas, demonstrando aprendizagem do conteúdo. | Responde com precisão e profundidade, nomeando os objetos de conhecimento mobilizados sem hesitação. | Responde com precisão, com imprecisões pontuais que não comprometem o raciocínio. | Responde de forma vaga, com erros conceituais relevantes ou dependendo dos colegas. | Não responde ou demonstra desconhecimento total. |
| **2. APLICAÇÃO DO CONTEÚDO À SOLUÇÃO** — Demonstra como os objetos de conhecimento fundamentaram as decisões do processo. | Explicita com precisão qual objeto de conhecimento fundamentou cada decisão relevante do processo investigativo, citando referência e demonstrando por que aquele conhecimento era o mais adequado. | Estabelece a relação conteúdo-decisão na maioria das perguntas, com alguma imprecisão pontual. | Não consegue explicitar a relação entre o conteúdo e as decisões do processo investigativo com clareza. | Não demonstra nenhuma relação entre os objetos de conhecimento e as decisões tomadas. |
| **3. EVOLUÇÃO CONCEITUAL** — Demonstra aprendizagem em relação ao que sabia no início do ciclo. | Identifica com precisão o que aprendeu, o que corrigiu e como o conhecimento evoluiu ao longo do ciclo. | Demonstra evolução em parte dos conceitos trabalhados, com alguma dificuldade de articular a trajetória. | Dificuldade em identificar diferenças entre o que sabia no início e o que domina agora. | Não demonstra nenhuma percepção de evolução conceitual ao longo do ciclo. |
| **4. CAPACIDADE DE TRANSFERÊNCIA** — Aplica o conhecimento a um contexto diferente do problema trabalhado. | Consegue transferir o aprendizado para um contexto novo com fundamentação técnica precisa. | Realiza a transferência com imprecisões que não comprometem a lógica do raciocínio. | Demonstra dificuldade em aplicar o conhecimento a contextos diferentes do problema original. | Não consegue realizar nenhuma transferência do conhecimento para contexto diferente. |
| **5. ARGUMENTAÇÃO SOB PRESSÃO** — Mantém coerência técnica diante de questionamentos imprevistos. | Mantém raciocínio coerente, reconhece limites com honestidade e reformula com fundamentação. | Mantém coerência na maior parte, com hesitações pontuais sem perda do fio técnico. | Fragilidade técnica diante de questionamentos imprevistos. | Não sustenta argumentação técnica diante de nenhum questionamento. |
| **6. AUTONOMIA INTELECTUAL E COERÊNCIA COM O LOGBOOK** — Defende o que registrou com consciência e sem depender do grupo. | Defende com precisão as decisões do Logbook, demonstrando autoria plena e independência intelectual. | Defende a maioria das decisões com coerência, com alguma imprecisão ou apoio pontual. | Depende dos colegas ou demonstra desconhecimento de parte do que registrou no próprio Logbook. | Não reconhece o que registrou ou não demonstra autonomia intelectual durante a arguição. |

**PONTUAÇÃO:** _____ / 24,0 **CONCEITO:** _____________

**Conversão:** 20–24 = Excelente (4,0) | 14–19 = Satisfatório (3,0) | 8–13 = Insatisfatório (2,0) | < 8 = Ausente (0)

> ⚠️ **Critérios 2 (Aplicação) e 3 (Evolução Conceitual) são inegociáveis — AUSENTE em qualquer um deles implica nota máxima de 2,0 na Defesa, independentemente do desempenho nos demais.**

**OBSERVAÇÕES:** _…_

**Professor(a):** _________________  **Data:** ___________
</details>

### Registro do Encerramento — 18/11
1. **O que apresentei/defendi (em 1 frase):** _…_
2. **Objeto(s) de conhecimento que a banca mais explorou:** _…_
3. **Pergunta que mais me desafiou e como respondi:** _…_
4. **O que levo deste semestre para o próximo módulo:** _…_

---

# 🆘 Estou atrasado no Logbook. E agora?

1. **Não apague nem "retroescreva" o passado.** Preencha agora e **escreva a data real** do preenchimento (ex.: *"preenchido com atraso em 12/11"*).
2. **Campo 01 e Checkpoint (sem consulta):** se perdeu a janela, registre **o que sabe hoje, sem consultar nada**, marcando-o como *preenchimento tardio*. Combine o tratamento com o professor.
3. **Priorize a ordem dos grupos:** Grupo 1 (16/11) → Defesa (18/11) → Grupo 2 (21/11) → Grupo 3 (26/11). Dentro de cada grupo, os Campos vêm antes dos Registros.
4. **Use o histórico do Git** (`git log --oneline`) para reconstruir o que fez em cada ciclo — ele é uma evidência melhor que a memória.
5. **Fale com o professor** antes do prazo, não depois.
