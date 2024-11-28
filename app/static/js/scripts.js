// Esperamos que el DOM esté completamente cargado antes de ejecutar el código
document.addEventListener("DOMContentLoaded", function () {
  var textareas = document.querySelectorAll('textarea.codeTextArea');

  textareas.forEach(function (textarea) {

    if (textarea.id !== 'code') {

      var editor = CodeMirror.fromTextArea(textarea, {
        mode: "python",
        lineNumbers: true,
        theme: "dracula",
        tabSize: 4,
        indentUnit: 4,
        lineWrapping: true,
      });

    }

  });
});

let isSubmitEnabled = false;

function updateTerminal(language) {
  var editors = document.querySelectorAll('.CodeMirror');
  editors.forEach(function (editorElement) {
    var editor = editorElement.CodeMirror;
    editor.setOption("mode", language.toLowerCase());
  });
  console.log(editors);
}

var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
  mode: "python",
  lineNumbers: true,
  theme: "dracula",
  tabSize: 4,
  indentUnit: 4,
  lineWrapping: true,

});

// function updateTerminal(language) {
//   editor.setOption("mode", language.toLowerCase());
//   console.log(editor);
// }

function toggleDropdown() {
  let dropdown = document.querySelector("#dropdown");
  dropdown.classList.toggle("hidden");
}

function selectLanguaje(language) {
  let languageDisplay = document.querySelector("#language");

  languageDisplay.textContent = language;

  const url = new URL(window.location.href);
  url.searchParams.set('language', language);
  window.location.href = url.toString();

  updateTerminal(language);

  toggleDropdown();

}

let buttonSubmitCode = document.getElementById('submitCode').addEventListener('click', () => {

  if(isSubmitEnabled){

    evaluateCode(true);

  }

})

let buttonRunCode = document.getElementById('runCode').addEventListener('click', () => {

  evaluateCode(false);

})

function evaluateCode(aux) {

  const container = document.querySelector('#containerTest');
  container.innerHTML = '';

  let languageDisplay = document.querySelector("#language");
  let language;

  if (languageDisplay.textContent === "Python") {

    language = "python";

  } else if (languageDisplay.textContent === "Java") {

    language = "java";

  } else {

    language = "csharp";

  }

  let problem = document.querySelector('#problemTitle').textContent.trim();

  const data = {
    code: editor.getValue(),
    language: language,
    problem: problem
  };

  fetch('http://127.0.0.1:5000/enviar', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
  })
    .then(response => response.json())
    .then(data => {
      console.log('Éxito:', data);
      let dataBools
      try {
        dataBools = data['message'];
      } catch (error) {
        console.log('Error:', error);
        isSubmitEnabled = false;
        let botonSubmit = document.getElementById("submitCode");
        botonSubmit.classList.add('disabledButton');
        mostrarMensaje("Error de compilación", "Por favor verifica tu código. Recuerda que no debes borrar la plantilla inicial de código.")
        //alert("ERROR DE COMPILACIÓN: Por favor verifica tu código. Recuerda que no debes borrar la plantilla inicial de código.")
      }

      if (language == 'csharp') {
        /*
        dataBools = dataBools.slice(1, -1);
        console.log(dataBools);
        let boolArrayStr = dataBools.split(",");

        dataBools = boolArrayStr.map(str => str.trim() === 'true');*/

        console.log(dataBools);

        if (typeof (dataBools) === 'string') {

          isSubmitEnabled = false;
          let botonSubmit = document.getElementById("submitCode");
          botonSubmit.classList.add('disabledButton');
          mostrarMensaje("Error de compilación", `Por favor verifica tu código. Recuerda que no debes borrar la plantilla inicial de código.\n\n${dataBools}`)
          //alert(`ERROR DE COMPILACIÓN: Por favor verifica tu código. Recuerda que no debes borrar la plantilla inicial de código.\n\n${dataBools}`)

        } else {
          showTests(dataBools, problem, language, aux);
        }

      }

      if (language == 'java') {

        if (dataBools.length == 2) {

          isSubmitEnabled = false;
          let botonSubmit = document.getElementById("submitCode");
          botonSubmit.classList.add('disabledButton');
          mostrarMensaje("Error de compilación", `Por favor verifica tu código. Recuerda que no debes borrar la plantilla inicial de código.\n\n${dataBools[0]}\n${dataBools[1]}`)
          //alert(`ERROR DE COMPILACIÓN: Por favor verifica tu código. Recuerda que no debes borrar la plantilla inicial de código.\n\n${dataBools[0]}\n${dataBools[1]}`)

        } else {

          showTests(dataBools, problem, language, aux);

        }

      }
      if (language == 'python') {

        console.log(typeof dataBools);
        if (typeof dataBools === 'string') {

          isSubmitEnabled = false;
          let botonSubmit = document.getElementById("submitCode");
          botonSubmit.classList.add('disabledButton');
          mostrarMensaje("Error de compilación", `Por favor verifica tu código. Recuerda que no debes borrar la plantilla inicial de código.\n\n${dataBools}`)
          //alert(`ERROR DE COMPILACIÓN: Por favor verifica tu código. Recuerda que no debes borrar la plantilla inicial de código.\n\n${dataBools[0]}`)
          //showTests(dataBools, problem, language, aux);
        } else {

          showTests(dataBools, problem, language, aux);

        }

      }

    })
    .catch((error) => {
      console.error('Error:', error);
      setTimeout(function () {
        isSubmitEnabled = false;
        let botonSubmit = document.getElementById("submitCode");
        botonSubmit.classList.add('disabledButton');
        mostrarMensaje("Error", "Por favor verifica tu código. Recuerda que no debes borrar la plantilla inicial de código.")
        //alert('ERROR: Por favor verifica tu código. Recuerda que no debes borrar la plantilla inicial de código.');
      }, 500);
    });

}

