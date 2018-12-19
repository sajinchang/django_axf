$(function () {
 //购物车中的加减
    $('.addShopping').click(function () {
        // alert(123);
        $add = $(this);
        var goodsid = $add.attr('id');

        $.get('/app/add_cart/', {'goodsid':goodsid,'way':'add'},function (data) {
            console.log(data);
            $add.prev().html(data['goods_num']);
            $('#total_price').text(data['total_price']);
        });
            });
    $('.subShopping').click(function () {
        $sub = $(this);
        var goodsid = $sub.attr('id');
         $.get('/app/add_cart/', {'goodsid':goodsid,'way':'sub'},function (data) {
            console.log(data);
            $sub.next().html(data['goods_num']);
            $('#total_price').text(data['total_price']);
        });

    });


//    单选和取消
    $('.select').click(function () {
        var $select = $(this);
        var cartid = $select.attr('cartid');
        // alert(123);
        
        $.get('/app/select/', {'cartid': cartid}, function (data) {
            if (data['flag']){
                $select.find('span').html('√');
            }
            else{
                $select.find('span').html('');
            }

            $('#total_price').text(data['total_price']);
        })
    });


    //全选和全不选
    $('#select_all').click(function () {
        $select_all = $(this);
        // alert($(this).text());
        if ($select_all.text().trim()){
            $('#all').html('');
            $('.select').find('span').text('');
            select_all('null');
        }
        else {
            $('#all').html('√');
            $('.select').find('span').text('√');
            select_all('all');
        }
    })

});

function select_all(way) {
    $.get('/app/select_all/', {'way': way}, function (data) {

        $('#total_price').text(data['total_price']);
        console.log(data);
    })
}