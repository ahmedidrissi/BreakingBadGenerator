function showImage() {
  fetch("/show-image", {
    method: "POST",
  }).then((_res) => {
      window.location.href = "/";
  });
}

function clearImage() {
    fetch("/clear-image", {
      method: "POST",
    }).then((_res) => {
        window.location.href = "/";
    });
  }