# Santa's Gift Dash 
Santa's Gift Dash is a fun and exciting 2platformer game where players must dodge obstacles, collect falling gifts, and avoid the mischievous Grinch! The goal is to rack up points by collecting as many gifts as possible while staying alive.

 ## Table of Contents
    About the Game
    Features
    Installation
    How to Play
    Assets and Images
    Game Controls
    License

 ### About the Game
In Santa's Gift Dash, the player controls a character who must move left and right to collect falling gifts dropped by Santa while avoiding the Grinch and dodging obstacles. Players have a limited number of lives, and the game is won if they survive for 5 minutes while accumulating as many points as possible.

 ### Features

    Gift Collection: Collect gifts dropped by Santa for points.
    Avoid Enemies: Dodge the Grinch and incoming obstacles to avoid losing lives.
    Custom Graphics: Unique sprites for characters, gifts, and obstacles.
    Time Limit: Win the game by surviving for 5 minutes.
    Game Over Conditions: Lose if you run out of lives.
    Pause Functionality: Pause and resume the game anytime with a single key press.

 ### Installation
To run the game locally, follow these steps:

### Prerequisites:
        Python 3.x installed on your system.
        Pygame library installed. If not, run the following command:

    pip install pygame

Download the Project:

    Clone the repository or download the project folder.

    git clone https://github.com/yourusername/santas-gift-dash.git

Run the Game:

    Navigate to the project folder and run the main script.

        cd santas-gift-dash
        python main.py

 ### How to Play

    Objective: Collect as many gifts as possible while avoiding obstacles and enemies.

    Survive: Make it through 5 minutes without losing all your lives.

    Scoring:
        Collecting a gift = +10 points
        Missing a gift = -1 life

    Game Over:
        Lose all lives, and it's Game Over.
        Survive 5 minutes, and you Win!

 ### Assets and Images

Place all image assets in the following directory structure:

project-folder/
│
├── assets/
│   └── images/
│       ├── santa.png
│       ├── player.png
│       ├── gift.png
│       ├── grinch.png
│       ├── background.png
│       └── obstacles.png
│
├── main.py
└── README.md



### Game Controls
Key	Action
Left Arrow	Move left
Right Arrow	Move right
Spacebar	Jump
P	Pause/Unpause the game
R	Restart the game after loss
Escape	Quit the game


## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the project with proper attribution.