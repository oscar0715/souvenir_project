$(document).ready(function() {
	$('select').material_select();
});


$('#non_field_errors_div').change(function(){
	Materialize.toast(this.html(), 4000);
})