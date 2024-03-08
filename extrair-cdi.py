import os
import json
from datetime import datetime
from random import random

import requests

URL = 'https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx'

data_e_hora = datetime.now()
data = datetime.strftime(data_e_hora, '%Y/%m/%d')
hora = datetime.strftime(data_e_hora, '%H:%M:%S')

try:
  response = requests.get(URL)
  response.raise_for_status()
except requests.HTTPError as exc:
  print("Dado não encontrado, continuando.")
  cdi = None
except Exception as exc:
  print("Erro, parando a execução.")
  raise exc
else:
  dado = json.loads(response.text)
  cdi = float(dado['taxa'].replace(',', '.')) + (random() - 0.5)

if os.path.exists('./taxa-cdi.csv') == False:

  with open(file='./taxa-cdi.csv', mode='w', encoding='utf8') as fp:
    fp.write('data,hora,taxa\n')

with open(file='./taxa-cdi.csv', mode='a', encoding='utf8') as fp:
  fp.write(f'{data},{hora},{cdi}\n')

print("Sucesso")