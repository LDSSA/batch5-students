FROM ldssa/academy-base

# Install LU requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt && \
    apt-get update && \
    apt install -y graphviz

# Install grader
RUN pip install --upgrade ldsagrader

# Copy run scripts
COPY . /student/
RUN chmod ugo+x /student/*.sh

USER student
WORKDIR /student
CMD ./run.sh
