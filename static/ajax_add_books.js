var TEST
$(document).ready(function(){
    $("#sent-isbn").click(function(){
        $(".my-new-book-detail").remove();
        $.ajax({
            url: "/add-books-ajax/",
            type: "POST",
            data: {
                isbn_input: $("#isbn-input").val(),
            },
            error: function() {
                alert("Ajax request error");
            },
            /*
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
            */
            success: function( response ){
                TEST = response;
                for(var i = 0;i < response["TotalItems"];i++ )
                {
                    console.log(i);
                    E = response["items"][i];
                    var display_item = [];
                    display_item.push("title : ");
                    display_item.push('<input type="text" name="title" value="' + E["title"] + '"> <br>');
                    display_item.push("subtitle : ");
                    display_item.push('<input type="text" name="subtitle" value="' + E["subtitle"] + '"> <br>');
                    display_item.push("authors : ");
                    for (var j in E["authors"]){
                    display_item.push('<input type="text" name="author" value="' + E["authors"][j] + '"> <br>');
                    }
                    display_item.push("publisher : ");
                    display_item.push('<input type="text" name="publisher" value="' + E["publisher"] + '"> <br>');
                    display_item.push("publisheddate : ");
                    display_item.push('<input type="text" name="publisheddate" value="' + E["publishedDate"] + '"> <br>');
                    display_item.push("identifier : ");
                    //display_item.push('<input type="text" name="" value="' +  + '"> <br>');
                    display_item.push('<br>');
                    display_item.push("description : ");
                    display_item.push('<input type="text" name="description" value="' + E["description"] + '"> <br>');

                    $("<div/>", {
                    "class": "my-new-book-detail",
                    html: display_item.join("")
                    }).appendTo("body");
                }
            }
        });
    });
});

