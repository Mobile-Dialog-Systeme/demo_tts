#!/bin/bash
SCRIPT_DIR=$(dirname "$0")
WORKSPACE_DIR=$(realpath "$SCRIPT_DIR/src")

if grep -qEi "(Microsoft|WSL)" /proc/version &> /dev/null; then
    PULSE_VOLUME="/mnt/wslg/PulseServer:/run/user/1000/pulse/native"
else
    PULSE_VOLUME="/run/user/1000/pulse:/run/user/1000/pulse"
fi
docker run -it --rm --network=host --volume="$WORKSPACE_DIR:/home/rosdev/ros2_ws/src/" --volume="$PULSE_VOLUME" --privileged demo_tts:latest