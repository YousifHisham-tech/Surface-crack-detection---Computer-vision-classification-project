let input = document.getElementById("imageInput");
let preview = document.getElementById("preview");
let result = document.getElementById("result");

// Image preview
input.addEventListener("change", () => {

    let file = input.files[0];

    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.style.display = "block";
    }
});

// Predict button
document.getElementById("detectButton").addEventListener("click", async () => {

    let file = input.files[0];

    if (!file) {
        alert("Please select an image first");
        return;
    }

    result.innerText = "Processing...";

    let formData = new FormData();
    formData.append("file", file);

    try {

        let response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        let data = await response.json();

        if (data.success) {
            result.innerText = "Prediction: " + data.prediction;
        } else {
            result.innerText = "Error: " + data.error;
        }

    } catch (err) {
        console.log(err);
        result.innerText = "Network error: " + err.message;
    }
});