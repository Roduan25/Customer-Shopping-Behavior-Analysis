import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. تحميل البيانات
df = pd.read_csv('customer_shopping_behavior.csv')

# 2. إعادة تشكيل البيانات (Reshaping)
# سنقوم بحساب مجموع المشتريات لكل فئة (Category) موزعة على فصول السنة (Season)
heatmap_data = df.pivot_table(index='Category', 
                             columns='Season', 
                             values='Purchase Amount (USD)', 
                             aggfunc='sum')

# 3. إعداد الشكل البصري
plt.figure(figsize=(10, 8))
sns.set_theme(style="white")

# 4. رسم الخريطة الحرارية
# annot=True لإظهار الأرقام داخل المربعات، cmap لاختيار الألوان
sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="YlGnBu", 
            cbar_kws={'label': 'Total Revenue (USD)'})

# إضافة العناوين
plt.title('Total Revenue by Category and Season', fontsize=15, pad=20)
plt.xlabel('Season', fontsize=12)
plt.ylabel('Category', fontsize=12)

# 5. حفظ الصورة لاستخدامها في GitHub
plt.savefig('category_season_heatmap.png', bbox_inches='tight')
print("✅ Heatmap saved as 'category_season_heatmap.png'")