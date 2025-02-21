function passwordVisibility(inputId, iconId) {
    const input = document.getElementById(inputId);
    const icon = document.getElementById(iconId);

    if(input.type === 'password') {
        input.type = 'text';
        icon.src = "/static/img/eye-open.svg";
    } else {
        input.type = 'password';
        icon.src = "/static/img/eye-close.svg";
    }
}