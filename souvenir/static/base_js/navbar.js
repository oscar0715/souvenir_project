(function($) {
	$(function() {
		$('.dropdown-button').dropdown({
		      inDuration: 300,
		      outDuration: 225,
		      hover: true, // Activate on hover
		      belowOrigin: true, // Displays dropdown below the button
		      alignment: 'right' // Displays dropdown with edge aligned to the left of button
		    }
		  );
	}); // End Document Ready
})(jQuery); // End of jQuery name space


$('.button-collapse').sideNav({
		menuWidth: 150, // Default is 300
		closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
		draggable: true // Choose whether you can drag to open on touch screens
	}
);