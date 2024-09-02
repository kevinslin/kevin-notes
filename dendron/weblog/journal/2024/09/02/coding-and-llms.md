---
id: z9v7jm0cvepy0kxnhtqye98
title: Address Mapper
desc: ''
updated: 1725310444752
created: 1725289710220
topic: projects
tags:
  - llm
---

Over the labor day weekend, I decided to try [cursor](https://www.cursor.com/). I think of this as the next version of github copilot. In addition to autocompletion, the entire IDE  becomes a LLM workspace where anything can be used as context and also prompted against. 
Cursor is a fork of vscode (my primary IDE), which is to the IDE space what chrome is to browsers. When installing cursor, there's a one click process to migrate over all your extensions which smoothes out the transition.

I wanted to build a map app where I could input a series of newline delimited addresses and plot them all in a map. 
The use case: I just moved to the bay area and want to find good caffee places that had fast internet. Asking perplexity yielded a bunch of potential locations - I wanted to visualize them in a map but didn't want to put them in to google maps one by one.
Example of the input:
```
270 Seventh St, San Francisco, CA
432B Octavia St, San Francisco, CA
3655 Lawton St, San Francisco, CA
672 Stanyan St, San Francisco, CA
Haus Coffee, Mission, San Francisco, CA
...
```

This is by no means a painkiller problem but it was a pain point for me and more importantly, was a well scoped mini project I could use to test out cursor.

Instead of going over the entire setup and prompting chronology, I'm going to skip ahead to output and takeaways.

## Demo
<iframe width="560" height="315" src="https://www.youtube.com/embed/F_-95MUTNOQ?si=SBNiePKYdoCDbGlN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## Takeaways:
- cursor is very impressive - it took me ~30min to build a web app in nextjs & typescript that fufilled the specifications as well as add some customization on top
- especially useful for some of the following usecase
    - changing implementation details of functions (eg. swap geocoding api from `opencagedata` to `mapbox`)
    - adding logs to all function calls
    - translating pseudo code into real code
    - making style adjustments in english 
    - adding additional enhancements to the functionality (eg. modify the location marker icons so that it shows labels as text above the icon)
- this was enough to make me set cursor as my default coding environment - will see if I run into any issues with this decision over the next week
- one thing I worry about is the "autopilot effect" - it becomes easy to be so reliant on the ai that we lose the underlying skills to do the thing itself (eg. developing a sense of direction vs relying on google maps)
    - for now, I do like to model out how I like the code to be implemented, if only in my head, and be able to still do that mental modelling so I have a baseline that I can use to compare with the output
- modern web apps are way too complex
    - my initial prompt (`write a webapp that given a series of addresses will plot it on a google maps like interface`), yielded a single html file with vanilla html and javascript that basically worked but needed to be refactored so that api keys (used for geocoding to translate human addresses to coordinates) weren't leaked on the client side
    - the simple thing to do is the [levels approach](https://x.com/levelsio) - write a backend in php that revelaed a single api endpoint that did the geocoding
    - since most of my experience with webapps came with nextjs, I had cursor generate nextjs scaffolding (in typescript of course). getting nextjs and typescript to bootstrap properly took up most of the time in getting this app off the ground
- need to figure out a good way of documenting experience with llms - copying and pasting the entire prompt and response chain is an option but much too cumbsersome and manual at this point

    

<!-- ## Setup
I started off by generating a scaffold using gpt4o.
```
write a webapp that given a series of addresses will plot it on a google maps like interface
```

This resulted in a single html file that basically worked. The main problems with this solution is that it put the API key on the client side which, unless you want clients to use their own api keys, is almost never what you want from a security perspective.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Address Plotter</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <style>
        #map {
            height: 600px;
            width: 100%;
        }
    </style>
</head>
<body>
    <h1>Address Plotter</h1>
    <textarea id="addresses" rows="5" cols="50" placeholder="Enter addresses, one per line"></textarea><br><br>
    <button onclick="plotAddresses()">Plot Addresses</button>
    <div id="map"></div>

    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script>
        const map = L.map('map').setView([37.7749, -122.4194], 13); // Default to San Francisco

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
        }).addTo(map);

        async function plotAddresses() {
            const addresses = document.getElementById('addresses').value.split('\n');
            for (const address of addresses) {
                const location = await geocodeAddress(address.trim());
                if (location) {
                    L.marker([location.lat, location.lng]).addTo(map)
                        .bindPopup(address)
                        .openPopup();
                }
            }
        }

        async function geocodeAddress(address) {
            const apiKey = 'YOUR_API_KEY'; // Replace with your OpenCage or Mapbox API key
            const response = await fetch(`https://api.opencagedata.com/geocode/v1/json?q=${encodeURIComponent(address)}&key=${apiKey}`);
            const data = await response.json();
            if (data.results && data.results.length > 0) {
                return data.results[0].geometry;
            }
            return null;
        }
    </script>
</body>
</html>
```

## Setup 2 - Nextjs

Using gpt4o, I used the following prompts to re-create this app using nextjs

1. Generate a nextjs app
```
generate scaffolding for a basic nextjs 12 typescript application
```

2. customize scaffold to create a map app
```
using this scaffold, create a maps app that takes a list of addresses and plots them on a map 
```

Note that I could have done this in cursor itself, this is just going by habit of using chatgpt directly to create an initial version of the app.  -->
