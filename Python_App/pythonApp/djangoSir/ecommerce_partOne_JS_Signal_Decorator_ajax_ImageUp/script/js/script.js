$(document).ready(function () {
    console.log("We are using JQuery");

    $('#btnRegister').click(function (event) {
        event.preventDefault();
        console.log("User clicked register button");

        const isValid = validateForm();
        if (!isValid) {
            return;
        }
        submitCategory();
    });
});


/* FORM VALIDATION FUNCTION */
function validateForm() {
    const name = $('#name').val().trim();
    const description = $('#description').val().trim();
    const errorName = $('#errorName');
    const errorDescription = $('#errorDescription');

    /*CLEAR PREVIOUS ERRORS*/
    errorName.text("");
    errorDescription.text("");
    let isValid = true;

    const nameRegex = /^[A-Za-z]+( [A-Za-z]+)*$/;
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

    if (description === "") {
        errorDescription.text("Description is required");
        isValid = false;
    } else if (description.length < 5) {
        errorDescription.text("Minimum 5 characters required");
        isValid = false;
    }
    return isValid;
}


/* AJAX FUNCTION */
function submitCategory() {
    const category_id = $('#category_id').val();
    const formData = new FormData($("#categoryForm")[0]);

    $.ajax({
        url: category_id ? `/category/edit/${category_id}/` : `/category/add/`,
        method: 'POST',
        data: formData,
        processData: false,  // Required for FormData
        contentType: false, // Both processData & contentType, these tell jQuery not to convert the FormData into a string,
        success: function (response) {
            /* DUPLICATE CATEGORY */
            if (response.success === false) {
                showMessage(response.message,"red");
                return;
            }
            // resetForm();
            $("#categoryForm")[0].reset();
            $("#imagePreview").hide(); // Hide image preview after submission
            showMessage(response.message,"green");
        },
        error: function (error) {
            console.log(error);
            showMessage("Something went wrong","red");
        }
    });
}

function showMessage(message, color) {
    $("#acknowledge")
        .text(message)
        .css("color", color)
        .fadeIn()
        .delay(2000)
        .fadeOut();
}


/* RESET FORM FUNCTION */
function resetForm() {
    $("#name").val("");
    $("#description").val("");
    $("#category_id").val("");
    $("#errorName").text("");
    $("#errorDescription").text("");
}

/* DELETE CATEGORY */
$(document).on('click', '.delete-btn', function () {
    const confirmDelete = confirm("Are you sure you want to delete this category?");

    if (!confirmDelete) { return; }

    const category_id = $(this).data('id');
    const currentRow = $(this).closest('tr');
    const csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        url: `/category/delete/${category_id}/`,
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
