# sockop-benchmark
Verify the runtime of eBPF helper functions to write/read TCP Header option 

## Load eBPF program
```
sudo ./sockop
```

## Get eBPF logs
```
sudo cat /sys/kernel/debug/tracing/trace_pipe 2>&1 | tee -a log.txt
```

## Run HTTP Server in Python 
```
# Use port 8888 or 55555 only
python3 -m http.server 55555
```

## Run the program to send requests on another terminal
```
# first argument is port number, second argument is number of requests
python3 send 8888 10000
```

