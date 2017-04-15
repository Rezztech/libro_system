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
        headers: {
            'X-CSRFToken': Cookies.get('csrftoken')
        },
        data: {
            isbn_input: $("#isbn-input").val().split('\n'),
        },
        error: function() {
            alert("Ajax request error");
        },
        success: function( response ){
            var isbn_result = $('#isbn-result').DataTable();
            for(var i = 0;i < response["TotalItems"];i++ )
            {
                E = response["items"][i];
                if (E['no_found']) {
                    msg += 'book "' + E['title'] + '" not found';
                }
                else {
                    isbn_result.row.add([
                        E['title'],
                        E['subtitle'],
                        E['authors'].join('<br>'),
                        E['publisher'],
                        E['publishedDate'],
                        E['industryIdentifiers'].map(
                            p => p['type'] + ': ' + p['identifier']).join('<br>'),
                        E['description']]);
                }
            }
            isbn_result.draw();
        }
    });
}

/*
function active_remove_click(){
    $(".remove-author").click(function(){
        console.log("YOOOOOOOOOOOOOOOOOOOOO");
        $("this").remove();
    });

}
*/

$(document).ready(function(){
    $("#isbn-input").focus();
    $("#add-books-submit").click(function(e) {
        e.preventDefault();
        isbn_to_book_detail_ajax();
    });
    // $("#isbn-input").keypress(function(keyin){
    //     if(keyin.which == 13){
    //         isbn_to_book_detail_ajax();
    //         return false;
    //     }
    // });
    /* fail
    $(document).on("click", ".remove-author", function(){
        active_remove_click();
        console.log("BYOOOOOOOOOOOOOOOOOOOOO");
        //$(this)
    })
    */
});

