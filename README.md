<h1 align="center">Weather API App — Python + PyQt5</h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/ba98194f-5209-4d02-b285-d758004e3cd3" alt="App Icon" width="100"/>
</p>

<p align="center">This is a desktop weather application built with <strong>Python</strong> and <strong>PyQt5</strong>, using the <a href="https://openweathermap.org/api" target="_blank">OpenWeatherMap API</a> to display real-time weather data.</p>
<p align="center">This program does not include an API key so you have to provide your API key, explained in the <code>Installation</code> section</p>
<p align="center">This is a simple project to make myself familiar with API requests.</p>

---

## What it does

- <strong>Real-time Weather Search</strong>: Enter a location to get live weather updates.
- <strong>Temperature Display</strong>: Ability to display the temperatures in both Celsius and Fahrenheit with a button switch at the bottom of the window.
- <strong>Dynamic Weather Icons</strong>: Visuals update based on live weather conditions using the Weather Condition Codes given by the API request.

---

## How it works

<h3>Weather Search Interface</h3>
<img src="https://github.com/user-attachments/assets/e96eb1e8-4166-42c8-b2f5-d8f4e7519fe3" width="360" alt="Weather Search Screenshot"/>

<h3>Celsius/Fahrenheit Toggle</h3>
<img src="https://github.com/user-attachments/assets/2771055d-4a06-4d38-8c96-b0b04e2f3f85" width="360" alt="Unit Toggle Screenshot"/>

---

## Installation

<ol>
  <li><strong>Clone the repository</strong><br>
    
  <code>git clone [https://github.com/supertost/Weather-API-App-Python.git](https://github.com/supertost/Weather-API-App-Python.git)</code><br>
  <code>cd Weather-API-App-Python</code></li>

  <li><strong>Install dependencies</strong><br>
    
  <code>pip install -r requirements.txt</code></li>

  <li><strong>Set your API key</strong><br>
    
  Create a <code>.env</code> file in the root folder with your OpenWeatherMap API key:<br>
  <pre><code>api_key=your_api_key</code></pre></li>
  Replace the <code>your_api_key</code> with your API key
  <li><strong>Run the app</strong><br>
    
  <code>python weatherapp.py</code></li>
</ol>

---

<p>This project was created after following Bro Code's Python course on YouTube: https://youtu.be/ix9cRaBkVe0?si=Jry5FF9Hq_utBpWA</p>
<p>My version includes an improved UI, image-based weather icons instead of emoji text, and a Celsius/Fahrenheit toggle — features not present in the original tutorial version.</p>
