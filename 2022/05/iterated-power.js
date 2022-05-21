// https://www.geogebra.org/calculator/ktqrj8sf

var i = 0;

function ggbOnInit() {
  ggbApplet.registerObjectUpdateListener("Iterate", "iterate");
}

function iterate() {
  ggbApplet.evalCommand("l_" + i + "=PerpendicularLine(A_" + i + ",yAxis)");
  ggbApplet.setVisible("l_" + i, false);
  if (!ggbApplet.isDefined("l_" + i)) {
    return 0;
  }

  ggbApplet.evalCommand("B_" + i + "=Intersect(l_" + i + ",g)");
  ggbApplet.setLabelVisible("B_" + i, false);
  if (!ggbApplet.isDefined("B_" + i)) {
    return 0;
  }

  ggbApplet.evalCommand("s_" + i + "=Segment(A_" + i + ",B_" + i + ")");
  ggbApplet.setLabelVisible("s_" + i, false);
  if (!ggbApplet.isDefined("s_" + i)) {
    return 0;
  }

  ggbApplet.evalCommand("m_" + i + "=PerpendicularLine(B_" + i + ",xAxis)");
  ggbApplet.setVisible("m_" + i, false);
  if (!ggbApplet.isDefined("m_" + i)) {
    return 0;
  }

  ggbApplet.evalCommand("A_" + (i + 1) + "=Intersect(m_" + i + ",f)");
  ggbApplet.setLabelVisible("A_" + (i + 1), false);
  if (!ggbApplet.isDefined("A_" + i)) {
    return 0;
  }

  ggbApplet.evalCommand("t_" + i + "=Segment(A_" + (i + 1) + ",B_" + i + ")");
  ggbApplet.setLabelVisible("t_" + i, false);
  if (!ggbApplet.isDefined("t_" + i)) {
    return 0;
  }

  i++;
}
