# Game Of Life
Simplistic Python implementation of Conway's Game of Life.

# Usage
Clone the repository using:
```
git clone https://github.com/piyushagade/Game-Of-Life.git
```

Tweak the universe (culture) by changing the system variable in **game_of_life.py**
The changeable varialbles are:

1. width, height (Obvious)
2. life_of_culture (Number of maximum generation to be simulated)
3. age_of_culture (Current age of culture)
4. no_of_seeds  (Number of first generation organisms)

Simulate the culture using:
```
cd Game-Of-Life
python game_of_life.py
```
# Output
The program generates PNG files in 'png' directory, which can be accessed using:
```
cd png
0.png
1.png
.
.
.
```
and a GIF animation in 'gif' folder, which can be accessed using:
```
cd gif
animation.gif
```

# Dependencies
1. matplotlib
2. numpy
3. imageio

# Screenshots
<img src="http://i.imgur.com/YF8MqRX.png">
<img src="http://i.imgur.com/7CmTSfv.png">
<img src="http://i.imgur.com/qACTKTq.png">
