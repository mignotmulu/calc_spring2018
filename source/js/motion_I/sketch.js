var x = 0;
var y = 0;
var v0 = 3;
var acc = .49; 
var vel = 0;

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  
  ellipse(x, y, 30, 30);
  x += vel;
  y += 0.6*vel;
  vel += acc;
  
  
}