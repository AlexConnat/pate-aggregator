# Pate-Aggregator

### Init Script 

```
#!/bin/bash
sudo apt update
sudo apt install -y python python-pip
git clone https://github.com/AlexConnat/pate-aggregator /home/ubuntu
cd /home/ubuntu/pate-student/
pip --no-cache-dir install -r requirements.txt
cd teachers_predictions/
python receive_predictions.py
```

