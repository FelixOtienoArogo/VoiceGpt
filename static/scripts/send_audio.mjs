/**Sends the recorded audio to the server **/
const audioPlay = document.getElementById('audioPlayer');
const downloadLink = document.getElementById('downloadLink');

export function sendAudio(audioBlob){
	const endpointUrl = 'http://127.0.0.1:5000/process_audio';

	const formData = new FormData();
	formData.append('audio', audioBlob);

	// Make a HTTP POST request to the API
	fetch(endpointUrl, {
		method: 'POST',
		body:formData,
	})
	.then(response => response.arrayBuffer())
	.then((audioData) => {
		//Handling the API response, both json and audio
		//console.log('Processing result:', jsonResponse);
		//const uint8Array = new Uint8Array(audioData);

		// Create a Blob from the array buffer
		const audioBlob = new Blob([audioData], { type: 'audio/mpeg' });

		//create an object URL from the Blob
		const respUrl = URL.createObjectURL(audioBlob);

		//Set the audio player source to the object URL
		audioPlay.src = respUrl;

		//Automatically play the audio
		audioPlay.play();
	})
	.catch(error => {
		console.error('Error sending audio to server:', error);
	});
}

