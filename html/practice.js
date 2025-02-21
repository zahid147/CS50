document.addEventListener('DOMContentLoaded', function(){
    let team1 = 0;
    let team2 = 0;

    document.querySelector('#add1').onclick = function() {
        team1 ++;
        document.querySelector('#score1').innerHTML = team1;
    }

    document.querySelector('#add2').onclick = function() {
        team2 ++;
        document.querySelector('#score2').innerHTML = team2;
    }

    document.querySelector('#reset').onclick = function() {
        team1 = team2 = 0;
        document.querySelector('#score1').innerHTML = team1;
        document.querySelector('#score2').innerHTML = team2;
    }
});