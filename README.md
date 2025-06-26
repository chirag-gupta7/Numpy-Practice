# NumPy Learning and Data Analysis Project

## Overview

This repository contains a comprehensive collection of Python scripts and examples demonstrating NumPy fundamentals, data analysis techniques, and practical applications. The project serves as both a learning resource and reference for NumPy array operations, statistical analysis, and data visualization.

## Project Structure

### Core NumPy Learning Files

#### `numpy_arange.py`
- **Purpose**: Demonstrates NumPy's `arange()` function for creating arrays with evenly spaced values
- **Key Concepts**: Array creation, start/stop/step parameters
- **Example**: Calculating Halley's Comet appearance years using arange with 76-year intervals

#### `numpy_shape_reshape.py`
- **Purpose**: Explores array shape properties and reshaping operations
- **Key Concepts**: `.shape` property, `.reshape()` method, dimensional transformations
- **Examples**: Converting 1D arrays to 2D, understanding array dimensions

### Data Analysis and Statistics Files

#### `bad_eggs.py`
- **Purpose**: Statistical analysis of egg freshness data using NumPy averages
- **Scenario**: Comparing three egg cartons to determine which has the lowest average freshness
- **Key Functions**: `np.average()` for calculating means across 2D arrays
- **Data Structure**: 2×6 arrays representing egg carton freshness ratings (0-1 scale)

#### `daily_Data.py`
- **Purpose**: Personal health data tracking and analysis
- **Tracked Metrics**: 
  - Sleep hours (April 2024)
  - Coffee consumption (cups per day)
  - Exercise duration (minutes per day)
- **Analysis**: Calculates and displays weekly averages for each metric
- **Data Structure**: 4×7 arrays representing weeks × days

#### `titanic.py`
- **Purpose**: Comprehensive analysis of Titanic passenger data
- **Dataset**: 50 passengers with columns: [ID, Survived, Class, Age]
- **Analysis Features**:
  - Survival statistics and percentages
  - Age demographics (oldest/youngest passengers)
  - Array shape and structure analysis
- **Key Functions**: `np.mean()`, `np.max()`, `np.min()`, `np.argmax()`, `np.argmin()`

#### `walking_Steps.py`
- **Purpose**: Weekly step count analysis and statistics
- **Data**: 7-day step tracking with detailed statistical analysis
- **Features**:
  - Daily step counts and weekly totals
  - Statistical measures (min, max, mean, standard deviation)
  - Activity pattern identification (most/least active days)
- **Educational Focus**: Understanding axis operations and NumPy statistical functions

#### `tallest_bulding.py`
- **Purpose**: Unit conversion demonstration using NumPy array operations
- **Functionality**: Converts building heights from feet to meters
- **Data**: Array of world's tallest building heights
- **Key Concept**: Element-wise array operations and multiplication

### Advanced Data Tracking

#### `dear_data.py`
- **Purpose**: Comprehensive personal data tracking inspired by the "Dear Data" project
- **Tracked Activities**:
  - ☕ Coffee consumption (hourly tracking)
  - 📱 Phone pickups (daily totals)
  - 👟 Step counting (hourly detail)
- **Features**:
  - Multiple data visualization types
  - 1D vs 2D array comparison
  - Advanced indexing and slicing demonstrations
  - Statistical analysis across different time periods
- **Dependencies**: matplotlib for visualization
- **Educational Value**: Demonstrates when to use different array dimensions

### Jupyter Notebook

#### `observational_data_analysis.ipynb`
- **Purpose**: Interactive data analysis and visualization
- **Format**: Jupyter Notebook for exploratory data analysis
- **Use Case**: Combining code, narrative text, and visualizations

## Requirements

- Python 3.x
- NumPy
- matplotlib (for dear_data.py visualizations)
- Jupyter Notebook (for .ipynb file)

## Installation

1. Ensure Python 3.x is installed on your system
2. Install required dependencies:
   ```bash
   pip install numpy matplotlib jupyter
   ```
3. Clone or download the repository files

## Usage

### Running Individual Scripts

Each Python file can be executed independently:

```bash
python bad_eggs.py          # Egg freshness analysis
python daily_Data.py        # Personal health metrics
python numpy_arange.py      # Array creation examples
python numpy_shape_reshape.py  # Shape and reshape demonstrations
python titanic.py           # Titanic passenger analysis
python walking_Steps.py     # Step count statistics
python tallest_bulding.py   # Unit conversion example
python dear_data.py         # Comprehensive data tracking
```

### Running the Jupyter Notebook

```bash
jupyter notebook observational_data_analysis.ipynb
```

## Key Learning Objectives

### NumPy Fundamentals
- Array creation with `np.array()` and `np.arange()`
- Understanding array shapes and dimensions
- Reshaping arrays for different data structures

### Statistical Analysis
- Calculating averages, means, and other descriptive statistics
- Finding minimum and maximum values
- Using `argmin()` and `argmax()` for index location

### Data Structures
- When to use 1D vs 2D arrays
- Organizing time-series data
- Handling multi-dimensional datasets

### Array Operations
- Element-wise operations and transformations
- Axis-specific operations (axis=0 vs axis=1)
- Indexing and slicing techniques

## File Categories

| Category | Files | Focus |
|----------|-------|-------|
| **NumPy Basics** | `numpy_arange.py`, `numpy_shape_reshape.py` | Core array operations |
| **Data Analysis** | `bad_eggs.py`, `daily_Data.py`, `titanic.py` | Statistical analysis |
| **Personal Tracking** | `walking_Steps.py`, `dear_data.py` | Real-world data applications |
| **Utilities** | `tallest_bulding.py` | Unit conversions |
| **Interactive** | `observational_data_analysis.ipynb` | Jupyter-based analysis |

## Examples of Key Concepts

### Array Creation and Manipulation
```python
# From numpy_arange.py
arr = np.arange(start=1986, stop=3001, step=76)  # Halley's Comet years

# From numpy_shape_reshape.py  
arr = arr.reshape(2, 4)  # Convert 1D to 2D array
```

### Statistical Analysis
```python
# From titanic.py
survival_percentage = (survivors / total_passengers) * 100
average_age = np.mean(passengers[:, 3])

# From walking_Steps.py
weekly_average = np.mean(weekly_steps)
max_day_index = np.argmax(weekly_steps)
```

### Data Tracking Patterns
```python
# From dear_data.py
daily_totals = np.sum(coffee_data, axis=0)  # Sum across hours
hourly_totals = np.sum(coffee_data, axis=1)  # Sum across days
```

## Educational Value

This collection demonstrates:
- **Progressive Learning**: From basic array operations to complex data analysis
- **Real-World Applications**: Using actual scenarios (Titanic data, personal tracking)
- **Best Practices**: Proper array dimensionality and statistical analysis
- **Visualization**: Integration with matplotlib for data presentation

## Contributing

When adding new examples:
1. Include clear comments explaining NumPy concepts
2. Use realistic datasets when possible
3. Demonstrate multiple NumPy functions per file
4. Add statistical analysis and insights

## Version History

- v1.0: Initial collection of NumPy learning examples
- Current: Comprehensive data analysis and tracking examples

## See Also

- [NumPy Documentation](https://numpy.org/doc/)
- [Dear Data Project](https://www.dear-data.com/) - Inspiration for personal data tracking
- [Matplotlib Documentation](https://matplotlib.org/) - For visualization examples
