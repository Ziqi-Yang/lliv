run: install-dev
    lliv
    
install-dev:
    pip install --no-build-isolation -ve .

install-normal:
    pip install .

install-dev-requirements:
    pip install -r ./dev-requirements.txt
