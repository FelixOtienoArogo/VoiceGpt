/**Sends the recorded audio to the server **/

export function sendAudio(audioBlob){
	const endpointUrl = 'http://127.0.0.1:5000/process_audio';

	const formData = new FormData();
	formData.append('audio', audioBlob);
	console.log(formData.get('audio'));

	// Make a HTTP POST request to the API
	fetch(endpointUrl, {
		method: 'POST',
		body:formData,
	})
	.then(response => response.json())
	.then(data => {
		//Handling the API response
		console.log('Processing result:', data);
	})
	.catch(error => {
		console.error('Error sending audio to server:', error);
	});
}

