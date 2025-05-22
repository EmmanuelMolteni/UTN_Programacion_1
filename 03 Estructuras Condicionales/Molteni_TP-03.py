from statistics import mode, median, mean
import random

def main():
    def mayorEdad():
        userInput = input("Ingrese su edad: ")
        edad = int(userInput)
        if not edad > 18:
            print("Es menor de edad")
        else:
            print("Es mayor de edad")
            
    def notaMayorMenor():
        userInput = input("Ingrese su nota")
        nota = int(userInput)
        if nota >= 6:
            print("Aprobado")
        else:
            print("Desaprobado")
            
    def ingreseNumeroPar():
        numero = int(input("Ingrese un numero par: "))
        while numero % 2 != 0:
            print("No es un numero par")
            numero = int(input("Ingrese un numero par: "))
        if numero % 2 == 0:
            print("Correcto, el numero es par.")
            
    def ingreseUsuarioyEdad():
        edad = int(input("Ingrese su edad"))
        if edad < 12:
            print("Es un niño")
        elif edad >= 12 and edad < 18:
            print("Es un adolescente")
        elif edad >= 18 and edad < 30:
            print("Es un adulto joven")
        else:
            print("Es un adulto")
            
    def tamanioContrasena():
        password = str(input("Ingrese contrasena entre 8 y 14 caracteres"))
        if len(password) >= 8 and len(password) <= 14:
            print("contrasena correcta")
        else:
            print("contrasena demasiado larga")
            
    def mediaMedianaModa():
        listaAleatoria = [3,2,1]
        # listaAleatoria = [random.randint(1, 100) for i in range(50)]
        if mean(listaAleatoria) > median(listaAleatoria) and median(listaAleatoria) > mode(listaAleatoria):
            print("Sesgo positivo o a la derecha")
        elif mean(listaAleatoria) < median(listaAleatoria) and median(listaAleatoria) < mode(listaAleatoria):
            print("Sesgo negativo o a la izquierda")
        elif mean(listaAleatoria) == median(listaAleatoria) and mean(listaAleatoria) == mode(listaAleatoria):
            print("Sin sesgo")
        else:
            print("Caso no contemplado")
    
    def tieneVocal():
        texto = str(input("Ingrese una palabra o frase: "))
        vocales = ["a","e","i","o","u"]
        if texto[len(texto)-1] in vocales:
            textoCompleto = texto + "!"
            print(textoCompleto)
        else:
            print(texto)

    def transformarNombre():
        nombre = input("Ingrese su nombre: ")
        print(
            "1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO\n"
            "2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n"
            "3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.\n"
            )
        opcion = int(input("Ingrese la opcion que desea:"))
        
        if opcion == 1:
            nombreModificado = nombre.upper()
            print(nombreModificado)
        elif opcion == 2:
            nombreModificado = nombre.lower()
            print(nombreModificado)
        elif opcion == 3:
            nombreModificado = nombre.title()
            print(nombreModificado)
        else:
            print("Ingrese una opcion valida")
    
    def terremotoMami():
        magnitudTerremoto = int(input("Ingrese la magnitud del terremoto: "))
        if magnitudTerremoto < 3:
            print("Muy Leve")
        elif magnitudTerremoto == 3:
            print("Leve")
        elif magnitudTerremoto == 4:
            print("Moderado")
        elif magnitudTerremoto == 5:
            print("Fuerte")
        elif magnitudTerremoto == 6:
            print("Muy Fuerte")
        elif magnitudTerremoto >= 7:
            print("Extremo")
    
if __name__ == "__main__":
    main()