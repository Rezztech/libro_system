$(document).ready(function(){
    $("#sent-isbn").click(function(){
        $.ajax({
            url: "/add-books-ajax/",
            type: "POST",
            data: {
                isbn_input: $("#isbn-input").val(),
            },
            error: function() {
                alert("Ajax request error");
            },
            success: function( data ){
                alert("Ajax request success");
                var items = [];
                $.each( data, function(key, val){
                    items.push("<li id='" + key + "'>" + val + "</li>");
                });
                $("<ul/>", {
                    "class": "my-new-list",
                    html: items.join("")
                }).appendTo("body");
            }
        });
    });
});

