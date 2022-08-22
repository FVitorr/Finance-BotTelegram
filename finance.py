
import datetime
import ast 
import pandas as pd
#Desenvolver um bot de controle de fianceiro

class log:
    def __init__(self) -> None:
        nameFile = "log.bin"
        try:
            arq = open(nameFile,"rb")
        except:
            arq = open(nameFile,"wb")
            
        self.bd = nameFile
    
    def object(self, valor, des = "Sem Descrição"):
        dateInfo = datetime.datetime.today()
        obj = {}
        obj["Date"] = str(dateInfo.strftime("%d-%m-%Y %H:%M"))
        obj["Valor"] = float(valor)
        obj["Desc"] = des
        return (obj)
    
    def writeLog(self, text):
        res = str(text).encode("utf-8")
        with open(self.bd,"ab") as arq:
            arq.write(res)
        return (1)

    def readLog(self):
        with open(self.bd,'rb') as arq:
            liner = arq.readlines()
        lines = []
        for i in liner:
            try:
                file = ast.literal_eval(i.decode("utf-8"))
                lines.append(file)
            except:
                pass
        return lines
    def document(self,date = None, format = '.xlsx'):
        nameFile = "rel" + str(datetime.date.today()) + format

        d ={}
        if (date == None):
        #Criar dicionario de dados
            file = self.readLog()
            dat = [i["Date"] for i in file]
            val = [i["Valor"] for i in file]
            des = [i["Desc"] for i in file]

            d["Data"] = dat
            d["Valor"] = val
            d["Descrição"] = des

        dados = pd.DataFrame(data=d)
        if format == ".xlsx":
            dados.to_excel(nameFile, index = False)
        if format == ".html":
            dados.to_html(nameFile)
        return nameFile

class finance:
    def __init__(self) -> None:
        pass
    def sum(self,dictDate):
        sum_ = 0
        for i in dictDate:
            sum_ += i["Valor"]
        return sum_

class comandLine:
    def __init__(self) -> None:
        pass
    def sep(self,entry):
        entry = entry.replace(" ",'')
        res = []
        if '-s' in entry:
            try: sald = entry[entry.index("-s")+ 2: entry.index("-d")]
            except: sald = entry[entry.index("-s")+ 2:]

            res.append(sald)
        if '-d' in entry:
            try: 
                if entry.index("-d") < entry.index("-s"):
                    desc = entry[entry.index("-d")+ 2: entry.index("-s")]
                else:
                    desc = entry[entry.index("-d")+ 2:]
            except: 
                desc = "Sem Descrição"
            if len(desc) == 0:
                desc = "Sem Descrição"
            res.append(desc)
        else:
            res.append("Sem Descrição")
        return res


''' 
text_ = log_.object(177.61,"Saldo Inter")
log_.writeLog(str(text_) + '\n')
'''
if __name__ == "__main__":
    log_ = log()
    cont = log_.readLog()
    log_.document()

''' f = finance()
    c = comandLine()
    info = c.sep("-s -89.0 -d")
    text_ = log_.object(info[0],info[1])
    log_.writeLog(str(text_) + '\n')
    print(f.sum(cont))
    print(cont[0]["Date"])'''
    