$(document).ready(function(){
    console.log('Jquery running')

    $('#btnAdd').click(function(event){
        event.preventDefault();
        console.log('Button Clicked')

        const firstNum = $('#firstNum').val();
        const secondNum = $('#secondNum').val();
        const csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val()

        // console.log(firstNum+' '+secondNum)

        $.ajax(
            {
                url:'/add/',
                method:'POST',
                data:{
                    firstNum: firstNum,
                    secondNum: secondNum,
                    csrfmiddlewaretoken: csrfmiddlewaretoken
                },
                success: function(response){
                    $('#firstNum').val("");
                    $('#secondNum').val("");
                    $('#acknowledgement').text(`${response.firstNum} + ${response.secondNum} = ${response.result}`);
                },
                error: function(error){
                    alert('There is an error')
                }
            }
        )
    });
});




// JavaScript built-in fetch API
// ---------------------------------
// document.addEventListener("DOMContentLoaded", function () {
//     console.log("JavaScript Running");

//     document.getElementById("btnAdd").addEventListener("click", function (event) {
//         event.preventDefault();
//         console.log("Button Clicked");

//         const firstNum = document.getElementById("firstNum").value;
//         const secondNum = document.getElementById("secondNum").value;
//         const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

//         // Create FormData
//         const formData = new FormData();

//         formData.append("firstNum", firstNum);
//         formData.append("secondNum", secondNum);
//         formData.append("csrfmiddlewaretoken", csrfToken);

//         fetch("/add/", {
//             method: "POST",
//             body: formData
//         })
//         .then(response => response.json())
//         .then(data => {
//             document.getElementById("firstNum").value = "";
//             document.getElementById("secondNum").value = "";

//             document.getElementById("acknowledgement").innerText =
//                 `${data.firstNum} + ${data.secondNum} = ${data.result}`;

//         })
//         .catch(error => {
//             alert("There is an error");
//             console.log(error);
//         });
//     });
// });