# LightsaberScoring_GalacticSaber
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <link rel="stylesheet" href="style.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  
  <title>Galactic Saber Match Scoring</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
    }
    .scoreButton {
      background-color: #000000;
      color: white;
      font-size: 2vw;
      border-width: 1px;
      border-style: solid;
      border-color: white;
      height: 24%;
      width: 100%;
      margin-bottom: 1px
    }
    .column {
      float: left;
      width: 18.75%;
      height: 100vh;
      background-color: #4D578E;
    }
    .scoreColumn {
      float: left;
      width: 18.75%;
      height: 100vh;
      padding-right: 1vw;
      padding-left: 1vw;
      background-color: #000000;
      color: lavender;
    }
    .middleColumn {
      float: left;
      width: 25%;
      height: 100vh;
    }
    .row {
      height: 100vh;
      width: 100vw;
      margin-left: auto;
      margin-right: auto;
      display: table;
      clear: both;
    }
    .bigText {
      margin-top: 0%;
      text-align: center;
      font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
      font-size: 18vh;
      color: #7e3e98;
    }
    .suddenDeathText {
      width: 100%;
      font-family: Impact;
      font-size: 4vw;
      color: red;
      text-align: center;
      position: relative;
      top: 40%;
    }
    .playerTag {
      position: relative;
      margin-top: 0%;
      padding-top: 5vh;
      padding-bottom: 5vh;
      width: 100%;
      background-color: #b7b7b7;
      color: #000000;
      text-align: center;
      font-size: 3.6vw;
      font-family: Comic Sans MS;
    }
    .plusMinusButton {
      padding: 0;
      vertical-align: center;
      height: 15%;
      width: 9vw;
      margin-bottom: 3vh;
      background-color:#666666;
      border-color:black;
      font-family: Impact;
      font-size:11vh;
      vertical-align:middle;
      text-align:center;

    }
    .timerButton {

      margin-top: 2vh;
      margin-left: 1vw;
      margin-right: 1vw;
      height: 10vh;
      position: relative;
      width: 10vw;
      font-size: 6vh;
    }
    .modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    padding-top: 100px; /* Location of the box */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
    }

/* Modal Content */
  .modal-content {
    background-color: #fefefe;
    margin: auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
  }

  /* The Close Button */
  .close {
    color: #aaaaaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
  }

  .close:hover,
  .close:focus {
    color: #000;
    text-decoration: none;
    cursor: pointer;
  }
    #sillyFoulBox:hover {
      background-color: #66307b;
    }


  </style>
