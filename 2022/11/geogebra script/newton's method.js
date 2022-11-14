// https://www.geogebra.org/calculator/hvfzm49w

// Global JavaScript

// 변수 선언, 초기화
// 스크립트로 만든 오브젝트 이름
var createdObjects = [];
// 점 체크박스 눌렀을 때 보이거나 숨길 점 목록
var points = [];
// 선 체크박스 눌렀을 때 보이거나 숨길 선 목록
var lines = [];

// 선, 점 보이기 설정
var showLines = true;
var showPoints = true;

/**
 * 주어진 점을 지나고 곡선에 접하는 접선을 생성
 * @param {string} name 생성할 접선 이름
 * @param {string} point 점 이름
 * @param {string} curve 곡선 이름
 * @returns 오브젝트 생성 성공 여부
 */
function tangentLine(name, point, curve) {
  if (!ggbApplet.evalCommand(`${name}=Tangent(${point},${curve})`)) {
    return false;
  }
  if (!showLines) {
    ggbApplet.setVisible(name, false);
  }
  ggbApplet.setLabelVisible(name, false);
  ggbApplet.setAuxiliary(name, true);
  createdObjects.push(name);
  lines.push(name);
  return true;
}

/**
 * 주어진 점을 지나고 x축에 수직인 직선 생성
 * @param {string} name 생성할 직선 이름
 * @param {string} point 점 이름
 * @returns 오브젝트 생성 성공 여부
 */
function vLine(name, point) {
  if (!ggbApplet.evalCommand(`${name}=PerpendicularLine(${point},xAxis)`)) {
    return false;
  }
  if (!showLines) {
    ggbApplet.setVisible(name, false);
  }
  ggbApplet.setLabelVisible(name, false);
  ggbApplet.setAuxiliary(name, true);
  createdObjects.push(name);
  lines.push(name);
  return true;
}

/**
 * 주어진 곡선의 x절편 생성
 * @param {string} name 생성할 점 이름
 * @param {string} obj 곡선 이름
 * @returns 오브젝트 생성 성공 여부
 */
function xIntercept(name, obj) {
  if (!ggbApplet.evalCommand(`${name}=Intersect(${obj},xAxis)`)) {
    return false;
  }
  ggbApplet.setVisible(name, false);
  ggbApplet.setLabelVisible(name, false);
  ggbApplet.setAuxiliary(name, true);
  createdObjects.push(name);
  return true;
}

/**
 * 주어진 두 오브젝트의 교점을 생성
 * @param {string} name 생성할 점 이름
 * @param {string} obj1 첫 번째 오브젝트
 * @param {string} obj2 두 번째 오브젝트
 * @returns 오브젝트 생성 성공 여부
 */
function intersect(name, obj1, obj2) {
  if (!ggbApplet.evalCommand(`${name}=Intersect(${obj1},${obj2})`)) {
    return false;
  }
  if (!showPoints) {
    ggbApplet.setVisible(name, false);
    ggbApplet.setLabelVisible(name, false);
  }
  ggbApplet.setAuxiliary(name, true);
  createdObjects.push(name);
  points.push(name);
  return true;
}

/**
 * x_{n} 텍스트 설정
 */
function setXText() {
  const i = ggbApplet.getValue('i');
  const x = ggbApplet.getXcoord(`A_${i}`);
  ggbApplet.setTextValue('text2', `x_${i}=${x.toFixed(6)}`);
}

/**
 * 초기화
 */
function ggbOnInit() {
  createdObjects = [];
  points = [];
  lines = [];
  setXText();
  ggbApplet.setValue('점', true);
  ggbApplet.setValue('선', true);
}

// Reset button (On Click)
(() => {
  // 생성한 오브젝트 전부 삭제
  createdObjects.map((name) => {
    ggbApplet.deleteObject(name);
  });

  // 변수 초기화
  createdObjects = [];
  points = [];
  lines = [];
  ggbApplet.setValue('i', 0);
  setXText();
})();

// Iterate button (On CLick)
(() => {
  // 뉴턴 방법 적용, i 증가
  const i = ggbApplet.getValue('i');
  tangentLine(`t_{${i}}`, `A_{${i}}`, 'f');
  xIntercept(`x_{${i}}`, `t_{${i}}`);
  vLine(`v_{${i}}`, `x_{${i}}`);
  intersect(`A_{${i + 1}}`, `v_{${i}}`, 'f');
  ggbApplet.setValue('i', i + 1);
  setXText();
})();

// Line checkbox (On Update)
(() => {
  // 선 보이기 설정 변경
  showLines = ggbApplet.getValue('선');
  lines.map((name) => {
    ggbApplet.setVisible(name, showLines);
  });
})();

// Point checkbox (On Update)
(() => {
  // 점 보이기 설정 변경
  showPoints = ggbApplet.getValue('점');
  points.map((name) => {
    ggbApplet.setVisible(name, showPoints);
    ggbApplet.setLabelVisible(name, showPoints);
  });
})();

// A_0 (On Update)
(() => {
  // x_{n} 텍스트 업데이트
  setXText();
})();
