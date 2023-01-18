var objetos = document.getElementsByTagName('h1');

objetos[0].innerHTML = 'Mudei com o JS!'

for(var i = 1; i < objetos.length; i++){
    objetos[i].innerHTML = 'Mudei com o JS!' + i;
};


var objetos2 = document.getElementsByTagName('h2')

for(var b = 0; b < 10; b++){
    objetos2[0].innerHTML = objetos2[0].innerHTML + '-bele-';
};