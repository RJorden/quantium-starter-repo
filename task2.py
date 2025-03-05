import pandas as pd
import sys, os

directory = sys.argv[1]

if not os.path.exists(directory):
    sys.exit(f'Directory {directory} does not exist')

files = []

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        files.append(pd.read_csv(os.path.join(directory, filename)))

df = pd.concat(files)

# we are only interested in Pink Morsel sales
df = df[df['product'] == 'pink morsel']
# create sales column (price * quantity)
df['sales'] = df.apply(lambda x: f"${float(x['price'][1:]) * x['quantity']:.2f}", axis=1)
# we only need sales, date and region
df.drop(columns=['product','price','quantity'])
# reorder columns
df = df.reindex(['sales','date','region'], axis=1).to_csv('pink_morsel_sales.csv', index=False)
