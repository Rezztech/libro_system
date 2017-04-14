var TEST
function create_isbn_select(Identifier_type){
    var isbn_select = "";
    isbn_select += '<select name="identifier">\n';
    isbn_select += '<option value="ISBN_13" ' + (Identifier_type == "ISBN_13" ? 'selected' : "") + '>ISBN_13</option>\n';
    isbn_select += '<option value="ISBN_10" ' + (Identifier_type == "ISBN_10" ? 'selected' : "") + '>ISBN_10</option>\n';
    isbn_select += '<option value="ISSN" ' + (Identifier_type == "ISSN" ? 'selected' : "") + '>ISSN</option>\n';
    isbn_select += '</select>';
    return isbn_select
}

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
            success: function( response ){
                TEST = response;
                for(var i = 0;i < response["TotalItems"];i++ )
                {
                    E = response["items"][i];
                    var display_item = [];
                    display_item.push("title : ");
                    display_item.push('<input type="text" name="title" value="' + E["title"] + '"> <br>');
                    display_item.push("subtitle : ");
                    display_item.push('<input type="text" name="subtitle" value="' + E["subtitle"] + '"> <br>');
                    display_item.push("authors : ");
                    display_item.push('add');
                    display_item.push('<br>');
                    for (var j in E["authors"]){
                        display_item.push('<input type="text" name="author" value="' + E["authors"][j] + '">');
                    display_item.push('X<br>');
                    }
                    display_item.push("publisher : ");
                    display_item.push('<input type="text" name="publisher" value="' + E["publisher"] + '"> <br>');
                    display_item.push("publisheddate : ");
                    display_item.push('<input type="text" name="publisheddate" value="' + E["publishedDate"] + '"> <br>');
                    display_item.push("identifier : ");
                    display_item.push('add');
                    display_item.push('<br>');
                    for(var j in E["industryIdentifiers"])
                    {
                        display_item.push(create_isbn_select(E["industryIdentifiers"][j]["type"]))
                        display_item.push('<input type="text" name="" value="' + E["industryIdentifiers"][j]["identifier"] + '">');
                        display_item.push('X<br>')
                    }
                    display_item.push("description : ");
                    display_item.push('<input type="textarea" name="description" value="' + E["description"] + '"> <br>');

                    $("<div/>", {
                    "class": "my-new-book-detail",
                    html: display_item.join("")
                    }).appendTo("body");
                }
            }
        });
    });
});

