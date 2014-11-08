function setupSocketIO() {
	socket = io.connect('http://' + document.domain + ':' + location.port);
	socket.on('lcd_text', function(msg) {
		if (msg['data']) {
			banner = "<div class='alert alert-success alert-dismissable fade in' role='alert'><button type='button' class='close' data-dismiss='alert'><span aria-hidden='true'>&times;</span><span class='sr-only'>Close</span></button>Your Message was Successfully Changed!</div>";
		}
		else {
			banner = "<div class='alert alert-danger alert-dismissable fade in' role='alert'><button type='button' class='close' data-dismiss='alert'><span aria-hidden='true'>&times;</span><span class='sr-only'>Close</span></button>Your Message was too Long. Change it, then try Again!</div>";
		}
		$('#placeholder').html(banner);
		
		window.setTimeout(function() {
          $('.alert').alert('close');
        }, 3000);
	});

	socket.on('last_message', function(msg) {
		$('#lcd_text').val(msg['data']);
	});

	socket.emit('connect');
}

function sendFormData() {
	socket.emit('lcd_text', {data: $('#lcd_text').val()});
}