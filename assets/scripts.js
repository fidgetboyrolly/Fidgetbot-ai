document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    handleUserInput(userInput);
});

document.getElementById('user-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        const userInput = document.getElementById('user-input').value;
        handleUserInput(userInput);
    }
});

function handleUserInput(userInput) {
    if (userInput === '//train_data') {
        document.getElementById('train').style.display = 'block';
        updateProgressBar();
    } else {
        // Handle user input and response
        console.log('User Input:', userInput);
    }
}

document.getElementById('train-photo-button').addEventListener('click', function() {
    const photo = document.getElementById('photo-upload').files[0];
    const description = document.getElementById('photo-description').value;
    // Handle photo training logic here
    console.log('Photo:', photo);
    console.log('Description:', description);
    updateProgressBar();
});

document.getElementById('train-video-button').addEventListener('click', function() {
    const video = document.getElementById('video-upload').files[0];
    const description = document.getElementById('video-description').value;
    // Handle video training logic here
    console.log('Video:', video);
    console.log('Description:', description);
    updateProgressBar();
});

document.getElementById('train-text-button').addEventListener('click', function() {
    const exampleMessage = document.getElementById('example-message').value;
    const exampleReply = document.getElementById('example-reply').value;
    // Handle text training logic here
    console.log('Example Message:', exampleMessage);
    console.log('Example Reply:', exampleReply);
    updateProgressBar();
});

function updateProgressBar() {
    // Example logic to calculate progress
    const totalTrainingData = 100; // Change this to the total training data required
    const currentTrainingData = 10; // Change this to the current training data count
    const progress = (currentTrainingData / totalTrainingData) * 100;
    
    document.getElementById('progress').style.width = progress + '%';
    document.getElementById('progress-text').innerText = progress + '% trained';
}
