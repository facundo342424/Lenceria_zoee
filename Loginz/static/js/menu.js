const menuIcon = document.getElementById('menu-icon');
const dropdownMenu = document.getElementById('dropdown-menu');

// Agrega un listener al ícono para alternar el menú
menuIcon.addEventListener('click', () => {
    if (dropdownMenu.style.display === 'none' || dropdownMenu.style.display === '') {
        dropdownMenu.style.display = 'block'; // Mostrar menú
    } else {
        dropdownMenu.style.display = 'none'; // Ocultar menú
    }
});

// Cierra el menú si haces clic fuera de él
window.addEventListener('click', (e) => {
    if (e.target !== menuIcon && !dropdownMenu.contains(e.target)) {
        dropdownMenu.style.display = 'none';
    }
});