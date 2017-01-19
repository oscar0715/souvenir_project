$(document).ready(function () {

	// add active to side navbar li
	var url = window.location.pathname;
	$('#profile_nav a').filter(function() {
		 return this.pathname === url;
	}).addClass('active');
});