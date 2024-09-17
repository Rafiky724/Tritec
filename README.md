# Proyecto Flask

Este proyecto es una aplicación web construida con Flask. A continuación se detallan los pasos para configurar y ejecutar el proyecto.

## Requisitos

Asegúrate de tener `python` y `pip` instalados en tu sistema.

## Configuración del Entorno

1. **Clona el repositorio** (si aún no lo has hecho):

    ```bash
    git clone <url-del-repositorio>
    cd <nombre-del-repositorio>
    ```

2. **Crea y activa un entorno virtual**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

## Ejecutar la Aplicación

1. **Inicia el servidor de desarrollo**:

    ```bash
    flask --app main run
    ```

2. **Abre tu navegador** y dirígete a `http://127.0.0.1:5000` para ver la aplicación en acción.

## Generar el archivo `requirements.txt`

Si necesitas actualizar o generar el archivo `requirements.txt` con las dependencias actuales, usa:

```bash
pip freeze > requirements.txt

## Codigos

1. **FizzBuzz**:

#Python

'''
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
'''

#cshard

'''
using TritecAPI.Interfaces;

namespace TritecAPI.problem_solver
{
    public class FizzBuzz : IProblemSolver
    {
        public string _fizzBuzz(long number)
        {
            return number % 15 == 0 ? "FizzBuzz" :
                   number % 3 == 0 ? "Fizz" :
                   number % 5 == 0 ? "Buzz" :
                   number.ToString();
        }
    }
}
'''

2. **Palindrome**:

#Python

'''
def is_palindrome(word):
    word = word.replace(" ", "").lower()
    
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True
'''

#cshard

'''
using TritecAPI.Interfaces;

namespace TritecAPI.problem_solver
{
    public class Palindrome
    {
        public bool _palindrome(string word)
        {
            word = word.Replace(" ", "").ToLower();

            int length = word.Length;
            for (int i = 0; i < length / 2; i++)
            {
                if (word[i] != word[length - i - 1])
                {
                    return false;
                }
            }
            return true;
        }
    }
}
'''

3. **Binary Search**:

#Python

'''
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
'''

#cshard

'''
using TritecAPI.Interfaces;

namespace TritecAPI.problem_solver
{
    public class BinarySearch
    {
        public int _binarySearch(int[] array, int target)
        {
            int left = 0;
            int right = array.Length - 1;

            while (left <= right)
            {
                int mid = left + (right - left) / 2;

                if (array[mid] == target)
                {
                    return mid;
                }
                else if (array[mid] < target)
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid - 1;
                }
            }

            return -1;
        }
    }
}
'''
