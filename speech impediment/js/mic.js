//download.js v4.2, by dandavis; 2008-2016. [CCBY2] see http://danml.com/download.html for tests/usage
// v1 landed a FF+Chrome compat way of downloading strings to local un-named files, upgraded to use a hidden frame and optional mime
// v2 added named files via a[download], msSaveBlob, IE (10+) support, and window.URL support for larger+faster saves than dataURLs
// v3 added dataURL and Blob Input, bind-toggle arity, and legacy dataURL fallback was improved with force-download mime and base64 support. 3.1 improved safari handling.
// v4 adds AMD/UMD, commonJS, and plain browser support
// v4.1 adds url download capability via solo URL argument (same domain/CORS only)
// v4.2 adds semantic variable names, long (over 2MB) dataURL support, and hidden by default temp anchors
// https://github.com/rndme/download

// We'll save all chunks of audio in this array.
var chunks = [];

// We will set this to our MediaRecorder instance later.
let recorder = null;

// We'll save some html elements here once the page has loaded.
let audioElement = null;
let startButton = null;
let stopButton = null;
let downloadButton = null;
let aDownload = null;
let blobUrl = null;
let blob = null;

/**
 * Save a new chunk of audio.
 * @param  {MediaRecorderEvent} event 
 */
const saveChunkToRecording = (event) => {
    console.log(event.data);
    chunks.push(event.data);
};

/**
 * Save the recording as a data-url.
 * @return {[type]}       [description]
 */
const saveRecording = () => {
    console.log(chunks);
    blob = new Blob(chunks, {
        type: 'audio/wav'
    });
    // blobUrl = URL.createObjectURL(blob);
    chunks = [];
};

/**
 * Start recording.
 */
const startRecording = () => {
    recorder.start();
    console.log("start recording");
};

/**
 * Stop recording.
 */
const stopRecording = () => {
    recorder.stop();
    console.log("stop recording");
};

// Wait until everything has loaded
(function() {
    audioElement = document.querySelector('.js-audio');
    startButton = document.querySelector('.js-start');
    stopButton = document.querySelector('.js-stop');
    
    // We'll get the user's audio input here.
    navigator.mediaDevices.getUserMedia({
        audio: true,
        video: false // We are only interested in the audio
    }).then(stream => {
        // Create a new MediaRecorder instance, and provide the audio-stream.
        recorder = new MediaRecorder(stream);
        // Set the recorder's eventhandlers
        recorder.ondataavailable = saveChunkToRecording;
        recorder.onstop = saveRecording;
    });
    startButton.addEventListener('click', startRecording);
    stopButton.addEventListener('click', stopRecording);
    
})();
