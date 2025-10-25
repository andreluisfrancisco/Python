"""
Este módulo é responsável por realizar varreduras de segurança em aplicações
"""

import time
from zapv2 import ZAPv2

proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

zap = ZAPv2(apikey='api_key', proxies=proxies)

TARGET = 'http://google.com'

print(f"Iniciando spider em {TARGET}")
zap.spider.scan(TARGET)
time.sleep(1)

while int(zap.spider.status()) < 100:
    print(f"Spider em andamento: {zap.spider.status()}%")
    time.sleep(2)

print("Spider completo. Iniciando varredura ativa.")

zap.ascan.scan(TARGET)

while int(zap.ascan.status()) < 100:
    print(f"Varredura em andamento: {zap.ascan.status()}%")
    time.sleep(5)

print("Varredura completa. Obtendo resultados.")

alerts = zap.core.alerts(baseurl=TARGET)

for alert in alerts:
    print(f"Alerta: {alert['alert']}")
    print(f"Descrição: {alert['description']}")
    print(f"Gravidade: {alert['risk']}")
    print(f"Recomendação: {alert['solution']}\n")
