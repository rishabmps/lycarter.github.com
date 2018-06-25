function initializePhotoswipe() {
	// insert the needed DOM elements
	console.log("initializing photoswipe gallery");

	pswp_internal = document.getElementById('pswp_container_script').innerHTML;

	var gals = document.getElementsByClassName('gallery');

	for (var i = 0; i < gals.length; i++) {
		gals[i].innerHTML = pswp_internal;
	}

	// actually initialize things
	var pswpElement = document.querySelectorAll('.pswp')[0];

	// build items array
	var items = [
	    {
	        src: 'https://placekitten.com/600/400',
	        w: 600,
	        h: 400
	    },
	    {
	        src: 'https://placekitten.com/1200/900',
	        w: 1200,
	        h: 900
	    }
	];

	// define options (if needed)
	var options = {
	    // optionName: 'option value'
	    // for example:
	    index: 0 // start at first slide
	};

	// Initializes and opens PhotoSwipe
	var gallery = new PhotoSwipe( pswpElement, PhotoSwipeUI_Default, items, options);
	gallery.init();
}