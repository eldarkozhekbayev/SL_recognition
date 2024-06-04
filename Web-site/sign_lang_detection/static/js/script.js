document.getElementById('startButton').addEventListener('click', function() {
    const word = document.getElementById('wordInput').value;
    const language = document.getElementById('languageSelect').value;
    const speed = parseInt(document.getElementById('speedControl').value);
    displaySigns(word, language, speed);
});

function displaySigns(word, language, speed) {
    fetch(`/get_letter_images/?word=${encodeURIComponent(word)}&language=${encodeURIComponent(language)}`)
        .then(response => response.json())
        .then(data => {
            let images = data.images;
            let index = 0;
            let letterContainer = document.getElementById('letterDisplay');
            letterContainer.innerHTML = '';

            function showLetter() {
                if (index < images.length) {
                    const signImage = document.getElementById('signImage');
                    const letterElement = document.createElement('span');
                    letterElement.classList.add('letter');

                    if (images[index] === '-') {
                        letterElement.classList.add('space');
                        letterElement.textContent = ' ';
                        signImage.style.display = 'none';
                    } else {
                        signImage.src = images[index];
                        signImage.style.display = 'block';
                        letterElement.textContent = word[index];
                    }

                    const lastLetterElement = letterContainer.querySelector('.last-letter');
                    if (lastLetterElement) {
                        lastLetterElement.classList.remove('last-letter');
                    }
                    letterElement.classList.add('last-letter');

                    letterContainer.appendChild(letterElement);

                    const delay = (11 - speed) * 100;

                    index++;
                    setTimeout(showLetter, delay);
                }
            }

            showLetter();
        });
}
