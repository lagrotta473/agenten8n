# Arquitetura do Agente Open Cloud

## Descrição Geral
Forneça uma visão geral sobre o que o agente Open Cloud faz e como ele se integra ao n8n.

## Diagrama de Arquitetura
Adicione aqui qualquer diagrama visual ou descrição passo a passo da arquitetura.

## Contrato com o Webhook do n8n
Detalhe o contrato da API que o agente deve seguir para se comunicar eficientemente com o n8n.

- **Método HTTP:** POST
- **Endpoint:** URL do webhook do n8n
- **Cabeçalhos Requeridos:**
  - Content-Type: application/json
- **Autenticação:** Bearer Token via cabeçalho `Authorization` (quando `OPEN_CLOUD_API_KEY` fornecida)

## Payload do Agente
Descreva o formato do payload que o agente envia ao n8n.

```json
{
  "field1": "value1",
  "field2": "value2"
}
```

## Respostas Esperadas do Webhook
- **200 OK:** Descrição do caso de sucesso
- **500 Internal Server Error:** Quando ocorre um erro no webhook
- **Timeout:** Detalhes sobre comportamento em casos de timeout

## Variáveis de Ambiente

### 7. Configuração Obrigatória

Abaixo estão as variáveis de ambiente necessárias para o funcionamento correto do agente:

| Variável | Descrição | Obrigatória | Exemplo |
|----------|-----------|-------------|---------|
| `N8N_WEBHOOK_URL` | URL do webhook do n8n | Sim | `https://n8n.exemplo.com/webhook/xyz` |
| `OPEN_CLOUD_API_KEY` | Chave de API para autenticação Bearer | **Sim** | `sk-abc123def456` |

> ⚠️ **Importante:** A `OPEN_CLOUD_API_KEY` é obrigatória. Sem ela, o agente não conseguirá se autenticar nos endpoints protegidos do n8n. Configure-a no arquivo `.env` antes de executar o projeto.

## Docker

O projeto já conta com os arquivos Docker configurados. Abaixo estão as instruções para build e execução.

### Arquivos Disponíveis

| Arquivo | Descrição |
|---------|-----------|
| `Dockerfile` | Imagem base `python:3.11-slim` com instalação das dependências |
| `.dockerignore` | Exclusões para otimizar o build |
| `docker-compose.yml` | Orquestração opcional do container |

### Build da Imagem

```bash
docker build -t agente-open-cloud:latest .
```

### Executando o Container

#### Usando arquivo .env

```bash
docker run --rm --env-file .env agente-open-cloud:latest
```

#### Passando variáveis diretamente

```bash
docker run --rm \
  -e N8N_WEBHOOK_URL="https://n8n.exemplo.com/webhook/xyz" \
  -e OPEN_CLOUD_API_KEY="sk-abc123def456" \
  agente-open-cloud:latest
```

### Docker Compose

```bash
docker-compose up --build
```

Para executar em background:

```bash
docker-compose up -d --build
```

Preencha cada seção com detalhes específicos do seu serviço e operação.
