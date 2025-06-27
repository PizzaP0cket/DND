(async () => {
    const editableDiv = document.querySelector('#prompt-textarea');
    if (!editableDiv) return "Editable input not found.";

    const stripped_prompt = `Your prompt here`;

    editableDiv.innerHTML = `<p>${stripped_prompt}</p>`;

    editableDiv.dispatchEvent(new InputEvent('input', { bubbles: true }));
    editableDiv.dispatchEvent(new Event('blur', { bubbles: true }));

    // Wait 1 second before pressing Enter
    await new Promise(resolve => setTimeout(resolve, 1000));

    const commandEnterEvent = new KeyboardEvent('keydown', {
        bubbles: true,
        cancelable: true,
        key: 'Enter',
        code: 'Enter',
        keyCode: 13,
        which: 13,
        metaKey: true,  // This simulates the Command key on macOS
    });

    editableDiv.dispatchEvent(commandEnterEvent);


    return "Prompt set, waited 1 second, then pressed Enter!";
})();
