// This handles the recording and streaming the voice from the client-side
let mediaRecorder;
let audioChunks = [];
const audioElem = document.getElementById('audioRecord');
const audioPlayer = document.getElementById('audioPlayer');
const errorElem = document.getElementById('error');
import { sendAudio } from "./send_audio.mjs"

//Declaring the MediaStreamConstraints object
const constraints = {
	audio: {
		mimeType: 'audio/mpeg',
	},
        video: false
        }
audioElem.addEventListener('click', recordAudio);

function recordAudio(){
//Ask the User for the access of the device microphone
navigator.mediaDevices.getUserMedia(constraints)
		.then(mediaStream => {
			mediaRecorder = new MediaRecorder(mediaStream);
			mediaRecorder.ondataavailable = (event) => {
				if (event.data.size > 0){
					audioChunks.push(event.data);
				}
			};

		mediaRecorder.onstop = () => {
                        const audioBlob = new Blob(audioChunks, { type: 'audio/mpeg'});
			sendAudio(audioBlob);
                        };

                mediaRecorder.start();
                audioElem.disabled = true;

                setTimeout(stopRecording, 200000);
		}).catch(err => {
			errorElem.innerHTML = err;
                        errorElem.style.display = "block";
		});
}

function stopRecording(){
	if (mediaRecorder.state === 'recording'){
        mediaRecorder.stop();
        audioElem.disabled = false;
	}
}
