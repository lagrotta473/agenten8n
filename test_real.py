import config
from agent_integration import AgentOpenCloud

def main():
    print(f"URL do webhook: {config.N8N_WEBHOOK_URL}")
    print(f"API Key configurada: {'Sim' if config.OPEN_CLOUD_API_KEY else 'Não'}")

    agent = AgentOpenCloud(
        config.N8N_WEBHOOK_URL,
        api_key=config.OPEN_CLOUD_API_KEY
    )

    payload = {'field1': 'value1', 'field2': 'value2'}
    print(f"Enviando payload: {payload}")

    status_code, response = agent.send_payload(payload)

    print(f"Status code: {status_code}")
    print(f"Response: {response}")

if __name__ == '__main__':
    main()
