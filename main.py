import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv('customer_shopping_behavior.csv')

# 2. Data Reshaping
# Calculate the total purchase amount for each Category across different Seasons
heatmap_data = df.pivot_table(index='Category', 
                             columns='Season', 
                             values='Purchase Amount (USD)', 
                             aggfunc='sum')

# 3. Set Visual Theme
plt.figure(figsize=(10, 8))
sns.set_theme(style="white")

# 4. Draw the Heatmap
# annot=True displays numbers inside cells, cmap sets the color palette
sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="YlGnBu", 
            cbar_kws={'label': 'Total Revenue (USD)'})

# Adding Titles and Labels
plt.title('Total Revenue by Category and Season', fontsize=15, pad=20)
plt.xlabel('Season', fontsize=12)
plt.ylabel('Category', fontsize=12)

# 5. Save the image for GitHub use
plt.savefig('category_season_heatmap.png', bbox_inches='tight')
print("✅ Heatmap saved as 'category_season_heatmap.png'")
