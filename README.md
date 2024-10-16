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

4. **Integer to Roman**

#Python

'''
def integer_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num
'''

5. **Roman to Integer**

#Python

'''
def roman_to_integer(num):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(num):
        value = roman_numerals[char]
        
        if value < prev_value:
            total -= value
        else:
            total += value
        
        prev_value = value
    
    return total
'''

6. **Money To English**

#Python

'''
def money_to_english(num):
    if num < 0:
        return "negative " + money_to_english(-num)
    
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if num == 0:
        return "zero dollars"
    
    dollars = int(num)
    cents = round((num - dollars) * 100)
    
    words = []
    
    if dollars >= 1000:
        words.append(units[dollars // 1000] + " thousand")
        dollars %= 1000
    
    if dollars >= 100:
        words.append(units[dollars // 100] + " hundred")
        dollars %= 100
    
    if dollars >= 20:
        words.append(tens[dollars // 10])
        dollars %= 10
    
    if dollars >= 10:
        words.append(teens[dollars - 10])
        dollars = 0
    
    if dollars > 0:
        words.append(units[dollars])
    
    dollar_words = " ".join(words).strip() + (" dollar" if len(words) == 1 and words[0] == "one" else " dollars")
    
    if cents > 0:
        words = []
        if cents >= 20:
            words.append(tens[cents // 10])
            cents %= 10
        
        if cents >= 10:
            words.append(teens[cents - 10])
            cents = 0
        
        if cents > 0:
            words.append(units[cents])
        
        cent_words = " ".join(words).strip() + (" cent" if len(words) == 1 and words[0] == "one" else " cents")
        return f"{dollar_words} and {cent_words}"
    
    return dollar_words
'''

7. **Tower of hanoi**

#Python

'''
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        return [(source, target)]
    
    moves = tower_of_hanoi(n - 1, source, auxiliary, target)
    
    moves.append((source, target))
    
    moves += tower_of_hanoi(n - 1, auxiliary, target, source)
    
    return moves

'''



8. **Spiral Matrix**

#Python

'''
def spiral_matrix(matrix):
    if not matrix or not matrix[0]:
        return []
    
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    result = []
    
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1  

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1  
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1 

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1  
    return result

'''
