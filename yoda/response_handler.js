// Declaring variables that you may want to use.
let names = ['cute', 'regular'];
let moods = ['dark', 'force', 'std'];

let dark_quotes = ["Once you start down the dark path, forever will it dominate your destiny, consume you it will.",
"In a dark place we find ourselves, and a little more knowledge lights our way.",
"Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
"Always two there are, no more, no less. A master and an apprentice.",
"In the end, cowards are those who follow the dark side."];
let force_quotes = ["Luminous beings are we, not this crude matter.",
"A Jedi uses the Force for knowledge and defense, never for attack.",
"Clear your mind must be, if you are to find the villains behind this plot.",
"The force. Life creates it, makes it grow. Its energy surrounds us and binds us.",
"My ally is the Force, and a powerful ally it is."];
let std_quotes = ["Patience you must have, my young padawan.",
"When nine hundred years old you reach, look as good you will not.",
"No! Try not! Do or do not, there is no try.",
"Judge me by my size, do you?",
"Difficult to see. Always in motion is the future."
];

var inputElement = document.getElementById("input")
inputElement.addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        respond()
    }
});

function respond() {
    
    var textElement = document.getElementById("yoda-text")
    var imageElement = document.getElementById("yoda-image")

    yodaImages = ['img/cute-dark.jpg', 'img/cute-force.jpg', 'img/cute-std.jpg', 'img/regular-dark.jpg', 'img/regular-force.jpg', 'img/regular-std.jpg']

    if (inputElement.value.includes('cute') || inputElement.value.includes('baby'))
    {
        //Baby yoda
        imageSrc = generateImage(['cute'])
    }
    else if (inputElement.value.includes('force'))
    {
        if (inputElement.value.includes('dark'))
        {
            // Battle sith lord
            imageSrc = generateImage(['dark'])
        }
        else
        {
            // Use the force
            imageSrc = generateImage(['force'])
        }
    }
    else
    {
        imageSrc = generateImage(['jpg'])
    }
    
    imageElement.setAttribute('src', imageSrc)
    textElement.innerText = generateText(imageSrc)
    inputElement.value = "" // Clear the textbox after pressing response
}

function generateImage(types)
{
    images = [];

    for (var i = 0; i < yodaImages.length; i++)
    {
        for (var j = 0; j < types.length; j++)
        {
            if (yodaImages[i].includes(types[j]))
            {
                images.push(yodaImages[i])
            }
        }
    }

    index = parseInt(Math.random() * images.length)
    return images[index]
}

function generateText(image)
{
    if (image.includes('regular'))
    {
        if (image.includes('dark'))
        {
            index = parseInt(Math.random() * dark_quotes.length)
            return dark_quotes[index]
        }
        else if (image.includes('force'))
        {
            index = parseInt(Math.random() * force_quotes.length)
            return force_quotes[index]
        }
        else
        {
            index = parseInt(Math.random() * std_quotes.length)
            return std_quotes[index]
        }
    }
    else //if yoda is a baby
    {
        return "H" + "m".repeat(Math.random() * 20 + 1) //need to generate random number of m's
    }
}