$(function () {
    jQuery.each($('[data-load]'), function () {
        // this refers to the element
        $(this).load("/pages/" + $(this).data("load"))
    })
})