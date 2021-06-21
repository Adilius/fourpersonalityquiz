
var visitorId = undefined

window.onload = function initFingerprintJS() {
    // Initialize an agent at application startup.
    fpPromise = FingerprintJS.load()
    console.log("FingerprintJS initialized")


    var visitorId;
    // Get the visitor identifier when you need it.
    fpPromise
    .then(fp => fp.get())
    .then(result => {
        // This is the visitor identifier:
        visitorId = result.visitorId
        console.log(visitorId)
        add_payload(visitorId)
    })

}

function add_payload(visitorId){
    console.log("Add Payload")
    quiz_element = document.getElementById('quiz')
    hiddenInput = document.createElement('input');
    hiddenInput.type = 'hidden';
    hiddenInput.name = "visitorId";
    hiddenInput.value = visitorId;
    quiz_element.appendChild(hiddenInput);
}