const form = document.getElementById("form");
const command = document.getElementById("command");

form.addEventListener("submit", function (e) {
    e.preventDefault();

    const userInput = command.value
    addElement(userInput);
    form.reset();

    // execute game command
    executeCommand(userInput).then(r => addElement(r))
})

async function executeCommand(userInput) {
    const data = {
        input: userInput
    };
    const requestOptions = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    };
    try {
        const response = await fetch('/execute_command', requestOptions);
        return await response.text();
    } catch (e) {
        addElement(`ERROR: ${e}`)
    }
}

function addElement(text) {
    const output = document.getElementById('outputs');

    const newElement = document.createElement('div');
    newElement.setAttribute("class", "output");

    newElement.innerHTML = text;

    output.appendChild(newElement);
}
