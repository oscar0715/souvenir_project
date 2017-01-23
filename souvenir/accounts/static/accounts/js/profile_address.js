$(document).ready(function() {
	$('select').material_select();
});


$('select').on('contentChanged', function() {
		// re-initialize (update)
		$(this).material_select();
});

$('select').change(function(){
	// alert(this.value)
	if (this.id === "id_user_country" ) {
		getDistrictList("id_user_province",this.value);
		getDistrictList("id_user_city",'0');
		getDistrictList("id_user_district",'0');		
		// if (this.value.valueOf()  === "86".valueOf() ) {
		// 	$('select[name=user_province]').parent().show();
		// 	$('select[name=user_city]').parent().show();
		// 	$('select[name=user_district]').parent().show();
		// } else {
		// 	$('select[name=user_province]').parent().hide();
		// 	$('select[name=user_city]').parent().hide();
		// 	$('select[name=user_district]').parent().hide();
		// }
	} else if (this.id === "id_user_province") {
		getDistrictList("id_user_city",this.value);
		getDistrictList("id_user_district",'0');
	} else if (this.id === "id_user_city")
		getDistrictList("id_user_district",this.value);
});

function getDistrictList(idString,code){ 
	$.ajax({   
		type: "GET",
		url: "/address/getDistrictList?code="+code,       
		dataType:'json',   
		success: function(data,textStatus){
			var select = document.getElementById(idString);
			// for ( var i=select.options.length-1; i>-1; i--){   
			// 	select[i] = null;   
			// }     
			select.options.length = 0
			if(data.length > 0) {
				// $("#id_user_province").show();  
				for ( i=0; i<data.length; i++ ) {   
					select.options[i] = new Option();   
					select.options[i].text = data[i].name;   
					select.options[i].value = data[i].code; 
				}
				// trigger event
					$('#'+idString).trigger('contentChanged');
			}else
				$('#'+idString).hide();  
		}    
	})   
}  

$("#id_user_country").change(function(){
	document.getElementById('id_detail_address').placeholder = "收信地址为其他国家，请在详细地址处写明完整地址。";
});

$('.modal').modal({
		dismissible: false, // Modal can be dismissed by clicking outside of the modal
		opacity: .5, // Opacity of modal background
		in_duration: 300, // Transition in duration
		out_duration: 200, // Transition out duration
		starting_top: '4%', // Starting top style attribute
		ending_top: '10%', // Ending top style attribute
		ready: function(modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.
			// alert("Ready");
			console.log(modal, trigger);
		},
		complete: function() {  } // Callback for Modal close
	}
);

$("#save_button").click(function(){
	$('#address_form').submit();
});