</head>
<body>
  <div class="row">
    <div class="scoreColumn">
      <div class="scoreButton" style="border-color: #000000;"><h1 id="p1score" class="bigText" style="position:relative; top: 10%;">00</h1></div>
      <button type="button" id="p15" onclick="p1Plus(5)" class="btn btn-primary scoreButton">Head or Torso</button>
      <button type="button" id="p13" onclick="p1Plus(3)" class="btn btn-primary scoreButton">Arms or Legs</button>
      <button type="button" id="p11" onclick="p1Plus(1)" class="btn btn-primary scoreButton">Hands or Hilt </button>
    </div>
  
    <div class="column" id="column">
      <h2 class="playerTag">Player One</h2>
      <div style="text-align: center;">
        <button type="button" id="p1-" onclick="p1Plus(-1)" class="btn btn-primary plusMinusButton" style="background-color:#666666; color:#ffffff; border-color:black; font-family: Impact; font-size:11vh; display:inline-block;">-</button>
        <button type="button" id="p1+" onclick="p1Plus(1)" class="btn btn-primary plusMinusButton" style="background-color:#666666; color:#ffffff; border-color:black; font-family: Impact; font-size:11vh; display:inline-block;">+</button>
      </div>
      <!-- heres the foul code -->
      <div class="dropup" style="width:100%; height: 62vh; position:relative; bottom: 1vh;">
        <div class="panel" id="fouls" data-toggle="collapse" href="#collapse2" style="background-color:#7e3e98;">
          <div id="sillyFoulBox" onclick="stop()" class="panel-heading">
            <h4 class="panel-title" style="text-align: center;">
              <p class="text" id="foulsText" style="font-family: Comic Sans MS; font-size: 3vw; top:4px; position:relative; color: black;">Fouls</p>
            </h4>
          </div>
          <div id="collapse2" class="panel-collapse collapse">
            <ul class="list-group">
              <a href="#" onclick="whiteFoul(1)" id="p1WhiteFoul" class="list-group-item" style="background-color: white; height:12.5vh; text-align: right;">0</a>
              <a href="#" onclick="yellowFoul(1)" id="p1YellowFoul" class="list-group-item" style="background-color: yellow; height:12.5vh; text-align: right;">0</a>
              <a href="#" onclick="redFoul(1)" id="p1RedFoul" class="list-group-item" style="background-color: red; height:12.5vh; text-align: right;">0</a>
              <a href="#" onclick="blackFoul(1)" id="p1BlackFoul" class="list-group-item" style="background-color: black; height:12.5vh; text-align: right;">0</a>
            </ul>
          </div>
          <div id="white1Modal" class="modal">
            <!-- Modal content -->
            <div class="modal-content">
              <span class="close">&times;</span>
              <p><b>Technical offense on the part of one or both combatants calling for an interruption of combat. A verbal warning is issued and will remain valid for the duration of the current match.</b></p>
              <p>Exiting the combat arena without authorization.</p>
              <p>Counter-attack.</p>
              <p>Corps à corps in order to avoid a touch.</p>
              <p>Covering/switching target area.</p>
              <p>Heavy touch.</p>
              <p>Excessive interruptions of combat.</p>
              <p>Gear not up to regulation standards.</p>
              <p>Non-presentation to the sparring area when called by the referee, after 3 calls separated by an interval of 1 minute.</p>
              <p>Unwarranted complaint.</p>
              <p>Refusal to comply.</p>
              <p>Involuntary exit from the arena.</p>
            </div>
          </div>
          <div id="yellow1Modal" class="modal">
            <!-- Modal content -->
            <div class="modal-content" style="background-color:yellow;">
              <span class="close">&times;</span>
              <b>Verbal warning with a penalty valid for the current match. The offending party's opponent is awarded 3 points. A second offense results in a red foul.</b>
              <p><br>Violent, vindictive or dangerous behavior.</p>
              <p>Shoving, disorganized actions, taking off one's mask before the referee's “Halt!” command.</p>
              <p>Asking for an interruption on the pretext of an unconfirmed injury.</p>
              <p>Thrusting touch.</p>
              <p>Touch landed with excessive force, or during or after a fall.</p>
              <p>Voluntary exit from the arena.</p>
              <p>Using the non-sword hand or arm.</p>
            </div>
          </div>
          <div id="red1Modal" class="modal" style="color: white;">
            <!-- Modal content -->
            <div class="modal-content" style="background-color: red;">
              <span class="close">&times;</span>
              <b>Penalty, the offending party's opponent is awarded 5 points. A second offense results in a red foul.</b>
              <p><br>Unsportsmanlike behavior during combat.</p>
              <p>Combatant disrupting order in the sparring area.</p>
              <p>Starting the combat before the “Fight!” command given by the referee.</p>
              <p>Keeping on fighting aSer the “Halt!” command given by the referee.</p>
              <p>Disruption of order in the sparring area by any individual.</p>
            </div>
          </div>
          <div id="black1Modal" class="modal">
            <!-- Modal content -->
            <div class="modal-content" style="background-color:black; color:white;">
              <span class="close">&times;</span>
              <b>The offending party is excluded from the competion.</b>
              <p><br>Intentional brutality.</p>
              <p>Offense against the spirit of fair play and sportsmanship.</p>
              <p>Fixing the outcome of a combat, losing intentionally, and/or gaining benefits from such collusion.</p>
              <p>Refusal to spar against any officially registered combatant.</p>
            </div>
          </div>
        </div>
      </div>
      
    </div>
    
    <div class="middleColumn" id="middleColumn" style="background-color:#212c68;">

      <!-- Timer Code Goes Here -->
        <div style="width: 100%; height:40vh; background-color: #000000; position: relative; top: 0px">
          <div style="text-align: center;">
            <button id="start" onclick="start()" class="btn btn-primary timerButton" style="background-color: #b7b7b7; color:#7e3e98; border-color:black; font-family: Impact; text-align: center; padding: 3px; vertical-align:middle; display:inline-block;">▶</button>
            <button id="stop" onclick="stop()" type="button" class="btn btn-primary timerButton" disabled="true" style="background-color: #b7b7b7; color:#7e3e98; border-color:black; font-family: Impact; font-weight:bolder; text-align: center; padding: 5px; vertical-align:middle; display:inline-block;">l l</button>
            <div style="text-align: center;">
              <span><h3 id="mins" style="font-family: Impact; font-size: 18vh; color:#7e3e98; display:inline-block;">3:</h3></span>
              <span><h3 id="seconds" style="font-family: Impact; font-size: 18vh; color:#7e3e98; display:inline-block;">00</h3></span>
            </div>
          </div>
        </div>

      <img src="\static\matchscoring\images\GSLogo.png" alt="gsLogo" id="gsLogo" style="position: relative; top:5%; border-style: solid; border-color: white; width: 25vw; height: 40vh;">
      <h1 id="SuddenDeath" class="suddenDeathText" style="display: none; font-family: Impact; font-size:7vw; text-align:center; position:relative; top:5%;">SUDDEN <br> DEATH</h1>

      <button type="reset" id="reset" onclick="reset()" class="btn btn-primary" style="position: relative; bottom: -6vh; left:6.5vw; width:48%; height: 14%; background-color:#666666; border-color:black; font-family: Impact; font-size: 7vh;">End</button>
    </div>

    <div class="column" id="column2" style="background-color:#4D578E;">
      <h2 class="playerTag">Player Two</h2>

      <!-- <button type="button" onclick="p2Plus(1)" class="btn btn-primary plusMinusButton"> <img src="/static\matchscoring\images\image.png" alt="+1"></button>
      <button type="button" onclick="p2Plus(-1)" class="btn btn-primary plusMinusButton"> <img src="/static\matchscoring\images\image.png" alt="-1"></button> -->
      <div style="text-align: center;">
        <button type="button" id="p2+" onclick="p2Plus(1)" class="btn btn-primary plusMinusButton" style="background-color:#666666; color:#ffffff; border-color:black; font-family: Impact; font-size:11vh; display:inline-block;">+</button>
        <button type="button" id="p2-" onclick="p2Plus(-1)" class="btn btn-primary plusMinusButton" style="background-color:#666666; color:#ffffff; border-color:black; font-family: Impact; font-size:11vh; display:inline-block;">-</button>
      </div>
      
      <!-- heres the foul code -->
      <div class="dropup" style=" width:100%; height: 62vh; position:relative; bottom: 1vh;">
        <div class="panel" id="fouls2" data-toggle="collapse" href="#collapse1" style="background-color:#7e3e98;">
          <div id="sillyFoulBox" onclick="stop()" class="panel-heading">
            <h4 class="panel-title" style="text-align: center;">
              <p class="text" id="fouls2Text" style="font-family: Comic Sans MS; font-size: 3vw; top:4px; position:relative; color: black;">Fouls</p>
            </h4>
          </div> 
          <div id="collapse1" class="panel-collapse collapse">
            <ul class="list-group">
              <a href="#" onclick="whiteFoul(2)"  id="p2WhiteFoul"  class="list-group-item" style="background-color: white;  height:12.5vh;">0</a>
              <a href="#" onclick="yellowFoul(2)" id="p2YellowFoul" class="list-group-item" style="background-color: yellow; height:12.5vh;">0</a>
              <a href="#" onclick="redFoul(2)"    id="p2RedFoul"    class="list-group-item" style="background-color: red;    height:12.5vh;">0</a>
              <a href="#" onclick="blackFoul(2)"  id="p2BlackFoul"  class="list-group-item" style="background-color: black;  height:12.5vh;">0</a>
            </ul>
          </div>
          <div id="white2Modal" class="modal">
            <!-- Modal content -->
            <div class="modal-content">
              <span class="close">&times;</span>
              <b>Technical offense on the part of one or both combatants calling for an interruption of combat. A verbal warning is issued and will remain valid for the duration of the current match. A second offense results in a yellow foul.</b>
              <p><br>Exiting the combat arena without authorization.</p>
              <p>Counter-attack.</p>
              <p>Corps à corps in order to avoid a touch.</p>
              <p>Covering/switching target area.</p>
              <p>Heavy touch.</p>
              <p>Excessive interruptions of combat.</p>
              <p>Gear not up to regulation standards.</p>
              <p>Non-presentation to the sparring area when called by the referee, after 3 calls separated by an interval of 1 minute.</p>
              <p>Unwarranted complaint.</p>
              <p>Refusal to comply.</p>
              <p>Involuntary exit from the arena.</p>
            </div>
          </div>
          <div id="yellow2Modal" class="modal">
            <!-- Modal content -->
            <div class="modal-content" style="background-color:yellow;">
              <span class="close">&times;</span>
              <b>Verbal warning with a penalty valid for the current match. The offending party's opponent is awarded 3 points. A second offense results in a red foul.</b>
              <p><br>Violent, vindictive or dangerous behavior.</p>
              <p>Shoving, disorganized actions, taking off one's mask before the referee's “Halt!” command.</p>
              <p>Asking for an interruption on the pretext of an unconfirmed injury.</p>
              <p>Thrusting touch.</p>
              <p>Touch landed with excessive force, or during or after a fall.</p>
              <p>Voluntary exit from the arena.</p>
              <p>Using the non-sword hand or arm.</p>
            </div>
          </div>
          <div id="red2Modal" class="modal" style="color: white;">
            <!-- Modal content -->
            <div class="modal-content" style="background-color:red;">
              <span class="close">&times;</span>
              <b>Penalty, the offending party's opponent is awarded 5 points. A second offense results in a red foul.</b>
              <p><br>Unsportsmanlike behavior during combat.</p>
              <p>Combatant disrupting order in the sparring area.</p>
              <p>Starting the combat before the “Fight!” command given by the referee.</p>
              <p>Keeping on fighting aSer the “Halt!” command given by the referee.</p>
              <p>Disruption of order in the sparring area by any individual.</p>
            </div>
          </div>
          <div id="black2Modal" class="modal">
            <!-- Modal content -->
            <div class="modal-content" style="background-color:black; color:white;">
              <span class="close">&times;</span>
              <b>The offending party is excluded from the competion.</b>
              <p><br>Intentional brutality.</p>
              <p>Offense against the spirit of fair play and sportsmanship.</p>
              <p>Fixing the outcome of a combat, losing intentionally, and/or gaining benefits from such collusion.</p>
              <p>Refusal to spar against any officially registered combatant.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="scoreColumn" style="background-color:rgb(0, 0, 0);
    color:lavender">
      <div class="scoreButton" style="border-color: #000000;"><h1 id="p2score" class="bigText" style="position:relative; top: 10%;">00</h1></div>

      <button type="button" id="p25" onclick="p2Plus(5)" class="btn btn-primary scoreButton">Head or Torso</button>
      <button type="button" id="p23" onclick="p2Plus(3)" class="btn btn-primary scoreButton">Arms or Legs</button>
      <button type="button" id="p21" onclick="p2Plus(1)" class="btn btn-primary scoreButton">Hands or Hilt </button>
    </div>

    </div>
  </div>

  <script>
    // var fontize = $("#title").css("font-size");
    // var i = 0/*remove unit from integer*/
    // while($("#container").find("span").width() > $("#container").width()) {
    // var currentFontSize = parseInt($("#container").find("span").css("font-size")); 
    // $("#container").find("span").css("font-size",currentFontSize-1); 
    // }

    // Start of ScoreKeeping Code
    var playerOneScore=00
    var playerTwoScore=00
    function p1Plus(amount) {
        playerOneScore+= amount;
        // if/else here helps to always keep the display two digits,
        if ((playerOneScore < 10) && (playerOneScore >= 0)) {
          document.getElementById('p1score').innerHTML= "0" + playerOneScore;
        }
        else {
          document.getElementById('p1score').innerHTML= playerOneScore;
        }
        suddenDeathCheck()
        winCheck()

        if (amount < 0) {
          if (playerOneScore < 10) {
            undoSuddenDeath();
          }
        }
    }
    function p2Plus(amount) {
        playerTwoScore+= amount;
        // if/else here helps to always keep the display two digits
        if ((playerTwoScore < 10) && (playerTwoScore >= 0)) {
          document.getElementById('p2score').innerHTML= "0" + playerTwoScore;
        }
        else {
          document.getElementById('p2score').innerHTML= playerTwoScore;
        }
        suddenDeathCheck()
        winCheck()

        if (amount < 0) {
          if (playerTwoScore < 10) {
            undoSuddenDeath();
          }
        }
    }
    function winCheck() {
      if (playerOneScore >= 15) {
        stop()
      }
      if (playerTwoScore >= 15) {
        stop()
      }
    }
    function suddenDeathCheck() {
        if ((playerOneScore >= 10) && (playerTwoScore >= 10)) {
          document.getElementById("column").style.backgroundColor="red";
          document.getElementById("column2").style.backgroundColor="red";
          document.getElementById("fouls").style.backgroundColor="black";
          document.getElementById("fouls2").style.backgroundColor="black";
          document.getElementById("middleColumn").style.backgroundColor="black";
          document.getElementById("start").style.backgroundColor="#666666";
          document.getElementById("stop").style.backgroundColor="#666666";
          
          document.getElementById("foulsText").style.color="red";
          document.getElementById("fouls2Text").style.color="red";
          document.getElementById("mins").style.color="red";
          document.getElementById("p1+").style.color="black";
          document.getElementById("p1-").style.color="black";
          document.getElementById("p1score").style.color="red";
          document.getElementById("p2+").style.color="black";
          document.getElementById("p2-").style.color="black";
          document.getElementById("p2score").style.color="red";
          document.getElementById("seconds").style.color="red";
          document.getElementById("start").style.color="black";
          document.getElementById("stop").style.color="black";

          document.getElementById("p11").disabled=true;
          document.getElementById("p13").disabled=true;
          document.getElementById("p21").disabled=true;
          document.getElementById("p23").disabled=true;
          
          document.getElementById("gsLogo").style.display="none";
          document.getElementById("SuddenDeath").style.display="block";
        }
    }
    function undoSuddenDeath() {
          document.getElementById("column").style.backgroundColor="#4D578E";
          document.getElementById("column2").style.backgroundColor="#4D578E";
          document.getElementById("fouls").style.backgroundColor="#7e3e98";
          document.getElementById("fouls2").style.backgroundColor="#7e3e98";
          document.getElementById("middleColumn").style.backgroundColor="#212c68";
          document.getElementById("start").style.backgroundColor="#b7b7b7";
          document.getElementById("stop").style.backgroundColor="#b7b7b7";
          
          document.getElementById("foulsText").style.color="black";
          document.getElementById("fouls2Text").style.color="black";
          document.getElementById("mins").style.color="#7e3e98";
          document.getElementById("p1+").style.color="white";
          document.getElementById("p1-").style.color="white";
          document.getElementById("p1score").style.color="#7e3e98";
          document.getElementById("p2+").style.color="white";
          document.getElementById("p2-").style.color="white";
          document.getElementById("p2score").style.color="#7e3e98";
          document.getElementById("seconds").style.color="#7e3e98";
          document.getElementById("start").style.color="#7e3e98";
          document.getElementById("stop").style.color="#7e3e98";

          document.getElementById("p11").disabled=false;
          document.getElementById("p13").disabled=false;
          document.getElementById("p21").disabled=false;
          document.getElementById("p23").disabled=false;
          
          document.getElementById("gsLogo").style.display="block";
          document.getElementById("SuddenDeath").style.display="none";
    }
    function alerthehe() {
      alert("yippee!");
    }
    
    // End of ScoreKeeping Code
    
    // Start of Foul Code
    var p1white = 0;
    var p1yellow = 0;
    var p1red = 0;
    var p1black = 0;

    var p2white = 0;
    var p2yellow = 0;
    var p2red = 0;
    var p2black = 0;
    
    function whiteFoul(playerNumber) { // white ?
      if (playerNumber == 1) {
        p1white++;
        document.getElementById('p1WhiteFoul').innerHTML= p1white;
      }
      else if (playerNumber == 2) {
        p2white++;
        document.getElementById('p2WhiteFoul').innerHTML= p2white;
      }
    }
    function yellowFoul(playerNumber) { // Yellow +3 opp
      if (playerNumber == 1) {
        p1yellow++;
        document.getElementById('p1YellowFoul').innerHTML= p1yellow;
        p2Plus(3)
      }
      else if (playerNumber == 2) {
        p2yellow++;
        document.getElementById('p2YellowFoul').innerHTML= p2yellow;
        p1Plus(3)
      }
    }
    function redFoul(playerNumber) { // Red +5 opp
      if (playerNumber == 1) {
        p1red++;
        document.getElementById('p1RedFoul').innerHTML= p1red;
        p2Plus(5)
      }
      else if (playerNumber == 2) {
        p2red++;
        document.getElementById('p2RedFoul').innerHTML= p2red;
        p1Plus(5)
      }
    }
    function blackFoul(playerNumber) { // black should ask for confirmation and then just end the game
      if (playerNumber == 1) {
        p1black++;
        document.getElementById('p1BlackFoul').innerHTML= p1black;
        reset()
      }
      else if (playerNumber == 2) {
        p2black++;
        document.getElementById('p2BlackFoul').innerHTML= p2black;
        reset()
      }
    }
    
    // Get the modal
    var modal = document.getElementsByClassName('modal');

    // Get the button that opens the modal
    var btn = document.getElementsByClassName("list-group-item");


    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close");

    // When the user clicks the button, open the modal 
    btn[0].onclick = function() {
        modal[0].style.display = "block";
    }

    btn[1].onclick = function() {
        modal[1].style.display = "block";
    }

    btn[2].onclick = function() {
        modal[2].style.display = "block";
    }

    btn[3].onclick = function() {
        modal[3].style.display = "block";
    }

    btn[4].onclick = function() {
        modal[4].style.display = "block";
    }

    btn[5].onclick = function() {
        modal[5].style.display = "block";
    }

    btn[6].onclick = function() {
        modal[6].style.display = "block";
    }

    btn[7].onclick = function() {
        modal[7].style.display = "block";
    }
    // When the user clicks on <span> (x), close the modal
    span[0].onclick = function() {
        modal[0].style.display = "none";
    }

    span[1].onclick = function() {
        modal[1].style.display = "none";
    }

    span[2].onclick = function() {
        modal[2].style.display = "none";
    }

    span[3].onclick = function() {
        modal[3].style.display = "none";
    }

    span[4].onclick = function() {
        modal[4].style.display = "none";
    }

    span[5].onclick = function() {
        modal[5].style.display = "none";
    }

    span[6].onclick = function() {
        modal[6].style.display = "none";
    }
    
    span[7].onclick = function() {
        modal[7].style.display = "none";
    }
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal[0]) {
            modal[0].style.display = "none";
        }
        if (event.target == modal[1]) {
            modal[1].style.display = "none";
        } 
        if (event.target == modal[2]) {
            modal[2].style.display = "none";
        }
        if (event.target == modal[3]) {
            modal[3].style.display = "none";
        } 
        if (event.target == modal[4]) {
            modal[4].style.display = "none";
        }
        if (event.target == modal[5]) {
            modal[5].style.display = "none";
        }
        if (event.target == modal[6]) {
            modal[6].style.display = "none";
        }  
        if (event.target == modal[7]) {
            modal[7].style.display = "none";
        }
    }
    
    // End of Foul Code
    
    // Timer Code
  
  var mins =3;
  var seconds =0;

  function start() {
    startTimer();
    document.getElementById('stop').disabled=false;

  }

  function stop() {
    document.getElementById('start').disabled=false;
    document.getElementById('stop').disabled=true;

    clearTimeout(timex);
    clearTimeout(timex);
    clearTimeout(timex);
  }
  
  function reset() {
    document.getElementById('start').disabled=false;
    
    clearTimeout(timex);
    clearTimeout(timex);
    clearTimeout(timex);
    
      mins =3;      
      seconds =0;
      playerOneScore = 0;
      playerTwoScore = 0;

      p1black = 0;

      
    $('#mins').html('3:');
    $('#seconds').html('00');
    $('#p1score').html('00');
    $('#p2score').html('00');

    undoSuddenDeath();
  }

  // everytime this function runs: seconds goes down by one, then it calls itself again
  function startTimer(){ 
    document.getElementById("start").disabled=true;

    
    timex = setTimeout(function(){
      seconds--;
      if(seconds < 0) {
        seconds=59; // converts one minute to 60 seconds
        mins--;     
        if(mins<0) { // doesn't run?
          mins=0;hours--;
          clearInterval(timex);
          clearTimeout(timex);
          clearTimeout(timex);
          clearTimeout(timex);
        }
        if(mins<10) {
          $("#mins").text(mins+':'); // changes display
        }
        else {
          $("#mins").text(mins+':'); // changes display
        }
      }
      if(seconds <10) {
        $("#seconds").text('0'+seconds); // changes display
      } 
      else {
        $("#seconds").text(seconds); // changes display
      }
  
        startTimer(); // calls itself to ensure timer keeps running
    },1000); // delay between calling itself again
  }

  </script>
  
</body>
</html>


