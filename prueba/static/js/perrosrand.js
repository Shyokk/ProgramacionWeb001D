//Necesito las constantes para poder llamar al botón de los perros desde la pagina de perros y el resultado de las imagenes
const dog_btn = document.getElementById('dog_btn');
const dog_result = document.getElementById('dog_result');

//Esto es para que el botón funcione cuando le hagan click
dog_btn.addEventListener('click', getRandomDog);

//Función que me permite obtener las imagenes de perritos
function getRandomDog() {
    //Desde este link obtengo las imagenes random
	fetch('https://random.dog/woof.json')
		.then(res => res.json())
		.then(data => {
            //Esto es para discriminar entre vídeos e imagenes
			if(data.url.includes('.mp4')) {
				getRandomDog();
			}
			else {
				dog_result.innerHTML = `<img src="${data.url}" alt="dog" />`;
			}
		});
}