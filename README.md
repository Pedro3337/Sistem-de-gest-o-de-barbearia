# 💈 Sistema de Gestão de Barbearia

Sistema web para gerenciamento de barbearias, desenvolvido com foco em organização, escalabilidade e boas práticas de arquitetura.

O sistema possui três perfis de usuários:

- 👑 Administrador
- ✂️ Barbeiro
- 👤 Cliente

Cada perfil possui funcionalidades específicas, permitindo o gerenciamento completo dos atendimentos da barbearia.

---

# 🚀 Tecnologias

## Front-end

- HTML5
- CSS3
- JavaScript

## Back-end

- Django Ninja API
- Python

## Banco de Dados

- MySQL

---

# 🏛 Arquitetura

O projeto será desenvolvido seguindo princípios da **Clean Architecture**, separando responsabilidades em:

- Entidades
- DTOs
- Casos de Uso
- Repositórios
- Serviços
- API

Essa organização facilita manutenção, testes e evolução do sistema.

---

# 📂 Módulos do Sistema

```
Sistema
│
├── Usuários
├── Clientes
├── Barbeiros
├── Serviços
├── Agendamentos
├── Atendimentos
├── Pagamentos
├── Relatórios
└── Administração
```

---

# 👥 Módulo Usuários

Responsável pela autenticação e gerenciamento de acesso.

## Entidade

### Usuário

| Campo | Tipo |
|--------|------|
| id | UUID |
| nome | String |
| email | String |
| senha | String |
| perfil | Enum |
| ativo | Boolean |

## Casos de Uso

- Login
- Logout
- Alterar senha
- Atualizar perfil

---

# 👤 Módulo Clientes

Responsável pelos clientes da barbearia.

## Entidade

### Cliente

| Campo | Tipo |
|--------|------|
| id | UUID |
| usuario_id | UUID |
| telefone | String |
| data_cadastro | DateTime |

## Casos de Uso

- Cadastrar cliente
- Atualizar cadastro
- Visualizar histórico
- Visualizar agendamentos

---

# ✂️ Módulo Barbeiros

Gerencia os barbeiros.

## Entidade

### Barbeiro

| Campo | Tipo |
|--------|------|
| id | UUID |
| usuario_id | UUID |
| telefone | String |
| especialidade | String |
| comissão | Decimal |
| ativo | Boolean |

## Casos de Uso

- Cadastrar barbeiro
- Atualizar barbeiro
- Alterar disponibilidade
- Visualizar agenda

---

# 💇 Módulo Serviços

Representa os serviços oferecidos.

## Entidade

### Serviço

| Campo | Tipo |
|--------|------|
| id | UUID |
| nome | String |
| descrição | String |
| duração | Integer |
| preço | Decimal |
| ativo | Boolean |

## Casos de Uso

- Cadastrar serviço
- Atualizar serviço
- Excluir serviço
- Listar serviços

---

# 📅 Módulo Agendamentos

Gerencia todos os horários marcados.

## Entidade

### Agendamento

| Campo | Tipo |
|--------|------|
| id | UUID |
| cliente_id | UUID |
| barbeiro_id | UUID |
| serviço_id | UUID |
| data_hora | DateTime |
| status | Enum |
| observação | Text |

## Status

- AGENDADO
- CANCELADO
- FALTOU
- CONCLUÍDO

## Casos de Uso

Cliente

- Agendar horário
- Cancelar agendamento

Barbeiro

- Confirmar atendimento
- Visualizar agenda

Administrador

- Visualizar agenda geral
- Reagendar atendimento

---

# ✅ Módulo Atendimentos

Representa um atendimento realmente realizado.

> Um atendimento somente será criado quando um agendamento for concluído.

## Entidade

### Atendimento

| Campo | Tipo |
|--------|------|
| id | UUID |
| agendamento_id | UUID |
| barbeiro_id | UUID |
| cliente_id | UUID |
| valor_total | Decimal |
| desconto | Decimal |
| valor_final | Decimal |
| data_realização | DateTime |
| observação | Text |

## Casos de Uso

- Iniciar atendimento
- Finalizar atendimento
- Aplicar desconto
- Registrar observações

---

# 💳 Módulo Pagamentos

Controla os pagamentos dos atendimentos.

## Entidade

### Pagamento

| Campo | Tipo |
|--------|------|
| id | UUID |
| atendimento_id | UUID |
| forma_pagamento | Enum |
| valor | Decimal |
| data_pagamento | DateTime |
| status | Enum |

## Formas de pagamento

- PIX
- Dinheiro
- Débito
- Crédito

## Casos de Uso

- Registrar pagamento
- Estornar pagamento
- Consultar pagamentos

---

# 📊 Módulo Relatórios

Este módulo não possui entidades.

Seu objetivo é consultar informações dos demais módulos.

## Casos de Uso

Administrador

- Dashboard
- Faturamento mensal
- Faturamento anual
- Faturamento por barbeiro
- Serviços mais realizados
- Clientes mais frequentes

Barbeiro

- Quantidade de atendimentos
- Valor faturado
- Comissão

---

# ⚙️ Módulo Administração

Responsável pela gestão completa da barbearia.

## Casos de Uso

- Gerenciar usuários
- Gerenciar clientes
- Gerenciar barbeiros
- Gerenciar serviços
- Gerenciar agendamentos
- Consultar relatórios
- Configurar sistema

---

# 👑 Perfis do Sistema

## Administrador

Possui acesso total ao sistema.

Pode:

- Gerenciar usuários
- Gerenciar barbeiros
- Gerenciar clientes
- Gerenciar serviços
- Visualizar relatórios
- Visualizar faturamento
- Configurar sistema

---

## ✂️ Barbeiro

Pode:

- Visualizar agenda
- Confirmar atendimento
- Finalizar atendimento
- Registrar pagamento
- Visualizar histórico
- Consultar faturamento pessoal

---

## 👤 Cliente

Pode:

- Criar conta
- Agendar horário
- Cancelar agendamento
- Consultar histórico
- Atualizar perfil

---

# 🔄 Fluxo da Aplicação

```
Cliente
    │
    ▼
Realiza Login
    │
    ▼
Agenda um Horário
    │
    ▼
Agendamento
(Status = AGENDADO)
    │
    ▼
Barbeiro confirma atendimento
    │
    ▼
Realiza o serviço
    │
    ▼
Finaliza atendimento
    │
    ▼
Sistema cria um Atendimento
    │
    ▼
Pagamento é registrado
    │
    ▼
Relatórios são atualizados
    │
    ▼
Administrador acompanha Dashboard
```

---

# 🏗 Estrutura da Arquitetura

```
Frontend

HTML
CSS
JavaScript

        │

        ▼

API Django Ninja

        │

        ▼

Casos de Uso

        │

        ▼

Entidades

        │

        ▼

Repositórios

        │

        ▼

MySQL
```

---

# 📌 Organização do Projeto

```
src/

users/
clientes/
barbeiros/
servicos/
agendamentos/
atendimentos/
pagamentos/
relatorios/

shared/

core/
```

---

# 📅 Roadmap

- [ ] Sistema de autenticação
- [ ] Cadastro de clientes
- [ ] Cadastro de barbeiros
- [ ] Cadastro de serviços
- [ ] Agendamento de horários
- [ ] Controle de atendimentos
- [ ] Registro de pagamentos
- [ ] Dashboard administrativo
- [ ] Relatórios financeiros
- [ ] Histórico de atendimentos
- [ ] Sistema de permissões
- [ ] Deploy da aplicação

---

# 📖 Licença

Projeto desenvolvido para fins de estudo, prática de arquitetura de software e composição de portfólio.