(() => {
    return new Promise((resolve) => {
        let lastText = "";
        let stableCount = 0;

        function getLatestResponseText() {
            const responseDivs = document.querySelectorAll('div.markdown.prose');
            const lastDiv = responseDivs[responseDivs.length - 1];
            return lastDiv?.innerText.trim() || "";
        }

        function checkIfStable() {
            const currentText = getLatestResponseText();

            if (currentText === lastText) {
                stableCount++;
            } else {
                stableCount = 0;
                lastText = currentText;
            }

            if (stableCount >= 2) {
                clearInterval(intervalId);
                resolve(currentText);
            }
        }

        // Start checking after a short delay
        setTimeout(() => {
            intervalId = setInterval(checkIfStable, 1000);
        }, 1000);

        let intervalId;
    });
})();
