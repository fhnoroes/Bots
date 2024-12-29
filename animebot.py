import telebot
import requests

chaveapi = "7964164900:AAEhvlMHT8ZCb1EP6bU93LcZIH4-vmhS__g"

url = "https://api.jikan.moe/v4/seasons/now"

bot = telebot.TeleBot(chaveapi)

@bot.message_handler(commands=["criador"])
def sobre(mensagem):
    bot.reply_to(mensagem,"Esse bot foi criado por Fhelype Norões para fins meramente de estudo. Caso precise contatá-lo envie um email para fhelypenoroes@gmail.com")

@bot.message_handler(commands=["atual"])
def listar(mensagem):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        listaanime = ""
        # Exibindo os animes da temporada
        for anime in dados['data']:
            listaanime += f"Título: {anime['title']}, Episódios: {anime['episodes']}\n"
        bot.reply_to(mensagem,listaanime)
    else:
        bot.reply_to(mensagem,f"Erro ao acessar a API: {resposta.status_code}")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def resposta(mensagem):
    bot.reply_to(mensagem,"Bem Vindo ao bot de animes em exibição.\nClique em /atual para que ele liste.\nClique em /criador para saber sobre quem desenvolveu.\nQualquer outra mensagem será desconsiderada.")
# Verificando o status da resposta

bot.polling()