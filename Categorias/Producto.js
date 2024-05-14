
    const API_URL = "https://mindicador.cl/api";

fetch(`${API_URL}/uf`)
    .then((response) => response.json())
    .then((data) => {
        const ufValue = data.serie[0].valor; 
        const ValorUF = ufValue;
        const Valorpiso = parseFloat(document.getElementById("preciopro").textContent);

        function calcularDivision() {
            const resultado = Valorpiso / ValorUF;
            const resultadoTruncado = resultado.toFixed(5);
            document.getElementById("resultado").textContent = `$${resultadoTruncado}`;
            
           
            document.getElementById("ocultarBtn").style.display = "block";
        }

        function ocultarResultado() {
            document.getElementById("resultado").textContent = ""; 
            document.getElementById("ocultarBtn");
        }

        document.getElementById("calcular").addEventListener("click", calcularDivision);
        document.getElementById("ocultarBtn").addEventListener("click", ocultarResultado);
    })
    .catch((error) => {
        console.error("Error al obtener datos de la API:", error);    
    });

    