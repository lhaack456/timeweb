FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    vim curl git sudo gcc g++ \
    python3 python3-pip python3-venv python3-dev\
    build-essential libffi-dev libc-dev

RUN useradd -m developer && echo "developer ALL=(ALL) NOPASSWD:ALL" >/etc/sudoers.d/developer

USER developer
WORKDIR /home/developer

COPY .profile ~/asgn/a7/timeweb/timeweb/.profile
RUN echo "source ~/asgn/a7/timeweb/timeweb/.profile"
RUN git clone https://github.com/lhaack456/timeweb

CMD ["/bin/bash"]
