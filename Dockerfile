FROM quay.io/ansible/ansible-rulebook:v1.0.0

ENV SOURCE_DIR=/code

COPY --chown=$USER . $SOURCE_DIR

RUN cd $SOURCE_DIR && ansible-galaxy collection install . --force
