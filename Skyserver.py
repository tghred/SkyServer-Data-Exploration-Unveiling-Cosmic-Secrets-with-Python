import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# PART 1: Analyzing and Plotting the Most Frequent Object
# الجزء الأول: تحليل ورسم الجرم الأكثر تكراراً
# ==========================================

# 1. Read the data / قراءة البيانات
df = pd.read_csv('Skyserver.csv')

# 2. Convert date format and sort chronologically / تحويل التاريخ والترتيب زمنيّاً
# Converting Modified Julian Date (MJD) to standard datetime
# تحويل التاريخ الميقاتي المعدل إلى تاريخ قياسي
df['date'] = pd.to_datetime(df['mjd'], unit='D', origin='1858-11-17')
df = df.sort_values('date')
df.set_index('date', inplace=True)

# 3. Isolate the most frequent object in the file / عزل الجِرم الأكثر تكراراً في الملف
most_frequent_star = df['objid'].value_counts().index[0]
single_star = df[df['objid'] == most_frequent_star].copy()

# 4. Calculate magnitude differences and color index / حساب الفروقات ومؤشر اللون
single_star['r_diff'] = single_star['r'].diff() # Light variation / معدل التغير الضوئي
single_star['u_r_color'] = single_star['u'] - single_star['r'] # (u - r) Color Index / مؤشر اللون

# Drop NaN values resulting from .diff() for plotting / حذف القيم الفارغة الناتجة عن الفروقات للرسم فقط
plot_data = single_star.dropna(subset=['r_diff'])

# 5. Plot 1: Light Curve and Differences (Subplots) / الرسمة الأولى: المنحنى الضوئي والفروقات
fig, ax = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Top Plot: Light Curve / الرسمة العلوية: المنحنى الضوئي
ax[0].plot(plot_data.index, plot_data['r'], color='royalblue', linewidth=0.8, alpha=0.5)
ax[0].scatter(plot_data.index, plot_data['r'], color='royalblue', s=25, label='Observed r')
ax[0].set_ylabel('Magnitude (r)')
ax[0].set_title(f'Stellar Light Curve for Object: {most_frequent_star}')
ax[0].invert_yaxis() # Astronomical inversion for magnitude / العكس الفلكي الصحيح لمحور السطوع

# Bottom Plot: Magnitude Differences / الرسمة السفلية: الفروقات الزهرية
ax[1].plot(plot_data.index, plot_data['r_diff'], color='indianred', linewidth=0.8, alpha=0.5)
ax[1].scatter(plot_data.index, plot_data['r_diff'], color='indianred', s=25)
ax[1].set_ylabel('Difference (r_diff)')
ax[1].set_xlabel('Date')

plt.tight_layout()
plt.show() # Display and close the first figure / عرض وإغلاق اللوحة الأولى بنجاح

# 6. Plot 2: Color-Magnitude Diagram (CMD) / الرسمة الثانية: مخطط اللون والقدر مستقلّاً
plt.figure(figsize=(8, 6))
plt.scatter(plot_data['r'], plot_data['u_r_color'], color='purple', alpha=0.7)
plt.xlabel('Apparent Magnitude (r)')
plt.ylabel('Color Index (u - r)')
plt.title(f'Color-Magnitude Diagram for Object: {most_frequent_star}')
plt.gca().invert_xaxis() # Brighter stars are typically on the left / النجوم الأسطع تكون على اليسار فلكياً
plt.show()


# ==========================================
# PART 2: Comparison of the Top 4 Most Frequent Objects
# الجزء الثاني: مقارنة الأجرام الأربعة الأكثر تكراراً
# ==========================================

# 1. Select specific columns and create a clean copy / اختيار الأعمدة وعمل نسخة مستقلة تماماً
filter_data = df[['objid', 'u', 'r', 'g', 'i', 'z', 'mjd', 'redshift']].copy()

# Reset time index for the new dataframe / إعادة ضبط الكشاف الزمني للنسخة الجديدة للتأكد من الترتيب
filter_data['date'] = pd.to_datetime(filter_data['mjd'], unit='D', origin='1858-11-17')
filter_data = filter_data.sort_values('date')
filter_data.set_index('date', inplace=True)

# Print summary statistics in the terminal / طباعة الإحصائيات في الـ Terminal
print(f"Shape of filter data: {filter_data.shape}")
print(f"Number of unique objects: {filter_data['objid'].nunique()}")
print("\n3. Top frequent objects in data / أكثر الأجرام تكراراً في البيانات:")
print(filter_data['objid'].value_counts().head())

# Get IDs of the top 4 most observed objects / استخراج معرفات أكثر 4 أجرام رُصدت
top_4_star = filter_data['objid'].value_counts().index[:4]

# Create a 2x2 grid for comparison / إنشاء شبكة رسم 2 في 2 للمقارنة
fig, ax = plt.subplots(2, 2, figsize=(12, 10), sharex=True, sharey=True)
ax_flat = ax.flatten() # Flatten 2D array to 1D for easy looping / تحويل المصفوفة لسلسلة أحادية لسهولة المرور

for i, obj_id in enumerate(top_4_star):
    # Isolate data for the current object / عزل بيانات الجرم الحالي
    star_data = filter_data[filter_data['objid'] == obj_id].dropna(subset=['r'])
    
    # Handle redshift text to avoid errors if missing / التعامل مع قيمة الإزاحة الحمراء لتجنب الأخطاء
    if not star_data.empty and pd.notna(star_data['redshift'].iloc[0]):
        star_redshift = star_data['redshift'].iloc[0]
        title_text = f"Obj: {str(obj_id)[:7]}... | Redshift: {star_redshift:.3f}"
    else:
        title_text = f"Obj: {str(obj_id)[:7]}..."
    
    # Plotting line and scatter points / الرسم النقطي والخطي للجرم الحالي
    ax_flat[i].plot(star_data.index, star_data['r'], color='royalblue', linewidth=0.8, alpha=0.5)
    ax_flat[i].scatter(star_data.index, star_data['r'], color='royalblue', s=20)
    ax_flat[i].set_title(title_text, fontsize=10)

# Invert y-axis once for all shared subplots / عكس المحور الصادي المشترك مرة واحدة لكل المحاور
ax_flat[0].invert_yaxis()

# Labeling global axes / تسمية المحاور الخارجية المشتركة
fig.text(0.5, 0.02, 'Date', ha='center', fontsize=12)
fig.text(0.02, 0.5, 'Magnitude (r)', va='center', rotation='vertical', fontsize=12)

plt.suptitle('Comparison of 4 Different Stellar Light Curves', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
