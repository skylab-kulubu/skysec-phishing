# SKY SEC Oltalama Sistemi

# Docker Yükleme
```bash
curl -L https://get.docker.com > /tmp/install_docker.sh;yes y|bash /tmp/install_docker.sh
```

# Compose İle Çalıştırma
```bash
sudo docker compose up -d
```

# Python İle Çalıştırma
```bash
./phishing/manage.py runserver 0.0.0.0:8000
```

# Dikkat!

Konteynerlerleri sırayla çalıştırmanız gerekebilir! Sırasıyla:

```bash
docker compose up -d db
```

```bash
docker compose up -d app
```

```bash
docker compose up -d nginx
```