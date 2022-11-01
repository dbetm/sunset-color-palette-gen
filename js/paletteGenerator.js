const NUMBER_COLORS = 4;
const NUM_CHANNELS = 3;


function genPalette() {
    let newColors = selectRandomColorGroup();

    const colorPalette = document.getElementById("colorPalette");
    const colorItems = colorPalette.getElementsByClassName("color-item");

    console.assert(
        newColors.length == NUMBER_COLORS,
        "Number of new generated colors must be: " + NUMBER_COLORS
    );

    for (let i = 0; i < colorItems.length; ++i) {
        let newRGBColor = formatRBGColor(
            newColors[i][0], newColors[i][1], newColors[i][2]
        );
        colorItems[i].style.backgroundColor = newRGBColor;
    }

    renderCodeColors()
}


function selectRandomColorGroup() {
    let numGroupColors = colorData.length;
    let groupIdx = Math.floor(Math.random() * (numGroupColors - 1));
    let groupColor = colorData[groupIdx];
    let newColors = [...Array(NUMBER_COLORS)].map(e => Array(NUM_CHANNELS));

    for(let i = 0; i < NUMBER_COLORS * NUM_CHANNELS; i += 1) {
        let colorIdx = Math.floor(i / 3);
        let channelIdx = i % 3;
        newColors[colorIdx][channelIdx] = [groupColor[i]]
    }

    return newColors;
}
