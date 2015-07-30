FROM ubuntu
MAINTAINER Gaston Pisacco

#this is a bug in the ubuntu distro
RUN sed -i "s/exit 101/exit 0/g" /usr/sbin/policy-rc.d
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
RUN apt-get update && apt-get -y install \
  gcc \
  git \
  mongodb \
  nginx \
  python \
  python-dev \
  python-pip \
  python-virtualenv \
  uwsgi \
  uwsgi-plugin-python

RUN mkdir /var/data
RUN git clone git://github.com/gpisacco/my_sequencer.git /var/data/my_sequencer #redo
RUN chmod 755 /var/data/my_sequencer/scripts/config.sh

EXPOSE 80

CMD /var/data/my_sequencer/scripts/config.sh