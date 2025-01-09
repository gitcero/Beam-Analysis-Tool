# Beam Analysis Tool

This project provides a modular Python tool for performing beam analysis with:
- Point Loads
- Moments
- Distributed Loads (rectangular, triangular, and trapezoidal)

## 📦 Project Structure

The code is organized into separate modules for clarity and maintainability:

- `main.py`: The main script that runs the analysis.
- `user_input.py`: Manages all user input and data collection.
- `distributed_loads.py`: Converts distributed loads into equivalent point loads.
- `reactions.py`: Calculates reactions for statically determinate beams.

## 🚀 Features
- Supports point loads, moments, and distributed loads.
- Calculates reactions for:
  - Simply supported beams
  - Beams with a single fixed or simple support
- Handles triangular, rectangular, and trapezoidal distributed loads.

## 📐 Reference System
- All force positions and support positions should be measured from the **left end** of the beam.

## 📊 Example Usage
```bash
python main.py
```
Follow the prompts to enter beam data, supports, and loads. The tool will calculate and display the reactions with detailed descriptions.

## 📚 Requirements
- Python 3.x

## 📥 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/git-cero/Beam-Analysis-Tool.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Beam-Analysis-Tool
   ```
3. Run the tool:
   ```bash
   python main.py
   ```

## ✅ Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## 📄 License
This project is licensed under the MIT License.