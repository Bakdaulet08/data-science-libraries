from scipy import stats

ages = [34, 37, 13, 64, 37, 47, 24, 38, 26, 41, 19, 51, 44]

t_stat, p_value = stats.ttest_1samp(ages, popmean=30)
print(f"T-test: {t_stat}, P-value: {p_value}")

group1 = [23, 25, 31, 35, 45]
group2 = [45, 51, 61, 35, 23]

stat, p_value = stats.mannwhitneyu(group1, group2)
print(f"U-stats: {stat}, P-value: {p_value}")