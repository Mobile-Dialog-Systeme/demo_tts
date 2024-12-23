# Demo TTS Project

This project sets up a Docker container based on ROS Iron and tests out the TTS framework Coqui TTS.
## Setup

### Build the Docker Image

To build the Docker image, run the following command in the root directory of the project:

```sh
docker build -t demo_tts .
```

### Run the Docker Container

To run the Docker container and start a shell session, use the following command:

```sh
docker run -it --rm demo_tts
```

### Start the TTS Script Manually

Once inside the Docker container, you can start the TTS script manually by running:

```sh
/start_tts.sh
```

## Development

### Project Structure

- `src/`: Contains the source code for the project.
  - `main.py`: Entry point for the TTS script.
  - `__init__.py`: Package initialization file.
- `requirements.txt`: Lists the Python dependencies.
- `setup.py`: Setup script for packaging the Python project.
- `start_tts.sh`: Shell script to start the TTS script.
- `Dockerfile`: Docker configuration file.

