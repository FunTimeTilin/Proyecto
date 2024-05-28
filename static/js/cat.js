const API_URL = "https://mindicador.cl/api";
const HTMLResponse = document.querySelector("#app");

fetch(`${API_URL}/uf`)
    .then((response) => response.json())
    .then((data) => {
        const ufValue = data.serie[0].valor; 
         
        const ValorUF = ufValue;
        const Valorpiso = 15000;
        function calcularDivision() {
            const resultado = Valorpiso / ValorUF;
            const resultadoTruncado = resultado.toFixed(5);
            document.getElementById("resultado").textContent = `$${resultadoTruncado}`;
        }
    document.getElementById("calcular").addEventListener("click", calcularDivision);
    })
    .catch((error) => {
        console.error("Error al obtener datos de la API:", error);    
        
    });