
    document.getElementById('searchInput').addEventListener('keyup', function() {
        const filter = this.value.toLowerCase();
        const rows = document.querySelectorAll('#productTable tbody tr');

        rows.forEach(row => {
            const cells = row.getElementsByTagName('td');
            let found = false;

            for (let i = 0; i < cells.length; i++) {
                if (cells[i].innerText.toLowerCase().includes(filter)) {
                    found = true;
                    break;
                }
            }

            if (found) {
                row.style.display = ''; 
            } else {
                row.style.display = 'none'; 
            }
        });
    });

