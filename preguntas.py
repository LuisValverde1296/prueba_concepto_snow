import math

def start_menu():
    print("-------------------------------------------------------------------------------------------------")
    print("-------------------------------Bienvenidos al menú principal-------------------------------------")
    print("-------------------------------------------------------------------------------------------------\n\n")
    print("Por favor elija el número de pregunta que desea resolver entre las siguientes opciones: ")
    print("1. Calcular la paga neta de un trabajador")
    print("2. Cálculos matemáticos básicos")
    print("3. Calcular la velocidad en m/s en una carrera de 1500 metros")
    print("4. Calcular la superficie de un triángulo")
    print("5. Calculadora de salario semanal")
    print("6. Intercambiar valores de variables A y B")
    print("7. Calcular la distancia recorrida en metros por un automóvil")
    print("8. Obtener promedio de un estudiante a partir de 3 notas parciales")
    print("9. Calculadora de notas de acuerdo a las respuestas del estudiante")
    print("10. Calcular la cantidad de CDs necesarios para hacer un respaldo")
    print("11. Salir del programa")
    
def check_exit(value):
    value == exit

def check_number(value):
    response = False
    if not value.isnumeric():
        print("Este campo debe ser un valor numérico, intente de nuevo: ")
    elif float(value) < 0:
        print("Este campo debe ser un número positivo, intente de nuevo: ")
    else:
        response = True
    return response

def call_calculate_payment():
    print("Inserte el número de horas trabajadas: ")
    worked_hours = input()
    while not check_number(worked_hours):
        worked_hours = input()
    print("inserte la tarifa horaria: ")
    payment_per_hour = input()
    while not check_number(payment_per_hour):
        payment_per_hour = input()
    print("inserte la tasa de impuestos entre 0 y 1: ")
    tax = input()
    while float(tax) < 0 or float(tax)>1:
        print("la tasa de impuestos debe ser un número entre 0 y 1")
        tax = input()
    salary = float(worked_hours)*float(payment_per_hour)
    actual_payment = salary - salary*float(tax)
    print("su salario neto es de: ", actual_payment)
    print("presione enter para continuar al menú principal")
    input()

def ask_for_numbers():
    print("Primer número: ")
    a = input()
    while not check_number(a):
        a = input()
    print("Segundo número: ")
    b = input()
    while not check_number(b):
        b = input()
    return a,b

def math_calcs():
    while True:
        print("------------------------------Menú secundario: Calculos matemáticos-------------------------------------")
        print("Seleccione el número que desea: ")
        print("1. Sumar dos números enteros")
        print("2. Restar dos números enteros")
        print("3. Multiplicar dos números enteros")
        print("4. Dividir un número entero entre otro")
        print("5. Volver al menú principal")
        print("Su elección: ")
        user_input = input()
        if user_input == "1":
            a,b = ask_for_numbers()
            print("Resultado: ")
            print(int(a)+int(b))
            print("Presione enter para continuar")
            input()
        elif user_input == "2":
            a,b = ask_for_numbers()
            print("Resultado: ")
            print(int(a)-int(b))
            print("Presione enter para continuar")
            input()
        elif user_input == "3":
            a,b = ask_for_numbers()
            print("Resultado: ")
            print(int(a)*int(b))
            print("Presione enter para continuar")
            input()
        elif user_input == "4":
            a,b = ask_for_numbers()
            print("Resultado: ")
            print(int(a)/int(b))
            print("Presione enter para continuar")
            input()
        else:
            break;

def calc_speed():
    print("Por favor inserte los minutos que tardó el corredor sin contar los segundos: ")
    minutes = input()
    while not check_number(minutes):
        minutes = input()
    print("Por favor inserte los segundos: ")
    seconds = input()
    while not check_number(seconds):
        seconds = input()
    while(int(seconds) < 0 or int(seconds) >= 60):
        print("los segundos deben ser una cantidad entre 0 y 59, intento de nuevo")
        seconds = input()
    total_seconds = int(minutes)*60 + int(seconds)
    speed = 1500/total_seconds
    print("La velocidad del corredor en metros por segundo es: ", speed)
    print("Presione enter para continuar al menú principal: ")
    input()

def calc_triangule_surface():
    print("Por favor inserte la medida de la base del triángulo en centímetros: ")
    base = input()
    while not check_number(base):
        base = input()
    print("Por favor inserte la medida de la altura del triángulo en centímetros: ")
    height = input()
    while not check_number(height):
        height = input()
    surface = (1/2)*float(base)*float(height)
    print("La superficie del triángulo es de: ", surface, " cm")
    print("Presione enter para continuar al menú principal: ")
    input()

