import os
from openai import OpenAI
from dotenv import load_dotenv

# Carrega as variaveis de ambiente do arquivo .env
load_dotenv()

# Configura o cliente OpenAI
# Certifique-se de ter a chave OPENAI_API_KEY no seu arquivo .env
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Definicao do System Prompt para o ChargeGrid Intelligence
SYSTEM_PROMPT = (
    "Voce e o ChargeGrid Intelligence, um assistente especializado em recarga de veiculos eletricos. "
    "Sua missao e ajudar usuarios com duvidas sobre cobrança, velocidade de recarga, "
    "compatibilidade de conectores e suporte a problemas tecnicos. "
    "Use uma linguagem simples, evitando jargoes tecnicos desnecessarios. "
    "Seu tom deve ser sempre acolhedor, direto e confiavel."
)

# Inicializa o historico de mensagens
historico = [{"role": "system", "content": SYSTEM_PROMPT}]

def enviar_mensagem(mensagem_usuario):
    """Envia a mensagem do usuario para a API e retorna a resposta."""
    historico.append({"role": "user", "content": mensagem_usuario})
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=historico
        )
        resposta_ia = response.choices[0].message.content
        historico.append({"role": "assistant", "content": resposta_ia})
        return resposta_ia
    except Exception as e:
        return f"Desculpe, ocorreu um erro ao processar sua solicitacao: {e}"

def main():
    print("--- ChargeGrid Intelligence: Assistente de Recarga de VE ---")
    print("Digite 'sair' ou 'exit' para encerrar o chat.\n")
    
    while True:
        user_input = input("Voce: ")
        
        if user_input.lower() in ['sair', 'exit']:
            print("ChargeGrid: Ate logo! Tenha uma excelente recarga.")
            break
            
        if not user_input.strip():
            continue
            
        resposta = enviar_mensagem(user_input)
        print(f"ChargeGrid: {resposta}\n")

if __name__ == "__main__":
    main()
