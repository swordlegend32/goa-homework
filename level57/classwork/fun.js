
const Btn = document.getElementById('btn1');

let debounce = false;

Btn.addEventListener('mouseover', function() {
    if(debounce) return; 
    debounce = true;    
    const RandomPosition = Math.floor(Math.random() * window.innerWidth - 150);
    const RandomPosition2 = Math.floor(Math.random() * window.innerHeight - 150);

    Btn.style.left = RandomPosition + 'px';
    Btn.style.bottom = RandomPosition2 + 'px';
    Btn.style.position = 'absolute';

    debounce = false;

});