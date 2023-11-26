function removeLastBackslash() {
    var elements = document.getElementsByTagName("figcaption");
    for (var i = 0; i < elements.length; i++) {
        var elementInnerText = elements[i].innerText;
        if(elementInnerText.includes('/')){
            elements[i].innerText = elementInnerText.replace(/\//g, '');
        }
    }
}

function addClickListener() {
    document.addEventListener('DOMContentLoaded', function () {
        // Get all elements with the "clickable" class
        var clickableElements = document.querySelectorAll('.clickable');
      
        // Add click event listener to each element
        clickableElements.forEach(function (element) {
          element.addEventListener('click', function () {
            var innerText = handleClick(element);
            var newUrl = '/' + innerText;
            console.log(newUrl);
            window.location.href = newUrl;
        });
});});}

function handleClick(element) {
    var figcaptionElement = element.querySelector('figcaption');
    var figcaptionText = figcaptionElement.innerText.split(' ')[0];
    return figcaptionText;
}

removeLastBackslash();
addClickListener();
handleClick(element);
