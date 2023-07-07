const buttons = document.querySelectorAll('button' )
let slides = document.querySelectorAll('.slide-container')
let menu = document.querySelector('#menu-bar')
let navbar = document.querySelector('.nav-bar')


let index = 0

menu.onclick = () => {
    menu.classList.toggle('fa-times')
    navbar.classList.toggle('active')
}

window.onscroll = () => {
    menu.classList.remove('fa-times')
    navbar.classList.remove('active')
}



buttons.forEach(button =>{
    button.addEventListener('click',()=>{
        const faq = button.nextElementSibling;
        const icon = button.children[1];

        faq.classList.toggle('show');
        icon.classList.toggle('active')
    })
} )

function next(){
    slides[index].classList.remove('active')
    index = (index + 1) % slides.length
    slides[index].classList.add('active')
}

function prev(){
    slides[index].classList.remove('active')
    index = (index - 1 + slides.length) % slides.length
    slides[index].classList.add('active')
}



window.addEventListener('scroll', reveal);

function reveal(){
    var reveals = document.querySelectorAll('.reveal');

    for(var i = 0; i < reveals.length; i++){
        var windowheight = window.innerHeight;
        var revealtop = reveals[i].getBoundingClientRect().top;
        var revealpoint = 150;

        if(revealtop < windowheight - revealpoint){
            reveals[i].classList.add('active');       
        }
        else{
            reveals[i].classList.remove('acive')
        }
    }
}