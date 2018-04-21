function getTotalCharacters() {
    var texts = document.getElementById("styled").value;
    var printLength = document.getElementById("totalChars");
    printLength.innerHTML = 'Total Characters Remaining: '+String(300 - texts.length);
}

