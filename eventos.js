var teclas = {
  UP: 38,
  DOWN: 40,
  LEFT: 37,
  RIGHT: 39
};
console.log(teclas);
document.addEventListener("keyup", dibujarTeclado);
var cuadrito= document.getElementById("area");
var papel= cuadrito.getContext("2d");
var x=150;
var y=150;

dibujarLinea("black",x-1,y-1,x+1,y+1,papel);

function dibujarLinea(color,xinicial,yinicial,xfinal,yfinal,lienzo){
    lienzo.beginPath();
    lienzo.strokeStyle=color;
    lienzo.moveTo(xinicial,yinicial);
    lienzo.lineTo(xfinal,yfinal);
    lienzo.stroke();
    lienzo.closePath();
    lienzo.lineWidth=3;




}

function dibujarTeclado(evento) {
    var colorcito="pink";
    var movimiento=10;
  switch (evento.keyCode) {
    case teclas.UP:
      dibujarLinea(colorcito,x,y,x,y-movimiento,papel);
      y=y-movimiento;
      break;
    case teclas.DOWN:
        dibujarLinea(colorcito,x,y,x,y+movimiento,papel);
        y=y+movimiento;
      break;
    case teclas.LEFT:
        dibujarLinea(colorcito,x,y,x-movimiento,y,papel);
        x=x-movimiento;
      break;
    case teclas.RIGHT:
        dibujarLinea(colorcito,x,y,x+movimiento,y,papel);
        x=x+movimiento;
      break;
    default:
      console.log("Otra tecla");
  }
}
