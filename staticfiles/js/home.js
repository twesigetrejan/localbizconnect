$(document).ready(function() {
    var imgIndex = 0; // Current image index
    var images = $('.content .image img'); // Select all images 
    // Function to show the next image
    function showNextImage() {
      images.eq(imgIndex).fadeOut(1000, function() { // Fade out current image
        imgIndex = (imgIndex + 1) % images.length; // Update index
        images.eq(imgIndex).fadeIn(1000); // Fade in next image
      });
    }
  
    // Start the slideshow with an interval
    setInterval(showNextImage, 3000); // Change interval value to adjust time between slides
  });
  