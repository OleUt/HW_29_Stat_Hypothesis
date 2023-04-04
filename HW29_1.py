import math
import scipy.stats

# interval_limits and frequencies
lim = [0, 24, 48, 72, 96, 120, 144, 168, 192, 216]
freq = [1, 2, 4, 6, 12, 16, 6, 2, 1]
n = 50
k = len(freq)
# H0: the distribution is normal

# interval midpoints
mid = []
for i in range(k):
    mid.append(lim[i] + (lim[i+1] - lim[i])/2)
print('interval midpoints:', mid)

# mean
mean = 0
for i in range(k):
    mean += mid[i] * freq[i]
mean = mean/n
print('mean =', mean)

# std dev
sd = 0
for i in range(k):
    # print('i=', i)
    sd += freq[i] * (mid[i] - mean)**2
sd = math.sqrt(sd/(n-1))
print('std dev =', sd)

# normalized interval limits + Laplace function
f = []
for i in range(k + 1):
    z_lim = (lim[i] - mean) / sd
    f.append(scipy.stats.norm.cdf(z_lim) - 0.5)

# expected freq normal distribution
ex_freq = []
for i in range(k):
    p = (f[i+1]-f[i])*n
    ex_freq.append(p)
print('expected freq normal distribution:', ex_freq)

print('H0: the distribution is normal')

# chi-square
chi = 0
for i in range(k):
    chi += (freq[i] - ex_freq[i]) **2 / ex_freq[i]
print('chi2 fact =', chi)

chi_tabl = scipy.stats.chi2.ppf((1-0.05), (k-2-1))
print('chi2 table =', chi_tabl)

if chi >= chi_tabl:
    print('H0 rejected, distribution is not normal')
else:
    print('H0 accepted, distribution is normal')
