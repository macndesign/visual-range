$(document).ready(function(){

    var REST_APP = {};

    REST_APP.document = $(document);
    REST_APP.list_render = $('#notes');
    REST_APP.all_fields = $('.field');

    // fields
    REST_APP.id = $('#id');
    REST_APP.content = $('#content');
    REST_APP.is_active = $('#is_active');
    REST_APP.title = $('#title');
    REST_APP.slug = $('#slug');
    REST_APP.user = $('#user');

    // buttons
    REST_APP.list = $('#list');
    REST_APP.new = $('#new');
    REST_APP.detail = $('#detail');
    REST_APP.edit = $('#edit');
    REST_APP.delete = $('#delete');

    REST_APP.reset_form = function () {
        REST_APP.all_fields.val('');
    };

    REST_APP.get_list = function () {
        // request ajax
        REST_APP.request = $.ajax({
            url: '/api/v1/notes/?format=json',
            type: 'GET'
        });
        // request done
        REST_APP.request.done(function(data){
            REST_APP.list_render.html('');
            $().toastmessage('showNoticeToast', "Dados atualizados");
            var objects = data.objects;
            for (var i = 0; i < objects.length; i ++) {
                REST_APP.list_render.append('<li>' + objects[i].id + ' - ' + objects[i].title + '</li>');
            }
        });
        // request fail
        REST_APP.request.fail(function(jqXHR, textStatus){
            $().toastmessage('showErrorToast', "Get list request failed: " + textStatus);
        });
    };

    REST_APP.get_item = function () {
        // request ajax
        REST_APP.request = $.ajax({
            url: '/api/v1/notes/' + REST_APP.id.val() + '/?format=json',
            type: 'GET'
        });
        // request done
        REST_APP.request.done(function(data){
            $().toastmessage('showSuccessToast', "Dados carregados com sucesso!");
            REST_APP.content.val(data.content);
            REST_APP.is_active.val(data.is_active);
            REST_APP.title.val(data.title);
            REST_APP.slug.val(data.slug);
            REST_APP.user.val('/api/v1/users/' + data.user.id + '/');
        });
        // request fail
        REST_APP.request.fail(function(jqXHR, textStatus){
            $().toastmessage('showErrorToast', "Get item request failed: " + textStatus);
        });
    };

    REST_APP.delete_item = function () {
        // request ajax
        REST_APP.request = $.ajax({
            url: '/api/v1/notes/' + REST_APP.id.val() + '/',
            type: 'DELETE'
        });
        // request done
        REST_APP.request.done(function(data){
            $().toastmessage('showSuccessToast', "Item excluído com sucesso!");
            // reset and listing after delete
            REST_APP.reset_form();
            REST_APP.get_list();
        });
        // request fail
        REST_APP.request.fail(function(jqXHR, textStatus){
            $().toastmessage('showErrorToast', "Delete item request failed: " + textStatus);
        });
    };

    REST_APP.post_data = function () {
        // form data
        REST_APP.data = JSON.stringify({
            "content": REST_APP.content.val(),
            "is_active": REST_APP.is_active.val(),
            "title": REST_APP.title.val(),
            "slug": REST_APP.slug.val(),
            "user": REST_APP.user.val()
        });
        // request ajax
        REST_APP.request = $.ajax({
            url: '/api/v1/notes/',
            data: REST_APP.data,
            type: 'POST',
            contentType: 'application/json'
        });
        // request done
        REST_APP.request.done(function(data){
            $().toastmessage('showSuccessToast', "Item salvo com sucesso!");
            // listing after post
            REST_APP.get_list();
        });
        // request fail
        REST_APP.request.fail(function(jqXHR, textStatus){
            $().toastmessage('showErrorToast', "Post data request failed: " + textStatus);
        });
    };

    REST_APP.edit_item = function () {
        // form data
        REST_APP.data = JSON.stringify({
            "content": REST_APP.content.val(),
            "is_active": REST_APP.is_active.val(),
            "title": REST_APP.title.val(),
            "slug": REST_APP.slug.val(),
            "user": REST_APP.user.val()
        });
        // request ajax
        REST_APP.request = $.ajax({
            url: '/api/v1/notes/' + REST_APP.id.val() + '/',
            data: REST_APP.data,
            type: 'PUT',
            contentType: 'application/json'
        });
        // request done
        REST_APP.request.done(function(data){
            $().toastmessage('showSuccessToast', "Item alterado com sucesso!");
            // listing after edit
            REST_APP.get_list();
        });
        // request fail
        REST_APP.request.fail(function(jqXHR, textStatus){
            $().toastmessage('showErrorToast', "Edit item request failed: " + textStatus);
        });
    };

    // listing
    REST_APP.document.on('click', '#' + REST_APP.list.attr('id'), function () {
        REST_APP.get_list();
    });

    // posting
    REST_APP.document.on('click', '#' + REST_APP.new.attr('id'), function () {
        REST_APP.post_data();
    });

    // deleting
    REST_APP.document.on('click', '#' + REST_APP.delete.attr('id'), function () {
        REST_APP.delete_item();
    });

    // getting
    REST_APP.document.on('click', '#' + REST_APP.detail.attr('id'), function () {
        REST_APP.get_item();
    });

    // editing
    REST_APP.document.on('click', '#' + REST_APP.edit.attr('id'), function () {
        REST_APP.edit_item();
    });

    // listing
    REST_APP.get_list();

});