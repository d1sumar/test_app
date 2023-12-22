let body = document.body;
let checkbox = document.querySelector('.form-check-input')

function Change() {
    theme = localStorage.getItem('theme')
    if (theme) {
        body.dataset.bsTheme = theme
    } else {
        localStorage.setItem('theme', 'dark')
        body.dataset.bsTheme = localStorage.getItem(('theme'))
    }
    condition = localStorage.getItem(('theme'))
    checkbox.checked = condition === 'light' ? false : true
}

Change()

function myFunction() {
    localStorage.setItem('theme', theme === 'dark' ? 'light' : 'dark')
    Change()
}