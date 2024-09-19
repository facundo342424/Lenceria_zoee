const lista_Productos = async () => {
    try {
        const response = await fetch ('http://127.0.0.1:8000/');
        const data = await response.json();
        

        let content =``;
        data.Productos.forEach(Productos,listaj) => {
            content+= `
            tr
            
            
            
            
            `
            

            
            
        }
    }



}