def handler(signum, frame):
    print(f"Signal handler called with signal: {signum}")

import signal, time
signal.signal(signal.SIGINT, handler)

# partie "attente"
#time.sleep(100)
signal.pause()