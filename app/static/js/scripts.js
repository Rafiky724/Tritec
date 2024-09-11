document.addEventListener("DOMContentLoaded", function () {
  var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
    mode: "python",
    lineNumbers: true,
    theme: "default",
    tabSize: 4,
    indentUnit: 4,
    lineWrapping: true,
  });
});
