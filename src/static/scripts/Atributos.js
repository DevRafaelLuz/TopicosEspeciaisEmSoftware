document.addEventListener("DOMContentLoaded", () => {
  const valoresDisponiveis = JSON.parse(document.getElementById("valores-json").textContent);
  const selects = Array.from(document.querySelectorAll(".atributo-select"));

  function atualizarSelects() {
    const usados = selects.map(s => s.value).filter(v => v !== "");
    const contagem = usados.reduce((acc, val) => {
      acc[val] = (acc[val] || 0) + 1;
      return acc;
    }, {});

    selects.forEach(select => {
      const valorAtual = select.value;
      select.innerHTML = "<option value=''>-- Escolha --</option>";

      const contagemLocal = { ...contagem };
      if (valorAtual) contagemLocal[valorAtual] = (contagemLocal[valorAtual] || 1) - 1;

      valoresDisponiveis.forEach(valor => {
        const usadosDoValor = contagemLocal[valor] || 0;
        const totalDoValor = valoresDisponiveis.filter(v => v === valor).length;
        if (usadosDoValor < totalDoValor || valor == valorAtual) {
          const option = document.createElement("option");
          option.value = valor;
          option.textContent = valor;
          if (valor == valorAtual) option.selected = true;
          select.appendChild(option);
        }
      });
    });
  }

  selects.forEach(select => {
    select.addEventListener("change", atualizarSelects);
  });

  atualizarSelects();
});