const form = document.getElementById("form");
const command = document.getElementById("command");

document.addEventListener('DOMContentLoaded', function() {
    getStartingInfo("/on_load").then(commands => {
        commands.forEach((command) => {addElement(command)});
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

async function getStartingInfo(url) {
    const requestOptions = {
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    };
    try {
        const response = await fetch(url, requestOptions);
        return await response.json();
    } catch (e) {
        addElement(`ERROR: ${e}`);
    }
}

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
        return await response.json();
    } catch (e) {
        addElement(`ERROR: ${e}`);
    }
}

function addElement(text) {
    const output = document.getElementById('outputs');

    const newElement = document.createElement('div');
    newElement.setAttribute("class", "output");

    newElement.innerHTML = text;

    output.appendChild(newElement);
}
