import math 

def calcular_area_circulo(raio):
    return math.pi * raio ** 2

def calcular_area_quadrado(lado, area):
    return lado * 2

def calcular_area_triangulo(base, altura):
    return (base * altura ) / 2

raio = float(input("Digite o raio do circulo:"))
lado = float(input("Digite o lado do quadrado:"))
area = float(input("Digite o area do quadrado:"))
base = float(input("Digite a base do triangulo:"))
altura = float(input("Digite a altura do triangulo:"))

area_circulo = calcular_area_circulo(raio)
area_quadrado= calcular_area_quadrado(lado, area)
area_triangulo = calcular_area_triangulo(base, altura)

print(f"Área do circulo:{ area_circulo:.2f}")
print(f"Área do quadrado:{ area_quadrado:.2f}")
print(f"Área do triangulo:{ area_triangulo:.2f}")