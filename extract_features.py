import socket
import requests
import re
import whois

# API key (replace with your actual key)
API_KEY = '90f7f4506ca48c67d4e15ca7c772b51f47723636c432a6e483a990b40df8d5a3a38c125eb6a2c3ee'
API_URL = 'https://ipqualityscore.com/api/json/ip/'

def get_ip_info(domain):
    try:
        ip = socket.gethostbyname(domain)
        response = requests.get(f'{API_URL}{API_KEY}/{ip}', timeout=5)
        if response.status_code == 200:
            data = response.json()
            return int(data.get("fraud_score", 0) > 70)  # 1 = suspicious, 0 = safe
        return 0
    except Exception:
        return 0

def extract_features(url):
    features = []
    
    # Basic structural features
    features.append(1 if re.match(r"http[s]?://\d+\.\d+\.\d+\.\d+", url) else 0)  # 1. UsingIP
    features.append(1 if len(url) > 75 else 0)                                  # 2. LongURL
    features.append(1 if re.search(r"bit\.ly|goo\.gl|tinyurl", url) else 0)     # 3. ShortURL
    features.append(1 if "@" in url else 0)                                     # 4. Symbol@
    features.append(1 if "//" in url[8:] else 0)                                # 5. Redirecting//
    features.append(1 if '-' in url.split('//')[-1].split('/')[0] else 0)       # 6. PrefixSuffix-
    features.append(len(url.split('.')) - 2 if len(url.split('.')) > 2 else 0)  # 7. SubDomains
    
    # Domain info features
    try:
        w = whois.whois(url)
        features.append(1 if 'https' in url.lower() else 0)                     # 8. HTTPS
        features.append(1 if w.expiration_date else 0)                         # 9. DomainRegLen
        features.append(len(w.domain_name[0]) if w.domain_name else 0)         # 10. DomainLength
    except Exception:
        features.append(0)  # HTTPS
        features.append(0)  # DomainRegLen
        features.append(0)  # DomainLength

    # Pad with zeros to match expected count (adjust after training output)
    while len(features) < 30:
        features.append(0)
    print(f"Extracted features for {url}: {features}")  # Debug print

    message = f"Feature extraction completed for {url}."
    return features, message