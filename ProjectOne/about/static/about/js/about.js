var canPlay = false;
var v = document.createElement('video');
if(v.canPlayType && v.canPlayType('video/mp4').replace(/no/, '')) {
    canPlay = true;
}

console.log(canPlay);


document.addEventListener('DOMContentLoaded', () =>{
    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    
    })

  })

  window.addEventListener('resize', function(event){
     let mediaQuery = window.matchMedia( "(min-width: 1000px)" );
     adjustSkillIcons(mediaQuery);
  });
  /**
   * 
   * @param {*} mediaQuery - media query concern with matches to see if window width is desired size
   */
  let iconSet = document.getElementById("skill-icon");
  let adjustSkillIcons = (mediaQuery) =>{
      /**
       * If The Screen is Large Enough And The Container is empty add the icon set to the container
       */
        
        if (mediaQuery.matches && !document.getElementById("container-large-screen").contains(iconSet)) {
            iconSet.parentElement.removeChild(iconSet);
            document.getElementById("container-large-screen").appendChild(iconSet);

        }
        else if (!mediaQuery.matches && !document.getElementById("container-smaller-screen").contains(iconSet)){
            iconSet.parentElement.removeChild(iconSet);
            document.getElementById("container-smaller-screen").appendChild(iconSet);
        }

  }