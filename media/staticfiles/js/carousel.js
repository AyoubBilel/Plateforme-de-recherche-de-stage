let slideIndex = 0;
showSlide(slideIndex);

// Définir l'intervalle de temps entre chaque diapositive (en millisecondes)
const interval = 3000;

// Lancer l'autoplay
let timer = setInterval(nextSlide, interval);

// Fonction pour passer à la diapositive suivante automatiquement
function autoPlay() {
    nextSlide();
}

// Fonction pour arrêter l'autoplay lorsqu'on interagit avec les boutons précédent/suivant
function resetTimer() {
    clearInterval(timer);
    timer = setInterval(autoPlay, interval);
}

function nextSlide() {
    resetTimer();
    showSlide(slideIndex += 1);
}

function prevSlide() {
    resetTimer();
    showSlide(slideIndex -= 1);
}

function showSlide(n) {
    let slides = document.getElementsByClassName("carousel-item");
    if (n >= slides.length) {
        slideIndex = 0;
    }
    if (n < 0) {
        slideIndex = slides.length - 1;
    }
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex].style.display = "block";
}
