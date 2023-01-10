from time import sleep

class aplication():
    def __init__(self, nombre, peso, altura):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
    
    
    def dieta(self):
        #funcion incompleta falta que sume todo los alimentos que coloque el usuario
        alimento = input("cual es el producto")
        proteinas = input("cuantas proteinas tiene ?")
        grasas = input("cuantas grasas tiene?")
        cabohidratos = input("cuantos carbohidratos tiene?")
        listaAlimentos = {alimento: {
            "proteinas": proteinas,
            "grasas": grasas,
            "cabohidratos": cabohidratos
            
        }
        }
        return listaAlimentos

    def actividad(self):
        print("ok para seguir calculando tu deficit calorico o aumentar masa muscular")
        sleep(0.5)
        print("necesito saber cual es tu nivel de actividad")
        global nivelActividad
        sleep(0.5)
        nivelActividad = float(input("""
sedentario 1.3/1.6 1 a 2 dias de entreno
algo activo 1.6/1.8 2 a 4 dias de entreno 
acivo 1.8/2.0 1 a 5 dias de entreno
muy activo 2.0/2.2 todos los dias
"""))
        return ""

    def deficitCalorico(self):
        print('ok tu peso es: ',self.peso)
        sleep(0.5)
        print('es bueno saberlo')
        sleep(0.5)
        normal = int(self.peso) * 22
        print(f'la calorias que consumes nada por existir es: {normal} ')
        sleep(0.5)
        self.actividad()
        if nivelActividad == 1.3:
            print("bueno algun dia tienes que mejorar vale. ok ya sabemos tu nivel pues...")
            sleep(0.5)
            return(f"tus calorias diaria son: {float(normal) * nivelActividad}")
        elif nivelActividad == 1.4:
            print("tienes que mejorar mas ")
            sleep(0.5)
            return(f"tus calorias diaria son: {float(normal) * nivelActividad}")
        elif nivelActividad == 1.5:
            print("ok estas mas o menos pero aun tienes que mejorar")
            sleep(0.5)
            return(f"tus calorias diaria son: {float(normal) * nivelActividad}")
        elif nivelActividad == 1.6:
            print('ok esta bien ')
            sleep(0.5)
            return(f"tus calorias diaria son: {float(normal) * nivelActividad}")
        elif nivelActividad == 1.7:
            print('ok ahora estamos hablando ')
            sleep(0.5)
            return(f"tus calorias diaria son: {float(normal) * nivelActividad}")
        elif nivelActividad == 1.8:
            print("ahora si este es el nivel que me gusta ")
            sleep(0.5)
            return(f"tus calorias diaria son: {float(normal) * nivelActividad}")
        elif nivelActividad == 1.9:
            print("ok ok ok eres UNA BESTIA")
            sleep(0.5)
            return(f"tus calorias diaria son: {float(normal) * nivelActividad}")
        elif nivelActividad == 2.0:
            print("ok ya hay que pararle pero estas excelente")
            sleep(0.5)
            return(f"tus calorias diaria son: {float(normal) * nivelActividad}")
        elif nivelActividad == 2.1:
            print('wow eres lo maximo')
            sleep(0.5)
            return(f"tus calorias diaria son: {float(normal) * nivelActividad}")
        elif nivelActividad == 2.2:
            print("no sabia que tenemos a la roca con nosotros")
            sleep(0.5)
            return(f"ok bestia, tus calorias diaria son: {float(normal) * nivelActividad}")
        elif nivelActividad <= 1.2 > 0:
            print("no haces casi nada aunmenta el ritmo")
            sleep(0.5)
            print('esperaba mas de ti...')
            sleep(0.5)
            return(f"tus calorias diaria son: {float(normal) * nivelActividad}")
        elif nivelActividad <= 0:
            return "entonces no hacer nada ._."

nombre = input("cual es tu nombre ?")
peso = input("cual es tu peso ?")
altura = input("cual es tu altura ?")

persona1 = aplication(nombre, peso, altura)

print("ok", nombre)

sleep(1)

deficit = input("que quieres hacer un deficit calorico o aumentar masa muscular ? D/M")

if deficit == "D" or deficit == ' D':
    print('bien')
    sleep(0.5)
    print(persona1.deficitCalorico())
elif deficit == 'M' or deficit == ' M':
    pass