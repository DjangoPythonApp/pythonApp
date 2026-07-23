function getCookie(name){
    let cookieValue = null;

    if (document.cookie && document.cookie !== ''){
        const cookies = document.cookie.split(';');

        for (let i = 0;i < cookies.length;i++){
            const cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
}

function checkReview(){
    const rating = document.getElementById('id_rating').value;
    const comments = document.getElementById('id_comments').value;

    fetch('/analyze/', {
        method: 'POST',
        headers: {
            'X-CSRFToken':
            getCookie('csrftoken'),
            'Content-Type':
            'application/x-www-form-urlencoded'
        },
        body:
        'rating=' + rating +
        '&comments=' + comments
    })

    .then(response =>response.json())
    .then(data => {document.getElementById('result').innerHTML = data.review_level;
    });
}