pyenv install <3.10.2>

pyenv global <3.10.2>

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pip install -r requirements.txt

python --version