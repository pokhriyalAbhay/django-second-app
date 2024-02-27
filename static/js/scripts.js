document.addEventListener("DOMContentLoaded", function() {
   gsap.to("#every", {duration: 2, 
        x: 200,
        delay:1,
       repeat: -1,
        yoyo:2,
      opacity: 0
    });
   
});
document.addEventListener("DOMContentLoaded", function() {
    gsap.to("#head1", {duration: 2, 
         y: 200,
         yoyo: 2,
         delay:4,
         repeat: -1,
       opacity: 0
     });
    
 });
 
 