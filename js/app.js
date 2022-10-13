var sunsetInfo;
var currentInfoIndex = -1;

// Entrypoint
window.onload = function() {
    renderCodeColors();

    fetch("assets/sunset_info.json")
        .then(response => response.json())
        .then(json => renderSunsetInfo(json));
};


function renderSunsetInfo(data=null) {
    sunsetInfo = data == null ? sunsetInfo : data;
    currentInfoIndex = (currentInfoIndex + 1) % sunsetInfo.length;

    let infoItem = sunsetInfo[currentInfoIndex];

    document.getElementById("infoTitle").innerHTML = infoItem.title;
    document.getElementById("infoContent").innerHTML = infoItem.content;
}


function copy(spanObj) {
    let input = document.createElement("input");

    let value = spanObj.textContent;
    input.value = value;

    document.body.appendChild(input);
    input.select();
    // copy content
    result = document.execCommand("copy");
	document.body.removeChild(input);

    // Display for 1.2 seconds a label indicating that was copied.
    spanObj.innerHTML = "copied!";

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
