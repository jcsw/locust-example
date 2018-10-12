# Locust Example #

### Example load testing with Locust ###

Install with Ubuntu
```
sudo apt-get install python3 python3-pip
python3 -m pip install locustio
```

Run
```
locust -f math-api.py --host=http://localhost:9900
```

To access web ui
```
http://localhost:8089/
```

Locust Documentation
```
https://docs.locust.io/en/latest/what-is-locust.html
```