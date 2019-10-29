$(function () {
    jQuery.each($('[data-load]'), function () {
        // this refers to the element
        $(this).load("/templates/" + $(this).data("load"))
    })
})