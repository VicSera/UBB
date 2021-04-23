let INITIAL = 0;
let LEFT = INITIAL;
let SPEED = 1;
let lastImageSize = 0;

let slider;
let popupImage;
let popup;

window.onload = main;

function main() {
    slider = $("#slider");
    lastImageSize = $("#slider img:last").width();
    popup = $("#popup");
    popupImage = $("#popup-image");
    INITIAL = -lastImageSize;
    LEFT = INITIAL;

    setInterval(onEachFrame, 10);

    $("#slider img").click(function() {
        // debugger;
        imageClicked($(this));
        console.log("Clicked an image");
    });

    popupImage.click(function () {
        popup.css({
            display: "none"
        });
        SPEED = 1;
    })
}

function onEachFrame() {
    LEFT += SPEED;
    if (LEFT > INITIAL + lastImageSize) {
        LEFT -= lastImageSize;
        $("#slider img:last").prependTo(slider);
        lastImageSize = $("#slider img:last").width();
    }

    slider.css({
        left: LEFT
    });
}

function imageClicked(image) {
    // debugger;
    SPEED = 0;

    popup.css({
        display: "flex"
    })

    const source = image.attr("src");

    popupImage.attr("src", source);
}

