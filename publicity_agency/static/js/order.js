$(document).ready(function () {
	$('#order-form').submit(function(){
		$('.error-message').remove();
		var submit = true;
		$('.check-item').each(function(){
			var el= $(this);
			if(el.val() === ''){
				el.closest('.form-item').append('<p class="error-message">Veuillez compléter ce champ</p>');
				submit = false;
			}
		});

		return submit;

	});
});