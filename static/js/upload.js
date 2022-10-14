var file = document.getElementById("myfile")

file.addEventListener("click", alert("Click"))
file.addEventListener("select", alert("select"))



// Example POST method implementation:
async function postData(url = 'https://wwwXX.api2convert.com/v2/dl/webX/upload-base64/abcdd66e-bfb6-4ef3-b443-787131bb84b3', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}




postData("https://schoolhub.elifrankel2.repl.co/make-custom-url-img", { image: file})
  .then((data) => {
    console.log(data); // JSON data parsed by `data.json()` call
  });




