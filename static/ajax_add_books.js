var TEST
var A_clear_book_detail_block //A jquery object
function create_isbn_select(Identifier_type){
    var isbn_select = "";
    isbn_select += '<select name="identifier">\n';
    isbn_select += '<option value="ISBN_13" ' + (Identifier_type == "ISBN_13" ? 'selected' : "") + '>ISBN_13</option>\n';
    isbn_select += '<option value="ISBN_10" ' + (Identifier_type == "ISBN_10" ? 'selected' : "") + '>ISBN_10</option>\n';
    isbn_select += '<option value="ISSN" ' + (Identifier_type == "ISSN" ? 'selected' : "") + '>ISSN</option>\n';
    isbn_select += '</select>';
    return isbn_select
}
function isbn_to_book_detail_ajax(){
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
            for(var i = 0;i < response["TotalItems"];i++ )
            {
                E = response["items"][i];
                /*
                display_item = A_clear_book_detail_block;
                display_item.find("#title").val(E["title"]);
                display_item.find("#subtitle").val(E["subtitle"]);
                display_item.appendTo("body");
                */
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
                    display_item.push('<span class="remove-author remove">✗</span> <br>')
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
                    display_item.push('<span class="remove-identifier remove">✗</span> <br>')
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
}

$(document).ready(function(){
    A_clear_book_detail_block = $(".book-detail-block").clone();
    $("#isbn-input").focus();
    $("#sent-isbn").click(function(){
        isbn_to_book_detail_ajax();
    });
    $("#isbn-input").keypress(function(keyin){
        if(keyin.which == 13){
            isbn_to_book_detail_ajax();
            return false;
        }
    });
    $(document).on("click","#add-new-authors",function(event){
        event.preventDefault();
        var new_author_item = $(".author-item:first").clone();
        new_author_item.find(":input").val("");
        $(this).parent().find(".authors-container").append(new_author_item);
    });
    $(document).on("click","#add-new-identifier",function(event){
        event.preventDefault();
        var new_identifier_item = $(".identifier-item:first").clone();
        new_identifier_item.find(":input").val("");
        $(this).parent().find(".identifier-container").append(new_identifier_item);
    });
    $(document).on("click", ".remove-author", function(event){
        event.preventDefault();
        if($(this.parentElement.parentElement).find(".author-item").length != 1){
            $(this).closest($(this)).parent().remove();
        }
    });
    $(document).on("click", ".remove-identifier", function(event){
        event.preventDefault();
        if($(this.parentElement.parentElement).find(".identifier-item").length != 1){
            $(this).closest($(this)).parent().remove();
        }
    });
});

