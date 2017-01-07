$(document).ready(function(){ 

	$('.arrow-more a').click(function(e){
		e.preventDefault(); 
		var id = $(this).attr('href'), 
		top = $(id).offset().top; 

		$('body,html').animate({scrollTop: top}, 1500); 
	});
	
});