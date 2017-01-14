$(document).ready(function() {
	$('select').material_select();
});

$('select').on('contentChanged', function() {
    // re-initialize (update)
    $(this).material_select();
});

$('select').change(function(){
	// alert(this.value)
	if (this.id === "id_post_country" ) {
		getDistrictList("id_post_province",this.value);
		getDistrictList("id_post_city",'0');
		getDistrictList("id_post_district",'0');		
		if (this.value.valueOf()  === "86".valueOf() ) {
			$('select[name=post_province]').parent().show();
			$('select[name=post_city]').parent().show();
			$('select[name=post_district]').parent().show();
		} else {
			$('select[name=post_province]').parent().hide();
			$('select[name=post_city]').parent().hide();
			$('select[name=post_district]').parent().hide();
		}
	} else if (this.id === "id_post_province") {
		getDistrictList("id_post_city",this.value);
		getDistrictList("id_post_district",'0');
	} else if (this.id === "id_post_city")
		getDistrictList("id_post_district",this.value);
});

function getDistrictList(idString,code){ 
	$.ajax({   
		type: "GET",
		url: "/posts/getDistrictList?code="+code,       
		dataType:'json',   
		success: function(data,textStatus){
			var select = document.getElementById(idString);
			// for ( var i=select.options.length-1; i>-1; i--){   
			// 	select[i] = null;   
			// }     
			select.options.length = 0
			if(data.length > 0) {
				// $("#id_post_province").show();  
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

