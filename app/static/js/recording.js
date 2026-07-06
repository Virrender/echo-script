const startButton = document.getElementById("start-btn");
const stopButton = document.getElementById("stop-btn");

let mediaRecorder;
let recordedChunks = [];

startButton.addEventListener("click", async () => {
  const stream = await navigator.mediaDevices.getUserMedia({
    audio: true,
  });

  startRecording(stream);
  startButton.disabled = true;
  stopButton.disabled = false;
});

stopButton.addEventListener("click", () => {
  stopRecording();

  startButton.disabled = false;
  stopButton.disabled = true;
});

function startRecording(stream) {
  mediaRecorder = new MediaRecorder(stream);
  mediaRecorder.ondataavailable = function (event) {
    if (event.data.size > 0) {
      recordedChunks.push(event.data);
    }
  };

  mediaRecorder.start();
}

function stopRecording() {
  mediaRecorder.onstop = async () => {
    const blob = new Blob(recordedChunks, {
      type: "audio/webm",
    });

    const formData = new FormData();
    const filename = `recording-${Date.now()}.webm`;
    formData.append("audio", blob, filename);

    const response = await fetch("/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    console.log(data);

    recordedChunks = [];
  };
  mediaRecorder.stop();
}
