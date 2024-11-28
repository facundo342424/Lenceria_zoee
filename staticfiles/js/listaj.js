<<<<<<< HEAD
let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6] },
        { orderable: false, targets: [8, 8] },
        { searchable: false, targets: [0, 8, 8] }
    ],
    pageLength: 6,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await lista_Productos();

    dataTable = $("#datatable-programmers").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const lista_Productos = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000");
        const data = await response.json();

        let content = ``;
        data.programmers.forEach((Productos, index) => {
            content += `


            
                <tr>
                    <td>${index + 1}</td>
                    <td>${Productos.Nombre}</td>
                    <td>${Productos.Marca}</td>
                    <td>${Productos.Precioy}</td>
                    <td>${Productos.Color}</td>
                    
                        
                        ? "<i class='fa-solid fa-check' style='color: green;'></i>" 
                        : "<i class='fa-solid fa-xmark' style='color: red;'></i>"}
                    </td>
                    <td>
                        <button class='btn btn-sm btn-primary'><i class='fa-solid fa-pencil'></i></button>
                        <button class='btn btn-sm btn-danger'><i class='fa-solid fa-trash-can'></i></button>
                    </td>
                </tr>`;
        });
        tableBody_programmers.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
=======
let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6] },
        { orderable: false, targets: [8, 8] },
        { searchable: false, targets: [0, 8, 8] }
    ],
    pageLength: 6,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await lista_Productos();

    dataTable = $("#datatable-programmers").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const lista_Productos = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000");
        const data = await response.json();

        let content = ``;
        data.programmers.forEach((Productos, index) => {
            content += `


            
                <tr>
                    <td>${index + 1}</td>
                    <td>${Productos.Nombre}</td>
                    <td>${Productos.Marca}</td>
                    <td>${Productos.Precioy}</td>
                    <td>${Productos.Color}</td>
                    
                        
                        ? "<i class='fa-solid fa-check' style='color: green;'></i>" 
                        : "<i class='fa-solid fa-xmark' style='color: red;'></i>"}
                    </td>
                    <td>
                        <button class='btn btn-sm btn-primary'><i class='fa-solid fa-pencil'></i></button>
                        <button class='btn btn-sm btn-danger'><i class='fa-solid fa-trash-can'></i></button>
                    </td>
                </tr>`;
        });
        tableBody_programmers.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
>>>>>>> dba47e5601253f8f0732039a4fab07c8a6aabe46
});