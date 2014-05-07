window.onload = myMain;

function myMain()
{
    $(document).ready(function(){
      $("#navMenu").slideUp();
      $("#navButton").click(function(){
        var img0 = $("#optionalFeaturedPicture");
        if(img0 != null)
        {
            $("#optionalFeaturedPicture").remove();
        }
        $("#navMenu").slideToggle(function(){
        
            var check=$(this).is(":hidden");
            if(check == true)
            {
                var img = $('<img />').attr({ 'id': 'optionalFeaturedPicture', 'src': 'unibucPic0.jpg', 'alt':'MyAlt' }).appendTo($('#navigationDiv'));
            }
        });
      });
        setFeaturedArticle(); //Link
        setRandomArticle(); //Link
        setOtherArticles();
        setPictures(); //Picture
        greenFunction();
    });

    
}

function greenFunction()
{
       $(document).ready(function() {

        // page is now ready, initialize the calendar...

        $('#calendar').fullCalendar({
            // put your options and callbacks here
        })

    }); 
}

function setPictures()
{
    var picNumber = Math.floor((Math.random()*10)+1) % 3;
    var img = $('<img />').attr({ 'id': 'featuredPicture', 'src': 'unibucPic' + picNumber + '.jpg', 'alt':'MyAlt' }).appendTo($('#navigationDiv'));
}

function setRandomArticle()
{    
    document.getElementById('randomLink').onclick = function()
    {
        var randomArticleChoice = Math.floor((Math.random()*10)+1);
        randomArticleChoice = randomArticleChoice%2;
        document.getElementById('featuredArticleIframe').src = "featuredArticle" + randomArticleChoice + ".html";
        return false;
    };    
}

function setFeaturedArticle()
{
    var minutes = 1000 * 60;
    var hours = minutes * 60;
    var d = new Date();
    var t = d.getTime();

    var h = Math.round(t / hours);
    
    var newSource = "featuredArticle" + h%2 + ".html";
    document.getElementById('featuredArticleIframe').src = newSource;
    
    document.getElementById('returnToFA').onclick = function()
    {
        document.getElementById('featuredArticleIframe').src = newSource;
        return false;
    };
}

function setOtherArticles()
{
    document.getElementById('historyLink').onclick = function()
    {
        document.getElementById('featuredArticleIframe').src = "history.html";
        return false;
    };
    
    document.getElementById('palaceLink').onclick = function()
    {
        document.getElementById('featuredArticleIframe').src = "palace.html";
        return false;
    };   
    
    document.getElementById('lawLink').onclick = function()
    {
        document.getElementById('featuredArticleIframe').src = "law.html";
        return false;
    };       
    
    document.getElementById('cultureLink').onclick = function()
    {
        document.getElementById('featuredArticleIframe').src = "culture.html";
        return false;
    };    
}
