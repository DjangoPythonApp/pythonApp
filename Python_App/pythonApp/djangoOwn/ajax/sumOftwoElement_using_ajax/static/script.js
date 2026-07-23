// JQuery using ajax to send data to the server and get the sum of two numbers
$(document).ready(function() {
    console.log("JQuery is working");
    $('#calculateSum').click(function(event) {
        event.preventDefault();
        let num1 = $('#num1').val();
        let num2 = $('#num2').val();
        const csrfToken = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            url: '/add/',
            method: 'POST',
            data: {
                'num1': num1,
                'num2': num2,
                'csrfmiddlewaretoken': csrfToken
            },
            success: function(response) {
                $('#num1').val('');
                $('#num2').val('');
                $('#result').text(`${response.num1} + ${response.num2} = ${response.sum}`);
            },
            error: function(error){
                alert("An error occurred while calculating the sum.");
            }
        });
    });
});
