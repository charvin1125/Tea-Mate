// Function to load CSV files using PapaParse
function loadCSV(file, callback) {
    Papa.parse(file, {
        complete: function(results) {
            callback(results.data);
        },
        header: true, // Assumes the first row contains headers
        skipEmptyLines: true
    });
}

// Example function to handle tea recommendation
function getTeaRecommendation() {
    const mood = moods[moodSlider.value];
    const location = document.getElementById('location').value.trim();

    if (!location) {
        alert("Please enter a location!");
        return;
    }

    // Get the tea recommendation based on mood
    const recommendedTea = teaRecData.filter(tea => tea.mood === mood);

    if (recommendedTea.length > 0) {
        const tea = recommendedTea[0];
        displayTeaCard(tea);
    } else {
        alert("No tea found for your mood.");
    }
}

// Function to display the tea card with name, image, and fun fact
function displayTeaCard(tea) {
    document.getElementById('teaName').textContent = tea.name;
    document.getElementById('teaImage').src = tea.image;
    document.getElementById('funFact').textContent = teaFactData.find(fact => fact.teaName === tea.name).fact;

    document.getElementById('teaCard').style.display = "block";
}

// Function to display time dynamically
function displayTime() {
    const time = new Date();
    const timeString = time.toLocaleTimeString();
    document.getElementById('timeDisplay').innerText = `Time: ${timeString}`;
}
setInterval(displayTime, 1000);

// Update the mood label based on the slider value
const moods = ["Calm", "Energized", "Balanced", "Focused", "Relaxed"];
const moodSlider = document.getElementById('mood');
const moodLabel = document.getElementById('moodLabel');

moodSlider.addEventListener('input', function() {
    moodLabel.textContent = moods[moodSlider.value];
});

// Tea data will be stored here
let teaRecData = [];
let teaFactData = [];

// Handle the file upload and parse the CSV files
document.getElementById('teaRecFile').addEventListener('change', function(e) {
    const file = e.target.files[0];
    loadCSV(file, function(data) {
        teaRecData = data; // Store the tea recommendation data
    });
});

document.getElementById('teaFactsFile').addEventListener('change', function(e) {
    const file = e.target.files[0];
    loadCSV(file, function(data) {
        teaFactData = data; // Store the tea facts data
    });
});
