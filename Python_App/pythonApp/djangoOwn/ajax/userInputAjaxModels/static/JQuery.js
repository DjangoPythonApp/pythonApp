$(document).ready(function() {
   console.log("JQuery is working");

   $('#submit-btn').click(function(event) {
       event.preventDefault();
       console.log("Submit button clicked");

       const isValid = validateForm();
       if (!isValid) {
           return;
       }
       submitForm();
    });
           
   });


   //Form validation function
   function validateForm() {
       const name = $('#name').val().trim();
       const email = $('#email').val().trim();
       const address = $('#address').val().trim();
       const age = $('#age').val().trim();

       const errorName = $('#errorName');
       const errorEmail = $('#errorEmail');
       const errorAddress = $('#errorAddress');
       const errorAge = $('#errorAge');

       // clear previous error messages
       errorName.text('');
       errorEmail.text('');
       errorAddress.text('');
       errorAge.text('');

       let isValid = true;

       const nameRegex=/^[A-Za-z]+( [A-Za-z]+)*$/;
        if (name === "") {
        errorName.text("Category name is required");
        isValid = false;
    } else if (name.length < 3) {
        errorName.text("Minimum 3 characters required");
        isValid = false;
    } else if (!nameRegex.test(name)) {
        errorName.text("Only letters allowed with single space between words");
        isValid = false;
    }
    if(email == ''){
        errorEmail.text("email is required");
        isValid = false;
    }
    if(address == ""){
        errorAddress.text('address is required');
        isValid = false;
    }
    if(age == ""){
        errorAge.text('age is required.');
        isValid = false;
    }
    return isValid;
}

function submitForm(){

    let category_id = $('#category_id').val();
    let name = $('#name').val().trim();
    let email = $('#email').val().trim();
    let address = $('#address').val().trim();
    let age = $('#age').val().trim();
    
    let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
$.ajax({
    url: category_id ? `/edit/${category_id}/` : `/form/`,
    method: 'POST',
    data : {

            category_id: category_id,
            name: name,
            email: email,
            address: address,
            age: age,
            csrfmiddlewaretoken: csrfmiddlewaretoken

    },
    success: function (response) {
            /* DUPLICATE CATEGORY */
            if (response.success === false) {
                showMessage(response.message,"red");
                return;
            }
            resetForm();
            showMessage(response.message,"green");
            setTimeout(function () {
                window.location.assign('/form/');
            }, 500);
        },
        error: function (error) {
            console.log(error);
            showMessage("Something went wrong","red");
        }

})

}

function showMessage(message, color) {
    $("#acknowledge")
        .text(message)
        .css("color", color)
        .fadeIn()
        .delay(2000)
        .fadeOut();
}

// * RESET FORM FUNCTION */
function resetForm() {
    $("#name").val("");
    $("#email").val("");
    $("#address").val("");
    $("#age").val("");
    $("#category_id").val("");
    $("#errorName").text("");
    $("#errorEmail").text("");
    $("#errorAddress").text("");
    $("#errorAge").text("");
}

/* DELETE CATEGORY */
$(document).on('click', '.delete-btn', function () {
    const confirmDelete = confirm("Are you sure you want to delete this category?");

    if (!confirmDelete) { return; }

    const category_id = $(this).data('id');
    const currentRow = $(this).closest('tr');
    const csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        url: `/delete/${category_id}/`,
        method: 'POST',
        data: {
            csrfmiddlewaretoken: csrfmiddlewaretoken
        },
        success: function (response) {
            if (response.success) {
                currentRow.remove();
                showMessage(response.message, "green");
            } else {
                showMessage(response.message,"red");
            }
        },
        error: function (error) {
            console.log(error);
            showMessage("Something went wrong","red");
        }
    });
});
