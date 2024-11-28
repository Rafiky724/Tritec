import importlib
import sys
from app.controllers.codes_controller import CodesController
from app.controllers.codes_controller_java import CodesControllerJava
import requests

def getResult(user_code, language, problem):
    """
    Determina el resultado del código proporcionado por el usuario según el lenguaje y el problema.
    """
    if language == "python":
        reload_module()
        return pythonProblem(user_code, problem)
    elif language == "csharp":
        return cSharpProblem(user_code, problem)
    elif language == "java":
        return javaProblem(user_code, problem)
    else:
        return "Invalid language"

def contains_if(code):
    return 'if' in code

def is_binary_search_code(code: str) -> bool:

    keywords = ["low", "high", "mid", "while", "return"]
    clean_code = code.replace(" ", "").lower()
    if not all(keyword in clean_code for keyword in keywords):
        return False
    modifies_low = "low=" in clean_code or "low+=" in clean_code
    modifies_high = "high=" in clean_code or "high-=" in clean_code

    return modifies_low and modifies_high


def pythonProblem(user_code, problem):

    if problem == "FizzBuzz" and contains_if(user_code):
        print("Error: El código no debe contener bucles 'if'.")
        return None
    
    if problem == "BinarySearch" and not is_binary_search_code(user_code):
        print("Error: El código no parece implementar una búsqueda binaria.")
        return None

    problem_controller = CodesController(user_code, problem)
    response = problem_controller.set_up()
    return response

def cSharpProblem(user_code, problem):

    if problem == "FizzBuzz" and contains_if(user_code):
        print("Error: El código no debe contener bucles 'if'.")
        return None
    
    if problem == "BinarySearch" and not is_binary_search_code(user_code):
        print("Error: El código no parece implementar una búsqueda binaria.")
        return None
    
    data = {'codigo': user_code, 'problema': problem}
    url = "https://localhost:7202/Codigo/Recibir"

    response = requests.post(url, json=data, verify=False)

    if response.status_code == 200:
        response_data = response.json()
        errores = response_data.get('errores')
        return response_data.get('resultado') if errores is None else errores
    else:
        return {"error": "Error al comunicarse con el servidor."}

def javaProblem(user_code, problem):
    if problem == "FizzBuzz" and contains_if(user_code):
        print("Error: El código no debe contener bucles 'if'.")
        return None
    
    if problem == "BinarySearch" and not is_binary_search_code(user_code):
        print("Error: El código no parece implementar una búsqueda binaria.")
        return None

    problem_controller = CodesControllerJava(user_code, problem)
    response = problem_controller.set_up()
    print(response)
    return response

def reload_module():
    """
    Recarga dinámicamente el módulo de pruebas de la aplicación.
    """
    module_name = "app.tests"
    if module_name in sys.modules:
        importlib.reload(sys.modules[module_name])
    else:
        importlib.import_module(module_name)
