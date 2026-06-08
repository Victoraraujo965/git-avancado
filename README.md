# Git Avançado

> Estudo prático de Git avançado com branching, rebase e automação de qualidade de código via pre-commit hooks.

---

## Sobre o projeto

Este repositório é parte da minha trilha de estudos em **Engenharia de Dados**. O objetivo é consolidar boas práticas de versionamento e qualidade de código que são usadas em times de tecnologia no mercado.

**O que foi praticado:**

- Branching e fluxo de trabalho com múltiplas branches
- Rebase para manter histórico linear
- Configuração de pre-commit hooks com `flake8` e `black`
- Padrão de mensagens de commit (Conventional Commits)

---

## Ferramentas de qualidade de código

Todo commit neste repositório passa automaticamente por duas verificações antes de ser aceito:

| Ferramenta | Função |
|---|---|
| **black** | Formata o código automaticamente no padrão PEP 8 |
| **flake8** | Analisa o código e aponta erros de estilo e sintaxe |

Se qualquer verificação falhar, o commit é bloqueado até a correção.

---

## Como usar este repositório

### Pré-requisitos

- Python 3.8+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/Victoraraujo965/git-avancado.git
cd git-avancado

# Instale as dependências
pip install -r requirements.txt

# Instale os hooks
pre-commit install
```

A partir daí, toda vez que você rodar `git commit`, o **black** e o **flake8** rodam automaticamente.

---

## Padrão de commits

Este projeto segue o padrão **Conventional Commits**:

```
feat: adiciona nova funcionalidade
fix: corrige bug
docs: atualiza documentação
refactor: refatora código sem mudar comportamento
chore: tarefas de manutenção (configs, dependências)
```

---

## Estrutura do projeto

```
git-avancado/
├── src/
│   └── exemplo.py              # Script de exemplo (tabuada com list comprehension)
├── .pre-commit-config.yaml     # Configuração dos hooks
├── requirements.txt            # Dependências do projeto
└── README.md
```

---

## Por que isso importa?

Em times com múltiplos desenvolvedores, consistência de código é crítica. Sem automação, cada pessoa formata de um jeito diferente — o que gera ruído nas revisões de código e dificulta a leitura.

Com pre-commit hooks:

- Zero discussão de estilo no time
- Código sempre legível e padronizado
- Erros simples são pegos antes do PR
- Revisões focam em lógica, não em formatação

É a primeira barreira de qualidade — rápida, barata e automática.

---

## Recursos

- [Pro Git (gratuito)](https://git-scm.com/book/pt-br/v2)
- [Conventional Commits](https://www.conventionalcommits.org/pt-br)
- [Black — The uncompromising code formatter](https://black.readthedocs.io)
- [Flake8 documentation](https://flake8.pycqa.org)
- [pre-commit docs](https://pre-commit.com)

---

*Projeto desenvolvido como parte da trilha de estudos em Engenharia de Dados — Victor Araujo*
