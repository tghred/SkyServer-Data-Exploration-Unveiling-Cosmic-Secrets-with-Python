import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# الجزء الأول: تحليل ورسم الجرم الأكثر تكراراً
# ==========================================

# 1. قراءة البيانات
df = pd.read_csv('Skyserver.csv')

# 2. تحويل التاريخ والترتيب زمنيّاً
df['date'] = pd.to_datetime(df['mjd'], unit='D', origin='1858-11-17')
df = df.sort_values('date')
df.set_index('date', inplace=True)

# 3. عزل الجِرم الأكثر تكراراً في الملف
most_frequent_star = df['objid'].value_counts().index[0]
single_star = df[df['objid'] == most_frequent_star].copy()

# 4. حساب الفروقات ومؤشر اللون
single_star['r_diff'] = single_star['r'].diff()
single_star['u_r_color'] = single_star['u'] - single_star['r']

# حذف القيم الفارغة الناتجة عن الـ diff فقط للرسم
plot_data = single_star.dropna(subset=['r_diff'])

# 5. الرسم البياني الأول: المنحنى الضوئي والفروقات (Subplots)
fig, ax = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# الرسمة العلوية: المنحنى الضوئي
ax[0].plot(plot_data.index, plot_data['r'], color='royalblue', linewidth=0.8, alpha=0.5)
ax[0].scatter(plot_data.index, plot_data['r'], color='royalblue', s=25, label='Observed r')
ax[0].set_ylabel('Magnitude (r)')
ax[0].set_title(f'Stellar Light Curve for Object: {most_frequent_star}')
ax[0].invert_yaxis() # العكس الفلكي الصحيح لمحور السطوع

# الرسمة السفلية: الفروقات الزهرية
ax[1].plot(plot_data.index, plot_data['r_diff'], color='indianred', linewidth=0.8, alpha=0.5)
ax[1].scatter(plot_data.index, plot_data['r_diff'], color='indianred', s=25)
ax[1].set_ylabel('Difference (r_diff)')
ax[1].set_xlabel('Date')

plt.tight_layout()
plt.show() # إغلاق وعرض اللوحة الأولى بنجاح

# 6. الرسم البياني الثاني: فصل الـ Color-Magnitude Diagram في شكل مستقل
plt.figure(figsize=(8, 6))
plt.scatter(plot_data['r'], plot_data['u_r_color'], color='purple', alpha=0.7)
plt.xlabel('Apparent Magnitude (r)')
plt.ylabel('Color Index (u - r)')
plt.title(f'Color-Magnitude Diagram for Object: {most_frequent_star}')
plt.gca().invert_xaxis() # تذكري: في الفلك النجوم الأسطع (أقل قدر) تكون على اليسار غالباً
plt.show()


# ==========================================
# الجزء الثاني: مقارنة الأجرام الأربعة الأكثر تكراراً
# ==========================================

# 2. اختيار الأعمدة وعمل نسخة مستقلة
filter_data = df[['objid', 'u', 'r', 'g', 'i', 'z', 'mjd', 'redshift']].copy()

# إعادة ضبط الكشاف الزمني للنسخة الجديدة للتأكد من الترتيب
filter_data['date'] = pd.to_datetime(filter_data['mjd'], unit='D', origin='1858-11-17')
filter_data = filter_data.sort_values('date')
filter_data.set_index('date', inplace=True)

# طباعة الإحصائيات في الـ Terminal
print(f"Shape of filter data: {filter_data.shape}")
print(f"Number of unique objects: {filter_data['objid'].nunique()}")
print("\n3. أكثر الأجرام تكراراً في البيانات:")
print(filter_data['objid'].value_counts().head())

# مقارنة سريعة بين أول 4 أجرام
top_4_star = filter_data['objid'].value_counts().index[:4]

fig, ax = plt.subplots(2, 2, figsize=(12, 10), sharex=True, sharey=True)
ax_flat = ax.flatten()

