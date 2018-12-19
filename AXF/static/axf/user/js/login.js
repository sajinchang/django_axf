//用户名非空校验
$(function () {
	function empty() {
    $('#error').hide();
			$('#submit').click(function(event){
			    // alert(123);
				var data = $('#inputUsername').val();
				data = $.trim(data);
				if(data.length < 1) {
					$('#error').show();
					event.preventDefault();
					$("#checkusername").text('用户名不能为空').css({color:'pink'})
				} else {
					$('#error').hide();
				}
			});
}

});

