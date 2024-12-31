FROM ros:iron-ros-base

ARG USERNAME=rosdev
ARG UID=1000
ARG GID=1000

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -qq && \
  apt-get upgrade -y -qq && \
  apt-get install -y --no-install-recommends \
  build-essential \
  python3.10 \
  libev-dev \
  software-properties-common \
  python3-pip \
  xauth \
  libpulse0:amd64 \
  libespeak1 \
  espeak \
  libportaudiocpp0 \
  libasound2-dev \
  libportaudio2 \
  libasound-dev \
  portaudio19-dev \
  alsa-utils \
  pulseaudio \
  curl \
  tmux \
  ranger \
  libhdf5-dev && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

  RUN ln -sf /usr/bin/python3 /usr/bin/python && \
      ln -sf /usr/bin/pip3 /usr/bin/pip

COPY pulse-client.conf /etc/pulse/client.conf

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

COPY start_tts.sh /start_tts.sh
RUN chmod +x /start_tts.sh

ENV TTS_MODEL_NAME="tts_models/de/thorsten/tacotron2-DDC"
RUN python -c "from TTS.api import TTS;TTS(model_name='${TTS_MODEL_NAME}')"


WORKDIR /home/${USERNAME}/ros2_ws/
COPY src /home/${USERNAME}/ros2_ws/src

CMD ["bash"]