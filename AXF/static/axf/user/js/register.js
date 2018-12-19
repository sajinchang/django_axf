$(function () {
   var $username = $('#inputUsername');

    // alert(123);
   $username.blur(function () {
      var username= $username.val().trim();
      // if (username == ''){
      //     alert('用户名不能为空')
      //     return false;
      // }

      $.getJSON('/app/checkuser/',
          {'username':username,
          },
          function (data) {
            var status = data['status'];
            if (status == 200){
               $('#checkusername').text('用户名可用').css({color:'green'})
            }
            else{
                $('#checkusername').text('用户名不可用').css({color:'red'})
            }

          }
          )
   });

    //密码验证
    check_password();
    //用户名非空校验
    empty();

});


//密码验证
function check_password() {
    var $password = $('#inputPassword');
    var $confirm = $('#confirmPassword');

    $confirm.blur(function () {
        var password = $password.val();
        var confirm = $confirm.val();
        if (password != confirm){
            $('#checkPassword').text('两次密码不一致!').css({color:'red'});
        }
        else {

            $('#checkPassword').text('');
        }

    })

}

//用户名非空校验
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

