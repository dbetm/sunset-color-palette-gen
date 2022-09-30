function componentToHex(codeH) {
    var hex = codeH.toString(16);
    return hex.length == 1 ? "0" + hex : hex;
}


function rgbStringToArray(rgbStr) {
    /* Convert an RGB string, for example: 'rgb(0, 35, 62)' to an array of
    integers, example: [0, 35, 62]
    */
    let tmpArr = rgbStr.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/).splice(1, 3);
    return tmpArr.map(function(item) {
        return parseInt(item, 10);
    });
}

function rgbToHex(red, green, blue) {
    return (
        "#"
        + componentToHex(red)
        + componentToHex(green)
        + componentToHex(blue)
    );
}
