#  Sistema de Gestão de Chamados (Help Desk)

Este projeto é um sistema de Help Desk desenvolvido para gerenciar chamados de suporte técnico, integrando **Python** e **PostgreSQL**. O foco principal foi aplicar conceitos de modelagem de dados relacional e práticas de desenvolvimento seguro.

##  Tecnologias Utilizadas
- **Linguagem:** Python
- **Banco de Dados:** PostgreSQL
- **Biblioteca de Conexão:** Psycopg2

##  Foco em Cibersegurança
Como entusiasta e estudante da área de Cibersegurança (participante dos programas **Hackers do Bem** e **Google Cybersecurity**), apliquei conceitos de defesa no desenvolvimento deste projeto:
- **Prevenção contra SQL Injection:** Todas as consultas ao banco de dados utilizam parâmetros seguros (`prepared statements`), impedindo a execução de códigos maliciosos via inputs de usuário.
- **Sanitização de Dados:** Tratamento de entradas para garantir a integridade do banco de dados.

##  Estrutura do Banco de Dados
O projeto utiliza uma estrutura relacional composta por:
- `usuarios`: Cadastro de colaboradores e seus setores.
- `chamados`: Registro detalhado dos incidentes, status e relacionamento com o usuário solicitante (Foreign Keys).

> *O script para criação das tabelas está disponível no arquivo `schema.sql`.*

## Funcionalidades
- Abrir chamados
- Listar chamados abertos
- Fechar chamados
- Registro de usuários
- Integração com PostgreSQL
  
##  Como Executar o Projeto
1. **Prepare o Banco de Dados:**
   - Crie um banco de dados chamado `helpdesk` no seu PostgreSQL.
   - Execute o script contido em `schema.sql`.

2. **Configure o Ambiente:**
   - Instale a dependência necessária: `pip install psycopg2-binary`.
   - No arquivo `database.py`, ajuste as credenciais em `DB_CONFIG` com seu usuário e senha local.

3. **Inicie a Aplicação:**
   - Execute o comando: `python app.py`.

---
Desenvolvido por **Arthur Barros de Queiroz - Graduando em Ciência da Computação** Goiânia, GO
