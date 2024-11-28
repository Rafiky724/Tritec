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
            
            if (number % 15 == 0)
            {
                return "FizzBuzz";
            }
            else if (number % 3 == 0)
            {
                return "Fizz";
            }
            else if (number % 5 == 0)
            {
                return "Buzz";
            }
            else
            {
                return number.ToString(); 
            }
        }
    }
}

--------------------------------------------------------------------------

using TritecAPI.Interfaces;

namespace TritecAPI.problem_solver
{
    public class FizzBuzz : IProblemSolver
    {
        public string _fizzBuzz(long number)
        {
            return (number % 3 == 0 ? "Fizz" : "") + (number % 5 == 0 ? "Buzz" : "") + (number % 3 != 0 && number % 5 != 0 ? number.ToString() : "");
        }
    }
}
'''
#Java

'''
public class FizzBuzz {
    
    public static String fizzBuzz(int numero) {
        if (numero % 3 == 0 && numero % 5 == 0) {
            return "FizzBuzz"; 
        } else if (numero % 3 == 0) {
            return "Fizz"; // Si es divisible solo por 3, retorna "Fizz"
        } else if (numero % 5 == 0) {
            return "Buzz"; // Si es divisible solo por 5, retorna "Buzz"
        } else {
            return Integer.toString(numero); // Si no es divisible ni por 3 ni por 5, retorna el número
        }
    }
}

---------------------------------------------------------------------------------------------------------------------------------------

