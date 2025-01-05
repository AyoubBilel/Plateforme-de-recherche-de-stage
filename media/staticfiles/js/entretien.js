let recognition;
let recognizing = false;

if ('webkitSpeechRecognition' in window) {
    recognition = new webkitSpeechRecognition();
    recognition.continuous = true;  // Reconnaissance vocale continue
    recognition.interimResults = false;
    recognition.lang = 'fr-FR';

    recognition.onstart = function() {
        recognizing = true;
    };

    recognition.onresult = function(event) {
        let transcript = event.results[event.results.length - 1][0].transcript;
        document.getElementById('response').value += ' ' + transcript;
    };

    recognition.onerror = function(event) {
        console.error(event.error);
    };

    recognition.onend = function() {
        recognizing = false;
    };
}

function startRecognition() {
    if (!recognizing) {
        recognition.start();
    }
}

function stopRecognition() {
    if (recognizing) {
        recognition.stop();
    }
}

function submitResponse() {
    document.getElementById('response-form').submit();
}
