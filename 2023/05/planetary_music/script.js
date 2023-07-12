const canvas = document.getElementById('canvas');
/** @type {CanvasRenderingContext2D} */
const ctx = canvas.getContext('2d');

let width, height;

resize = () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  width = canvas.width;
  height = canvas.height;
};
window.addEventListener('resize', resize);
resize();

class Sun {
  constructor(r, color, g) {
    this.r = r;
    this.color = color;
    this.x = width / 2;
    this.y = height / 2;
    this.g = g;
  }

  draw() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.r, 0, 2 * Math.PI);
    ctx.closePath();
    ctx.fillStyle = this.color;
    ctx.fill();
  }
}

const frequency_factor = 4;
class Planet {
  constructor(x, y, vx, vy, r, color) {
    this.x = x;
    this.y = y;
    this.vx = vx;
    this.vy = vy;
    this.r = r;
    this.color = color;
    this.vol = new Tone.Volume(-10).toDestination();
    this.osc = new Tone.Oscillator(this.v * frequency_factor).connect(this.vol);
  }

  get v() {
    return Math.sqrt(this.vx ** 2 + this.vy ** 2);
  }

  draw() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.r, 0, 2 * Math.PI);
    ctx.fillStyle = this.color;
    ctx.fill();
  }

  move(dt) {
    this.x += this.vx * dt;
    this.y += this.vy * dt;
    let dx = this.x - sun.x;
    let dy = this.y - sun.y;
    let d2 = dx ** 2 + dy ** 2;
    let d = Math.sqrt(d2);
    let accel = sun.g / d2;
    this.vx -= (accel * dx) * dt / d;
    this.vy -= (accel * dy) * dt / d;
    this.osc.set({ frequency: this.v * frequency_factor });
  }
}

const sun = new Sun(20, '#ffc10788', 3000000);
const planets = [];

gene = [135.5259652603542, 141.80177340729358, 117.64249757691634, 83.7842975500333, 140.67154561572661, 56.7265774905456]

planets.push(new Planet(width / 2, height / 2 + gene[0], gene[1], gene[2], 8, '#007bff'));
planets.push(new Planet(width / 2 + gene[3], height / 2 + gene[4], gene[5], 0, 7, '#7bff00'));

let muted = true;
document.addEventListener('click', () => {
  if (muted) {
    sun.color = '#ffc107';
    muted = false;
    planets.forEach((planet) => {
      planet.osc.start();
    });
  } else {
    sun.color = '#ffc10788';
    muted = true;
    planets.forEach((planet) => {
      planet.osc.stop();
    });
  }
});

let prev_timeStampe;
function render(timeStamp) {
  if (!prev_timeStampe) prev_timeStampe = timeStamp;
  // const dt = (timeStamp - prev_timeStampe) / 1000;
  const dt = 0.01;
  prev_timeStampe = timeStamp;

  ctx.clearRect(0, 0, width, height);
  sun.draw();
  planets.forEach((planet) => {
    planet.draw();
    planet.move(dt);
  });
  requestAnimationFrame(render);
}

requestAnimationFrame(render);
