const form = document.getElementById("form");
const command = document.getElementById("command");

form.addEventListener("submit", function (e) {
    e.preventDefault();

    addElement(command.value);
    form.reset();

    // execute game command
})

function addElement(text) {
    const output = document.getElementById('outputs');

    // Create some element, e.g. div
    const newElement = document.createElement('div');
    newElement.setAttribute('id', "some-id-for-new-element");

    newElement.innerHTML = text;

    output.appendChild(newElement);
}
