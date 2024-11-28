// Esperamos que el DOM esté completamente cargado antes de ejecutar el código
document.addEventListener("DOMContentLoaded", function() {
  var textareas = document.querySelectorAll("textarea[id='code']"); 

  textareas.forEach(function(textarea) {
      var editor = CodeMirror.fromTextArea(textarea, {
          mode: "python",
          lineNumbers: true,
          theme: "dracula",
          tabSize: 4,
          indentUnit: 4,
          lineWrapping: true,
      });
  });
});

function updateTerminal(language) {
var editors = document.querySelectorAll('.CodeMirror'); 
editors.forEach(function(editorElement) {
  var editor = editorElement.CodeMirror; 
  editor.setOption("mode", language.toLowerCase());
});
console.log(editors);
}

// var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
//   mode: "python",
//   lineNumbers: true,
//   theme: "dracula",
//   tabSize: 4,
//   indentUnit: 4,
//   lineWrapping: true,

// });

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

let buttonRunCode = document.getElementById('submitCode').addEventListener('click', () => {
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
        alert("ERROR DE COMPILACIÓN: Por favor verifica tu código. Recuerda que no debes borrar la plantilla inicial de código.")
      }

      if (language == 'csharp') {
        /*
        dataBools = dataBools.slice(1, -1);
        console.log(dataBools);
        let boolArrayStr = dataBools.split(",");

        dataBools = boolArrayStr.map(str => str.trim() === 'true');*/
        showTests(dataBools, problem, language);

      }

      if (language == 'java') {

        if (dataBools.length == 2) {

          alert(`ERROR DE COMPILACIÓN: Por favor verifica tu código. Recuerda que no debes borrar la plantilla inicial de código.\n\n${dataBools[0]}\n${dataBools[1]}`)

        }else{

          showTests(dataBools, problem, language);

        }

      }
      if (language == 'python'){
        
        if (dataBools.length == 1){

          //alert(`ERROR DE COMPILACIÓN: Por favor verifica tu código. Recuerda que no debes borrar la plantilla inicial de código.\n\n${dataBools[0]}`)
          showTests(dataBools, problem, language);
        }else{

          showTests(dataBools, problem, language);

        }

      }
      
    })
    .catch((error) => {
      console.error('Error:', error);
      setTimeout(function () {
        alert('ERROR: Por favor verifica tu código. Recuerda que no debes borrar la plantilla inicial de código.');
      }, 500);
    });

})

function showTests(dataBools, problem, language) {

  const container = document.querySelector('#containerTest');

  container.innerHTML = '';

  let numberTest = 1;

  dataBools.forEach(result => {

    const ul = document.createElement('ul');

    const li = document.createElement('li');
    li.className = 'flex tests mb-2 p-3 rounded-lg justify-between items-center';

    const img = document.createElement('img');
    img.alt = result ? 'Resultado Bueno' : 'Resultado Malo';
    img.src = result ? './static/img/good.png' : './static/img/bad.png';

    let textTest = document.createTextNode("Prueba " + numberTest.toString());

    li.appendChild(textTest);
    li.appendChild(img);

    ul.appendChild(li);

    container.appendChild(ul);
    numberTest++;
  });

  if (dataBools.every(elemnt => elemnt === true)) {

    setTimeout(function () {
      alert('Felicidades. Tu código ha pasado todas las pruebas.');
      submitCode(editor.getValue(), language, problem, dataBools, document.getElementById("submitCode").dataset.problemId, true);
    }, 500);

  } else {

    setTimeout(function () {
      alert('Error. Tu código no ha pasado todas las pruebas.');
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

/*
let buttonSubmit = document.getElementsById('submitCode').addEventListener('click', () => {

  let languageDisplay = document.querySelector("#language");
  let language;

  if (languageDisplay.textContent === "Python") {

    language = "python";

  } else if(languageDisplay.textContent === "Java") {

    language = "java";

  }else{

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
    })
    .catch((error) => {
      console.error('Error:', error);
      setTimeout(function() {
        alert('ERROR: Al enviar el código"');
      }, 500); 
    });

})*/