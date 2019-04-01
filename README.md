# Pate-Student

### Init Script 

```
#!/bin/bash
sudo apt update
sudo apt install -y python python-pip
git clone https://github.com/AlexConnat/pate-student
cd pate-student/
pip --no-cache-dir install -r requirements.txt
cd teachers_predictions/
sudo python receive_predictions.py
```

