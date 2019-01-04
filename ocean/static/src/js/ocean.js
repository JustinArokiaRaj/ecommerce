$(document).ready(function(){

	$('#head1').click(function(){
		alert('Header 1 Works ..!!!');
	});
	$('.counter').each(function () {
    $(this).prop('Counter',0).animate({
        Counter: $(this).text()
    }, {
        duration: 4000,
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
    });
});

});