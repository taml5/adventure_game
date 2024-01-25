const form = document.getElementById("form");
const command = document.getElementById("command");

document.addEventListener('DOMContentLoaded', function() {
    executeCommand("look", '/on_load').then(r => {
        const commands = eval(r)

        for (const command of commands) {
            addElement(command);
        }
    });
});


form.addEventListener("submit", function (e) {
    e.preventDefault();

    const userInput = command.value
    addElement(userInput);
    form.reset();

    // execute game command
    executeCommand(userInput, '/execute_command').then(r => {
        const commands = eval(r)

        for (const command of commands) {
            addElement(command);
        }
    });
})

async function executeCommand(userInput, url) {
    const data = {
        input: userInput
    };
    const requestOptions = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    };
    try {
        const response = await fetch(url, requestOptions);
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
