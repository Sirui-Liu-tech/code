import matplotlib.pyplot as plt

data = [
    [110.15, 5087, 0.184, 0.018382904],
    [106.00, 5366, 0.176, 0.017583647],
    [105.00, 5458, 0.173, 0.017283926],
    [103.47, 5574, 0.172, 0.017184019],
    [102.20, 5623, 0.170, 0.016984205],
    [101.20, 5688, 0.169, 0.016884298],
    [100.00, 5765, 0.167, 0.016684483],
    [98.40, 5868, 0.164, 0.016384762],
    [97.60, 5916, 0.163, 0.016284855],
    [96.00, 6015, 0.161, 0.016085041],
    [94.30, 6132, 0.159, 0.015885227],
    [92.78, 6222, 0.156, 0.015585505],
    [90.08, 6394, 0.152, 0.015185877],
    [87.97, 6527, 0.150, 0.014986063],
    [85.40, 6692, 0.145, 0.014486528],
    [82.75, 6857, 0.142, 0.014186806],
    [79.65, 7046, 0.138, 0.013787178],
    [77.04, 7207, 0.134, 0.01338755],
    [74.91, 7336, 0.131, 0.013087828],
    [72.69, 7473, 0.128, 0.012788107],
    [70.25, 7615, 0.126, 0.012588293],
    [68.68, 7713, 0.124, 0.012388479],
    [66.49, 7842, 0.121, 0.012088757],
    [64.41, 7965, 0.119, 0.011888943],
    [62.70, 8066, 0.117, 0.011689129],
    [60.80, 8179, 0.115, 0.011489315],
    [58.50, 8310, 0.112, 0.011189594],
    [56.77, 8413, 0.110, 0.01098978],
    [53.70, 8593, 0.107, 0.010690058],
    [51.56, 8718, 0.104, 0.010390337],
    [49.17, 8853, 0.101, 0.010090616],
    [47.64, 8941, 0.099, 0.009890802],
    [44.73, 9105, 0.096, 0.00959108],
    [43.01, 9199, 0.094, 0.009391266],
    [41.83, 9279, 0.092, 0.009191452],
    [40.63, 9341, 0.090, 0.008991638],
    [38.97, 9430, 0.089, 0.008891731],
    [37.90, 9491, 0.087, 0.008691917],
    [36.46, 9570, 0.084, 0.008392195],
    [35.11, 9646, 0.082, 0.008192381],
    [34.18, 9695, 0.081, 0.008092474],
    [33.08, 9753, 0.078, 0.007792753],
    [32.48, 9786, 0.077, 0.007692846],
    [31.43, 9852, 0.076, 0.007592939],
    [30.46, 9903, 0.073, 0.007293217],
    [29.62, 9946, 0.071, 0.007093403],
    [28.74, 9993, 0.068, 0.006793682],
    [28.63, 9997, 0.068, 0.006793682],
    [26.56, 10101, 0.054, 0.005394983],
    [26.50, 10105, 0.052, 0.005195168],
    [26.38, 10110, 0.047, 0.004695633]
]

pt_values = [row[0] for row in data]
si_values = [row[2] for row in data]

plt.scatter(pt_values, si_values)
plt.xlabel('Pt')
plt.ylabel('Si')
plt.title('Scatter Plot: Pt vs. Si')

plt.show()
