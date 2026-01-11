import subprocess, time


while True:
  p = subprocess.Popen(["python", "main.py"])
  p.wait()
  time.sleep(5)