function showTests(dataBools, problem, language, aux) {

  const container = document.querySelector('#containerTest');

  container.innerHTML = '';

  let numberTest = 1;

  dataBools.forEach((result, index) => {

    const ul = document.createElement('ul');
  
    const li = document.createElement('li');
    li.className = 'flex tests mb-2 p-3 rounded-lg justify-between items-center fade-in';  // Añadimos la clase fade-in
  
    const img = document.createElement('img');
    img.alt = result ? 'Resultado Bueno' : 'Resultado Malo';
    img.src = result ? './static/img/good.png' : './static/img/bad.png';
  
    let textTest = document.createTextNode("Prueba " + numberTest.toString());
  
    li.appendChild(textTest);
    li.appendChild(img);
  
    ul.appendChild(li);
  
    container.appendChild(ul);
  
    // Usamos setTimeout para añadir la clase "fade-in-visible" con un retraso basado en el índice
    setTimeout(() => {
      li.classList.add('fade-in-visible');
    }, index * 200); // 500 ms de retraso entre cada elemento
  
    numberTest++;
  });

  if (dataBools.every(elemnt => elemnt === true)) {

    setTimeout(function () {
      //alert('Felicidades. Tu código ha pasado todas las pruebas.');
      
      isSubmitEnabled = true;

      if(aux){
        mostrarMensaje("¡Enviado!", "Tu código ha pasado todas las pruebas y ha sido subido con éxito.")
        submitCode(editor.getValue(), language, problem, dataBools, document.getElementById("submitCode").dataset.problemId, true);

      }else{

        mostrarMensaje("¡Felicidades!", "Tu código ha pasado todas las pruebas.")
        let botonSubmit = document.getElementById("submitCode");
        botonSubmit.classList.remove('disabledButton');

      }
      
    }, 500);

  } else {

    setTimeout(function () {
      isSubmitEnabled = false;
      let botonSubmit = document.getElementById("submitCode");
      botonSubmit.classList.add('disabledButton');
      //alert('Error. Tu código no ha pasado todas las pruebas.');
      mostrarMensaje("Error", "Tu código no ha pasado todas las pruebas.")
    }, 500);

  }

}

function submitCode(code, lang, problem, test, id, value) {

  const Data = {

    code: code,
    language: lang,
    problem: problem,
    test: test,
    id: id,
    value: value

  }

  fetch('http://127.0.0.1:5000/submit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'  // Indicar que se está enviando JSON
    },
    body: JSON.stringify(Data)  // Convertir los datos a JSON
  })
    .then(response => response.json())  // Convertir la respuesta a JSON
    .then(data => {
      console.log(data);  // Manejar la respuesta de Flask
    })
    .catch(error => {
      console.error('Error:', error);  // Manejar errores
    });

}

function mostrarMensaje(title, description) {

  let modal = document.getElementById('modal');
  document.getElementById('titleModal').innerHTML = title;
  document.getElementById('descriptionModal').innerHTML = description;

  modal.style.opacity = 1;
  setTimeout(() => {
    modal.style.opacity = 0;
  }, 7000);
}