# Investment Optimization Program

## Overview

The Investment Optimization Program is designed to assist in making strategic investment decisions. It leverages various algorithms - Brute Force, Glouton (Greedy), and Dynamic Programming - to analyze and select the best combination of stock actions that maximize profit while adhering to a specified budget.

## Features

- **Data Processing**: Loads and cleans stock action data from a CSV file.
- **Algorithm Selection**: Offers the choice of three distinct algorithms:
  - **Brute Force**: Exhaustively searches all possible combinations of actions.
  - **Glouton (Greedy)**: Utilizes a greedy approach for quick and effective decision-making.
  - **Dynamic Programming**: Applies a more sophisticated method to solve the problem efficiently.
- **Result Visualization**: Displays the best combination of actions, total profit, and investment cost.

## How to Use

1. **Clone the Repository**

```code
git clone https://github.com/kenza12/Projet-7.git
cd Projet-7
```

2. **Set Up Your Environment**

- Ensure Python 3 is installed on your system.
- Create a virtual environment:
  
```code
  python3 -m venv venv
```

- Activate the virtual environment:
  - On Windows: `venv\Scripts\activate`
  - On macOS/Linux: `source venv/bin/activate`

- Install dependencies:
  
```code
  pip install -r requirements.txt
```

3. **Run the Program**

Execute the script with the desired algorithm and data file:

```code
python main.py path/to/your/datafile.csv [algorithms]
```

Replace `[algorithms]` with one or more of the following: `bruteforce`, `glouton`, `dynamic`.

4. **View Results**

The program will output the most profitable combination of actions based on the chosen algorithm.

## Dependencies

- Python 3
- Pandas
- Numpy
- tabulate