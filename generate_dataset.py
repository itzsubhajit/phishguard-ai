import pandas as pd
import random
import os

phishing_urls = []
legit_urls = []

# Generate 500 phishing URLs
for i in range(500):
    prefixes = ['http://', 'http://www.']
    domains = [f"login-verify-{i}.com", f"secure-account-{i}.net", f"update-banking-{i}.org", f"signin-confirm-{i}.xyz"]
    paths = ['/login', '/verify', '/account/update', '/secure/confirm']
    query = f"?id={random.randint(1000,9999)}" if random.random() > 0.5 else ""
    url = random.choice(prefixes) + random.choice(domains) + random.choice(paths) + query
    phishing_urls.append(url)

# Generate 500 legit URLs
for i in range(500):
    prefixes = ['https://', 'https://www.']
    domains = [f"google-{i}.com", f"example-{i}.org", f"site-{i}.net", f"blog-{i}.io"]
    paths = ['/', '/about', '/contact', '/home']
    query = f"?user={random.randint(1,100)}" if random.random() > 0.8 else ""
    url = random.choice(prefixes) + random.choice(domains) + random.choice(paths) + query
    legit_urls.append(url)

df = pd.DataFrame({
    'url': phishing_urls + legit_urls,
    'label': [1]*500 + [0]*500
})
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

os.makedirs('training/data', exist_ok=True)
df.to_csv('training/data/dataset.csv', index=False)
print("Generated synthetic dataset at training/data/dataset.csv")
