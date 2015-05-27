# Detecting Spikes

This piece of Python code functions as a *spike detector*, returning the times that an action potential occurred in an electrical signal recorded from a neuron.

The spike detector was submitted to fulfil the requirements of the [Exploring Neural Data](https://class.coursera.org/neuraldata-001) course offered by Brown university through Coursera.

The Python script operates on two sets of neural recordings (easy and hard), plots the spike times for each, the action potential waveforms and prints some performance criteria. 

## Example

The outputs for the example dataset are illustrated below.

![](https://github.com/alkashef/detectingspikes/raw/master/AP_example.png)

![](https://github.com/alkashef/detectingspikes/raw/master/Waveform_example.png)

    Action Potential Detector Performance: 
        Correct number of action potentials = 20
        Percent True Spikes = 100.0
        False Spike Rate = 0.0 spikes/s

## Project Setup

### Dependencies

This project was developed using the Anaconda Python distribution running Python 2.7.8 on a Windows 7 64-bit machine.

### Project Files

- **README.md:** This file.

- **Problem Set 1.pdf:** Provides context, describes the dataset, and the requirements of this assignment.

- **\*.npy**: Example, easy, hard and challenge datasets.

- **exploring.py:** Script used to explore the example dataset.

- **problem_set1.py:** Spike detector script.

- **problem_set1_submit.py:** Script used to submit the spike detector for evaluation.

- **\*.png:** Output spike times and action potential waveform plots for the easy and the hard datasets.
 
## Contributors

The data and the code except for **exploring.py** and the following functions in **problem_set1.py**, were given by the course instructors: 
- **good_AP_finder()**
- **plot_spikes()**
- **plot_waveforms()**

## License

This is an open source free program provided under The MIT License (MIT). A copy of the license is available in LICENSE.txt at the root of the source code. If not, please see <http://opensource.org/licenses/MIT>.