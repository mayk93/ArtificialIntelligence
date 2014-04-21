window.onload = myMain;

function myMain() 
{
    var user        = document.getElementById("inputBox").value;
    var button      = document.getElementById("inputButton");
    
    button.onclick  = function(){startGame(user);}    
}

function getTurn(turnAsNumber)
{
    switch(turnAsNumber%2)
    {
        case 0:
        {
            return "X";
        }
        case 1:
        {
            return "0";
        }
        default:
        {
            return "Error";
        }
    }
}

var turnAsNumber = 0;
var turnAsString = getTurn(turnAsNumber);

function startGame(user)
{
    $('#turnParagraph').text("Turn for: X");
    $('#inputParagraph').text("User: " + user);
    
    for(var i = 0; i <= 8; i++)
    {
        var id = "gameButton" + i;
        var currentButton = document.getElementById(id);
        currentButton.disabled = false;
        currentButton.onclick = function(){mark(this.id);}
    }       
}

function someoneWon()
{ 
    if
    (
    (document.getElementById("gameButton0").innerHTML != "")
    &&
    (document.getElementById("gameButton1").innerHTML != "")
    &&
    (document.getElementById("gameButton2").innerHTML != "")
    )
    {
        if
        ((
        (document.getElementById("gameButton0").innerHTML == document.getElementById("gameButton1").innerHTML)
        &&
        (document.getElementById("gameButton1").innerHTML == document.getElementById("gameButton2").innerHTML)
        ))
        {
            return true;
        }
    }
    
    if
    (
    (document.getElementById("gameButton3").innerHTML != "")
    &&
    (document.getElementById("gameButton4").innerHTML != "")
    &&
    (document.getElementById("gameButton5").innerHTML != "")
    )
    {
        if
        ((
        (document.getElementById("gameButton3").innerHTML == document.getElementById("gameButton4").innerHTML)
        &&
        (document.getElementById("gameButton4").innerHTML == document.getElementById("gameButton5").innerHTML)
        ))
        {
            return true;
        }
    }
    
    if
    (
    (document.getElementById("gameButton6").innerHTML != "")
    &&
    (document.getElementById("gameButton7").innerHTML != "")
    &&
    (document.getElementById("gameButton8").innerHTML != "")
    )
    {
        if
        ((
        (document.getElementById("gameButton6").innerHTML == document.getElementById("gameButton7").innerHTML)
        &&
        (document.getElementById("gameButton7").innerHTML == document.getElementById("gameButton8").innerHTML)
        ))
        {
            return true;
        }
    }
    
    if
    (
    (document.getElementById("gameButton0").innerHTML != "")
    &&
    (document.getElementById("gameButton3").innerHTML != "")
    &&
    (document.getElementById("gameButton6").innerHTML != "")
    )
    {
        if
        ((
        (document.getElementById("gameButton0").innerHTML == document.getElementById("gameButton3").innerHTML)
        &&
        (document.getElementById("gameButton3").innerHTML == document.getElementById("gameButton6").innerHTML)
        ))
        {
            return true;
        }
    }
    
    if
    (
    (document.getElementById("gameButton1").innerHTML != "")
    &&
    (document.getElementById("gameButton4").innerHTML != "")
    &&
    (document.getElementById("gameButton7").innerHTML != "")
    )
    {
        if
        ((
        (document.getElementById("gameButton1").innerHTML == document.getElementById("gameButton4").innerHTML)
        &&
        (document.getElementById("gameButton4").innerHTML == document.getElementById("gameButton7").innerHTML)
        ))
        {
            return true;
        }
    }
    
    if
    (
    (document.getElementById("gameButton3").innerHTML != "")
    &&
    (document.getElementById("gameButton5").innerHTML != "")
    &&
    (document.getElementById("gameButton8").innerHTML != "")
    )
    {
        if
        ((
        (document.getElementById("gameButton3").innerHTML == document.getElementById("gameButton5").innerHTML)
        &&
        (document.getElementById("gameButton5").innerHTML == document.getElementById("gameButton8").innerHTML)
        ))
        {
            return true;
        }
    }
    
    if
    (
    (document.getElementById("gameButton0").innerHTML != "")
    &&
    (document.getElementById("gameButton4").innerHTML != "")
    &&
    (document.getElementById("gameButton8").innerHTML != "")
    )
    {
        if
        ((
        (document.getElementById("gameButton0").innerHTML == document.getElementById("gameButton4").innerHTML)
        &&
        (document.getElementById("gameButton4").innerHTML == document.getElementById("gameButton8").innerHTML)
        ))
        {
            return true;
        }
    }
    
    if
    (
    (document.getElementById("gameButton2").innerHTML != "")
    &&
    (document.getElementById("gameButton4").innerHTML != "")
    &&
    (document.getElementById("gameButton6").innerHTML != "")
    )
    {
        if
        ((
        (document.getElementById("gameButton2").innerHTML == document.getElementById("gameButton4").innerHTML)
        &&
        (document.getElementById("gameButton4").innerHTML == document.getElementById("gameButton6").innerHTML)
        ))
        {
            return true;
        }
    }                    
    
    return false;     
}

function allDisabled()
{
    var numberOfDisabledButtons = 0;
    for(var i = 0; i <= 8; i++)
    {
        var id = "gameButton" + i;
        if(document.getElementById(id).disabled == true)
        {
            numberOfDisabledButtons++;
        }
    }
    
    if(numberOfDisabledButtons == 9)
    {
        return true;
    } 
    
    return false;
}

function disableAll()
{
    for(var i = 0; i<= 8; i++)
    {
        document.getElementById("gameButton" + i).disabled = true;
    } 
}

function update(turnAsNumber)
{
    var turnAsString = getTurn(turnAsNumber);
    $('#turnParagraph').text("Turn for: " + turnAsString);
    
    if(someoneWon() == true)
    {
        disableAll();
        $('#turnParagraph').text("We have a winner: " + turnAsString);
    }
    else
    {
        if(allDisabled() == true)
        {
        $('#turnParagraph').text("Draw.");
        }
    }
}

function mark(id)
{
    turnAsString = getTurn(turnAsNumber);
    turnAsNumber++;

    document.getElementById(id).innerHTML = turnAsString;
    document.getElementById(id).disabled = true;
    
    update(turnAsNumber);
}
