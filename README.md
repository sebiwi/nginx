# Ansible/Molecule Test Driven Development example

This repository explains how to create an Ansible role using
Test Driven Development, with Molecule.

Each git commit contains a single feature added. Look into the
git history in order to see how the code evolved from empty role,
to a role capable of installing, starting and configuring nginx
in order to answer requests to the `/hello` location with a
200 HTTP status code and a string.

# Requirements

This needs Python 2.7.11, Ansible, Molecule, the `docker` Python
module, and Docker. All the Python dependencies are in the requirements.txt
file.

# Usage

```
# Install the dependencies
pip install -r requirements.txt

# Launch the whole test suit
molecule test

# Create the container
molecule create

# Launch assertions
molecule verify

# Launch Ansible code
molecule converge

# Destroy container
molecule destroy
```
