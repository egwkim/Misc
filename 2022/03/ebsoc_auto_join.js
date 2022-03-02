/* 사용법
 * 
 * ebs 온클 접속하여 우리 학교 -> 해당 반 검색 (2반)
 * 코드를 복사해서 개발자도구에 붙여넣기 후 엔터
 * joinAll(); 입력 후 엔터
 * 반 선택하기
 * 
 * 혹시 선택하지 말아야 할 반 있다면 아래 button.splice 주석 해제하고
 * 2 대신에 알아서 인덱스 찾아서 넣기 (알아서)
 * 
 * 
 * 테스트한 환경
 * Windows 10
 * Chrome
**/

const buttons = Array.from(document.querySelectorAll('#page > div.page_schoolmain > div.sec.sec_school_search > div > div > ul > li > div.right > div > span > a'));
// buttons.splice(2,1);

function timeout(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function delayedClick(element) {
	element.click();
	await timeout(500);
}

async function delayedClickSelector(selector) {
	await delayedClick(document.querySelector(selector));
}

async function join(element) {
	await delayedClick(element);
	await new Promise(resolve => setTimeout(resolve, 3500));
	await delayedClickSelector('#learningTargetSelect > div.popup_area > div > div.btn_area > a.btn.btn_md.btn_keycolor');
	await delayedClickSelector('#confirmPop > div.popup_area > div > div.btn_area > a.btn.btn_md.btn_keycolor');
	await delayedClickSelector('#alertPop > div.popup_area > div > div.btn_area > a');
}

async function joinAll() {
	for (const btn of buttons) {
		await join(btn);
	}
}
