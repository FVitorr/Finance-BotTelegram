import telebot
import finance as f 
import os

#Chave da Api
KEY_API = ""
bot = telebot.TeleBot(KEY_API) #Iniciar bot

print("Bot Active")

log = f.log()
fin = f.finance()
com = f.comandLine()

@bot.message_handler(commands=["help"])
def set(mensagem):
    msg = '''❓ Comando /ext- Usado para operaçoes de RETIRADA (-) for Efetuado\n
    🔑/ext -s VALOR(Ex: 10.00) -d DESCRIÇÃO\n
❓ Comando /set- Usado para operaçoes de DEPOSITO (+) for Efetuado\n
    🔑/set -s VALOR(Ex: 10.00) -d DESCRIÇÃO\n
❓Comando /rel- Usado para exportar dados/Informação\n
    🔑/rel \t - Retorna Saldo em conta\n
    🔑/rel -c \t - Retorna Documento (.xlsx) com todas as movimentaçoes registradas\n
'''
    bot.reply_to(mensagem,msg)

@bot.message_handler(commands=["ext"])
def ext(mensagem):
    #sent = com.sep(mensagem.text[mensagem.text.index("ext") + 3:])
    #text_ = log.object(float(ent[0]) * -1,ent[1])
    try:
        ent = com.sep(mensagem.text[mensagem.text.index("ext") + 3:])
        text_ = log.object(float(ent[0]) * -1,ent[1])
        #Salvar entrada no log
        log.writeLog(str(text_) + '\n')
        bot.reply_to(mensagem," Sucesso :)")
    except:
        bot.reply_to(mensagem," Entrada Invalida :(")

@bot.message_handler(commands=["set"])
def set(mensagem):
    try:
        ent = com.sep(mensagem.text[mensagem.text.index("set") + 3:])
        text_ = log.object(ent[0],ent[1])
        #Salvar entrada no log
        log.writeLog(str(text_) + '\n')
        bot.reply_to(mensagem," Sucesso :)")
    except:
        bot.reply_to(mensagem," Entrada Invalida :(")

@bot.message_handler(commands=["cof"])
def cof(mensagem):
    #sent = com.sep(mensagem.text[mensagem.text.index("ext") + 3:])
    #text_ = log.object(float(ent[0]) * -1,ent[1])
    print(mensagem.text[mensagem.text.index("cof") + 3:])
    try:
        entry = mensagem.text[mensagem.text.index("cof") + 3:]
        entry += '-d VarSystem'
        ent = com.sep(entry)
        print(ent)
        text_ = log.object(float(ent[0]) * -1,ent[1])
        #Salvar entrada no log
        log.writeLog(str(text_) + '\n')
        bot.reply_to(mensagem," Sucesso :)")
    except:
        bot.reply_to(mensagem," Entrada Invalida :(")


@bot.message_handler(commands=["rel"])
def rel(mensagem):
    if ("-c" in mensagem.text):
        #bot.send_document(mensagem.chat.id,document="C:\Wordspace\Python/18 - PROJETOS\FinanceBot/rel2022-08021.xlsx")
        try:
            msg = log.document()
            print(msg)
            with open("C:\Wordspace\Python/18 - PROJETOS\FinanceBot/" + msg, "rb") as file:
                bot.send_document(mensagem.chat.id, document=file)
            #Deletar file
            os.remove("C:\Wordspace\Python/18 - PROJETOS\FinanceBot/" + msg)
        except:
            pass
    else:
        try:
            date = log.readLog()
            date = "\nSaldo Conta:\n\tR$ %.2f " % (fin.sum(date))
            bot.reply_to(mensagem,str(date))
        except:
            pass

def verificar(mensagem):
    print(mensagem.chat.id)
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """ -- Finance Bot Start --
    /help\t-\t Como usar
    /ext \t-\t Dinheiro Retirado
    /set \t-\t Dinheiro Ganho
    /rel\t-\tRelatorio"""
    bot.reply_to(mensagem, texto)# marca a mensagem e envia


bot.polling() #loop Infinito do bot
