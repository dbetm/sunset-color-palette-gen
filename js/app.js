// Entrypoint
window.onload = function() {
    renderCodeColors();
};


function copy(spanObj) {
    let input = document.createElement("input");

    let value = spanObj.textContent;
    input.value = value;

    document.body.appendChild(input);
    input.select();
    // copy content
    result = document.execCommand("copy");
	document.body.removeChild(input);

    // Display for 1.5 seconds a label indicating that was copied.
    spanObj.innerHTML = "copied +)";

    setTimeout(function() {
        spanObj.innerHTML = value;
    }, 1200);
}

function renderCodeColors() {
    let colorPalette = document.getElementById("colorPalette");
    let colorItems = colorPalette.getElementsByClassName("color-item");

    for(colorItem of colorItems) {
        let styleItem = window.getComputedStyle(colorItem, null);
        let colorCode = styleItem.getPropertyValue("background-color");
        let spanChild = colorItem.getElementsByTagName("span")[0];
        insertColorCode(spanChild, colorCode);
    }
}

function insertColorCode(spanObj, colorCode) {
    let rgbArr = rgbStringToArray(colorCode);
    let hexValue = rgbToHex(rgbArr[0], rgbArr[1], rgbArr[2]);
    spanObj.innerHTML = hexValue;
}
