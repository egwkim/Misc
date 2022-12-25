// https://geogebra.org/classic/vuzzhz93

// Global JavaScript
function reset () {
    a = ggbApplet.getXcoord('A');
    b = ggbApplet.getXcoord('B');
    ggbApplet.setValue('l', Math.min(a,b));
    ggbApplet.setValue('r', Math.max(a,b));
  }
  
  function ggbOnInit() {}


// A (On Update)
reset();


// B (On Update)
reset();


// Iterate button (On click)
(()=>{
    const signL = Math.sign(ggbApplet.getYcoord('Left'));
    const signR = Math.sign(ggbApplet.getYcoord('Right'));
    const signM = Math.sign(ggbApplet.getYcoord('M'));
    if (signL * signR != -1 || signM == 0) {
      return false;
    }
    
    const x_m = ggbApplet.getValue('x_m');
    if (signL * signM == -1) {
      ggbApplet.setValue('r', x_m);
    } else {
      ggbApplet.setValue('l', x_m);
    }
})();


// Reset button (On click)
reset();

