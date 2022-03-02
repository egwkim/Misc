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

const buttons = Array.from(document.querySelectorAll('#page > div.page_schoolmain > div.sec.sec_school_search > div > div > ul > li > div.right > div > span > a'));
buttons.splice(2,1);

async function joinAll() {
	for (const btn of buttons) {
		await join(btn);
	}
}