async function create_url() {
    let target_url = document.getElementById('target-url').value;
    let url_info_field = document.getElementById('url-info');
    const url = 'http://localhost:8000/url';
    const body = {target_url: target_url};
    const headers = {'Content-Type': 'application/json'};
    const data = {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(body)
    };

    const request = await fetch(url, data);
    const response = await request.json();
    if (request.status == 200) {
        url_info_field.innerHTML = 
        `<p>URL encurtada: <a href="${response.url}">${response.url}</a></p>
         <p>Informações da URL: <a href="${response.admin_url}">${response.admin_url}</a></p>`
    } else if (request.status == 400) {
        url_info_field.innerHTML = `<p>${response.detail}</p>`
    } else {
        console.error('A unexpected error ocurred on the request!')
    };
    console.log(request.status, response);
};


