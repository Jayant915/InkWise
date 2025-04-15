
const canvas = document.getElementById('handwritingCanvas');
const ctx = canvas.getContext('2d');
const clearButton = document.getElementById('clearCanvas');
const processButton = document.getElementById('processCanvas');
const ocrResultsDiv = document.getElementById('ocrResults');

let isDrawing = false;
let lastX = 0;
let lastY = 0;

function startDrawing(e) {
    isDrawing = true;
    lastX = e.offsetX;
    lastY = e.offsetY;
}

function draw(e) {
    if (!isDrawing) return;
    ctx.beginPath();
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.strokeStyle = '#000';
    ctx.lineWidth = 3;
    ctx.lineCap = 'round';
    ctx.stroke();
    lastX = e.offsetX;
    lastY = e.offsetY;
}

function stopDrawing() {
    isDrawing = false;
}

canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);

clearButton.addEventListener('click', () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ocrResultsDiv.textContent = ''; // Clear previous results
});

processButton.addEventListener('click', () => {
    const imageData = canvas.toDataURL('image/png');
    sendImageData(imageData);
});

function sendImageData(imageData) {
    ocrResultsDiv.textContent = 'Processing...';

    // Simulate sending data to a backend (replace with your actual backend call)
    setTimeout(() => {
        // Simulate OCR results
        const simulatedResults = 'Simulated OCR text: This is your handwriting';
        ocrResultsDiv.textContent = simulatedResults;
        // In a real application, you'd replace the simulated results with:
        // fetch('/api/ocr', {
        //     method: 'POST',
        //     body: JSON.stringify({ image: imageData }),
        //     headers: { 'Content-Type': 'application/json' },
        // })
        // .then(response => response.json())
        // .then(data => {
        //     ocrResultsDiv.textContent = data.text; // Assuming the backend returns { text: '...' }
        // })
        // .catch(error => {
        //     ocrResultsDiv.textContent = 'Error processing image.';
        // });
    }, 2000); // Simulate a 2-second processing time
}