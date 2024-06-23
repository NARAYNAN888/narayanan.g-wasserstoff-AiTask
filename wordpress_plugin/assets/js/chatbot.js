jQuery(document).ready(function($) {
    $('#chatbot-send').on('click', function() {
        var userQuery = $('#chatbot-input').val();
        $('#chatbot-input').val('');

        $.ajax({
            url: 'http://localhost:8000/query', // Replace with your backend API endpoint
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ query: userQuery }),
            success: function(response) {
                $('#chatbot-messages').append('<div class="user-message">' + userQuery + '</div>');
                $('#chatbot-messages').append('<div class="bot-response">' + response.response + '</div>');
            }
        });
    });
});
