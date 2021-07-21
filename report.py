#import needed modules
import requests, time, json, sys
from datetime import date

#loads variables from json files
try:
    variaveis = json.load(open('variables.json', 'r'))
    chaves = json.load(open('keys.json', 'r', encoding='utf8'))
except Exception as e:
    with open('variables.json', 'w') as write_file:
        variaveis['report'] = 'An error ocourred'
        json.dump(variaveis, write_file)
        sys.exit()

#request to API

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Sec-GPC': '1',
    'Origin': variaveis["url"],
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': f'{variaveis["url"]}/?Portal',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}

data = {
  'Dados': '{"Pesquisa":"","Ativo":"EmAberto","Ordem":[],"DataCriacao":"","DataInicioCriacao":"","DataFimCriacao":"","DataFinalizacao":"","DataInicioFinalizacao":"","DataFimFinalizacao":"","DataExpira":"","DataInicioExpira":"","HoraInicioExpira":"","DataFimExpira":"","HoraFimExpira":""}',
  'App': 'Portal',
  'Mobile': 'false'
}

page = requests.post(f'{variaveis["url"]}/Chamados/lista', headers=headers, cookies=chaves['cookies'], data=data)

#json from API response
lista = page.json()

#creates time and date objects
hoje = date.today()
t = time.localtime()
hora = time.strftime("%H:%M", t)

#converts number to name of months
def mes(arg):
	if arg == 1:
		return "janeiro"
	if arg == 2:
		return "fevereiro"
	if arg == 3:
		return "março"
	if arg == 4:
		return "abril"
	if arg == 5:
		return "maio"
	if arg == 6:
		return "junho"
	if arg == 7:
		return "julho"
	if arg == 8:
		return "agosto"
	if arg == 9:
		return "setembro"
	if arg == 10:
		return "outubro"
	if arg == 11:
		return "novembro"
	if arg == 12:
		return "dezembro"

#return an emoji for the SLA of the ticket
def sla(arg):
	if arg:
		return chaves['sla_in']
	else:
		return chaves['sla_out']

#create the ticket string
progress = ''
for item in lista['root']:
	with open('list.txt', 'r') as pmodel:
		pmodel = pmodel.read()
		pmodel = pmodel.replace('{status}', chaves[item['St']])
		pmodel = pmodel.replace('{ticket_protocol}', str(item['Codigo']))
		pmodel = pmodel.replace('{ticket_title}', item['Assunto'])
		pmodel = pmodel.replace('{ticket_sol}', item['Solicitante'])
		if 'Operador' in item:
			pmodel = pmodel.replace('{ticket_user}', item['Operador'])
		else:
			pmodel = pmodel.replace('{ticket_user}', 'Sem Atendente')
		progress += pmodel + '\n'

#creates the message string
mensagem = open('model.txt', 'r', encoding='utf8').read()
mensagem = mensagem.replace('{day}', str(hoje.day).zfill(2))
mensagem = mensagem.replace('{month_name}', mes(hoje.month))
mensagem = mensagem.replace('{time}', str(hora))
mensagem = mensagem.replace('{ticket_list}', progress)
mensagem = mensagem.replace('{total_tickets}', str(lista['total']))

#dumps the message into the variables json
variaveis['report'] = mensagem
with open('variables.json', 'w', encoding='utf8') as write_file:
    json.dump(variaveis, write_file)
