# Local Notepad

A simple local web-based notepad that allows editing and sharing text across devices in the same network.

## Features
- Real-time text editing and saving.
- Accessible from any device within the local network.
- Dark theme for comfortable night-time use.

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/local-notepad.git
cd local-notepad
```

### 2. Install Dependencies
Make sure you have **Python 3** installed, then install Flask:
```sh
pip install flask
```

### 3. Run the Server
```sh
python server.py
```

### 4. Access the Notepad
Open a browser and go to:
```sh
http://127.0.0.1:5000
```
To access it from another device on the same Wi-Fi network, find your local IP address and replace `127.0.0.1` with it.

## File Structure
```
local-notepad/
│── server.py        # Main Flask server
│── README.md        # Project documentation
└── templates/
    └── index.html   # Frontend HTML template
```

## License
This project is open-source and available under the MIT License.
