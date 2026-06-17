# WhatsApp Bot Supabase

Um bot automatizado em Python que busca contatos armazenados em um banco de dados **Supabase** e realiza disparos de mensagens via WhatsApp utilizando a **Z-API**.

## 🏗️ Arquitetura e Tecnologias

- **Python**: Linguagem principal do projeto.
- **Supabase**: Backend-as-a-Service (PostgreSQL) utilizado para armazenar e consultar a tabela de `contatos`.
- **Z-API**: API de integração responsável por disparar as mensagens no WhatsApp.
- **python-dotenv**: Gerenciamento de variáveis de ambiente de forma segura.

## 🚀 Como Rodar o Projeto

### 1. Pré-requisitos
- Python 3.10+ instalado.
- Conta e projeto configurados no Supabase (com uma tabela chamada `contatos` que tenha pelo menos as colunas `id`, `nome`, e `telefone`).
- Instância ativa na Z-API.


### 🛠️ Pré-requisitos (2): Estrutura do Banco (Supabase)
Antes de ir para o código, no editor SQL do seu projeto no Supabase, crie uma tabela de contatos.

```sql
CREATE TABLE contatos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) NOT NULL, -- formato ex: 5511999999999
    processado BOOLEAN DEFAULT FALSE -- para controle futuro de quem já recebeu
);

-- Insira dados de teste
INSERT INTO contatos (nome, telefone) VALUES 
('João', '5511911111111'),
('Maria', '5511922222222'),
('Pedro', '5511933333333');
```

### 2. Instalação
Clone o repositório e instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Configuração do Ambiente
Crie ou edite um arquivo `.env` na raiz do projeto contendo as seguintes variáveis:
```env
# SUPABASE CONFIG
SUPABASE_URL="sua_url_supabase"
SUPABASE_KEY="sua_chave_service_role" # Recomendado usar a service_role para evitar bloqueios por RLS

# Z-API CONFIG
ZAPI_INSTANCE_ID="seu_instance_id"
ZAPI_INSTANCE_TOKEN="seu_instance_token"
ZAPI_CLIENT_TOKEN="seu_client_token"

# MENSAGEM
MENSAGEM_TEMPLATE="Olá, <nome_contato>! Esta é uma mensagem de teste do nosso sistema usando Python e Z-API."
```

### 4. Execução
Execute o script principal a partir do diretório do projeto:
```bash
python src/main.py
```

## ✨ Boas Práticas Aplicadas

- **Modularização (Separation of Concerns):** O código é dividido em módulos claros (`config.py`, `database.py`, `whatsapp.py`), garantindo que cada arquivo tenha apenas uma responsabilidade (ex: conexão com banco separada da lógica de envio).
- **Tratamento de Exceções Seguro:** Captura e lida com falhas em requisições de rede ou banco de dados de maneira controlada, evitando que falhas quebrem o software inesperadamente.
- **Logging Customizado:** Uso da biblioteca `logging` do Python (`logger.py`) em vez de simples `print()`s. Permite monitorar eventos com níveis variados (INFO, WARNING, ERROR).
- **Segurança e `.env`:** Variáveis sensíveis e credenciais nunca ficam no código. Todas as chaves secretas são injetadas pelo arquivo `.env`.
- **Fail-Fast na Configuração:** O sistema valida logo na inicialização (`validar_configuracoes`) se todas as variáveis obrigatórias estão presentes, prevenindo erros ao decorrer da execução do código.