public class FizzBuzz {
    public static String fizzBuzz(int numero) {
        return (numero % 3 == 0 ? "Fizz" : "") + (numero % 5 == 0 ? "Buzz" : (numero % 3 != 0 ? Integer.toString(numero) : ""));
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

#Java

'''

public class Palindrome {
    public static boolean isPalindrome(String word) {
        // Eliminar espacios y convertir a minúsculas
        word = word.replace(" ", "").toLowerCase();
        
        int length = word.length();
        for (int i = 0; i < length / 2; i++) {
            if (word.charAt(i) != word.charAt(length - i - 1)) {
                return false;
            }
        }
        return true;
    }
}
        
'''

3. **Binary Search**:

#Python

'''
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

----------------------------------------

def binary_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


'''

#cshard

'''

using System;

namespace TritecAPI.problem_solver
{
    public class BinarySearch
    {
        public int _binarySearch(int[] array, int target)
        {
            for (int i = 0; i < array.Length; i++)
            {
                if (array[i] == target)
                {
                    return i; 
                }
            }

            return -1;
        }
    }
}

-----------------------------------------------------------------------------------------------------------------------------------

using System;

namespace TritecAPI.problem_solver
{
    public class BinarySearch
    {
        public int _binarySearch(int[] array, int target)
        {
            int low = 0;
            int high = array.Length - 1;

            (low <= high)
            while (low <= high)
            {
     
                int mid = low + (high - low) / 2;

     
                if (array[mid] == target)
                {
                    return mid; 
                }
                else if (array[mid] < target)
                {
                    low = mid + 1;
                }
                else
                {
                    high = mid - 1;
                }
            }

            return -1;
        }
    }
}


'''



#Java
'''
public class BinarySearch {
    public static int binarySearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;  
    }
}


-----------------------------------------------------------------------------------------------------------------------------------


public class BinarySearch {
    public static int binarySearch(int[] arr, int target) {
        int low = 0;
        int high = arr.length - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;  

            if (arr[mid] == target) {
                return mid;
            }

            if (arr[mid] < target) {
                low = mid + 1;
            }

            else {
                high = mid - 1;
            }
        }

        return -1;
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

#C#

'''
using System.Text; 

namespace TritecAPI.problem_solver
{
    public class IntegerToRoman
    {
        public string _intToRoman(int num)
        {
            var romanSymbols = new (int, string)[]
            {
                (1000, "M"),
                (900, "CM"),
                (500, "D"),
                (400, "CD"),
                (100, "C"),
                (90, "XC"),
                (50, "L"),
                (40, "XL"),
                (10, "X"),
                (9, "IX"),
                (5, "V"),
                (4, "IV"),
                (1, "I")
            };

            var result = new StringBuilder();  // Aquí se usa StringBuilder

            foreach (var (value, symbol) in romanSymbols)
            {
                while (num >= value)
                {
                    result.Append(symbol);
                    num -= value;
                }
            }

            return result.ToString();
        }
    }
}

'''

#Java

'''
public class IntegerToRoman {
    public static String integerToRoman(int num) {
        // Arreglo con los valores de los números romanos
        int[] val = {
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        };

        // Arreglo con los símbolos correspondientes a cada valor
        String[] syms = {
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        };

        // Cadena para almacenar el resultado
        StringBuilder romanNum = new StringBuilder();

        // Iterar sobre los valores romanos
        for (int i = 0; i < val.length; i++) {
            // Mientras el número sea mayor que el valor actual
            while (num >= val[i]) {
                romanNum.append(syms[i]);  // Añadir el símbolo correspondiente
                num -= val[i];             // Restar el valor de num
            }
        }

        return romanNum.toString();
    }
}
        

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

#C#

'''
using System.Collections.Generic;

namespace TritecAPI.problem_solver
{
    public class RomanToInteger
    {
        public int _romanToInt(string s)
        {
            var romanMap = new Dictionary<char, int>
            {
                {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
                {'C', 100}, {'D', 500}, {'M', 1000}
            };

            int result = 0;
            int prevValue = 0;

            foreach (char c in s)
            {
                int currValue = romanMap[c];
                result += currValue;

                if (currValue > prevValue)
                {
                    // Si el valor actual es mayor que el anterior (e.g., IV, IX),
                    // restamos dos veces el valor anterior porque ya lo sumamos una vez.
                    result -= 2 * prevValue;
                }

                prevValue = currValue;
            }

            return result;
        }
    }
}

'''

#Java

'''

import java.util.HashMap;
import java.util.Map;

public class RomanToInteger {
    public static int romanToInteger(String num) {
        // Crear un mapa de los valores de los números romanos
        Map<Character, Integer> romanNumerals = new HashMap<>();
        romanNumerals.put('I', 1);
        romanNumerals.put('V', 5);
        romanNumerals.put('X', 10);
        romanNumerals.put('L', 50);
        romanNumerals.put('C', 100);
        romanNumerals.put('D', 500);
        romanNumerals.put('M', 1000);

        int total = 0;
        int prevValue = 0;

        // Recorrer el número romano de derecha a izquierda
        for (int i = num.length() - 1; i >= 0; i--) {
            char currentChar = num.charAt(i);
            int value = romanNumerals.get(currentChar);

            // Si el valor actual es menor que el valor anterior, restamos, sino sumamos
            if (value < prevValue) {
                total -= value;
            } else {
                total += value;
            }

            prevValue = value;  // Actualizamos el valor anterior
        }

        return total;
    }
}
        
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

#C#

'''
using System; 

namespace TritecAPI.problem_solver
{
    public class MoneyToEnglish
    {
        private static readonly string[] Ones = new string[] { "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" };
        private static readonly string[] Tens = new string[] { "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" };
        private static readonly string[] Thousands = new string[] { "", "thousand", "million", "billion" };

        public string ConvertToWords(decimal number)
        {
            if (number == 0)
            {
                return "zero dollars";
            }

            string numberInWords = "";

            // Handling negative numbers
            if (number < 0)
            {
                numberInWords = "negative ";
                number = Math.Abs(number);  // Math.Abs() necesita el using System;
            }

            // Convert dollars (integer part)
            long dollars = (long)number;
            numberInWords += ConvertWholeNumber(dollars) + " dollar" + (dollars != 1 ? "s" : "");

            // Convert cents (decimal part)
            int cents = (int)((number - dollars) * 100);
            if (cents > 0)
            {
                numberInWords += " and " + ConvertWholeNumber(cents) + " cent" + (cents != 1 ? "s" : "");
            }

            return numberInWords;
        }

        private string ConvertWholeNumber(long number)
        {
            if (number == 0)
            {
                return "";
            }

            string result = "";
            int thousandIndex = 0;

            while (number > 0)
            {
                if (number % 1000 != 0)
                {
                    result = ConvertHundreds(number % 1000) + (Thousands[thousandIndex] != "" ? " " + Thousands[thousandIndex] : "") + " " + result;
                }
                number /= 1000;
                thousandIndex++;
            }

            return result.Trim();
        }

        private string ConvertHundreds(long number)
        {
            string result = "";

            if (number >= 100)
            {
                result += Ones[number / 100] + " hundred ";
                number %= 100;
            }

            if (number >= 20)
            {
                result += Tens[number / 10] + " ";
                number %= 10;
            }

            if (number > 0)
            {
                result += Ones[number] + " ";
            }

            return result.Trim();
        }
    }
}

'''

#Java

'''
public class MoneyToEnglish {
    
    public static String moneyToEnglish(double num) {
        if (num < 0) {
            return "negative " + moneyToEnglish(-num);
        }

        // Arrays con las palabras correspondientes
        String[] units = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        String[] teens = {"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
                          "sixteen", "seventeen", "eighteen", "nineteen"};
        String[] tens = {"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

        // Si el número es 0
        if (num == 0) {
            return "zero dollars";
        }

        // Separar la parte de los dólares y los centavos
        int dollars = (int) num;
        int cents = (int) Math.round((num - dollars) * 100);

        StringBuilder words = new StringBuilder();

        // Convertir dólares a palabras
        if (dollars >= 1000) {
            words.append(units[dollars / 1000]).append(" thousand ");
            dollars %= 1000;
        }

        if (dollars >= 100) {
            words.append(units[dollars / 100]).append(" hundred ");
            dollars %= 100;
        }

        if (dollars >= 20) {
            words.append(tens[dollars / 10]).append(" ");
            dollars %= 10;
        }

        if (dollars >= 10) {
            words.append(teens[dollars - 10]).append(" ");
            dollars = 0;
        }

        if (dollars > 0) {
            words.append(units[dollars]).append(" ");
        }

        // Agregar "dollar" o "dollars"
        String dollarWords = words.toString().trim() + (words.toString().trim().equals("one") ? " dollar" : " dollars");

        // Si hay centavos, convertirlos a palabras
        if (cents > 0) {
            words.setLength(0); // Limpiar el StringBuilder para los centavos

            if (cents >= 20) {
                words.append(tens[cents / 10]).append(" ");
                cents %= 10;
            }

            if (cents >= 10) {
                words.append(teens[cents - 10]).append(" ");
                cents = 0;
            }

            if (cents > 0) {
                words.append(units[cents]).append(" ");
            }

            // Agregar "cent" o "cents"
            String centWords = words.toString().trim() + (words.toString().trim().equals("one") ? " cent" : " cents");
            return dollarWords + " and " + centWords;
        }

        return "asdasd";
    }
}
        
'''

7. **Spiral Matrix**

#Python

'''
def spiralmatrix(matrix):
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
#C#

'''
using System;
using System.Collections.Generic;

namespace TritecAPI.problem_solver
{
    public class SpiralMatrix
    {
        public List<int> SpiralOrder(int[][] matrix)
        {
            var result = new List<int>();
            if (matrix == null || matrix.Length == 0) return result;

            int top = 0, bottom = matrix.Length - 1;
            int left = 0, right = matrix[0].Length - 1;

            while (top <= bottom && left <= right)
            {
                // Recorrer de izquierda a derecha
                for (int i = left; i <= right; i++)
                {
                    result.Add(matrix[top][i]);
                }
                top++;

                // Recorrer de arriba hacia abajo
                for (int i = top; i <= bottom; i++)
                {
                    result.Add(matrix[i][right]);
                }
                right--;

                if (top <= bottom)
                {
                    // Recorrer de derecha a izquierda
                    for (int i = right; i >= left; i--)
                    {
                        result.Add(matrix[bottom][i]);
                    }
                    bottom--;
                }

                if (left <= right)
                {
                    // Recorrer de abajo hacia arriba
                    for (int i = bottom; i >= top; i--)
                    {
                        result.Add(matrix[i][left]);
                    }
                    left++;
                }
            }

            return result;
        }
    }
}
'''

#Java

'''
import java.util.ArrayList;
import java.util.List;

public class SpiralMatrix {
    public static List<Integer> spiralMatrix(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        
        // Verificar si la matriz está vacía
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return result;
        }

        int top = 0, bottom = matrix.length - 1;
        int left = 0, right = matrix[0].length - 1;

        while (top <= bottom && left <= right) {
            // Recorrer de izquierda a derecha en la fila superior
            for (int i = left; i <= right; i++) {
                result.add(matrix[top][i]);
            }
            top++;

            // Recorrer de arriba a abajo en la columna derecha
            for (int i = top; i <= bottom; i++) {
                result.add(matrix[i][right]);
            }
            right--;

            // Recorrer de derecha a izquierda en la fila inferior (si aún es válida)
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    result.add(matrix[bottom][i]);
                }
                bottom--;
            }

            // Recorrer de abajo a arriba en la columna izquierda (si aún es válida)
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    result.add(matrix[i][left]);
                }
                left++;
            }
        }

        return result;
    }
}
        
'''
8. **Median Of Two Sorted Arrays**

#Python

'''
def median_of_two_sorted_arrays(array1, array2):
    array1.extend(array2)
    sorted_array = sorted(array1)
    tamanio = len(sorted_array)

    if tamanio % 2 == 1:
        mediana = sorted_array[tamanio // 2]
    else:
        mediana = (sorted_array[tamanio // 2 - 1] + sorted_array[tamanio // 2]) / 2.0 
    return mediana
'''
# C$

'''
using System;

namespace TritecAPI.problem_solver
{
    public class MedianOfTwoSortedArrays
    {
        public double FindMedianSortedArrays(int[] nums1, int[] nums2)
        {
            if (nums1.Length > nums2.Length)
            {
                // Asegúrese de que nums1 sea el más pequeño
                var temp = nums1;
                nums1 = nums2;
                nums2 = temp;
            }

            int x = nums1.Length;
            int y = nums2.Length;

            int low = 0, high = x;
            while (low <= high)
            {
                int partitionX = (low + high) / 2;
                int partitionY = (x + y + 1) / 2 - partitionX;

                int maxX = (partitionX == 0) ? int.MinValue : nums1[partitionX - 1];
                int minX = (partitionX == x) ? int.MaxValue : nums1[partitionX];

                int maxY = (partitionY == 0) ? int.MinValue : nums2[partitionY - 1];
                int minY = (partitionY == y) ? int.MaxValue : nums2[partitionY];

                if (maxX <= minY && maxY <= minX)
                {
                    if ((x + y) % 2 == 0)
                    {
                        return (Math.Max(maxX, maxY) + Math.Min(minX, minY)) / 2.0;
                    }
                    else
                    {
                        return Math.Max(maxX, maxY);
                    }
                }
                else if (maxX > minY)
                {
                    high = partitionX - 1;
                }
                else
                {
                    low = partitionX + 1;
                }
            }

            throw new ArgumentException("Input arrays are not sorted.");
        }
    }
}


#Java

'''

import java.util.Arrays;

public class MedianOfTwoSortedArrays {
    public static double medianOfTwoSortedArrays(int[] array1, int[] array2) {
        // Crear una lista para combinar ambos arrays
        int[] combinedArray = new int[array1.length + array2.length];
        
        // Copiar los elementos de ambos arrays a la lista combinada
        System.arraycopy(array1, 0, combinedArray, 0, array1.length);
        System.arraycopy(array2, 0, combinedArray, array1.length, array2.length);
        
        // Ordenar el array combinado
        Arrays.sort(combinedArray);
        
        // Calcular el tamaño del array combinado
        int size = combinedArray.length;
        
        // Si el tamaño es impar, la mediana es el valor del medio
        if (size % 2 == 1) {
            return combinedArray[size / 2];
        } else {
            // Si el tamaño es par, la mediana es el promedio de los dos valores centrales
            return (combinedArray[size / 2 - 1] + combinedArray[size / 2]) / 2.0;
        }
    }
}
        
'''

9. **Longer Valid Parentheses**


#Python
'''
def longer_valid_parentheses(s):
    stack = []  
    count = 0  

    for char in s:
        if char == "(":  
            stack.append("(")  
        elif char == ")":  
            if stack:  
                stack.pop()  
                count += 1  

    return count  
'''

# C#

'''
using System;
using System.Collections.Generic;

namespace TritecAPI.problem_solver
{
    public class LongerValidParentheses
    {
        public int LongestValidParentheses(string s)
        {
            Stack<int> stack = new Stack<int>();
            stack.Push(-1); 
            int maxLength = 0;

            for (int i = 0; i < s.Length; i++)
            {
                if (s[i] == '(')
                {
                    stack.Push(i); 
                }
                else
                {
                    stack.Pop();

                    // Verificamos si hay un paréntesis de apertura válido para el cierre
                    if (stack.Count > 0)
                    {
                        maxLength = Math.Max(maxLength, i - stack.Peek()); // Calculamos el largo de la subsecuencia válida
                    }
                    else
                    {
                        stack.Push(i); // Si la pila está vacía, guardamos la posición del paréntesis de cierre
                    }
                }
            }

            return maxLength;
        }
    }
}

'''

#Java

'''

import java.util.Stack;

public class LongerValidParentheses {
    public static int longerValidParentheses(String s) {
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);  // Agregar un marcador inicial para manejar casos como "()"

        int maxLength = 0;

        for (int i = 0; i < s.length(); i++) {
            char charAt = s.charAt(i);

            if (charAt == '(') {
                // Coloca el índice del paréntesis de apertura en la pila
                stack.push(i);
            } else if (charAt == ')') {
                // Desapilar el índice del paréntesis de apertura correspondiente
                stack.pop();

                // Si la pila no está vacía, calcular la longitud del paréntesis válido
                if (!stack.isEmpty()) {
                    maxLength = Math.max(maxLength, i - stack.peek());
                } else {
                    // Si la pila está vacía, agregamos el índice actual como marcador base
                    stack.push(i);
                }
            }
        }

        return maxLength/2;
    }
}
        
'''

10. **Count Of Smaller Numbers After Self**


#Python
'''

def count_Smaller(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    counts = [0] * len(nums)
        
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                counts[i] += 1
        
    return counts

'''

# C#

'''
using System;
using System.Collections.Generic;

namespace TritecAPI.problem_solver
{
    public class CountofSmallerNumbersAfterSelf
    {
        public int[] CountSmaller(int[] nums)
        {
            int n = nums.Length;
            int[] result = new int[n];
            if (n == 0)
                return result;

            // Usamos un árbol de búsqueda balanceado para contar los elementos menores
            List<int> sortedList = new List<int>();

            for (int i = n - 1; i >= 0; i--)
            {
                int index = BinarySearch(sortedList, nums[i]);
                result[i] = index;
                InsertInSortedList(sortedList, nums[i]);
            }

            return result;
        }

        // Método para insertar un número en la lista ordenada
        private void InsertInSortedList(List<int> list, int num)
        {
            int low = 0, high = list.Count;
            while (low < high)
            {
                int mid = (low + high) / 2;
                if (list[mid] < num)
                {
                    low = mid + 1;
                }
                else
                {
                    high = mid;
                }
            }
            list.Insert(low, num);
        }

        // Método para realizar una búsqueda binaria
        private int BinarySearch(List<int> list, int target)
        {
            int low = 0, high = list.Count;
            while (low < high)
            {
                int mid = (low + high) / 2;
                if (list[mid] < target)
                {
                    low = mid + 1;
                }
                else
                {
                    high = mid;
                }
            }
            return low;
        }
    }
}

'''

#Java


'''
public class CountSmaller {
    public static int[] countSmaller(int[] nums) {
        int[] counts = new int[nums.length];
        
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] < nums[i]) {
                    counts[i]++;
                }
            }
        }
        
        return counts;
    }
}
        

'''