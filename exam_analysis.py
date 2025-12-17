import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# ======================================
# 1) مسار الملف (حسب الهيكلة)
# ======================================

file_path = "Data/Clean_data.xlsx"

# ======================================
# 2) قراءة البيانات
# ======================================

male_df = pd.read_excel(file_path, sheet_name="Male")
female_df = pd.read_excel(file_path, sheet_name="Female")
time_df = pd.read_excel(file_path, sheet_name="Time")

# ======================================
# 3) أسماء الأسئلة (Parts)
# ======================================

questions = time_df["Question"].tolist()

# ======================================
# 4) حساب متوسط الدرجات
# ======================================

male_avg = male_df[questions].mean()
female_avg = female_df[questions].mean()

# ======================================
# 5) بناء جدول التحليل
# ======================================

analysis_df = pd.DataFrame({
    "Question": questions,
    "Male_AvgScore": male_avg.values,
    "Female_AvgScore": female_avg.values,
    "MaxPoints": time_df["MaxPoints"],
    "EstimatedTime": time_df["EstimatedTime"]
})

analysis_df["Male_ScoreRatio"] = (
    analysis_df["Male_AvgScore"] / analysis_df["MaxPoints"]
)

analysis_df["Female_ScoreRatio"] = (
    analysis_df["Female_AvgScore"] / analysis_df["MaxPoints"]
)

print("\nAnalysis Table:")
print(analysis_df)

# ======================================
# 6) تحليل العلاقة (Correlation)
# ======================================

male_corr, male_p = pearsonr(
    analysis_df["EstimatedTime"],
    analysis_df["Male_ScoreRatio"]
)

female_corr, female_p = pearsonr(
    analysis_df["EstimatedTime"],
    analysis_df["Female_ScoreRatio"]
)

print("\nCorrelation Results:")
print(f"Male: r = {male_corr:.3f}, p-value = {male_p:.4f}")
print(f"Female: r = {female_corr:.3f}, p-value = {female_p:.4f}")

# ======================================
# 7) الرسم البياني
# ======================================

plt.figure()
plt.scatter(
    analysis_df["EstimatedTime"],
    analysis_df["Male_ScoreRatio"],
    label="Male"
)
plt.scatter(
    analysis_df["EstimatedTime"],
    analysis_df["Female_ScoreRatio"],
    label="Female"
)

plt.xlabel("Estimated Time (minutes)")
plt.ylabel("Average Score Ratio")
plt.title("Estimated Time vs Student Performance")
plt.legend()
plt.show()
