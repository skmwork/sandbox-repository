function basketUpdating(data, url, csrf_token){
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        dataType: 'JSON',
        success: function(json) {
            console.log(json.basket_products)
            if(json.basket_products.total_price){
                $('#basket_total_price').text("("+json.basket_products.total_price.replace(".", ",")+")")
                arr = json.basket_products.products;
                $('.basket-items').html('');
                console.log(arr)
                if(arr.length>0){
                    arr.forEach(function(item, i, arr) {
                        $('.basket-items').append('<li class="dropdown-item">'+item.name+', '+item.nmb+'шт. по '+item.price.replace(".", ",")+'р.'
                        +'<a class="delete" href="/" data-product_in_basket_id="'+item.id+'">x</a></li>')
                    });
                }
                else{
                    $('.basket-items').append('<li class="dropdown-item">Корзина пуста<li>')
                }
            }

        },
        error: function(xhr, ajaxOptions, thrownError) {
            console.log(thrownError + "\r\n" + xhr.statusText + "\r\n" + xhr.responseText)
        }
    });

}

$(document).ready(function(){
    var form = $('#buy_product');
    form.submit( function(e){
        e.preventDefault();
        var nmb = $('#number').val()
        var csrf_token = $('#csrf_token [name="csrfmiddlewaretoken"]').val()
        var submit_btn = $('#submit_btn')
        var product_id = submit_btn.data("product_id")
        console.log(product_id)
        var url = form.attr("action");
        var data = {}
        data.product_id = product_id;
        data.nmb = nmb;
        data['csrfmiddlewaretoken'] = csrf_token;
        basketUpdating(data, url, csrf_token)
    })
});

function toggleDropdown (e) {
  const _d = $(e.target).closest('.dropdown'),
    _m = $('.dropdown-menu', _d);
  setTimeout(function(){
    const shouldOpen = e.type !== 'click' && _d.is(':hover');
    _m.toggleClass('show', shouldOpen);
    _d.toggleClass('show', shouldOpen);
    $('[data-toggle="dropdown"]', _d).attr('aria-expanded', shouldOpen);
  }, e.type === 'mouseleave' ? 300 : 0);
}

$('body')
  .on('mouseenter mouseleave','.dropdown',toggleDropdown)
  .on('click', '.dropdown-menu a', toggleDropdown);

$(document).on('click', '.delete', function(e) {
   e.preventDefault();
   var csrf_token = $('#csrf_token [name="csrfmiddlewaretoken"]').val()
   var product_in_basket_id = $(this).data("product_in_basket_id")
   var url = '/order/delete_product_from_basket';
   var data = {}
   data.product_in_basket_id = product_in_basket_id;
   data.csrfmiddlewaretoken = csrf_token;
   basketUpdating(data, url, csrf_token)
});