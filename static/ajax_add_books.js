var A_clear_book_detail_block //A jquery object
function isbn_to_book_detail_ajax(){
    $(".book-detail-block").remove();
    $.ajax({
        url: "/add-books-ajax/",
        type: "POST",
        data: {
            isbn_input: $("#isbn-input").val(),
        },
        error: function() {
            alert("Ajax request error");
            var display_item = A_clear_book_detail_block.clone();
            display_item.appendTo("body");
        },
        success: function( response ){
            for(var i = 0;i < response["TotalItems"];i++ )
            {
                E = response["items"][i];
                var display_item = A_clear_book_detail_block.clone();
                display_item.find("#title").val(E["title"]);
                display_item.find("#subtitle").val(E["subtitle"]);
                display_item.find("#publisher").val(E["publisher"]);
                display_item.find("#publisheddate").val(E["publisheddate"]);
                display_item.find("#description").val(E["description"]);
                A_clear_author_item = A_clear_book_detail_block.find(".author-item").clone();
                for(var j in E["authors"]){
                    if(j == 0){
                        display_item.find(".author-item").find(":input").val(E["authors"][j])
                    }
                    else{
                        new_author_item = A_clear_author_item.clone();
                        new_author_item.find(":input").val(E["authors"][j]);
                        new_author_item.appendTo(display_item.find(".authors-container"));
                    }
                }
                A_clear_identifier_item = A_clear_book_detail_block.find(".identifier-item").clone();
                for(var j in E["industryIdentifiers"]){
                    if(j == 0){
                        display_item.find(".identifier-item").find(":input").val(E["industryIdentifiers"][j]["identifier"]);
                    }
                    else{
                        new_identifier_item = A_clear_identifier_item.clone();
                        //failing. so I move select after appendTo
                        new_identifier_item.find(":input").val(E["industryIdentifiers"][j]["identifier"]);
                        new_identifier_item.appendTo(display_item.find(".identifier-container"));
                    }
                }
                display_item.appendTo("body");
                
                //fill up select
                for(var j in E["industryIdentifiers"]){
                    $(".book-detail-block:last").find(".identifier-container").find("select").eq(j).val(E["industryIdentifiers"][j]["type"]);
                }
            }
            if(response["TotalItems"] == 0){
                var display_item = A_clear_book_detail_block.clone();
                display_item.appendTo("body");
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

