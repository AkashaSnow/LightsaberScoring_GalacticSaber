var timer;
var timeLeft = 180; // seconds
// What to do when the timer runs out
function gameOver() {

  // re-show the button, so they can start it again
  document.getElementById('playAgainButton').style.visibility = 'visible';}

  function updateTimer() {
  timeLeft = timeLeft - 1;
  if(timeLeft >= 0)
  {
    var time = document.getElementById('timer');
    time.textContent = timeLeft;
  }
  else {
    gameOver();
  }
}
// The button has an on-click event handler that calls this
function start() {
  // setInterval is a built-in function that will call the given function
  // every N milliseconds (1 second = 1000 ms)
  timer = setInterval(updateTimer, 1000);
  // It will be a whole second before the time changes, so we'll call the update
  // once ourselves
  updateTimer();
  // We don't want the to be able to restart the timer while it is running,
  // so hide the button.
   document.getElementById('playAgainButton').style.visibility = 'hidden';
}