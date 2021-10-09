$("form[name=signup_form]").submit(function(e){

    var $form = $(this);
    var $error = $form.find(".error");
    var dtaa = $form.serialize();

    $.ajax({
        url: "/user/signup",
        type: "POST",
        data: data,
        datatype: "json",
        success: function(resp){
            window.location.href = "index/";
        },
        error: function(resp){
            console.log(resp);
            $error.text(resp.response.JSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault();
});