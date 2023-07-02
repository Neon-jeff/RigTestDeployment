
const toggle1 = document.querySelector('.sidebar-toggle')
const sidebar = document.querySelector('.sidebar')

function hideSidebar() {
    sidebar.classList.add('hide-sidebar')
}

toggle1.addEventListener('click', e => {
    sidebar.classList.toggle('hide-sidebar')
})
