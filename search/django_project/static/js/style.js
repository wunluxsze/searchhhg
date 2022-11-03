
let watch = document.getElementById('watch');

   watch.innerText = (new Date()).toLocaleTimeString('en-GB');

   setInterval(function() {
   watch.innerText = (new Date()).toLocaleTimeString('en-GB');
   },1000);

