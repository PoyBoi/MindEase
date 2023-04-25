function sendData() {
    const input = document.getElementById("userBox").value;
    const data = {input: input};
    fetch('/myPythonFile.py', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
    }
    });
}