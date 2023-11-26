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

function runDropHandler(){
    var elements = document.getElementsByClassName('folder'); // Assign ondrop attribute to each element with the specified classname
    for (i = 0; i < elements.length; i ++) {
        elements[i].ondrop = dropHandler;
        elements[i].ondragover = function(ev) { ev.preventDefault(); };
    };
}

function runHoverHandler(){
    var elements = document.getElementsByClassName('clickable'); // Assign ondrop attribute to each element with the specified classname
    for (i = 0; i < elements.length; i ++) {
        elements[i].onmouseover = hoverHandler;
    };
}

function dropHandler(ev) {
    ev.preventDefault()
    console.log('File dropped!', ev.dataTransfer.files); // Your custom ondrop logic here
}

function hoverHandler(ev){
    ev.preventDefault();
    customMenu.style.left = ev.pageX + 'px'; // Position the custom menu at the mouse coordinates
    customMenu.style.top = ev.pageY + 'px';
    customMenu.style.display = 'block'; // Display the custom menu
    document.addEventListener('click', function () {
        customMenu.style.display = 'none'; // Hide the custom menu when clicking outside of it
    });
}

function handleMenuItemClick(item) {
    var action = item.innerText;
    var filePath = item.className;
    alert(filePath);
    //alert('Do you wish to ' + action + ' ' + filePath + '?');

    // You can add custom logic based on the clicked menu item
    // For example, perform an action associated with the item

    // Hide the custom menu
    customMenu.style.display = 'none';
}

runHoverHandler();
runDropHandler();
removeNoneInParenthesis();
removeLastBackslash();
addClickListener();

