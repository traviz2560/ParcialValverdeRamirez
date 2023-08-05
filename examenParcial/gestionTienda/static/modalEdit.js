;(function () {
  const modal = new bootstrap.Modal(document.getElementById("modal"))
  const modaldelete = new bootstrap.Modal(document.getElementById("modalDelete"))

  htmx.on("htmx:afterSwap", (e) => {
    if (e.detail.target.id == "editar") {
      modal.show()
    }
    if (e.detail.target.id == "borrar") {
      modaldelete.show()
    }
  })

  htmx.on("htmx:beforeSwap", (e) => {
    if (e.detail.target.id == "editar" && !e.detail.xhr.response) {
      modal.hide()
      e.detail.shouldSwap = false
    }
    if (e.detail.target.id == "borrar" && !e.detail.xhr.response) {
      modaldelete.hide()
      e.detail.shouldSwap = false
    }
  })

  htmx.on("hidden.bs.modal", () => {
    document.getElementById("editar").innerHTML = ""
    document.getElementById("borrar").innerHTML = ""
  })
})()