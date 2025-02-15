document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    if (userInput === '//train_data') {
        document.getElementById('train').style.display = 'block';
    } else {
        // Handle user input and response
        console.log('User Input:', userInput);
    }
});

document.getElementById('train-photo-button').addEventListener('click', function() {
    const photo = document.getElementById('photo-upload').files[0];
    const description = document.getElementById('photo-description').value;
    // Handle photo training logic here
    console.log('Photo:', photo);
    console.log('Description:', description);
});

document.getElementById('train-video-button').addEventListener('click', function() {
    const video = document.getElementById('video-upload').files[0];
    const description = document.getElementById('video-description').value;
    // Handle video training logic here
    console.log('Video:', video);
    console.log('Description:', description);
});

document.getElementById('train-text-button').addEventListener('click', function() {
    const exampleMessage = document.getElementById('example-message').value;
    const exampleReply = document.getElementById('example-reply').value;
    // Handle text training logic here
    console.log('Example Message:', exampleMessage);
    console.log('Example Reply:', exampleReply);
});
