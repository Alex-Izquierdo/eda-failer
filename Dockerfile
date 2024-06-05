FROM quay.io/ansible/ansible-rulebook:main

ENV SOURCE_DIR=/code

COPY --chown=$USER . $SOURCE_DIR

RUN cd $SOURCE_DIR && ansible-galaxy collection install . --force
