def predictor_base_conocimiento(sexo, edad, nivel_estudios):
    """
    Predictor basado en conocimiento para el consumo de alcohol.
    Devuelve una probabilidad entre 0 y 1, junto con una explicación.
    :param sexo: str, "Hombre" o "Mujer"
    :param edad: str, Rango de edad ("De 15 a 24 años", "De 25 a 44 años", "45 años o más")
    :param nivel_estudios: str, "Básico e inferior", "Medio", "Superior"
    :return: tuple (float, str), Probabilidad de consumo de alcohol y explicación
    """
    
    # Probabilidad base
    probabilidad = 0.5  # Punto medio por defecto
    explicacion = "La predicción se basa en reglas de conocimiento sobre edad, sexo y nivel de estudios."
    
    # Reglas basadas en patrones observados
    if edad == "De 15 a 24 años" and nivel_estudios == "Básico e inferior":
        probabilidad = 0.85
        explicacion += " Personas jóvenes con menor nivel educativo tienen mayor probabilidad de consumo."
    elif edad == "De 25 a 44 años" and nivel_estudios in ["Medio", "Superior"]:
        probabilidad = 0.6
        explicacion += " Adultos con educación media o superior tienen un consumo moderado."
    elif edad == "45 años o más":
        probabilidad = 0.3
        explicacion += " Personas mayores tienen menor probabilidad de consumo."
    
    # Ajuste basado en el sexo
    if sexo == "Hombre":
        probabilidad += 0.05  # Incremento ligero
        explicacion += " Los hombres suelen tener una probabilidad ligeramente mayor de consumo."
    elif sexo == "Mujer":
        probabilidad -= 0.05  # Reducción ligera
        explicacion += " Las mujeres suelen tener una probabilidad ligeramente menor de consumo."
    
    # Asegurar que la probabilidad está entre 0 y 1
    probabilidad = max(0, min(1, probabilidad))
    
    return probabilidad, explicacion


def interactuar_con_predictor():
    print("Bienvenido al predictor basado en conocimiento. Responde las siguientes preguntas.")
    sexo = input("Sexo (Hombre/Mujer): ")
    edad = input("Edad (De 15 a 24 años / De 25 a 44 años / 45 años o más): ")
    nivel_estudios = input("Nivel de estudios (Básico e inferior / Medio / Superior): ")
    
    probabilidad, explicacion = predictor_base_conocimiento(sexo, edad, nivel_estudios)
    print(f"\nProbabilidad de consumo de alcohol: {probabilidad:.2f}")
    print(f"Explicación: {explicacion}")


# Ejecutar interacción con el usuario
if __name__ == "__main__":
    interactuar_con_predictor()
