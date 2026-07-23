// Wait until DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("categoryForm");

    if (form) {

        form.addEventListener("submit", function (event) {
            const name = document.getElementById("name");
            const description = document.getElementById("description");

            const errorName = document.getElementById("errorName");
            const errorDescription = document.getElementById("errorDescription");

            let isValid = true;
            const nameRegex = /^[A-Za-z]+( [A-Za-z]+)*$/;

            // Clear previous errors
            errorName.innerText = "";
            errorDescription.innerText = "";

            // NAME VALIDATION
            if (name.value.trim() === "") {
                errorName.innerText = "Category name is required";
                isValid = false;
            } else if (name.value.trim().length < 3) {
                errorName.innerText = "Minimum 3 characters required";
                isValid = false;
            } else if (!nameRegex.test(name.value)) {
                errorName.innerText = "Only letters allowed with single space between words";
                isValid = false;
            }

            // DESCRIPTION VALIDATION
            if (description.value.trim() === "") {
                errorDescription.innerText = "Description is required";
                isValid = false;
            } else if (description.value.trim().length < 5) {
                errorDescription.innerText = "Minimum 5 characters required";
                isValid = false;
            }

            // STOP FORM if invalid
            if (!isValid) {
                event.preventDefault();
            }
        });
    }
});