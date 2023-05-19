const legendTips = {
    "MHHW": "Mean Higher High Water",
    "NFHL100": "FEMA 100-year Flood",
    "CAT1": "Category-1 Hurricane",
    "CAT2": "Category-2 Hurricane",
    "CAT3": "Category-3 Hurricane",
    "CAT5": "Category-5 Hurricane"
};

const legendPopup = (item) => {
    "use strict";

    item.addEventListener('mouseover', (event) => {
        // Get the element that triggered the event
        const hoveredElement = event.target;
        const parentElement = hoveredElement.parentNode;

        const popup = document.createElement('div');
        popup.setAttribute('id', 'legend_popup');
        popup.textContent = legendTips[parentElement.children[0].innerHTML];
        popup.classList.add('popup');

        const parentPos = parentElement.getBoundingClientRect();
        const popupMessageTop = parentPos.top - 10;
        const popupMessageLeft = parentPos.left + parentPos.width + 5;
        popup.style.top = `${popupMessageTop}px`;
        popup.style.left = `${popupMessageLeft}px`;
        document.body.appendChild(popup);
    });

    item.addEventListener("mouseout", () => {
        const popup = document.getElementById("legend_popup");
        document.body.removeChild(popup);
    });
};

const sliderPopup = (item) => {
    "use strict";

    item.addEventListener('mouseover', (event) => {
        // Get the element that triggered the event
        const hoveredElement = event.target;

        const popup = document.createElement('div');
        popup.setAttribute('id', 'slider_popup');
        popup.textContent = legendTips[hoveredElement.innerHTML];
        popup.classList.add('popup');

        const popup_hidden_span = document.createElement('span');
        popup_hidden_span.style.visibility = "hidden";
        popup_hidden_span.innerHTML = popup.textContent;
        document.body.appendChild(popup_hidden_span);

        const hoveredPos = hoveredElement.getBoundingClientRect();
        const popupMessageTop = hoveredPos.top - 10;
        const popupMessageLeft = hoveredPos.left - hoveredPos.width - popup_hidden_span.offsetWidth;
        document.body.removeChild(popup_hidden_span);

        popup.style.top = `${popupMessageTop}px`;
        popup.style.left = `${popupMessageLeft}px`;
        document.body.appendChild(popup);
    });

    item.addEventListener("mouseout", () => {
        const popup = document.getElementById("slider_popup");
        document.body.removeChild(popup);
    });
};

const addListeners = () => {
    "use strict";
    const lineChart = document.getElementById("line-chart");
    const legendItems = lineChart.getElementsByClassName("traces");

    for (let i = 0; i < legendItems.length; i++) {
        legendPopup(legendItems[i]);
    }

    const ySlider = document.getElementById("map-y-slider");
    const marks = ySlider.getElementsByClassName("rc-slider-mark-text");

    for (let i = 0; i < marks.length; i++) {
        sliderPopup(marks[i]);
    }
};
