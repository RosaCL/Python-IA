import numpy as np

class MonitorarTemperatura:
    def __init__(self):
        # lista para armazenar as leituras de temperatura
        self.leituraTemperatura = []

    def adcionarTemperaturas(self, valor):
        self.leituraTemperatura.append(valor)
        print(f"Nova temperatura registrada:{valor} ºC")

    def calcular_estaticas(self):
        dados = np.array(self.leituraTemperatura)
        estatistica = {
            "maximo": dados.max(),
            "minima": dados.min(),
            "media": dados.mean()
        }
        return estatistica
    def verificar_segurança(self):
        fora_do_limite = False
        for temp in self.leituraTemperatura:
            if temp  < 20 or temp > 80:
                print(f"Alerta!!! Temperatura fora do limite seguro:{temp} ºC ")
                fora_do_limite = True
        if not fora_do_limite:
            print("Todas as temperaturas estão dentro do limite seguro.")


monitor = MonitorarTemperatura()
leituraTemperatura = [25,30,90,45,78]
for temp in leituraTemperatura:
    monitor.adcionarTemperaturas(temp)
estatisticas = monitor.calcular_estaticas()
print(f"Estatiticas das temperaturas registradas:")
print(f"Temperaturas máximas: {estatisticas['maximo']} ºC")
print(f"Temperaturas mínima: {estatisticas['minima']} ºC")
print(f"Temperaturas média: {estatisticas['media']} ºC")
monitor.verificar_segurança()