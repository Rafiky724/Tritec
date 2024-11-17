import importlib
import sys
from app.controllers.codes_controller import CodesController
import requests

def getResult(user_code, language, problem):
    if language == "python":
        print(language, problem)
        reload_module()
        return pythonProblem(user_code, problem)
    elif language == "csharp":
        return cSharpProblem(user_code, problem)
    else:
        return "Invalid language"

def pythonProblem(user_code, problem):
    problem = CodesController(user_code, problem)
    response = problem.set_up()
    return response

def cSharpProblem(user_code, problem):
    data = {'codigo': user_code, 'problema': problem}
    url = "https://localhost:7202/Codigo/Recibir"

    response = requests.post(url, json=data, verify=False)

    if response.status_code == 200:
        return response
    else:
        return {"error": "Error"}
    
def reload_module():
    module_name = f"app.tests"
    if module_name in sys.modules:
        importlib.reload(sys.modules[module_name])
    else:
        importlib.import_module(module_name)