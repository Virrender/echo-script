
const recordButton = document.getElementById("record-btn");


let mediaRecorder;
let recordedChunks = [];
let isRecording = false;

recordButton.addEventListener("click", async () => {
  if (!isRecording){
    const stream = await navigator.mediaDevices.getUserMedia({
      audio: true,
    });
    startRecording(stream);
    isRecording=true;
    recordButton.textContent="🛑"
  } 
  else {
    stopRecording();

    isRecording=false;
    recordButton.textContent="🎙️"
  }
})


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
    formData.append("audio", blob);

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
