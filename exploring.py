
import numpy as np
import matplotlib.pylab as plt
import problem_set1 as ps1

# -----------------------------------------------------------------------------

filename = "spikes_example.npy"
answersFile = "spikes_example_answers.npy"

# -----------------------------------------------------------------------------

plt.close('all')

data = np.load(filename)[()];
t = data['time']
v = data['voltage']

plt.figure()

plt.plot(t, v)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (uV)')
plt.title('Spikes in Raw Signal')
plt.show()

vClipped = np.copy(v)

threshold = max(v)*1.45/4

for ix in range(len(vClipped)):
    if (vClipped[ix] < threshold):
        vClipped[ix] = 0

plt.hold = True

APTimes = []
for ix in range(len(vClipped)-1):
    if (vClipped[ix+1] > vClipped[ix]):
        currentMax = ix+1
    elif (vClipped[ix+1] < vClipped[ix]):
        APTimes.append(t[currentMax])
APTimes = np.unique(APTimes)

APMarks = np.ones(len(APTimes)) * max(v) + max(v)/4

plt.plot(APTimes, APMarks, 'rv', linewidth=50)

actualTimes = ps1.get_actual_times(answersFile)
ps1.detector_tester(APTimes, actualTimes)

plt.figure()
plt.xlabel('Time (s)')
plt.ylabel('Voltage (uV)')
plt.title('Spike waveforms')

halfWindow = 0.003 # in seconds
samplingTime = np.absolute(np.diff(t)[0])
numOfSamplesInHalfWindow = halfWindow//samplingTime
spikeWindow = np.arange(-halfWindow, halfWindow+samplingTime, samplingTime)

for APtime in APTimes:
    for idx in range(len(t)):
        if (t[idx] == APtime):
            spikeIndex = idx
            startIndex = spikeIndex-numOfSamplesInHalfWindow
            endIndex = startIndex + len(spikeWindow)
            spikeVoltage = v[startIndex:endIndex]
            plt.plot(spikeWindow, spikeVoltage)

# -----------------------------------------------------------------------------
