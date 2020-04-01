$(document).ready(function(){
    var form = $('#from_buying_product');
    console.log(form);
    form.submit( function(e){
        e.preventDefault();
        var nmb = $('#number').val()

        var submit_btn = $('#submit_btn')
        var product_id = submit_btn.data("product_id")
        var product_name = submit_btn.data("product_name")
        alert(product_id+' '+product_name);
    })

});