for i, obj_id in enumerate(top_4_star):
    star_data = filter_data[filter_data['objid'] == obj_id].dropna(subset=['r'])
    
    # تجنب الخطأ إذا كان الـ redshift مفقوداً أو فارغاً
    if not star_data.empty and pd.notna(star_data['redshift'].iloc[0]):
        star_redshift = star_data['redshift'].iloc[0]
        title_text = f"Obj: {str(obj_id)[:7]}... | Redshift: {star_redshift:.3f}"
    else:
        title_text = f"Obj: {str(obj_id)[:7]}..."
    
    # الرسم النقطي والخطي
    ax_flat[i].plot(star_data.index, star_data['r'], color='royalblue', linewidth=0.8, alpha=0.5)
    ax_flat[i].scatter(star_data.index, star_data['r'], color='royalblue', s=20)
    ax_flat[i].set_title(title_text, fontsize=10)

# عكس المحور الصادي المشترك مرة واحدة لكل المحاور (بسبب sharey=True)
ax_flat[0].invert_yaxis()

# تسمية المحاور الخارجية
fig.text(0.5, 0.02, 'Date', ha='center', fontsize=12)
fig.text(0.02, 0.5, 'Magnitude (r)', va='center', rotation='vertical', fontsize=12)

plt.suptitle('Comparison of 4 Different Stellar Light Curves', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
ax[1].set_xlabel('Date')

plt.scatter(plot_data['r'], plot_data['u_r_color'], color='purple')
plt.xlabel('Apparent Magnitude (r)')
plt.ylabel('Color Index (u - r)')
plt.title('Color-Magnitude Diagram')
plt.show()

plt.tight_layout()
plt.show()




# 2. اختيار الأعمدة وعمل نسخة مستقلة تماماً في الذاكرة لـ filter_data
filter_data = df[['objid', 'u', 'r', 'g', 'i', 'z', 'mjd', 'redshift']].copy()
# تعديل التواريخ لتناسب ال mjd 
filter_data['date'] = pd.to_datetime(filter_data['mjd'], unit='D', origin='1858-11-17')
filter_data= filter_data.sort_values('date')
filter_data.set_index('date', inplace=True)

#عزل الجِرم الأكثر تكراراً في الملف

#معرفة عدد الصفوف والأعمدة
print(filter_data.shape)

#معرفة عدد الاجرام الفريدة

print(filter_data['objid'].nunique())

#معرفة أكثر النحوم تكرارا

print("\n3. أكثر الأجرام تكراراً في البيانات:")
print(filter_data['objid'].value_counts().head())


# مقارنة سريعة بين تلك الأجرام وسطوعها 
top_4_star = filter_data['objid'].value_counts().index[:4]


fig, ax = plt.subplots(2,2, figsize=(12,10), sharex=True, sharey=True)

# تحويل المصفوفة ثنائية الأبعاد (2,2) إلى قائمة أحادية (4 عناصر) لتسهيل المرور عليها بـ Loop
ax_flat = ax.flatten()
for i , obj_id in enumerate(top_4_star):
    #عزل بيانات الجرم الحالي     
    star_data = filter_data[filter_data['objid'] == obj_id].dropna(subset=['r'])
    # الحصول على قيمة الإزاحة الحمراء الثابتة له لتكتب في العنوان    
    star_redshift = star_data['redshift'].iloc[0]
    
    # الرسم النقطي والخطي للجرم    
    ax_flat[i].plot(star_data.index, star_data['r'], color='royalblue', linewidth = 0.8, alpha= 0.5)
    ax_flat[i].scatter(star_data.index, star_data['r'], color='royalblue', s=20)
    
    #العناوين    
    ax_flat[i].set_title(f"Obj: {str(obj_id)[:7]}... | Redshift: {star_redshift:.3f}", fontsize=10)
    
    # عكس المحور الصادي فلكياً لأننا نرسم الـ Magnitude
    ax_flat[i].invert_yaxis()
    
    
# تسمية المحاور الخارجية فقط لمنع الازدحام بفضل (sharex & sharey)
fig.text(0.5, 0.04, 'Date', ha='center', fontsize=12)
fig.text(0.04, 0.5, 'Magnitude (r)', va='center', rotation='vertical', fontsize=12)

plt.suptitle('Comparison of 4 Different Stellar Light Curves', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
