const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

function resizeCvs() {
  canvas.setAttribute('width', window.innerWidth - 10);
  canvas.setAttribute('height', window.innerHeight - 10);
}

window.onresize = resizeCvs;

resizeCvs();
