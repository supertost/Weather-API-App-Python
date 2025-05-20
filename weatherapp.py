import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

from dotenv import load_dotenv
import os


class Weather(QWidget):


    def __init__(self):

        super().__init__()


        self.degree_selection = "celcius"

        self.city_label = QLabel("Enter a city to view: ", self)
        self.city_input = QLineEdit(self)
        self.retrieve_weather_button = QPushButton("Get Weather Data",self)

        self.celcius_button = QPushButton("°C",self)
        self.fahrenheit_button = QPushButton("°F",self)

        self.temperature_label = QLabel(self)
        self.weather_icon_label = QLabel(self)
        self.weather_description_label = QLabel(self)
        #self.retrieve_weather_button = QPushButton("Get Weather Data",self)
        #self.temperature_label = QLabel("25°C", self)
        #self.weather_icon_label = QLabel(self)
        #self.weather_description_label = QLabel("Sunny", self)

        #self.setStyleSheet("background-color: #383838")

        self.initUI()
    

    def initUI(self):

        self.setWindowTitle("Weather App")
        self.setFixedSize(500, 720)
        self.setWindowIcon(QIcon("weather_icons/appicon.png"))

        #self.weather_icon_label.setGeometry(aw=25, ah=25)

        vbox = QVBoxLayout()
    
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.retrieve_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.weather_icon_label)
        vbox.addWidget(self.weather_description_label)

        hbox = QHBoxLayout()

        hbox.addWidget(self.celcius_button)
        hbox.addWidget(self.fahrenheit_button)

        vbox.addLayout(hbox)

        self.setLayout(vbox)


        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.weather_icon_label.setAlignment(Qt.AlignCenter)
        self.weather_description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temperature_label.setObjectName("temperature_label")
        self.weather_icon_label.setObjectName("weather_icon_label")
        self.weather_description_label.setObjectName("weather_description_label")

        self.setStyleSheet("""

            Weather {
                           
                background-color: #383838;
                color: white;
                margin-right: 10px; 
                margin-left: 10px; 
            }
                           
            QLabel {

                color: white;            
            }
                           
            QLabel#city_label {

                font-size: 30px;
                font-weight: bold;
                margin-top: 30px;
                margin-bottom: 30px;
            }
                           
            QLabel#temperature_label {

                font-size: 30px;
                font-weight: bold;
                margin-top: 30px;
                margin-bottom: 10px;
            }
                           
            QLabel#weather_description_label {

                font-size: 30px;
                font-weight: bold;
                margin-top: 5px;
                margin-bottom: 10px;
            }
                           
            QPushButton {
                           
                background-color: #454545;
                color: white;
                width: 40px;
                border-radius: 10px;
                padding: 10px;
                font-size: 20px;
                margin-right: 20px; 
                margin-left: 20px;
            }
                           
            QPushButton:hover {
                           
                background-color: #575757;
            }
                           
            QLineEdit {
                           
                background-color: #454545;
                           
                color: white;
                font-size: 20px;
                           
                border-radius: 10px;
                padding: 10px;
                           
                margin-bottom: 10px;
                max-width: 500px;
                           
                margin-right: 20px; 
                margin-left: 20px;
            }
                           
        """)


        self.celcius_button.setStyleSheet("background-color: #575757;")

        self.retrieve_weather_button.clicked.connect(self.get_weather)

        # Fahrenheit - Celcius Conversion
        self.celcius_button.clicked.connect(self.celcius_selection)
        self.fahrenheit_button.clicked.connect(self.fahrenheit_selection)

    def celcius_selection(self):
        self.degree_selection = "celcius"
        self.celcius_button.setStyleSheet("background-color: #575757;")
        self.fahrenheit_button.setStyleSheet("background-color: #454545;")
        #print(degree_selection)
    def fahrenheit_selection(self):
        self.degree_selection = "fahrenheit"

        self.fahrenheit_button.setStyleSheet("background-color: #575757;")
        self.celcius_button.setStyleSheet("background-color: #454545;")
        #print(degree_selection)

    def get_weather(self):
        print("button pressed")

        load_dotenv()
        api_key = os.getenv("API_KEY")

        city_entered = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_entered}&appid={api_key}"

        try:

            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data['cod'] == 200:
                
                self.display_weather(data)
        
        except requests.exceptions.HTTPError as http_error:

            match response.status_code:

                case 400:
                    self.error("Bad Request -- Check Input")
                case 401:
                    self.error("Unauthorized -- Invalid API Key")
                case 403:
                    self.error("Access Denied")
                case 404:
                    self.error("Not Found -- City Not Found")
                case 500:
                    self.error("Internal Server Error -- Try Again Later")
                case 502:
                    self.error("Bad Gateway -- Invalid response from the server")
                case 503:
                    self.error("Service Unavailable -- Try Again Later")
                case 504:
                    self.error("Gateway Timeout -- No response from the server")
                case _:
                    self.error(f"HTTP Error Occured -- {http_error}")
        
        
        except requests.exceptions.ConnectionError:
            print("Connection Error")
        
        except requests.exceptions.Timeout:
            print("Request Timed Out")
        
        except requests.exceptions.TooManyRedirects:
            print("Too many redirects")

        except requests.exceptions.RequestException as req_error:
            print(f"Request Error: {req_error}")


    def error(self, message):
        self.temperature_label.setText(message)

    def display_weather(self, data):
        
        temperature_kelvin = data["main"]["temp"]
        temperature_celcius = temperature_kelvin - 273.15
        temperature_fahrenheit = temperature_celcius * 1.8 + 32

        if self.degree_selection == "celcius":
            self.temperature_label.setText(f"{temperature_celcius:.1f}°C")
        else:
            self.temperature_label.setText(f"{temperature_fahrenheit:.1f}°F")

        weahter_description = data["weather"][0]["description"]
        self.weather_description_label.setText(weahter_description)

        weather_id = data["weather"][0]["id"]

        pixmap1 = QPixmap(self.weather_icon(weather_id))
        pixmap1 = pixmap1.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.weather_icon_label.setPixmap(pixmap1)


        print(data)


    @staticmethod
    def weather_icon(weather_id):
        
        if 200 <= weather_id <= 232:
            return "weather_icons/thunderstorm.png"
        
        elif 300 <= weather_id <= 321:
            return "weather_icons/drizzle.png"
        
        elif 500 <= weather_id <= 531:
            return "weather_icons/rainy.png"
        
        elif 600 <= weather_id <= 622:
            return "weather_icons/snowy.png"
        
        elif 700 <= weather_id <= 781:
            return "weather_icons/cloudy.png"
        
        elif weather_id == 800:
            return "weather_icons/sunny.png"
        
        elif weather_id >= 800:
            return "weather_icons/cloudy.png"

if __name__ == '__main__':

    app = QApplication(sys.argv)

    weather_app = Weather()
    weather_app.show()
    sys.exit(app.exec_())






