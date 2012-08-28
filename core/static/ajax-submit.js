"use strict;";

var AJAXSubmit = function () {
    if (!$) {
        var $ = django.jQuery;
    }

    function ajax_submit(e) {
        e.preventDefault();

        var data = {
            // Don't forget the CSRF middleware token!
            "csrfmiddlewaretoken": $("input[name='csrfmiddlewaretoken']").val(),
            "abreviatura": $("input#id_abreviatura").val(),
            "descricao": $("input#id_descricao").val()
        };

        $.ajax({
            type: "POST",
            url: "",
            data: data,
            success: function() {
                alert("Saved!");
            }
        });

        return false;
    }

    $(document).ready(function() {
        var btn = $("div.submit-row input[name='_continue']");
        btn.click(ajax_submit);
    });
}();