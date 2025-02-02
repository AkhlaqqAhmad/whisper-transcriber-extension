document.getElementById('transcribeButton').addEventListener('click', async () => {
    const fileInput = document.getElementById('audioFile');
    const file = fileInput.files[0];
    const resultDiv = document.getElementById('result');
    const loadingDiv = document.getElementById('loading');

    if (!file) {
        alert('Please upload an audio file.');
        return;
    }

    resultDiv.innerText = '';  // Clear previous results
    loadingDiv.style.display = 'block';  // Show loading message

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('http://localhost:8000/transcribe', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`Transcription failed: ${response.status} ${response.statusText}`);
        }

        const result = await response.json();
        resultDiv.innerText = `📝 Transcription:\n${result.transcription}`;
    } catch (error) {
        console.error('Error:', error);
        resultDiv.innerText = '❌ Transcription failed. Please try again.';
    } finally {
        loadingDiv.style.display = 'none';  // Hide loading message
    }
});
