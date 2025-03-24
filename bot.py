import openai

# Configurar a chave da API do OpenAI
openai.api_key = "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"

# Contexto inicial do chatbot
contexto = """
Bem-vindo ao Chatbot de Pesquisa de Mercado!
Estou aqui para responder suas dúvidas sobre como participar da pesquisa.
Aqui estão algumas informações básicas:
1. Você precisará preencher um formulário inicial com suas informações de contato.
2. Após o cadastro, receberá um convite por e-mail com as instruções.
3. A pesquisa será feita online e levará cerca de 15 minutos.
4. Participantes podem receber incentivos, como vouchers ou prêmios.
Agora, pode fazer até 3 perguntas!
"""

# Função para gerar respostas usando o novo método ChatCompletion
def responder_pergunta(pergunta, contexto):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Modelo mais recente para chat
            messages=[
                {"role": "system", "content": contexto},
                {"role": "user", "content": pergunta},
            ],
            max_tokens=100,
            temperature=0.7
        )
        return response['choices'][0]['message']['content']  # Retorna a mensagem gerada
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"

# Função principal do chatbot
def chatbot():
    print(contexto)

    perguntas = []
    respostas = []

    for i in range(3):
        pergunta = input(f"Pergunta {i+1}: ")
        perguntas.append(pergunta)
        resposta = responder_pergunta(pergunta, contexto)
        respostas.append(resposta)
        print(f"Resposta: {resposta}")

    # Resumo da interação
    print("\nResumo da interação:")
    for i, (pergunta, resposta) in enumerate(zip(perguntas, respostas)):
        print(f"{i+1}. Pergunta: {pergunta}")
        print(f"   Resposta: {resposta}")

    print("\nObrigado por usar o Chatbot de Pesquisa de Mercado!")

# Executar o chatbot
if __name__ == "__main__":
    chatbot()
