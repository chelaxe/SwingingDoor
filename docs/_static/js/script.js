jQuery(function($){
    $(function(){
        $("a.reference > img")
            .parents("a")
                .removeClass("reference");
    });
});
