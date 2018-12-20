$(function () {
   $('#alipay').click(function () {
       // alert(123);
      var $btn =  $(this);
      var orderid = $btn.attr('orderid');
      $.getJSON('/app/pay/', {'orderid': orderid}, function (data) {
         console.log(data);
         if (data['code'] === 200){
             window.open('/app/alipay'+ '?orderid=' + orderid,target='_self');

         }
         else
            return false
      });
   });
});