def calc_weekly_payment():
    print("Por favor inserte la tarifa horaria del trabajador: ")
    amount_per_hour = input()
    while not check_number(amount_per_hour):
        amount_per_hour = input()
    print("Por favor inserte las horas que trabaja diariamente el trabajador: ")
    hours_worked_per_day = input()
    while not check_number(hours_worked_per_day):
        hours_worked_per_day = input()
    first_payment_case = float(amount_per_hour) * (float(hours_worked_per_day)*5)
    second_payment_case = float(amount_per_hour) * (float(hours_worked_per_day)*6)
    print("En un horario de trabajo de 5 días por semana el trabajador gana: ", first_payment_case, " por semana")
    print("Y en un horario de trabajo de 6 días por semana el trabajador gana: ", second_payment_case, " por semana")
    print("Presione enter para continuar al menú principal: ")
    input()

def trade_values():
    a,b = ask_for_numbers()
    c = a
    a = b
    b = c
    print("A: ", a)
    print("B: ", b)
    print("Presione enter para continuar al menú principal: ")
    input()

def calc_distance_traveled():
    print("Por favor inserte la velocidad del automóvil en metros por segundo: ")
    speed = input()
    while not check_number(speed):
        speed = input()
    print("Por favor inserte el tiempo en segundos en que transitó el automóvil: ")
    time = input()
    while not check_number(time):
        time = input()
    distance = float(speed) * float(time)
    print("La distancia total viajada por el automóvil en: ", time, " a una velocidad constante de: ", speed , " metros por segundo es de: ", distance , " metros")
    print("Presione enter para continuar al menú principal: ")
    input()

def calc_media_of_student():
    print("Por favor inserte la primera nota: ")
    first_grade = input()
    while not check_number(first_grade):
        first_grade = input()
    print("Por favor inserte la segunda nota: ")
    second_grade = input()
    while not check_number(second_grade):
        second_grade = input()
    print("Por favor inserte la tercera nota: ")
    third_grade = input()
    while not check_number(third_grade):
        third_grade = input()
    media = (float(first_grade) + float(second_grade) + float(third_grade))/3.0
    print("El promedio del estudiante es de: ", media)
    print("Presione enter para continuar al menú principal: ")
    input()

def calc_student_grade():
    print("Por favor inserte la cantidad de respuestas correctas que tuvo el estudiante: ")
    correct_answers = input()
    while not check_number(correct_answers):
        correct_answers = input()
    print("Por favor inserte la cantidad de respuestas incorrectas que tuvo el estudiante: ")
    incorrect_answers = input()
    while not check_number(incorrect_answers):
        incorrect_answers = input()
    print("Por favor inserte la cantidad de preguntas que el estudiante dejó en blanco: ")
    blank_spaces = input()
    while not check_number(blank_spaces):
        blank_spaces = input()
    total_points = 4*(int(correct_answers)+int(incorrect_answers)+int(blank_spaces))
    obtained_points = 4*int(correct_answers) - int(incorrect_answers)
    grade = (float(obtained_points) * 100.0) / float(total_points) 
    print("La nota del estudiante es: ", grade)
    print("Presione enter para continuar al menú principal: ")
    input()

def calc_backup():
    print("Por favor inserte el tamaño del disco duro en GigaBytes: ")
    drive_size = input()
    while not check_number(drive_size):
        drive_size = input()
    total_size_megabytes = float(drive_size) * 1024
    total_CD_needed = total_size_megabytes/700.0
    print("El total de CDs necesitados para hacer un respaldo de un disco duro de ", drive_size, " gigabytes es: ", math.ceil(total_CD_needed))
    print("Presione enter para continuar al menú principal: ")
    input()

def main_loop():
    start_menu()
    print("Su elección: ")
    user_input = input()
    # print(eleccion_usuario)
    
    if user_input == "1":
        call_calculate_payment()
    elif user_input == "2":
        math_calcs()
    elif user_input == "3":
        calc_speed()
    elif user_input == "4":
        calc_triangule_surface()
    elif user_input == "5":
        calc_weekly_payment()
    elif user_input == "6":
        trade_values()
    elif user_input == "7":
        calc_distance_traveled()
    elif user_input == "8":
        calc_media_of_student()
    elif user_input == "9":
        calc_student_grade()
    elif user_input == "10":
        calc_backup()
    elif user_input == "11":
        exit(0)
    else:
        print("elección errónea, por favor vuelva a intentarlo")

if __name__ == "__main__":
    while(True):
        main_loop()