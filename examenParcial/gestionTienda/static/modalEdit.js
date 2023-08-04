;(function () {
  const modal = new bootstrap.Modal(document.getElementById("modal"))

  htmx.on("htmx:afterSwap", (e) => {
    if (e.detail.target.id == "editar") {
      modal.show()
    }
  })

  htmx.on("htmx:beforeSwap", (e) => {
    if (e.detail.target.id == "editar" && !e.detail.xhr.response) {
      modal.hide()
      e.detail.shouldSwap = false
    }
  })

  htmx.on("hidden.bs.modal", () => {
    document.getElementById("editar").innerHTML = ""
  })
})()