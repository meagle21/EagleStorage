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
        var clickableElements = document.querySelectorAll('.clickable');
        clickableElements.forEach(function (element) {
          element.addEventListener('click', function () {
            var id = handleClick(element);
            var newUrl = '/' + id;
            console.log(newUrl);
            window.location.href = newUrl;
        });
});});}

function handleClick(element) {
    var figcaptionElement = element.querySelector('figcaption');
    var figcaptionText = figcaptionElement.id.slice(0, -1);
    return figcaptionText;
}

function removeNoneInParenthesis(){
    var elements = document.getElementsByTagName("figcaption");
    for (var i = 0; i < elements.length; i++) {
        elements[i].innerText = elements[i].innerText.replace("(None)", "");
        }
}

function handleTakeToStatsRequest(){
    window.location.href = '/cloud_storage_stats'
}

function updateClassToIncludeDroppable(){
    var elements = document.getElementsByClassName("folder")
    for (var i = 0; i < elements.length; i ++){
        elements[i].className = elements[i].className + ' dropArea';
    }
}

updateClassToIncludeDroppable()
removeNoneInParenthesis();
removeLastBackslash();
addClickListener();

