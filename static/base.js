const btnOpen = document.querySelector('.btn-open');
const btnClose = document.querySelector('.head-btn');
const sidebar = document.querySelector('.sidebar');
const main = document.querySelector('.main');


btnOpen.addEventListener('click', (e) => {
    console.log('Sidebar opened');
    sidebar.style.width = "80vw";
    main.style.marginLeft = "80vw";
});

btnClose.addEventListener('click', () => {
    console.log('Sidebar closed');
    sidebar.style.width = "0";
    main.style.marginLeft = "0";
});