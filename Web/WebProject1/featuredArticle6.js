window.onload = myMain;

function myMain()
{
    $(document).ready(function(){
      map = new GMaps({
        div: '#map',
        lat: 44.435481,
        lng: 26.102527,
        enableNewStyle: true
      });
    });
}
