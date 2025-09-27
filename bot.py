from twilio.rest import Client
import schedule
import time
import random

# Suas credenciais do Twilio
account_sid = "ACcfd228973d40c7c60001c6dd1c64fca0"
auth_token = "0e10c6f35ef44249b3f4e54ac6f3f1a6"
client = Client(account_sid, auth_token)

# Lista de mensagens motivacionais
mensagens = [
    "📚 Bora estudar agora! 🚀",
    "💡 Lembre-se: conhecimento é poder!",
    "🔥 Foco nos estudos, você consegue!",
    "⏰ Hora de aprender algo novo!"
]

# Função que envia mensagem no WhatsApp
def enviar_lembrete():
    mensagem_escolhida = random.choice(mensagens)  # escolhe uma mensagem aleatória
    mensagem = client.messages.create(
        from_="whatsapp:+14155238886",    # Número do sandbox do Twilio
        to="whatsapp:+5515997165768",     # Seu número com DDI
        body=mensagem_escolhida            # usa a mensagem escolhida
    )
    print("Mensagem enviada:", mensagem.sid)

# --- AGENDAMENTO DOS HORÁRIOS ---
# Horários que se repetem todo dia
horarios_diarios = ["19:55", "21:00"]

# Horários específicos por dia da semana
horarios_semana = {
    "monday": ["18:00", "20:00"],
    "wednesday": ["20:00"],
    "friday": ["20:00", "22:30"]
}

# Agenda diária
for hora in horarios_diarios:
    schedule.every().day.at(hora).do(enviar_lembrete)

# Agenda por dia da semana
for dia, horas in horarios_semana.items():
    for hora in horas:
        getattr(schedule.every(), dia).at(hora).do(enviar_lembrete)

print("🤖 Bot iniciado! Aguardando horários...")

# ------------------- Loop infinito para rodar os agendamentos -------------------
while True:
    schedule.run_pending()
    time.sleep(1)

